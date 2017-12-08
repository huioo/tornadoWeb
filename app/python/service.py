#!/usr/bin/env python
# -*- coding: utf-8 -*-
from utils.schema import singleton


@singleton
class Chapter(object):
    def __init__(self):
        self.name = 'aaa'

    @property
    def names(self):
        return

    def add(self):
        pass


if __name__ == '__main__':
    from common.db import MySQLdbImpl

    mydb = MySQLdbImpl().mydb
    cursor = mydb.cursor()
    r = cursor.execute('SELECT * FROM `python_chapter`')
    result = cursor.fetchall()
    print result[0][1]
    cursor.close()
    mydb.close()

