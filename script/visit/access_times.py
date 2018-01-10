#!/usr/local/bin/python3
# coding:utf-8

# ====================================================
# Author: chang - EMail:changbo@hmg100.com
# Last modified: 2017-5-13
# Filename: accesstimes.py
# Description: real time analysis nginx log,base time, os, re, pymysql, Thread
# blog:http://www.cnblogs.com/changbo
# ====================================================

"""
需求：每隔1分钟读取nginx日志文件
notice:
模拟日志切割过程中初始化脚本参数
cp access.log access2017xxxx.log  && echo > access.log && echo '0'> offset1.txt
"""


import time
import os
import re
import pymysql
from threading import Thread
import logging
# from django.db import connection

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='accesstimes.log',
                    filemode='w')

keypage = ['/sys/get_user.do']
keyIP = ['127.0.0.1', '::1', '124.126.91.243']
engdate = {'Jan': '1', 'Feb': '2', 'Mar': '3', 'Apr': '4', 'May': '5', 'Jun': '6', 'Jul': '7', 'Aug': '8', 'Sept': '9',
           'Oct': '10', 'Nov': '11', 'Dec': '12'}

# db = pymysql.connect("xxx.xxx.xxx.xxx", "xxx", "xxxxxx", "yunwei")
# cursor = db.cursor()
# cleantable = 'TRUNCATE abnormal'


def date_format(nginxdate):
    """
    nginxdate format: [08/Jan/2018
    """
    print nginxdate
    day = (nginxdate.split('[')[1]).split('/')[0]
    month = engdate[(nginxdate.split('[')[1]).split('/')[1]]
    year = (nginxdate.split('[')[1]).split('/')[2]
    return year + '-' + month + '-' + day


def handle_line(logline):
    susptmp = logline.split(" ")
    if len(susptmp) > 2 and susptmp[0] not in keyIP:
        del susptmp[1:3]   # 删除【 - - 】
        if len(susptmp) > 2:
            ip = susptmp[0]
            # date format: [08/Jan/2018:14:17:33 +0800] , time1 format: 14:17:33 +0800, dated format: 2018-1-8
            time1 = (susptmp[1].split(':', 1))[1][:-1]
            dated = date_format((susptmp[1].split(':', 1))[0])
            # 61.158.149.71     14:17:3     2018-1-08
            logging.debug('Insert success! {} {} {}'.format(ip, time1, dated))

            # sql = "INSERT INTO reqinfo(ip, timedd, datedd) VALUES('%s', '%s', '%s')" % (ip, time1, dated)
            # try:
            #     cursor.execute(sql)
            #     db.commit()
            #     logging.debug('Insert success!')
            # except Exception as e:
            #     logging.debug(e)


# online analysis log
def analysis_log():
    with open('access.log') as f1:
        while True:
            # get offset, and jump the Specify log line
            last_offset =  ()
            f1.seek(int(last_offset))
            # 获取该行偏移量
            where = f1.tell()
            line = f1.readline()
            write_offset(str(where))
            if not line:
                time.sleep(10)
                # f1.seek(where)
            else:
                # 处理该行，并获取改行的偏移量且写入文件
                handle_line(line)
                nowoffset = f1.tell()
                write_offset(str(nowoffset))


def get_offset():
    """ get log offset """
    with open('offset1.txt') as f2:
        offset = f2.readline()
        return offset


def write_offset(number):
    """ write log offset """
    with open('offset1.txt', 'w+') as f3:
        f3.write(number)
        f3.flush()


if __name__ == '__main__':
    if not os.path.exists('offset1.txt'):
        with open("offset1.txt", 'w') as f:
            f.write('0')

    t1 = Thread(target=analysis_log)
    t1.start()
