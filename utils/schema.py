#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
设计模式调用工具模块
"""


def singleton(cls, *s_args, **s_kw):
    """ 类（class） 的单例模式装饰器（decorator）方法 """
    instances = {}

    def _singleton(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return _singleton
