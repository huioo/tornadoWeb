#!/usr/bin/env bash

# tornado 日志
target_path=/mnt/logs/fls
bakdir_path=/mnt/logs/fls
namedir=`date +"%Y%m"`
enddir=$bakdir_path/$namedir
log_id=$(date -d yesterday +"%Y-%m-%d")

[ -d $enddir ]|| mkdir $enddir
cd $enddir

if [ -f "log_activity_day_m0.$log_id" ];then
    tar -zcvf $log_id.python_web.tar.gz  log_activity_day_*.$log_id
    rm -rf *.$log_id
else
    echo "log_activity_day_m0.$log_id 不存在"
fi
