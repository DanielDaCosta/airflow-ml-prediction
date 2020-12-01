import boto3
import pandas as pd
import joblib
import os
from tempfile import mkstemp


def read_csv_from_s3(bucket, key, sep=','):
    """Read csv from s3
    Args:
        Bucket (str): The name of the bucket to download from.
        key (str): The name of the key to download from.
        sep (str): Delimeter to use.
    Returns:
        (DataFrame): A comma-separated values (csv) file
                    is returned as two-dimensional data
                    structure with labeled axes.
    """
    s3 = boto3.client('s3')
    filedescriptor, csv = mkstemp(suffix='.csv')
    with os.fdopen(filedescriptor, 'wb') as fileobj:
        s3.download_fileobj(Bucket=bucket, Key=key, Fileobj=fileobj)
    return pd.read_csv(csv, sep=sep, escapechar='\\', encoding='utf-8')


def save_results(bucket, key, results, start_time):
    """Save results to s3
    Args:
        Bucket (str): The name of the bucket to download from.
        key (str): The name of the key to download from.
        results (DataFrame)
    Returns:
        (dict): Dict containg some metadata about the insertion.
    """
    date = f'{start_time.year}-{start_time.month:02d}-{start_time.day:02d}'
    time = f'{start_time.hour:02d}-{start_time.minute:02d}'
    week = start_time.isocalendar()[1]

    s3 = boto3.client('s3')
    s3_response_result = s3.put_object(
        Body=results.to_csv(index=False),
        Bucket=bucket,
        Key=f"{key}/result_w{week:02d}_{date}_{time}.csv")

    return s3_response_result


def read_sav_from_s3(bucket, key):
    """Read serialized model from s3
    Args:
        Bucket (str): The name of the bucket to download from.
        key (str): The name of the key to download from.
    Returns:
        any Python object. ML model serialized.
    """
    s3 = boto3.client('s3')
    filedescriptor, sav = mkstemp(suffix='.sav')
    with os.fdopen(filedescriptor, 'wb') as fileobj:
        s3.download_fileobj(Bucket=bucket, Key=key, Fileobj=fileobj)
    return joblib.load(sav)