import os

aws_access_key_id = os.environ.get('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY')

region = "us-east-2"

bucket_name = 'leucinetechapp'

default_storage_directory = 'media/'

temp_file = 'media/tmp'
