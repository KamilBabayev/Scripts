#!/usr/bin/python3
import os
import boto3
from datetime import datetime
day=str(datetime.now())[:10]

access_key = '***************'
secret_key = '************************'
subfolder = day + '/'
#subfolder='2017-09-05/'

records = '/var/lib/freeswitch/recordings'
actual_day = records + '/' + day
#actual_day = records + '/' + '2017-09-05'

print(subfolder)
print(actual_day)
print('------------------')

client = boto3.client('s3', aws_access_key_id=access_key,
                     aws_secret_access_key=secret_key)

client.put_object(Bucket='backupfs01', Key=subfolder)



def upload_files(path, subfolder):
    client = boto3.client('s3')
    session = boto3.Session(
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
    )
    s3 = session.resource('s3')
    bucket = s3.Bucket('backupfs01')

    for subdir, dirs, files in os.walk(path):
        for file in files:
            full_path = os.path.join(subdir, file)
            with open(full_path, 'rb') as data:
                key2 = subfolder + str(full_path[len(path)+1:])
                #key2 = '2017-09-04/' + str(full_path[len(path)+1:])
                #bucket.put_object(Key=full_path[len(path)+1:], Body=data)
                bucket.put_object(Key=key2, Body=data)

if __name__ == "__main__":
    upload_files(actual_day, subfolder)

