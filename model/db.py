#!/usr/bin/env python
# -*- coding: utf-8 -*-
import threading


engine = None


class _Engine(object):
    """ 数据库引擎对象 """
    def __init__(self, connect):
        self._connect = connect

    def connect(self):

        return self._connect

