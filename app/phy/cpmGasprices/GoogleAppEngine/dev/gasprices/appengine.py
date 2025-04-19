
from google.cloud import storage
from gasprices.config import *


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


def list_blobs(bucket_name):
    """Lists all the blobs in the bucket."""
    storage_client = storage.Client()
    blobs = storage_client.list_blobs(bucket_name)
    retval = []
    for blob in blobs:
        retval.append(blob.name)
    return retval


def list_gs_files(endswith="", startswith=""):
    retval = []
    for filename in list_blobs(bucket_name):
        if filename.endswith(endswith) and filename.startswith(startswith):
            retval.append(filename)
    retval.sort(reverse=False)
    return retval
