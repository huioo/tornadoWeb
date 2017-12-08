#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sqlite3

from schema import singleton


@singleton
class DataBasebUtil(object):
    def __init__(self):
        self.dbs = {}

    def gen_mysql_link(self, a):
        if a == 1:
            self.dbs.update({'a':'1'})
        if a == 2:
            self.dbs.update({'b':'2'})
        if a == 3:
            self.dbs.update({'c':'3'})

    def gen_sqlite_link(self, name, path):
        con = sqlite3.connect(path)
        return con


if __name__ == '__main__':
    DataBasebUtil().gen_sqlite_link('', '.')
