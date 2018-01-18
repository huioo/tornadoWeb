#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

NAME_REGEX = re.compile(u'^[\u4E00-\u9FA5]{2,6}(?:(·|•)[\u4E00-\u9FA5]{2,6})*$')
PHONE_REGEX = re.compile('^[1-9]\d{10}$')
IDNO_REGEX = re.compile(
    '^(^[1-9]\d{7}((0\d)|(1[0-2]))(([0|1|2]\d)|3[0-1])\d{3}$)|'
    '(^[1-9]\d{5}[1-9]\d{3}((0\d)|(1[0-2]))(([0|1|2]\d)|3[0-1])((\d{4})|\d{3}[Xx])$)$'
)
MAIL_REGEX = re.compile(u'^\w+[-+.\w]*@\w+([-.]\w+)*\.\w+([-.]\w+)*$')
BIRTH_DAY = re.compile(r'\d{4}-\d{1,2}-\d{1,2}')
SEX = re.compile('[FMfm]')


def check_refer(request):
    referer = request.headers.get('Referer', '')
    if not referer:
        return False
    if referer.find(request.uri) != -1:
        return False
    return True


def check_name(name):
    try:
        name = name.decode('utf8')
    except:
        return False
    if NAME_REGEX.match(name) is None:
        return False
    return True


def check_phone(phone):
    if PHONE_REGEX.match(phone) is None:
        return False
    return True


def check_idno(idno):
    if IDNO_REGEX.match(idno) is None:
        return False
    return True


def check_birthday(birthday):
    if BIRTH_DAY.match(birthday) is None:
        return False
    return True


def check_sex(sex):
    if SEX.match(sex) is None:
        return False
    return True

