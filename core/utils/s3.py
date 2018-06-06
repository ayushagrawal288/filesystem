import boto3
from botocore.exceptions import ClientError


aws_access_key_id = "AKIAIPCLMKEZHM5DCUDQ"
aws_secret_access_key = "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"

region = "us-east-2"

bucket_name = 'leucinetechapp'

s3 = boto3.resource('s3', region, aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

temp_file = 'core/temp'


class S3Filesystem(object):
    @staticmethod
    def create(filename, file):
        data = s3.Object(bucket_name, filename).put(Body=file)
        return data

    @staticmethod
    def delete(filename):
        s3.Object(bucket_name, filename).delete()

    @staticmethod
    def fetch(filename):
        try:
            s3.Object(bucket_name, filename).download_file(temp_file)
        except ClientError as e:
            if e.response['Error']['Code'] == '404':
                raise ValueError('no file found by that name')
        file = open(temp_file, 'rb')
        data = file.read().decode('utf-8')
        file.close()
        return data

    @staticmethod
    def rename(new_name, previous_name):
        try:
            s3.Object(bucket_name, new_name).copy_from(CopySource='/' + bucket_name + '/' + previous_name)
            s3.Object(bucket_name, previous_name).delete()
        except ClientError as e:
            if e.response['Error']['Code'] == 'NoSuchKey':
                raise ValueError('no file found by that name')

    @staticmethod
    def list():
        data = list()
        for obj in s3.Bucket(bucket_name).objects.all():
            data.append({
                "filename": obj.key,
                "size": obj.size,
                "updated_at": obj.last_modified.isoformat(),
            })
        return data
