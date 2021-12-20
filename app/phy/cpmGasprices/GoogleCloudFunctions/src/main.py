import pandas as pd
from datetime import datetime
from datetime import time as time2
#import time
from google.cloud import storage
import requests
import os

from gasprices.google_storage import *
from gasprices.visualize import *
from gasprices.format_helper import *
from gasprices.misc_helper import *


tpl_url_data_ext_tk_prices = "https://dev.azure.com/tankerkoenig/362e70d1-bafa-4cf7-a346-1f3613304973/_apis/git/repositories/0d6e7286-91e4-402c-af56-fa75be1f223d/items?path=/prices/{to_year:n}/{to_month}/{to_year:n}-{to_month:02d}-{to_day:02d}-prices.csv"
tpl_file_data_ext_tk_prices = "data/external/prices/{location}/prices_{to_year}-{to_month:02d}-{to_day:02d}.csv"
tpl_gsfile_data_ext_tk_stations = 'gs://{bucket}/data/external/stations/{location}/current.csv'
tpl_gsfile_data_ext_tk_stations_location = 'gs://{bucket}/data/external/stations/{location}.csv'

tpl_file_data_interim_prices_location = "data/interim/prices/{location}/prices_{from_year}-{from_month:02d}-{from_day:02d}.csv"

tpl_file_data_proc_prices_location = "data/processed/prices/{location}/prices_{from_year}-{from_month:02d}-{from_day:02d}_{from_hour:02d}-{from_minute:02d}-{from_second:02d}_-_{to_year}-{to_month:02d}-{to_day:02d}_{to_hour:02d}-{to_minute:02d}-{to_second:02d}.csv"

weekdays_en = ['Monday', 'Tuesday', 'Wednesday',
               'Thursday', 'Friday', 'Saturday', 'Sunday']
translate_weekdays_en2de = {'Monday': 'Mo', 'Tuesday': 'Di', 'Wednesday': 'Mi',
                            'Thursday': 'Do', 'Friday': 'Fr', 'Saturday': 'Sa', 'Sunday': 'So'}

timespans = [{'from_time': '00:00', 'from': '00:00', 'thru_time': '23:59:59', 'thru': '23:59:59', 'timespan': '21', 'time-of-day': 'full'},
             {'from_time': '17:00', 'from': '17:00', 'thru_time': '21:59:59', 'thru': '21:59:59', 'timespan': '21', 'time-of-day': 'earlyevening'}]


def download_pricefiles_http(request):
    event = {}
    event['bucket'] = '2021.gasprices.cprima.net'
    download_pricefiles(event, None)
    return 'download_pricefiles_http'


def download_pricefiles(event, context):
    metadata = {'type': 'prices',
                'location': 'deutschland', 'source': 'tankerkoenig'}
    days_range = 30

    existing_files = list_blobs(
        event['bucket'], endswith="csv", startswith="data/external/prices/deutschland/prices_")

    for day in list_datetime_obj(days_range):
        gsfile = format_templatestring(
            tpl_file_data_ext_tk_prices, from_datetime=datetime.now(), thru_datetime=day, location=metadata['location'])

        if gsfile in existing_files:
            print(gsfile + " existing.")
        else:
            url = format_templatestring(
                tpl_url_data_ext_tk_prices, from_datetime=datetime.now(), thru_datetime=day, location=metadata['location'])+"&download=true"
            metadata = enrich_metadata(metadata, from_date=day, thru_date=day, from_time=day,
                                       thru_time=get_end_of_day_time(day), time_of_day='full', timespan=False, location=metadata['location'], _type='prices')
            print("Going to request "+url)
            r = requests.get(url)
            if r.ok:
                upload_blob_string(
                    event['bucket'], r.content, gsfile, metadata)


def download_stationsfiles(event, context):
    pass


def extract_from_pricefile_for_location_http(request):
    event = {}
    event['bucket'] = '2021.gasprices.cprima.net'
    event['name'] = "data/external/prices/deutschland/prices_2021-12-19.csv"
    extract_from_pricefile_for_location(event, None)
    return 'extract_from_pricefile_for_location_http'


def extract_from_pricefile_for_location(event, context):

    if "data/external/prices/deutschland/" in event['name']:

        metadata = get_metadata(event['bucket'], event['name'])
        metadata = enrich_metadata(metadata, location='wolfsburg')

        gsfile = tpl_gsfile_data_ext_tk_stations_location.format(
            bucket=event['bucket'], location=metadata['location'])
        df_stations = pd.read_csv(gsfile, encoding='utf-8')
        df_stations = df_stations.drop(
            ['dist', 'diesel', 'e5', 'e10', 'isOpen'], axis=1)

        gsfile = 'gs://'+event['bucket']+'/' + event['name']
        df_prices = pd.read_csv(gsfile, encoding='utf-8')

        # df_prices = df_prices.drop(
        #     ['dieselchange', 'e5change', 'e10change'], axis=1)
        df_prices['date'] = pd.to_datetime(
            df_prices['date'], errors='coerce', utc=True)
        df_prices['weekday'] = df_prices['date'].dt.day_name()
        df_prices['weekday'] = pd.Categorical(
            df_prices['weekday'], categories=weekdays_en, ordered=True)
        df_prices['quarter'] = df_prices['date'].dt.to_period('Q')

        df_merged = pd.merge(df_prices, df_stations, left_on='station_uuid',
                             right_on='id', how='inner', suffixes=('_left', '_right'))
        del(df_prices)
        del(df_stations)

        f = event['name'].replace(
            'data/external/prices/deutschland/', 'data/interim/prices/'+metadata['location']+'/')
        upload_blob_string(event['bucket'], df_merged.to_csv(None, sep=',', header=True, index=False,
                           encoding='utf-8'), f, metadata)


def merge_stationprices_http(request):
    event = {}
    event['bucket'] = '2021.gasprices.cprima.net'
    event['name'] = "data/interim/prices/wolfsburg/prices_2021-12-19.csv"
    merge_stationprices(event, None)
    return 'merge_stationprices_http'

# exists each file in range of days?
# if not, trigger their creation
# if existing
# - read metadata
# - enrich metadata done
# - format filename done
# - read datafiles done
# - concat datafiles done
# - save csv done


def merge_stationprices(event, context):
    metadata = get_metadata(event['bucket'], event['name'])
    metadata = enrich_metadata(metadata, location='wolfsburg')
    days_range = 21
    if "data/interim/prices/"+metadata['location']+"/prices_" in event['name']:
        days_list = list_datetime_obj(22)
        needle_list = list_formatted_tplstr(
            tpl_file_data_interim_prices_location, days_list, metadata['location'])
        haystack_list = list_blobs(
            event['bucket'], endswith=".csv",
            startswith="data/interim/prices/"+metadata['location']+"/prices_")
        datafile_list = list_blobs(
            event['bucket'], endswith=".csv",
            startswith="data/interim/prices/"+metadata['location']+"/prices_", needle_list=needle_list)

        if len(haystack_list) >= days_range:

            df = pd.concat([pd.read_csv('gs://'+event['bucket']+'/'+f,
                                        parse_dates=['date'])
                            for f in datafile_list
                            ], ignore_index=True)
            df['date'] = pd.to_datetime(df['date'], errors='coerce', utc=True)
            df['weekday'] = df['date'].dt.day_name()
            df['weekday'] = pd.Categorical(
                df['weekday'], categories=weekdays_en, ordered=True)

            for timespan in timespans:

                from_datetime = add_date_time(
                    min(days_list), timespan['from_time'])
                thru_datetime = add_date_time(
                    max(days_list), timespan['thru_time'])

                metadata = enrich_metadata(metadata,
                                           from_date=min(days_list),
                                           thru_date=max(days_list),
                                           from_time=from_datetime,
                                           thru_time=thru_datetime,
                                           time_of_day=timespan['time-of-day'],
                                           timespan=timespan['timespan'],
                                           location=metadata['location'])

                gsfile = format_templatestring(
                    tpl_file_data_proc_prices_location, from_datetime, thru_datetime, location=metadata['location'])

                upload_blob_string(event['bucket'], df.to_csv(
                    None, sep=',', header=True, index=True, encoding='utf-8'), gsfile, metadata)
                # upload_blob_string(event['bucket'], df.to_json(
                #    path_or_buf=None, date_format='iso', orient='records'), f.replace('.csv', '.json'), metadata)
    else:
        pass


def visualize_weekly_http(request):
    event = {}
    event['bucket'] = '2021.gasprices.cprima.net'
    event['name'] = "data/processed/prices/wolfsburg/prices_2021-11-28_17-00-00_-_2021-12-19_21-59-59.csv"
    visualize_weekly(event, None)
    return 'Hello World!'


def visualize_weekly(event, context):
    metadata = get_metadata(event['bucket'], event['name'])
    if "data/processed/prices/"+metadata['location']+"/prices_" in event['name']:

        gsfile = 'gs://'+event['bucket']+'/' + event['name']
        df_prices = pd.read_csv(gsfile, encoding='utf-8')
        df_prices['date'] = pd.to_datetime(
            df_prices['date'], errors='coerce', utc=True)
        df_prices['weekday'] = df_prices['date'].dt.day_name()
        df_prices['weekday'] = pd.Categorical(
            df_prices['weekday'], categories=weekdays_en, ordered=True)

        from_datetime = datetime.strptime(
            metadata['from_date'] + ' ' + metadata['from_time'], '%Y-%m-%d %H:%M:%S')
        thru_datetime = datetime.strptime(
            metadata['thru_date'] + ' ' + metadata['thru_time'], '%Y-%m-%d %H:%M:%S')

        title = "Tankstellenpreise in "+metadata['location'].capitalize()
        subtitle = "vom {from_day:02d}.{from_month:02d}. bis {to_day:02d}.{to_month:02d}. zwischen {from_hour:02d}:{from_minute:02d} und {to_hour:02d}:{to_minute:02d}"
        subtitle = subtitle.format(from_year=from_datetime.year, from_month=from_datetime.month, from_day=from_datetime.day,
                                   from_hour=from_datetime.hour, from_minute=from_datetime.minute, from_second=from_datetime.second,
                                   to_year=thru_datetime.year, to_month=thru_datetime.month, to_day=thru_datetime.day,
                                   to_hour=thru_datetime.hour, to_minute=thru_datetime.minute, to_second=thru_datetime.second)

        df_weekly = df_prices.groupby('weekday')[['e5', 'e10', 'diesel']].mean().rename(
            index=translate_weekdays_en2de, inplace=False)

        generate_save_plot_e5_diesel(df_weekly, 'wolfsburg',
                                     title, subtitle, '/tmp/current.png')
        metadata['type'] = 'figure'
        upload_blob_file(event['bucket'], '/tmp/current.png',
                         'reports/figures/wolfsburg_current.png', metadata)
        upload_blob_file('plots.'+event['bucket'], '/tmp/current.png',
                         'reports_figures_wolfsburg_current.png', metadata)


def hello_world(event, context):
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
    pass
