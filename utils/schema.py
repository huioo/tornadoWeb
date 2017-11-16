#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
设计模式调用工具模块
"""


def singleton(cls, *args, **kw):
    """ 单例模式装饰器方法 """
    instances = {}

    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return _singleton
