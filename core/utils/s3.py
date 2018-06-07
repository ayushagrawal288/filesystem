import boto3
from botocore.exceptions import ClientError


class S3Filesystem(object):
    def __init__(self, aws_access_key_id, aws_secret_access_key, region, bucket_name, temp_file):
        self.s3 = boto3.resource('s3', region, aws_access_key_id=aws_access_key_id,
                                 aws_secret_access_key=aws_secret_access_key)
        self.bucket_name = bucket_name
        self.temp_file = temp_file

    def create(self, filename, file):
        data = self.s3.Object(self.bucket_name, filename).put(Body=file)
        return data

    def delete(self, filename):
        self.s3.Object(self.bucket_name, filename).delete()

    def fetch(self, filename):
        try:
            self.s3.Object(self.bucket_name, filename).download_file(temp_file)
        except ClientError as e:
            if e.response['Error']['Code'] == '404':
                raise ValueError('no file found by that name')
        file = open(self.temp_file, 'rb')
        dic = dict(
            filename=file.name,
            data=file.read().decode('utf-8')
        )
        file.close()
        return dic

    def rename(self, new_name, previous_name):
        try:
            self.s3.Object(self.bucket_name, new_name).copy_from(CopySource='/' + self.bucket_name + '/' +
                                                                            previous_name)
            self.s3.Object(self.bucket_name, previous_name).delete()
        except ClientError as e:
            if e.response['Error']['Code'] == 'NoSuchKey':
                raise ValueError('no file found by that name')

    def list(self):
        data = list()
        for obj in self.s3.Bucket(self.bucket_name).objects.all():
            data.append({
                "filename": obj.key,
                "size": obj.size,
                "updated_at": obj.last_modified.isoformat(),
            })
        return data
