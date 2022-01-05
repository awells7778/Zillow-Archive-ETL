from secrets import s3_access_key, s3_secret_key, s3_bucket, s3_file_key, local_data_directory
from directory_list import file_list

import boto3
import os

# First, we set up our connection to our S3 bucket.

client = boto3.client('s3', aws_access__key_id = s3_access_key, aws_secret_access__key = s3_secret_key)

# Next, we loop through our local file folder to import them into our s3 bucket.

for file in os.listdir(local_data_directory):
    if '.csv' in file and file in file_list:
        upload_file_bucket = s3_bucket
        upload_file_key = s3_file_key + str(file)
        
        client.upload_file(f'{local_data_directory}\\{file}', upload_file_bucket, upload_file_key)