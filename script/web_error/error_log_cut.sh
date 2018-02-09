#!/usr/bin/env bash
#
date=`date  +"%Y-%m-%d"`
path=/mnt/logs/log/pyerrors

tar zcf /log/errors/pyerror.log.${date}.tar.gz  log_activity_day_*_error.log.$date*
rm -f log_activity_day_*_error.log.$date*