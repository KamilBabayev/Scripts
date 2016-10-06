#!/bin/bash
# This script will copy old month files from remote server 
# will name folder as old month , will archieve and compress as 
# old month archieve and will upload to remote ftp server.
# NOTE:  add remote ftp same file existense check feature when you have time.


old_month=$(date +%B -d "1 month ago")
cd /htmlnfs
mkdir archieve-$old_month
cd archieve-$old_month
cur_year=$(date +%Y)
cur_month=$(date +%m)
prev_month=$(expr $cur_month - 1)
backup_month=$cur_year-0$prev_month
echo $backup_month

for i in {01..31}; do mkdir $backup_month-$i ; done
for i in {01..31}; do sshpass -p 'remote_ssh_here' scp -rv remote_server_ip:/var/www/html/$backup_month-$i-*  ./$backup_month-$i ; done

apath=/htmlnfs/archieve-$old_month
for i in {01..31}; do find $apath/$backup_month-$i  -type f -print  >  $apath/$backup_month-$i/files ; done

bzip_path=/htmlnfs/bzip-archieve-$old_month
mkdir $bzip_path ; cd $bzip_path

for i in {01..31}; do tar cjvf $backup_month-$i-records.tar.bz2 --files-from $apath/$backup_month-$i/files ; done
for i in $(ls *records.tar.bz2); do curl -T  $i ftp://ftpuser:ftppass@ftp_server/$backup_month/ ; done
