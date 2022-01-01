from google.cloud import storage
from datetime import datetime
from gasprices.format_helper import *
from gasprices.misc_helper import *


def list_files(bucket_name, endswith="", startswith=""):
    retval = []
    for filename in list_blobs(bucket_name):
        if filename.endswith(endswith) and filename.startswith(startswith):
            retval.append(filename)
    retval.sort(reverse=False)
    return retval


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


# def list_blobs(bucket_name):
#     """Lists all the blobs in the bucket."""
#     storage_client = storage.Client()
#     blobs = storage_client.list_blobs(bucket_name)
#     retval = []
#     for blob in blobs:
#         retval.append(blob.name)
#     return retval

def list_blobs(bucket_name, endswith="", startswith="", needle_list=[]):
    storage_client = storage.Client()
    blobs = storage_client.list_blobs(bucket_name)
    retval = []
    for blob in blobs:
        if blob.name.endswith(endswith) and blob.name.startswith(startswith):
            if len(needle_list) > 0:
                if blob.name in needle_list:
                    retval.append(blob.name)
            else:
                retval.append(blob.name)
    retval.sort(reverse=False)
    return retval


def enrich_metadata(metadata, from_date=False, thru_date=False, from_time=False, thru_time=False, time_of_day=False, timespan=False, location=False, _type=False, from_iso_week_no=False, thru_iso_week_no=False):
    if from_date:
        metadata['from_date'] = format_templatestring(
            "{from_year}-{from_month:02d}-{from_day:02d}", from_date)
    if thru_date:
        metadata['thru_date'] = format_templatestring(
            "{to_year}-{to_month:02d}-{to_day:02d}", datetime.now(), thru_datetime=thru_date)
    if from_time:
        metadata['from_time'] = format_templatestring(
            "{from_hour:02d}:{from_minute:02d}:{from_second:02d}", from_time)
    if thru_time:
        metadata['thru_time'] = format_templatestring(
            "{to_hour:02d}:{to_minute:02d}:{to_second:02d}", datetime.now(), thru_datetime=thru_time)
    if time_of_day:
        metadata['time_of_day'] = time_of_day
    if timespan:
        metadata['timespan'] = timespan
    if location:
        metadata['location'] = location
    if _type:
        metadata['type'] = _type
    if from_iso_week_no:
        metadata['from_iso_week_no'] = from_iso_week_no
    if thru_iso_week_no:
        metadata['thru_iso_week_no'] = thru_iso_week_no
    return metadata


def get_metadata(bucket_name, gsfile):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.get_blob(gsfile)
    return blob.metadata


def get_gsfiles_pastXdays(event, days_range, metadata, tpl):
    days_list = list_datetime_obj(days_range+1)
    needle_list = list_formatted_tplstr(
        tpl, days_list, metadata['location'])
    haystack_list = list_blobs(
        event['bucket'], endswith=".csv",
        startswith="data/interim/prices/"+metadata['location']+"/prices_")
    datafile_list = list_blobs(
        event['bucket'], endswith=".csv",
        startswith="data/interim/prices/"+metadata['location']+"/prices_", needle_list=needle_list)
    if len(haystack_list) >= days_range:
        return datafile_list
    else:
        return False
