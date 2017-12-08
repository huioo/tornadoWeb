#!/usr/bin/env python
# -*- coding: utf-8 -*-
import MySQLdb
from DBUtils import PersistentDB
from threading import local


class PersistentMySQL(object):
    """ MySQLdb模块 MySQL 数据库的 PersistentDB 连接池 """

    def __init__(self, folder=[], creator=MySQLdb, maxusage=None, setsession=None, failures=None, ping=1, closeable=False,
                 threadlocal=local, *args, **kwargs):
        """
        :param folder: xml映射文件所在的文件夹
        :param creator: 创建新的DB API 2连接的函数或DB API 2数据库适配器模块
        :param maxusage: 单个连接重复使用次数
        :param setsession: 初始化数据库会话的SQL命令参数，形式list
        :param failures: 故障转移的可选异常类或异常类元组
        :param ping: 使用ping()检查连接的时间，0从不检查，默认1请求时检查，2创建游标检查，4执行检查之前检查，7所有情况
        :param closeable: 为 True 时，允许自行关闭链接
        :param threadlocal:
        args, kwargs: 传递给 creator 的构造函数/初始化方法的参数
        """
        self.folder = folder
        self.pool = PersistentDB(creator=creator, maxusage=maxusage, setsession=setsession, failures=failures, ping=ping,
                closeable=closeable, threadlocal=threadlocal, *args, **kwargs)
        # 定义允许的操作类型
        self.crud = ['select', 'insert', 'update', 'delete']

    def get_pool(self):
        """ 获取连接池对象 """
        return self.pool

    def get_connect(self):
        """ 从连接池中获取一个连接，各线程连接独立 """
        return self.pool.connection()


if __name__ == '__main__':
    import DBUtils.PooledDB
    pool = DBUtils.PooledDB(
            creator=MySQLdb,
            maxusage=10,

            db='mydb',
            host='localhost',
            user='root',
            password='123456',
    )
    for i in range(5):
        con = pool.connection()
        cursor = con.cursor()
        print id(con)
        count = cursor.execute('select * from `user`')
        print '总共记录条数', count
        cursor.close()
        con.close()

