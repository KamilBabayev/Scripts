#!/bin/bash
# This script will copy old month files from remote server 
# will name folder as old month , will archieve and compress as 
# old month archieve and will upload to remote ftp server.
# NOTE:  add remote ftp same file existense check feature when you have time.

cd /htmlnfs
mkdir archieve-$(date +%B -d "1 month ago")
cd archieve-$(date +%B -d "1 month ago")
cur_year=$(date +%Y)
cur_month=$(date +%m)
prev_month=$(expr $cur_month - 1)
backup_month=$cur_year-0$prev_month
echo $backup_month

for i  in {01..02} ; do sshpass -p 'password_here'  scp -rv remote_linux_server:/var/www/html/$backup_month-$i-* . ; done

find  . -type f -print  >  files
tar cjvf $backup_month-records.tar.bz2 --files-from files
curl -T `ls *.tar.bz2`   ftp://ftpuser:ftppass@remote_ftp_server_ip/


