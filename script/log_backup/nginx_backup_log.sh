#!/usr/bin/env bash

#description: make the backup logs file for python_web
target_path=/mnt/logs/nginx
bakdir_path=/mnt/logs/nginx
namedir=`date +"%Y%m"`
enddir=$bakdir_path/$namedir
log_id=$(date -d yesterday +"%Y%m%d")

# get directory name
#log_path=$(date -d yesterday +"%Y%m")
[ -d $enddir ]|| mkdir $enddir

cd $enddir
ls $target_path/access.log
mv $target_path/access.log  .
/usr/sbin/nginx -s reload
cd $enddir
ls
sleep 10
tar -zcvf $log_id.access.tar.gz  access.log --remove-files