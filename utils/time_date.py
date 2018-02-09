#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import math
import logging

from datetime import datetime, timedelta


class CurrentTimeStringUtils(object):
    """ 当前时间的各种形式获取方法 """
    @classmethod
    def microtime(cls, get_as_float=False):
        """ 类似php的microtime()函数 """
        if get_as_float:
            return time.time()
        else:
            return '%f %d' % math.modf(time.time())

    @classmethod
    def now_str(cls, format_str='%Y-%m-%d %H:%M:%S'):
        """
        %Y-%m-%d %H:%M:%S       '2018-01-18 14:36:57'
        %Y-%m-%d                '2018-01-18'
        %Y-%m-%d 00:00:00       '2018-01-18 00:00:00'
        """
        return datetime.now().strftime(format_str)

    @classmethod
    def date_str(cls, format_str='%Y-%m-%d', days=0, **kwargs):
        """
        :param format_str:
        :param days: 时间差值，-1 昨天，+1 明天
        :param kwargs: weeks、days、hours、minutes、seconds、milliseconds（毫秒） 和 microseconds（微秒）
        :return: %Y-%m-%d   '2018-01-18'
        """
        now = datetime.now()
        yesterday = now + timedelta(
            days=days,
            **kwargs
        )
        result = yesterday.strftime(format_str)
        return result


class DateConvertedUtils(object):
    @classmethod
    def get_age(cls, birth):
        age = 0
        try:
            date_time = datetime.strptime(birth, '%Y-%m-%d')
            current_time = datetime.now()
            age = current_time.year - date_time.year
            if current_time.month < date_time.month:
                age -= 1
            elif current_time.month == date_time.month and current_time.day < date_time.day:
                age -= 1
            return age
        except:
            import traceback
            print traceback.format_exc()
            logging.info('birth:%s type is not valid' % birth)
            return age


if __name__ == '__main__':
    print DateConvertedUtils.get_age(birth="1948-09-29")
