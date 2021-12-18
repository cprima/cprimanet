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
from gasprices.generator import *


def getDaysSinceYesterdayAsList(days_range):
    """Returns datetime objects since yesterday as a list"""
    retval = []
    end_date = datetime.date.today() - datetime.timedelta(days=1)
    start_date = end_date - days_range*day_delta
    for i in range((end_date - start_date).days):
        retval.append(end_date - i*day_delta)
    return retval


def formatStringPaddedYMD(url_tpl, tmp_date):
    """Formats a string with padded day and month integers from datetime object"""
    return url_tpl.format(year=tmp_date.year, month=tmp_date.month, day=tmp_date.day)


def requestUrlsAndUploadBlobs(filename, source_string):
    upload_blob_string(bucket_name, source_string, filename)
    return


def retrievePricefiles():
    """@todo: rename"""
    existing_files = list_gs_files(endswith="csv")
    for d in getDaysSinceYesterdayAsList(days_range):
        url = formatStringPaddedYMD(tk_prices_url_tpl, d) + "&download=true"
        filename = formatStringPaddedYMD(tk_prices_filename_tpl, d)
        if filename in existing_files:
            print(filename + " existing.")
            pass
        else:
            print("requesting "+filename)
            r = requests.get(url)
            requestUrlsAndUploadBlobs(filename, r.content)
    return


def retrieveStationfile():
    """@todo: rename"""
    url = formatStringPaddedYMD(tk_stations_url_tpl, datetime.date.today(
    ) - datetime.timedelta(days=1)) + "&download=true"
    filename = tk_stations_filename_tpl
    r = requests.get(url)
    requestUrlsAndUploadBlobs(filename, r.content)
    return


def retrieve_data():
    retrievePricefiles()
    retrieveStationfile()
