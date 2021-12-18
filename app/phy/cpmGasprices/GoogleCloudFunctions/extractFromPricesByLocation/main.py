import pandas as pd
import datetime
import time
from google.cloud import storage
import matplotlib.pyplot as plt
import math


def upload_blob_file(bucket_name, source_file_name, destination_blob_name, metadata={'foo': 'bar'}):
    """Uploads a file to the bucket."""
    if destination_blob_name.endswith(".csv"):
        content_type = 'text/csv'
    elif destination_blob_name.endswith(".json"):
        content_type = 'application/json'
    elif destination_blob_name.endswith(".png"):
        content_type = 'image/png'
    else:
        content_type = 'text/plain'
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name, content_type=content_type)
    blob.metadata = metadata
    blob.patch()
    return


def upload_blob_string(bucket_name, source_string, destination_blob_name, metadata={'foo': 'bar'}):
    """Uploads a string as file to the bucket. Depends on `from google.cloud import storage`"""
    if destination_blob_name.endswith(".csv"):
        content_type = 'text/csv'
    elif destination_blob_name.endswith(".json"):
        content_type = 'application/json'
    elif destination_blob_name.endswith(".png"):
        content_type = 'image/png'
    else:
        content_type = 'text/plain'
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_string(source_string, content_type=content_type)
    blob.metadata = metadata
    blob.patch()
    return


def getDaysSinceYesterdayAsList(days_range):
    """Returns datetime objects since yesterday as a list"""
    retval = []
    end_date = datetime.date.today() - datetime.timedelta(days=1)
    start_date = end_date - days_range * datetime.timedelta(days=1)
    for i in range((end_date - start_date).days):
        retval.append(end_date - i * datetime.timedelta(days=1))
    return retval


def list_blobs(bucket_name):
    """Lists all the blobs in the bucket."""
    storage_client = storage.Client()
    blobs = storage_client.list_blobs(bucket_name)
    retval = []
    for blob in blobs:
        retval.append(blob.name)
    return retval


def generate_save_plot(df, location, subtitle, filename):
    plt.rcdefaults()
    plt.style.use('Solarize_Light2')
    px = 1/plt.rcParams['figure.dpi']

    serif_font = {'fontname': 'Linux Biolinum'}
    #plt.rcParams['font.family'] = serif_font
    plt.rcParams.update({'font.sans-serif': 'Linux Biolinum'})
    colors = plt.rcParams["axes.prop_cycle"]()

    px = 1/plt.rcParams['figure.dpi']
    fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1,
                                   sharex=True, figsize=(640*px, 360*px))

    fig.suptitle("Tankstellenpreise in "+location.capitalize(),
                 fontsize=24, **serif_font)

    e5min = df['e5'][df['e5'] > 0.1].min()
    e5max = df['e5'][df['e5'] > 0.1].max()
    e5min = (math.floor(e5min*100)/100)-0.01
    e5max = (math.ceil(e5max*100)/100)+0.01
    #print(e5min, e5max)
    dieselmin = df['diesel'][df['diesel'] > 0.1].min()
    dieselmax = df['diesel'][df['diesel'] > 0.1].max()
    dieselmin = (math.floor(dieselmin*100)/100)-0.01
    dieselmax = (math.ceil(dieselmax*100)/100)+0.01

    c = next(colors)["color"]
    ax1.plot(df.e5, label='e5', color=c)
    ax1.set_title(subtitle)
    ax1.legend()
    ax1.set_ylim([e5min, e5max])

    c = next(colors)["color"]
    ax2.plot(df.diesel, label='diesel', color=c)
    ax2.legend()
    ax2.set_ylim([dieselmin, dieselmax])

    plt.tight_layout()
    plt.savefig(filename)
    # plt.show()


def format_filename_tpl(tpl, location, from_date, thru_date, timespan):
    try:
        from_time = time.strptime(timespan['from'], '%H:%M:%S')
    except ValueError:
        from_time = time.strptime(timespan['from'], '%H:%M')
    except Exception as e:
        print(e)
    try:
        thru_time = time.strptime(timespan['thru'], '%H:%M:%S')
    except ValueError:
        thru_time = time.strptime(timespan['thru'], '%H:%M')
    except Exception as e:
        print(e)
    finally:
        f = tpl.format(
            location=location,
            from_year=from_date.year, from_month=from_date.month, from_day=from_date.day,
            from_hour=from_time.tm_hour, from_minute=from_time.tm_min, from_second=from_time.tm_sec,
            to_year=thru_date.year, to_month=thru_date.month, to_day=thru_date.day,
            to_hour=thru_time.tm_hour, to_minute=thru_time.tm_min, to_second=thru_time.tm_sec
        )
    return f


def list_gs_files(bucket_name, endswith="", startswith=""):
    retval = []
    for filename in list_blobs(bucket_name):
        if filename.endswith(endswith) and filename.startswith(startswith):
            retval.append(filename)
    retval.sort(reverse=False)
    return retval


def extract_from_prices_by_location(event, context):
    """Background Cloud Function to be triggered by Cloud Storage.
       This generic function logs relevant data when a file is changed.

    Args:
        event (dict):  The dictionary with data specific to this type of event.
                       The `data` field contains a description of the event in
                       the Cloud Storage `object` format described here:
                       https://cloud.google.com/storage/docs/json_api/v1/objects#resource
        context (google.cloud.functions.Context): Metadata of triggering event.
    Returns:
        None; the output is written to Stackdriver Logging
    """

    print("extract_from_prices_by_location!")
    # print('Event ID: {}'.format(context.event_id))
    # print('Event type: {}'.format(context.event_type))
    print('Bucket: {}'.format(event['bucket']))
    print('File: {}'.format(event['name']))
    # print('Metageneration: {}'.format(event['metageneration']))
    # print('Created: {}'.format(event['timeCreated']))
    # print('Updated: {}'.format(event['updated']))

    if "data/external/tankerkoenig/prices" in event['name']:
        days = ['Monday', 'Tuesday', 'Wednesday',
                'Thursday', 'Friday', 'Saturday', 'Sunday']

        df_stations = pd.read_csv(
            'gs://'+event['bucket']+'/data/external/tankerkoenig/stations/wolfsburg.csv', encoding='utf-8')
        df_stations = df_stations.drop(
            ['dist', 'diesel', 'e5', 'e10', 'isOpen'], axis=1)

        f = 'gs://'+event['bucket']+'/' + event['name']
        print(f)
        df_prices = pd.read_csv(f, encoding='utf-8')
        print('dataframe df_prices number of rows: {}'.format(len(df_prices)))
        print('dataframe df_prices columns: {}'.format(df_prices.columns))

        df_prices = df_prices.drop(
            ['dieselchange', 'e5change', 'e10change'], axis=1)
        df_prices['date'] = pd.to_datetime(
            df_prices['date'], errors='coerce', utc=True)
        df_prices['weekday'] = df_prices['date'].dt.day_name()
        df_prices['weekday'] = pd.Categorical(
            df_prices['weekday'], categories=days, ordered=True)
        df_prices['quarter'] = df_prices['date'].dt.to_period('Q')

        df_merged = pd.merge(df_prices, df_stations, left_on='station_uuid',
                             right_on='id', how='inner', suffixes=('_left', '_right'))
        #df_merged.index = pd.to_datetime(df_merged['date'], utc=True)
        print('dataframe df_merged number of rows: {}'.format(len(df_merged)))
        del(df_prices)
        del(df_stations)

        metadata = {'type': 'prices', 'location': 'wolfsburg'}
        f = event['name'].replace(
            'data/external/tankerkoenig/prices/', 'data/interim/wolfsburg/')
        upload_blob_string(event['bucket'], df_merged.to_csv(None, sep=',', header=True, index=False,
                           encoding='utf-8'), f, metadata)


def concat_price_stations_21days_timespans(event, context):
    print("concat_price_stations_21days_timespans!")
    print('Bucket: {}'.format(event['bucket']))
    print('File: {}'.format(event['name']))
    if "data/interim/wolfsburg/prices_" in event['name']:
        needle_list = []
        for d in getDaysSinceYesterdayAsList(22):
            needle_list.append(d.strftime(
                "data/interim/wolfsburg/prices_%Y-%m-%d.csv"))
        print('needle_list: ' + ', '.join(needle_list))
        haystack_list = list_gs_files(
            event['bucket'], endswith=".csv", startswith="data/interim/wolfsburg/prices_")
        print('haystack_list: ' + ', '.join(haystack_list))
        datafile_list = []
        for file in haystack_list:
            if file in needle_list:
                datafile_list.append(file)
        print('datafile_list: ' + ', '.join(datafile_list))
        if len(haystack_list) >= 21:
            metadata = {'type': 'prices', 'location': 'wolfsburg'}
            from_date = min(getDaysSinceYesterdayAsList(22))
            thru_date = max(getDaysSinceYesterdayAsList(22))
            timespans = [{'from': '00:00', 'thru': '23:59:59', 'timespan': '21', 'time-of-day': 'full'},
                         {'from': '17:00', 'thru': '21:59:59', 'timespan': '21', 'time-of-day': 'earlyevening'}]
            filename_tpl = "data/processed/wolfsburg/prices_{from_year}-{from_month:02d}-{from_day:02d}_{from_hour:02d}-{from_minute:02d}-{from_second:02d}_-_{to_year}-{to_month:02d}-{to_day:02d}_{to_hour:02d}-{to_minute:02d}-{to_second:02d}.csv"
            days = ['Monday', 'Tuesday', 'Wednesday',
                    'Thursday', 'Friday', 'Saturday', 'Sunday']
            df = pd.concat([pd.read_csv('gs://'+event['bucket']+'/'+f, parse_dates=['date'])
                           for f in datafile_list], ignore_index=True)
            df['date'] = pd.to_datetime(df['date'], errors='coerce', utc=True)
            df['weekday'] = df['date'].dt.day_name()
            df['weekday'] = pd.Categorical(
                df['weekday'], categories=days, ordered=True)
            for timespan in timespans:
                metadata['timespan'] = timespan['timespan']
                metadata['time_of_day'] = timespan['time-of-day']
                metadata['from_date'] = format_filename_tpl(
                    "{from_year}-{from_month:02d}-{from_day:02d}", "wolfsburg", from_date, thru_date, timespan)
                metadata['thru_date'] = format_filename_tpl(
                    "{to_year}-{to_month:02d}-{to_day:02d}", "wolfsburg", from_date, thru_date, timespan)
                metadata['from_time'] = format_filename_tpl(
                    "{from_hour:02d}-{from_minute:02d}-{from_second:02d}", "wolfsburg", from_date, thru_date, timespan)
                metadata['thru_time'] = format_filename_tpl(
                    "{to_hour:02d}-{to_minute:02d}-{to_second:02d}", "wolfsburg", from_date, thru_date, timespan)
                f = format_filename_tpl(
                    filename_tpl, 'wolfsburg', from_date, thru_date, timespan)
                upload_blob_string(event['bucket'], df.to_csv(
                    None, sep=',', header=True, index=True, encoding='utf-8'), f, metadata)
                # upload_blob_string(event['bucket'], df.to_json(
                #    path_or_buf=None, date_format='iso', orient='records'), f.replace('.csv', '.json'), metadata)


def visualize_weekly_http(request):
    event = {}
    event['bucket'] = '2021.gasprices.cprima.net'
    event['name'] = "data/processed/wolfsburg/prices_"
    visualize_weekly(event, None)
    return 'Hello World!'


def visualize_weekly(event, context):
    print("visualize_weekly!")
    print('Bucket: {}'.format(event['bucket']))
    print('File: {}'.format(event['name']))
    if "data/processed/wolfsburg/prices_" in event['name']:
        days = ['Monday', 'Tuesday', 'Wednesday',
                'Thursday', 'Friday', 'Saturday', 'Sunday']
        translate_dict = {'Monday': 'Mo', 'Tuesday': 'Di', 'Wednesday': 'Mi',
                          'Thursday': 'Do', 'Friday': 'Fr', 'Saturday': 'Sa', 'Sunday': 'So'}
        storage_client = storage.Client()
        blobs = storage_client.list_blobs(event['bucket'])
        data = []
        for blob in blobs:
            if blob.name.startswith('data/p') and blob.name.endswith('.csv') and blob.metadata['type'] == 'prices':
                #print(blob.name, blob.metadata)
                new = blob.metadata
                new['blobname'] = blob.name
                data.append(new)

        print(data)
        df_prices = pd.DataFrame.from_dict(data)
        print(df_prices)

        df_subset = df_prices[df_prices['thru_date'] == df_prices['thru_date'].max(
        )][df_prices['time_of_day'].str.match('earlyevening')].iloc[0]

        from_datetime = datetime.datetime.strptime(
            df_subset['from_date'] + ' ' + df_subset['from_time'], '%Y-%m-%d %H-%M-%S')
        thru_datetime = datetime.datetime.strptime(
            df_subset['thru_date'] + ' ' + df_subset['thru_time'], '%Y-%m-%d %H-%M-%S')
        subtitle = "vom {from_day:02d}.{from_month:02d}. bis {to_day:02d}.{to_month:02d}. zwischen {from_hour:02d}:{from_minute:02d} und {to_hour:02d}:{to_minute:02d}"
        subtitle = subtitle.format(from_year=from_datetime.year, from_month=from_datetime.month, from_day=from_datetime.day,
                                   from_hour=from_datetime.hour, from_minute=from_datetime.minute, from_second=from_datetime.second,
                                   to_year=thru_datetime.year, to_month=thru_datetime.month, to_day=thru_datetime.day,
                                   to_hour=thru_datetime.hour, to_minute=thru_datetime.minute, to_second=thru_datetime.second)

        df_weekly = pd.read_csv(
            'gs://'+'2021.gasprices.cprima.net'+'/'+df_subset['blobname'], encoding='utf-8')

        df_weekly['date'] = pd.to_datetime(
            df_weekly['date'], errors='coerce', utc=True)
        df_weekly['weekday'] = df_weekly['date'].dt.day_name()
        df_weekly['weekday'] = pd.Categorical(
            df_weekly['weekday'], categories=days, ordered=True)
        df_weekly = df_weekly.groupby('weekday')[['e5', 'e10', 'diesel']].mean().rename(
            index=translate_dict, inplace=False)

        generate_save_plot(df_weekly, 'wolfsburg',
                           subtitle, '/tmp/current.png')
        metadata = df_subset.to_dict()
        del(metadata['blobname'])
        metadata['type'] = 'figure'
        upload_blob_file(event['bucket'], '/tmp/current.png',
                         'reports/figures/wolfsburg_current.png', metadata)
        upload_blob_file('plots.'+event['bucket'], '/tmp/current.png',
                         'reports_figures_wolfsburg_current.png', metadata)

# def upload_blob_file(bucket_name, source_file_name, destination_blob_name, metadata={'foo': 'bar'}):
    # print('Event ID: {}'.format(context.event_id))
    # print('Event type: {}'.format(context.event_type))
    #print('Bucket: {}'.format(event['bucket']))
    #print('File: {}'.format(event['name']))
    # print('Metageneration: {}'.format(event['metageneration']))
    # print('Created: {}'.format(event['timeCreated']))
    # print('Updated: {}'.format(event['updated']))
