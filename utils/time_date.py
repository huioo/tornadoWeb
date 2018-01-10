#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime, timedelta


def get_now_str():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def get_today_str(only_date=False):
    result = get_now_str()[:10] + ' 00:00:00'
    if only_date:
        return result[:10]
    else:
        return result


def get_date_str(days=-1, format_str='%Y-%m-%d', **kwargs):
    """  weeks、days、hours、minutes、seconds、milliseconds（毫秒） 和 microseconds（微秒）  """
    now = datetime.now()
    yesterday = now + timedelta(
        days=days,
        hours=kwargs.get('hours', 0),
        minutes=kwargs.get('minutes', 0),
        seconds=kwargs.get('seconds', 0)
    )
    result = yesterday.strftime(format_str)
    return result


if __name__ == '__main__':
    print get_date_str()
