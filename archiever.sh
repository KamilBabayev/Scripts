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

for i in {01..31}; do mkdir $backup_month-$i ; done
for i in {01..31}; do sshpass -p 'remote_ssh_pass' scp -rv remote_ssh_server:/var/www/html/$backup_month-$i-*  ./$backup_month-$i ; done

find  /htmlnfs/archieve-$(date +%B -d "1 month ago")  -type f -print  >  files
tar cjvf ../$backup_month-records.tar.bz2 --files-from files
cd ..
curl -T `ls *.tar.bz2`   ftp://ftpuser:ftppass@10.44.1.100/

