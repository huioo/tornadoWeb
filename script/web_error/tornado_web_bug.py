#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
CURRENT_PATH = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.dirname(CURRENT_PATH))


import json
import time
import datetime
import urllib
import urllib2
import logging
import requests

import smtplib
from email.mime.text import MIMEText


CHUANGLAN_NEW = {
    'account': 'N2042705',
    'password': 'caXTqGpD9V0591'
}


def do_try(func, times, sleep_time=5):
    try_num = 0
    max_try_num = times
    while try_num < max_try_num:
        try:
            result = func()
            return result
        except:
            try_num += 1
            time.sleep(sleep_time)


class SmsChuanglan_New(object):
    def __init__(self):
        # 服务地址
        self.host = "https://vsms.253.com"

        # 端口号
        self.port = 80

        # 版本号
        self.version = "v1.1"

        # 查账户信息的URI
        self.balance_get_uri = "/msg/balance/json"

        # 智能匹配模版短信接口的URI
        self.sms_send_uri = "/msg/send/json"

        self.sms_param_uri = "/msg/variable/json"

        self.account = CHUANGLAN_NEW['account']
        self.password = CHUANGLAN_NEW['password']

    def parse_balance(self):
        link = self.host + self.balance_get_uri
        params = {
            "account": self.account,
            "password": self.password
        }
        data = json.dumps(params)
        request = urllib2.Request(link)
        request.add_header('Content-Type', 'application/json;charset=utf-8')
        response = urllib2.urlopen(request, data=data)
        return json.loads(response.read())['balance']

    def send_sms(self, mobile, text):
        link = self.host + self.sms_send_uri
        param_list = {
            'account': self.account,
            'password': self.password,
            'msg': text,
            'phone': mobile,
            'sendtime': '',
            'report': "false",
            'extend': ''
        }
        params = json.dumps(param_list)
        request = urllib2.Request(link)
        request.add_header('Content-Type', 'application/json;charset=utf-8')
        response = urllib2.urlopen(request, data=params)
        result = None
        try:
            result = json.loads(response.read())
            print result
        except:
            pass
        return result

    def get_user_balance(self):
        """
        取账户余额
        """
        return do_try(self.parse_balance, times=5)


def send_email(receiver, title, body):
    host = 'smtp.mxhichina.com'
    sender = 'report@heiniubao.com'
    pwd = 'Heiniu1003'
    msg = MIMEText(body, 'html', 'utf-8')
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


class Monitor(object):
    def __init__(self):
        self._need_to_fix_bug = False

    def send_sms_warning_of_bug(self, message, phone_list=None):
        if self._need_to_fix_bug and isinstance(phone_list, (tuple, list)):
            sender = SmsChuanglan_New()
            for phone in phone_list:
                sender.send_sms(phone, message)
            return len(phone_list)

    def send_email_details_of_bug(self, title, body, email_list=None):
        if self._need_to_fix_bug and isinstance(email_list, (tuple, list)):
            send_email(email_list, title, body)
            return len(email_list)


class BugWarningMonitor(Monitor):
    def __init__(self, file_names):
        super(BugWarningMonitor, self).__init__()
        self.log_paths = file_names

    def parse_web_error_log_file(self):
        sms_message, log = "", ""
        for filename in self.log_paths:
            with open(filename, 'r') as f:
                log = f.read()
                if log:
                    log += log
        if log:
            self._need_to_fix_bug = True
            sms_message = 'python web server 发现一个异常，请及时处理，详细信息在/mnt/logs/heiniubao/中查看。'
        return sms_message, log

    def warn_developers(self, phone_list=None, email_list=None):
        title = 'python web error, time {}'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        sms_message, error_log = self.parse_web_error_log_file()
        self.send_sms_warning_of_bug(sms_message, phone_list)
        self.send_email_details_of_bug(title, error_log.replace('\n', '</br>'), email_list)


if __name__ == '__main__':
    log_path = "/mnt/logs/heiniubao/"
    filelist = [
        'log_activity_day_m0_error.log',
        'log_activity_day_m1_error.log',
        'log_activity_day_m2_error.log',
        'log_activity_day_m3_error.log',
        'log_activity_day_s0_error.log',
        'log_activity_day_s1_error.log',
        'log_activity_day_s2_error.log',
        'log_activity_day_s3_error.log',
    ]
    error_log_paths = [log_path + file_name for file_name in filelist]
    phone = ['15131928891', '15351530597', '15010764190', '15732631108']
    email = ['liubingtong@heiniubao.com', 'zhutonghui@heiniubao.com', 'chenhailong@heiniubao.com', 'sunze@heiniubao.com']
    BugWarningMonitor(error_log_paths).warn_developers(phone, email)


