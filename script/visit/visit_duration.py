#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
平均访问时长，超过0.05s的访问链接统计
"""
import os
import re
import datetime
import collections
import smtplib
from email.mime.text import MIMEText

DURATION_COUNT = collections.Counter()
VISIT_IP_COUNT = collections.Counter()
VISIT_LONG_URL_COUNT = collections.Counter()
VISIT_LONG_DURATION_MAX_TEN_URL = collections.defaultdict(list)
SUM_VISIT = {
    'sum': 0,
    'time': 0,
}
VISIT_URL_DURATION = collections.defaultdict(int)
VISIT_URL_TIMES = collections.defaultdict(int)


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

            pattern = r'([\S]+\s)(?:[\S]+\s)(?:[\S]+\s)(?:\[.*\]\s)"([^"]+)"\s(?:.*)"(.*)"'
            regex_obj = re.compile(pattern)
            ip, request_url, request_time = regex_obj.match(logline).groups()
            # print 'ip:', ip, 'request_time:', request_time
            request_time = float(request_time)
            try:
                # ip访问统计
                VISIT_IP_COUNT.update([ip])
                # DURATION_COUNT.update([float(request_time)])
                url = request_url.split(' ')[1].split('?')[0]

                SUM_VISIT['sum'] += 1
                SUM_VISIT['time'] += request_time
                if request_time > delay:
                    # 访问时间超过 delay 的url统计
                    VISIT_LONG_URL_COUNT.update([url])
                    # 统计访问某url时间过长的前10 个请求时间
                    if len(VISIT_LONG_DURATION_MAX_TEN_URL[url]) < 10:
                        VISIT_LONG_DURATION_MAX_TEN_URL[url].append(request_time)
                    else:
                        if VISIT_LONG_DURATION_MAX_TEN_URL[url][-1] < request_time:
                            VISIT_LONG_DURATION_MAX_TEN_URL[url].pop()
                            VISIT_LONG_DURATION_MAX_TEN_URL[url].append(request_time)
                    VISIT_LONG_DURATION_MAX_TEN_URL[url].sort(reverse=True)

                # 各 url 总访问时长及次数统计
                VISIT_URL_DURATION[url] += request_time
                VISIT_URL_TIMES[url] += 1

            except Exception as e:
                print logline
                print e
            # ip, request_time
            # re.findall(r'([\S]+\s)(?:[\S]+\s)(?:[\S]+\s)(?:\[.*\]\s)(?:".+"\s)"(.*)"', logline)
            # request_url, request_time
            # re.findall(r'(?:[\S]+\s)(?:[\S]+\s)(?:[\S]+\s)(?:\[.*\]\s)"([^"]+)"\s(?:.*)"(.*)"', logline)


def pattern_format_sting(pattern1, pattern2, cmp, index, *args, **kwargs):
    if cmp(index):
        return pattern1.format(*args, **kwargs)
    return pattern2.format(*args[1:], **kwargs)


def main():
    delay = 0.00
    nginx_path = '/mnt/logs/nginx'
    nginx_log_file_path = get_log_store_path(nginx_path)
    # analyse_nginx_log(nginx_log_file_path, 'access_s.log', delay)
    # 本地测试
    analyse_nginx_log(os.path.dirname(os.path.realpath(__file__)), 'access.log.tmp', delay)

    average_visit_duration_url = [
        (url, VISIT_URL_DURATION[url] / VISIT_URL_TIMES[url]) for url in VISIT_URL_TIMES.iterkeys()
    ]
    # 各url平均访问时长，所有情况（包括<>=delay的url）
    average_visit_duration_url.sort(key=lambda x: x[1], reverse=True)
    print "平均访问时长 ", SUM_VISIT['time'] / SUM_VISIT['sum']
    print "-" * 100
    # print average_visit_duration_url
    print "平均访问时长前20的url及duration情况："
    print '\n'.join(["{} ### 平均访问：次数{}，时长:{}".format(item[0], VISIT_URL_TIMES[item[0]], item[1]) for item in average_visit_duration_url[:20]])
    print "-" * 100
    # 访问次数前20个url的访问次数情况
    print "超过{}s的访问链接：".format(delay)
    print '\n'.join(["{} ## 访问次数:{}".format(*item) for item in VISIT_LONG_URL_COUNT.most_common()][:20])
    print "-" * 100
    #
    print '访问超过{}s的访问url及前10个超过{}s的duration：'.format(delay, delay*2)
    print '\n'.join(
        [pattern_format_sting('{} ## 访问时长:\n   {}', '   {}', lambda x: x is 0, i, k, duration)
            for k in VISIT_LONG_DURATION_MAX_TEN_URL.iterkeys()
                for i, duration in enumerate(VISIT_LONG_DURATION_MAX_TEN_URL[k]) if duration > delay*2]
    ),

    # 邮件信息
    receiver = [  # 接受邮箱地址
        'zhutonghui@heiniubao.com',
        'chenhailong@heiniubao.com',
        'sunze@heiniubao.com',
        'xiaowenzhao@heiniubao.com',
    ]
    title = 'nginx访问统计 {}'.format(datetime.datetime.now().strftime("%Y%m%d"))  # 标题
    body = [
        "访问总次数（记录行数） {}，总体平均访问时长 {}".format(SUM_VISIT['sum'], SUM_VISIT['time'] / SUM_VISIT['sum']),
        '</br>'.join(["{} ### 平均访问：次数{}，时长:{}".format(item[0], VISIT_URL_TIMES[item[0]], item[1]) for item in average_visit_duration_url[:50]]),
        "</br>超过{}s的访问链接：".format(delay),
        '</br>'.join(["{} ## 访问次数:{}".format(*item) for item in VISIT_LONG_URL_COUNT.most_common()][:50]),
        '</br>访问超过{}s的访问url及前10个超过{}s的duration：'.format(delay, delay*2),
        '</br>'.join(
            [pattern_format_sting('{} ## 访问时长:</br>   {}', '   {}', lambda x: x is 0, i, k, duration)
                for k in VISIT_LONG_DURATION_MAX_TEN_URL.iterkeys()
                    for i, duration in enumerate(VISIT_LONG_DURATION_MAX_TEN_URL[k]) if duration > delay*2]
        ),
    ]

    host = 'smtp.mxhichina.com'
    sender = 'report@heiniubao.com'
    pwd = 'Heiniu1003'
    msg = MIMEText('</br>'.join(body), 'html', 'utf-8')
    msg['subject'] = title
    msg['from'] = sender
    if isinstance(receiver, list):
        msg['to'] = ",".join(receiver)
        # print msg
    else:
        msg['to'] = receiver
        # print msg
    s = smtplib.SMTP(host, port=80)
    # s.starttls()
    s.login(sender, pwd)
    s.sendmail(sender, receiver, msg.as_string())
    s.quit()
    s.close()


if __name__ == '__main__':
    main()

