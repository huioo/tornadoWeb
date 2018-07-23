# -*- coding: utf-8 -*-
import os
import sys
import smtplib
from email.mime.text import MIMEText

CURRENT_PATH = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.dirname(CURRENT_PATH))
from limitscript.sendmessage import *

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
LOG_PATH = "/mnt/logs/fls/"


def send_msg_to_users(message):
    phone_list = ['15131928891']
    sender = SmsChuanglan_New()
    for phone in phone_list:
        sender.send_sms(phone, message)


def send_email(title, body):
    receiver = "liubingtong@heiniubao.com"
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


def main():
    for filename in filelist:
        filename = LOG_PATH + filename
        file_data = open(filename, 'r')
        log = file_data.read()
        if log != "":
            message = "python web server 发现一个异常，请及时处理，详细信息在/mnt/logs/log/中查看。"
            send_msg_to_users(message)
            send_email("fulishe web error", log)
            file_obj = open(filename, 'w')
            file_obj.write("")
            file_obj.close()
        file_data.close()


if __name__ == '__main__':
    main()
