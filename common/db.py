#!/usr/bin/env python
# -*- coding: utf-8 -*-
import threading

from utils.schema import singleton


@singleton
class __MySqlInterface(object):
    def __init__(self):
        self.dbs = {}

    def gen_db_link(self, a):
        if a == 1:
            self.dbs.update({'a':'1'})
        if a == 2:
            self.dbs.update({'b':'2'})
        if a == 3:
            self.dbs.update({'c':'3'})


if __name__ == '__main__':
    pass
