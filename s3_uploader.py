#!/usr/bin/python
import os
from boto.s3.connection import S3Connection
from boto.s3.key import Key


access_key = 'AO****QPROWJWQh3ECKA'		#enter valid one
secret_key = 'ni6***iNJcwndsslfsfe************J#KLJSHweek1sbA'

my_bucket='crossbucket01'
my_file='/var/log/messages'
web_log = os.listdir('/opt/data/web/')          # dir which contains apache docker logs
db_log = os.listdir('/opt/data/db')             # dir which contains mysql docker logs

web_log_list = []
db_log_list = []

# Loops which forms correct log_file_names and sum all files in log_files variable
for file in web_log:
        web_log_list.append(os.path.join('/opt/data/web/', file))

for file in db_log:
        db_log_list.append(os.path.join('/opt/data/db/', file))

log_files = web_log_list + db_log_list
print log_files


# Creating connections creating bucket if not exists and uploading log files into bucket
conn = S3Connection(access_key, secret_key)

if not conn.get_bucket(my_bucket):
        bucket = conn.create_bucket(my_bucket)
        print "created"
else:
        bucket = conn.get_bucket(my_bucket)
        print "getted"

k = Key(bucket)
#k.key=my_file
#k.set_contents_from_filename(my_file)

for f in log_files:
        k.key=f
        k.set_contents_from_filename(f)
        print "File", f, "successfully uploaded"
