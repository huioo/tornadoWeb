#!/usr/local/bin/python3
# coding:utf-8

# ====================================================
# Author: chang - EMail:changbo@hmg100.com
# Last modified: 2017-5-13
# Filename: reqcounts.py
# Description: real time analysis nginx log,pymysql, Thread, logging
# blog:http://www.cnblogs.com/changbo
# ====================================================


import pymysql
import logging
from threading import Thread

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='reqcounts.log',
                    filemode='w')


db = pymysql.connect("xxx.xxxx.xxx.xxx", "xxxx", "xxxxx", "xxxxx")
cursor = db.cursor()
# cleantable = 'TRUNCATE tablename'


def analysisdb():
    listtime = []
    listip = []
    listdated = []

    sql3 = 'SELECT ip, timedd, datedd FROM reqinfo'
    cursor.execute(sql3)
    results = cursor.fetchall()
    for row in results:
        listtime.append(row[1])
        listip.append(row[0])
        listdated.append(row[2])

        try:
            # 统计1分钟内页面访问次数
            sql1 = "SELECT count(*) from reqinfo where timedd='%s' and ip='%s' and datedd='%s'" % (
                listtime[0], listip[0], listdated[0])
            sql4 = "DELETE from reqinfo where timedd='%s' and ip='%s' and datedd='%s'" % (
                listtime[0], listip[0], listdated[0])
            sql5 = "DELETE FROM reqcounts WHERE timesddd=0"
            cursor.execute(sql1)
            datad = cursor.fetchone()
            sql2 = "INSERT INTO reqcounts(ip, timesddd, timeddd, dateddd) VALUES('%s' , '%s' , '%s', '%s')" % (
            listip[0], datad[0], listtime[0], listdated[0])
            cursor.execute(sql2)
            db.commit()
            logging.debug('-----Insert success -------')
            # delete already insert data of requinfo
            cursor.execute(sql4)
            db.commit()
            del listtime[0]
            del listip[0]
            del listdated[0]
            cursor.execute(sql5)
            db.commit()
        except Exception as e:
            logging.debug(e)

if __name__ == '__main__':
        t2 = Thread(target=analysisdb)
        t2.start()