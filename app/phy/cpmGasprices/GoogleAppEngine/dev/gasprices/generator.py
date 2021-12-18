import os
import datetime
import time
import requests
from urllib.parse import urlparse
import pandas as pd
import calendar
import math
import matplotlib.pyplot as plt

from google.cloud import storage

from gasprices.config import *
from gasprices.appengine import *
from gasprices.collector import *


def getDaysSinceYesterdayAsList(days_range):
    """Returns datetime objects since yesterday as a list"""
    retval = []
    end_date = datetime.date.today() - datetime.timedelta(days=1)
    start_date = end_date - days_range*day_delta
    for i in range((end_date - start_date).days):
        retval.append(end_date - i*day_delta)
    return retval


def getPricefilesFromStorage(days_range=30, fullweeks=False):
    retval = []
    needle_list = []

    if fullweeks:
        for d in getDaysOfPreviousWeeksAsList(weeks=fullweeks):
            needle_list.append(d.strftime(
                "data_external_tk_prices_%Y-%m-%d.csv"))
    else:
        for d in getDaysSinceYesterdayAsList(days_range):
            needle_list.append(d.strftime(
                "data_external_tk_prices_%Y-%m-%d.csv"))

    csv_files_list = list_gs_files(
        endswith="csv", startswith="data_external_tk_prices_")
    for file in csv_files_list:
        if file in needle_list:
            retval.append(file)
    return retval


def get_dataframe_prices_from_storage(days_range=30, fullweeks=False):
    list_temp_raw = []
    filenames = getPricefilesFromStorage(days_range, fullweeks)
    days = ['Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'Saturday', 'Sunday']
    for filename in filenames:
        temp = pd.read_csv('gs://'+bucket_name+'/'+filename, encoding='utf-8')
        list_temp_raw.append(temp)
    df = pd.concat(list_temp_raw)
    df = df.drop(['dieselchange', 'e5change', 'e10change'], axis=1)
    df['date'] = pd.to_datetime(df['date'], errors='coerce', utc=True)
    df['weekday'] = df['date'].dt.day_name()
    df['weekday'] = pd.Categorical(
        df['weekday'], categories=days, ordered=True)
    df['quarter'] = df['date'].dt.to_period('Q')
    return df


def get_dataframe_stations_from_storage(location="wolfsburg"):
    df = pd.concat([pd.read_csv(
        'gs://'+bucket_name+'/'+'data_filtered_tk_stations_'+location+'.csv',
        encoding='utf-8')], ignore_index=True)
    df = df.drop(['dist', 'diesel', 'e5', 'e10', 'isOpen'], axis=1)
    return df


def getDaysOfPreviousWeeksAsList(weeks=3):
    """Returns datetime objects of previous full weeks as a list"""
    retval = []
    today = datetime.date.today()
    offsetA = weeks * 7 + 1
    offsetB = (weeks * 7) - 1
    start_date = today - \
        datetime.timedelta(days=today.weekday()) - \
        datetime.timedelta(days=offsetA)
    end_date = start_date + datetime.timedelta(days=offsetB)

    for i in range((end_date - start_date).days):
        retval.append(end_date - i*datetime.timedelta(days=1))
    return retval


def merge_dataframes_stations_prices(location, days_range=30, fullweeks=False):
    df_prices = get_dataframe_prices_from_storage(days_range, fullweeks=False)
    df_stations = get_dataframe_stations_from_storage(location)
    df_merged = pd.merge(df_prices, df_stations, left_on='station_uuid',
                         right_on='id', how='inner', suffixes=('_left', '_right'))
    df_merged.index = pd.to_datetime(df_merged['date'], utc=True)
    return df_merged


def calculate_start_date(days_range=30, fullweeks=False):
    if fullweeks:
        return min(getDaysOfPreviousWeeksAsList(fullweeks))
    else:
        return min(getDaysSinceYesterdayAsList(days_range))


def calculate_end_date(days_range=30, fullweeks=False):
    if fullweeks:
        return max(getDaysOfPreviousWeeksAsList(fullweeks))
    else:
        return max(getDaysSinceYesterdayAsList(days_range))


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
                                   sharex=True, figsize=(640*px, 480*px))

    fig.suptitle("Benzinpreise in "+location.capitalize(),
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
    plt.show()


def make_datasets(location="wolfsburg", days_range=30, fullweeks=False):
    from_date = calculate_start_date(days_range, fullweeks)
    thru_date = calculate_end_date(days_range, fullweeks)
    df = merge_dataframes_stations_prices(location, days_range, fullweeks)
    #df = df_merged
    timespans = [{'from': '00:00', 'thru': '23:59:59'},
                 {'from': '17:00', 'thru': '21:59:59'}]
    for timespan in timespans:
        f = format_filename_tpl(
            my_subset_prices_location_date_timespan_filename_tpl, location, from_date, thru_date, timespan)
        df4 = df.to_csv(None, sep=',', header=True,
                        index=True, encoding='utf-8')
        upload_blob_string(bucket_name, df4, f)

        datafilename = format_filename_tpl(
            my_weeklyaggregate_prices_location_date_timespan_filename_tpl, location, from_date, thru_date, timespan)
        plotfilename = datafilename.replace(".csv", ".png")
        plotfilename = plotfilename.replace("data_", "plot_")
        subtitle = format_filename_tpl(
            figure_subtitle_tpl, location, from_date, thru_date, timespan)
        #existing_files = list_gs_files(endswith="csv")
        df2 = df.between_time(timespan['from'], timespan['thru']).groupby(
            'weekday')[['e5', 'e10', 'diesel']].mean()
        generate_save_plot(df2, location, subtitle, plotfilename)
        df3 = df2.to_csv(None, sep=',', header=True,
                         index=True, encoding='utf-8')
        upload_blob_file(bucket_name, plotfilename, plotfilename)
        upload_blob_string(bucket_name, df3, datafilename)
    return
