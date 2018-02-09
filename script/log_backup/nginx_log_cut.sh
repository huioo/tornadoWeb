#!/bin/bash
# # 零点执行该脚本  cd /mnt/logs/ && sh nginx_backup_log.sh >> /tmp/nginx_backup.log

# # Nginx 日志文件所在的目录
base_path="/mnt/logs/nginx"

# # 获取昨天的 yyyyMM：201801
yesterday=$(date -d '1 day ago' '+%Y%m')

# # 检查备份nginx日志文件的directory是否存在
yesterday_log_store_path="/mnt/logs/nginx/$yesterday"

if [ ! -d "$yesterday_log_store_path" ]
then
    mkdir -p $yesterday_log_store_path
    echo "yesterday_log_store_path is not exists"
fi

# # 切割并迁移nginx日志文件
target_log_file_path="/mnt/logs/nginx"
target_log_file_name="access_s.log"

mv ${target_log_file_path}/${target_log_file_name} ${yesterday_log_store_path}/${target_log_file_name}


# # 向 Nginx 主进程发送 USR1 信号。USR1 信号是重新打开日志文件
kill -USR1 $(cat /usr/local/nginx/logs/nginx.pid)


# # 压缩迁移过去的nginx日志文件
  #  tar -zcvf access_s_filter_3121.log.tar.gz access_s_filter_3121.log
log_id=$(date -d '1 day ago' '+%d')
  # access_s.log 截取(.log) 》》 access_s
tar_file_name_prefix=${target_log_file_name:0:-4}

tar -zcvf ${yesterday_log_store_path}/${tar_file_name_prefix}_${log_id}.log.tar.gz ${yesterday_log_store_path}/${target_log_file_name}
rm ${yesterday_log_store_path}/${target_log_file_name}
