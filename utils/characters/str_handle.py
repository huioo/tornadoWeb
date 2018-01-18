#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import logging

from str_code import to_unicode


def remove_emoj(text):
    text = to_unicode(text)
    re_pattern = re.compile(u'[^\u0000-\uD7FF\uE000-\uFFFF]', re.UNICODE)
    filtered_string = re_pattern.sub(u'', text)
    return filtered_string


def mask_name(raw_name):
    """    给名字打"*"    """
    if not raw_name:
        return ''
    name = raw_name[0] + '*' * (len(raw_name) - 1)
    return name


def mask_phone(raw_phone):
    """    给手机号打"*"    """
    if not raw_phone:
        return ''
    try:
        length = len(raw_phone)
        return raw_phone[0:3] + '*' * (length - 7) + raw_phone[length - 4:]
    except Exception, e:
        logging.error(e)
        return raw_phone


def mask_id_no(raw_id_no):
    """    给身份证打"*"    """
    if not raw_id_no:
        return ''
    try:
        length = len(raw_id_no)
        return raw_id_no[:4] + '*'*(length-8) + raw_id_no[length - 4:]
    except Exception, e:
        logging.error(e)
        return raw_id_no

