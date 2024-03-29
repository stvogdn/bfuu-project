
from storages.backends.s3boto3 import S3Boto3Storage

class MediaStorage(S3Boto3Storage):
    bucket_name = 'bfuu-wsc-media'
    custom_domain = '{}.s3.amazonaws.com'.format(bucket_name)

class StaticStorage(S3Boto3Storage):
    bucket_name = 'bfuu-wsc-static'
    custom_domain = '{}.s3.amazonaws.com'.format(bucket_name)
