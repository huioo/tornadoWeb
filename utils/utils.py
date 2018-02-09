# -*- coding: utf-8 -*-
import random
import re
import string
import uuid
import json
import socket
import struct
import datetime
import logger
import urllib
import hashlib

import db_interface




def is_employee_phone(phone):
    """
    判断手机号是否为内部员工手机号
    :param phone:
    :return:
    """
    sql = 'SELECT phone FROM t_employees'
    db = db_interface.MysqlInstance.instance().db
    entities = db_interface.MysqlInstance.instance().query(db, sql)
    for entity in entities:
        if entity.phone == phone:
            return True

    return False


channel_re = re.compile(r'[a-z0-9]')
phone_re = re.compile(r'[0-9]{11}')


def is_valid_channel_name(channel):
    return channel_re.match(channel)


def is_valid_phone(phone):
    return phone_re.match(phone)


def gen_order_no():
    return uuid.uuid4()


def get_random_str(num=15):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(num))


def fill_zero(data, max_length=10):
    data = str(int(data))
    zero_num = max_length - len(data)
    if zero_num >= 1:
        return '0' * zero_num + str(data)
    return data


def replace_html_tag(content):
    return re.sub('<[^>]*?>', '', content)


def url_encode_dict(target_dict):
    encode_list = []
    for k, v in target_dict.items():
        if not isinstance(v, (str, unicode)):
            v = str(v)
        encode_list.append('{}={}'.format(k, urllib.quote(v)))
    return '&'.join(encode_list)


def safe_int(value, default=0):
    try:
        value = int(value)
    except:
        value = default
    return value


class FancyDict(dict):
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError, k:
            raise AttributeError, k

    def __setattr__(self, key, value):
        self[key] = value

    def __delattr__(self, key):
        try:
            del self[key]
        except KeyError, k:
            raise AttributeError, k


def ip_to_ip_num(ip):
    """
    ip转换为ip对应的数字，例如
    '101.226.103.0/25' -> 1709336320
    :param ip:
    :return:
    """
    return int(socket.ntohl(struct.unpack("I", socket.inet_aton(str(ip)))[0]))


def ip_num_to_ip(ip_num):
    """
    ip对应的数字转换为ip
    1709336320 -> '101.226.103.0/25'
    :param ip_num:
    :return:
    """
    return socket.inet_ntoa(struct.pack('I', socket.htonl(ip_num)))


class JsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        if isinstance(obj, datetime.timedelta):
            return obj.total_seconds()
        if isinstance(obj, set):
            return list(obj)
        return super(JsonEncoder, self).default(obj)


def add_extension_url_arg(url, name, value):
    if '?' in url:
        separator = '&'
    else:
        separator = '?'
    try:
        value_quote = urllib.quote(value)
    except:
        value_quote = ''
    url = '{url}{separator}{name}={value}'.format(
        url=url, separator=separator, name=name, value=value_quote
    )
    return url


def remove_ascii_hidden_character(content):
    content = re.sub('[\x00-\x1F]', '', content)
    return content


def md5_value(content):
    return hashlib.md5(content).hexdigest().upper()


if __name__ == '__main__':
    print md5_value('123')
    print md5_value('123456')
