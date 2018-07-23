#!/usr/bin/env bash

#check the trackback for python webserver
#2018-07-23

date=`date  +"%Y-%m-%d-%H:%M"`
file_path=/mnt/logs
log_path=/mnt/logs/heiniubao

errorlog_list=(
log_activity_day_m0_error.log
log_activity_day_m1_error.log
log_activity_day_m2_error.log
log_activity_day_m3_error.log
log_activity_day_s0_error.log
log_activity_day_s1_error.log
log_activity_day_s2_error.log
log_activity_day_s3_error.log
)

python /mnt/logs/bug_monitor.py >> /mnt/logs/bug_monitor.log

[ -e reference.log ] || touch reference.log
cat $log_path/*_error.log > /mnt/logs/reference.log
cp /mnt/logs/reference.log  /mnt/logs/log/reference.log.$date

for errlog in ${errorlog_list[@]}
        do
            if [ -s $log_path/$errlog ]
                then
                    # cat $log_path/$errlog > /mnt/logs/errmsg.log
                    > $log_path/$errlog
            fi
        done




num=`ps aux |grep "grep"|wc -l`
if [ $num -lt 2 ]
        then
                #ls $log_path/*  | grep acti | grep _w -v | xargs grep Traceback -A30 -B4 >/mnt/logs/errmsg.log
                cat $log_path/*_error.log >/mnt/logs/errmsg.log
                [ -e reference.log ]||touch reference.log

        md5sum $file_path/errmsg.log > $file_path/mdsum/md1.txt
        md5sum $file_path/reference.log > $file_path/mdsum/md2.txt

        echo `awk -F' ' '{print NR=$1}' $file_path/mdsum/md1.txt` >$file_path/mdsum/md1.txt
        echo `awk -F' ' '{print NR=$1}' $file_path/mdsum/md2.txt` >$file_path/mdsum/md2.txt


        diff $file_path/mdsum/md1.txt  $file_path/mdsum/md2.txt > /tmp/diff.log
        status=$?

        if  [  $status = 0 ]
                then
                        echo "no error">/dev/null
                else
                        if [  -s /mnt/logs/errmsg.log ]
                                then
                                        sed -i "31s/time/$date/" email_test.py
                                        rm -f $file_path/reference.log | mv errmsg.log reference.log
#                                       cat /mnt/logs/errmsg.log >/mnt/logs/log/reference.log
                                        python email_test.py
#                                       awk -F "-" '{print NR=$1}' reference.log |sort -u |grep : >>/mnt/logs/traceback.log
#                                       echo "$date" >>/mnt/logs/traceback.log
                                        python smes.py
                                        cp /mnt/logs/reference.log  /mnt/logs/log/reference.log.$date
                                        sed -i "31s/$date/time/" email_test.py

                                        for errlog in ${errorlog_list[@]}
                                                do
                                                        cp $log_path/$errlog $file_path/log/pyerrors/$errlog.$date
                                                        cat /dev/null/ >$log_path/$errlog
                                                done
                                else
                                        echo "normal" >/dev/null
                        fi
        fi

        else
                echo "too many process are running,wait a while" >/dev/null
fi