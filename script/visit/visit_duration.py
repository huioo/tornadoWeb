#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
平均访问时长，超过0.05s的访问链接统计
"""
import os
import re
import datetime
import collections


DURATION_COUNT = collections.Counter()  # 全部访问时长统计
VISIT_IP_COUNT = collections.Counter()  # 访问ip统计
DELAY = 0.05
VISIT_LONG_COUNT = collections.Counter()    # 响应过长次数统计
VISIT_LONG_URL_COUNT = collections.Counter()    # 响应过长url统计
SUM_VISIT = {
    'sum': 0,
    'time': 0,
}


def get_log_store_path(nginx_path):
    yesterday = datetime.datetime.now() + datetime.timedelta(days=-1)
    log_store_directory_name = yesterday.strftime("%Y%m")
    path = os.path.join(nginx_path, log_store_directory_name)
    print "nginx logfile storage path [", path, "] sys sep [", os.sep, "]"
    return path


def analyse_nginx_log(path, log_name, delay):
    with open(os.path.join(path, log_name), 'r') as f:
        while True:
            logline = f.readline()
            if not logline:
                break

            pattern = r'(?:[\S]+\s)(?:[\S]+\s)(?:[\S]+\s)(?:\[.*\]\s)"([^"]+)"\s(?:.*)"(.*)"'
            regex_obj = re.compile(pattern)
            request_url, request_time = regex_obj.match(logline).groups()
            # print 'ip:', ip, 'request_time:', request_time
            request_time = float(request_time)
            try:
                # DURATION_COUNT.update([float(request_time)])
                # VISIT_IP_COUNT.update([ip])
                SUM_VISIT['sum'] += 1
                SUM_VISIT['time'] += request_time
                if request_time > delay:
                    VISIT_LONG_COUNT.update([request_time])
                    VISIT_LONG_URL_COUNT.update([request_url.split(' ')[1].split('?')[0]])
            except Exception as e:
                print logline
                print e
            # ip, request_time
            # re.findall(r'([\S]+\s)(?:[\S]+\s)(?:[\S]+\s)(?:\[.*\]\s)(?:".+"\s)"(.*)"', logline)
            # request_url, request_time
            # re.findall(r'(?:[\S]+\s)(?:[\S]+\s)(?:[\S]+\s)(?:\[.*\]\s)"([^"]+)"\s(?:.*)"(.*)"', logline)


def main():
    nginx_path = '/mnt/logs/nginx'
    nginx_log_file_path = get_log_store_path(nginx_path)
    analyse_nginx_log(nginx_log_file_path, 'access_s.log', DELAY)
    # 本地测试
    # analyse_nginx_log(os.path.dirname(os.path.realpath(__file__)), 'access.log', delay)

    # print SUM_VISIT, VISIT_LONG_COUNT
    print "平均访问时长 ", SUM_VISIT['time'] / SUM_VISIT['sum']
    print "-"*100
    print "超过{}s的访问链接：".format(DELAY)
    print '\n'.join(["{} ## 访问次数:{}".format(*item) for item in VISIT_LONG_URL_COUNT.most_common(25)])


if __name__ == '__main__':
    main()

