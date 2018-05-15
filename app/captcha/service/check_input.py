#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re


VALID = 0

INVALID_HTTP_REFERER = 10000

INVALID_INPUT_PHONE = 20000
INVALID_INPUT_NAME = 20001
INVALID_INPUT_PASSWORD = 20002
INVALID_INPUT_EMAIL = 20003
INVALID_INPUT_RANDOM = 20004


RE_PHONE = re.compile('^1\d{10}$')
RE_NAME = re.compile('^[a-zA-z][a-zA-Z0-9_]{2,9}$')
RE_PASSWORD = re.compile('^[.\n]*$')
RE_EMAIL = re.compile('^\w+[-+.\w]*@\w+([-.]\w+)*\.\w+([-.]\w+)*$')
RE_DIGIT = re.compile('^\d+$')


def check_valid_request(referer, uri):
    """
    校验获取验证码请求是否安全
    :param referer:
    :param uri:
    :return:
    """
    if referer == '' or referer.find(uri) != -1:
        return INVALID_HTTP_REFERER
    return VALID


def check_exist():
    pass


def verify_random(self, r):
    """ 验证码随机串 """
    key = 'captcha_r_' + r
    value = self.redis_server.get(key)
    if value is None:
        return INVALID_INPUT_RANDOM
    self.redis_server.incr(key)
    # 验证完保留，用户可以不刷新页面再次获取验证码
    value = int(value) + 1
    if value >= self.random_valid:
        logging.info('delete key:%s' % key)
        self.redis_server.delete(key)
    return ERROR_SUCCESS


def check_phone(phone):
    if RE_PHONE.match(phone) is None:
        return INVALID_INPUT_PHONE
    return VALID


def check_name(name):
    if RE_NAME.match(name) is None:
        return INVALID_INPUT_NAME
    return VALID


def check_password(password):
    if RE_PASSWORD.match(password) is None:
        return INVALID_INPUT_PASSWORD
    return VALID


def check_email(email):
    if RE_EMAIL.match(email) is None:
        return INVALID_INPUT_EMAIL
    return VALID


