#!/usr/bin/python3
# This is very useful script. I need always to remove old months files.


import os
from datetime import datetime
date = datetime.now()

year = date.year
day = date.day
last_month = date.month - 1

archieve_dir = '/var/lib/freeswitch/recordings/' + str(year) + '-'


if day == 30:
    # print('today is last day of month')

    if date.month == 1:
        last_month = 12
        print(last_month)
        files_to_delete = archieve_dir + last_month + '-*'
        os.system('rm -rf {}'.format(files_to_delete))
    elif last_month < 10:
        last_month = '0' + str(last_month)
        print(last_month)
        files_to_delete = archieve_dir + last_month + '-*'
        print(files_to_delete)
        os.system('rm -rf {}'.format(files_to_delete))
    else:
        #last_month = date.month - 1
        files_to_delete = archieve_dir + last_month + '-*'
        os.system('rm -rf {}'.format(files_to_delete))
        print(last_month)

