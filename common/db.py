#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sqlite3
import MySQLdb
import torndb
import redis
import threading

from utils.schema import singleton

from common.constants import CONFIG_INFO


class Base(object):
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
        cur = con.cursor()
        self.dbs.update(name=con)


class RedisImpl(Base):
    def __init__(self):
        pass

    def connection(self):
        conn = redis.StrictRedis(host='localhost', port=6379,
                 db=0, password=None)
        return conn


class TorndbImpl(Base):
    def __init__(self):
        self.mydb = self.connect_mydb()

    def connect_mydb(self):
        conf = CONFIG_INFO.mydb
        # 建立和数据库系统的连接
        con = torndb.Connection(
            database=conf['db'],
            host='localhost',
            user=conf['username'],
            password=conf['password']
        )
        return con

    @staticmethod
    def query_all(dbs, sql, *args):
        """ 多个数据库进行查询 """
        all_rows = []
        for db in dbs:
            rows = db.query(sql, *args)
            if rows:
                all_rows.extend(rows)
        return all_rows


class MySQLdbImpl(Base):
    def __init__(self):
        self.mydb = self.connect_mydb()

    def connect_mydb(self):
        conf = CONFIG_INFO.mydb
        # 建立和数据库系统的连接
        con = MySQLdb.connect(
            db=conf['db'],
            host='localhost',
            user=conf['username'],
            passwd=conf['password'],
            charset=conf['charset']
        )
        return con


def __mysqldb_example():
    # 获取数据库连接
    mydb = MySQLdbImpl().mydb
    # 获取操作游标
    cursor = mydb.cursor()
    try:
        # 如果数据表已经存在使用 execute() 方法删除表。
        cursor.execute("DROP TABLE IF EXISTS `user`")
        # 执行SQL,创建一个数据库.
        cursor.execute("""create table IF NOT EXISTS `user`(
            id int auto_increment primary key not null, 
            username varchar(20),
            password varchar(20)
            );""")
        # 插入一条记录
        value = ['aaa', 'aaa']
        cursor.execute("insert into `user` (`username`, `password`) values(%s,%s)", value)
        # 插入多条记录
        values = []
        for i in range(6):
            values.append(('名字', '密码'))
            # values.append(('名字' + str(i), '密码' + str(i)))
        cursor.executemany("""insert into `user` (`username`, `password`) values(%s,%s) """, values)
        # 更新操作
        print '修改id为1的数据'
        print '修改记录数', cursor.execute("UPDATE `user` SET username='abc',password='abc' WHERE id = 1")
        # 删除操作
        print '删除id为6的数据'
        print '删除记录数', cursor.execute("DELETE FROM `user` WHERE id=6 or id=7")
        # 查询插入记录
        count = cursor.execute('select * from `user`')
        print '总共记录条数', count
        result = cursor.fetchone()
        print "只获取一条记录:", result
        results = cursor.fetchmany(2)
        print "获取5条记录，注意由于之前执行有了fetchone()，所以游标已经指到第二条记录了，即从第二条开始的所有记录"
        for r in results:
            print '1/5', r
        # 重置游标位置，0,为偏移量，正数向后偏移，复数反之；mode＝absolute | relative,默认为relative,
        cursor.scroll(0, mode='absolute')  # 相对最初进行偏移，此处为第一个位置
        # cursor.scroll(-2, mode='relative')  # 向前偏移2个位置
        # 获取所有结果
        results = cursor.fetchall()
        print '偏移过后的结果'
        for r in results:
            print r
        # 提交到数据库执行
        mydb.commit()
    except Exception as e:
        print e
        # 发生错误，回滚事务
        mydb.rollback()

    # 关闭连接，释放资源
    cursor.close()
    # 关闭数据库连接
    mydb.close()

def __torndb_example():
    mydb = TorndbImpl().mydb
    mydb.execute('create table IF NOT EXISTS blog (id int,content text)')
    content = 'wawuee'
    # mydb.execute('insert into blog(id,content) values (%d,"%s")' % (1, content))        # return 0 （成功）
    # mydb.insert("INSERT INTO blog (id,content) VALUES (%s,%s)", 2, "aaa")               # return 0 （成功）
    # mydb.insertmany("INSERT INTO blog (id,content) VALUES (%s,%s)", [[3, 'bbb'], [4, 'ccc']])   # return 0 （成功）
    # execute包括创建表，插入表，删除表等等，另外其也单独封装了insert、insertmany、update、updatemany函数，同时除了一般的
    # execute函数，其还有execute_lastrowid、execute_rowcount、executemany、executemany_lastrowid、executemany_rowcount函数。
    print mydb.query('SELECT * FROM blog')
    # [{'content': u'wawuee', 'id': 1L}, {'content': u'aaa', 'id': 2L}, ...]
    result = mydb.iter('SELECT * FROM blog')
    for i in result:
        print i # Row 对象
    # print mydb.iter('SELECT * FROM blog')


if __name__ == '__main__':
    con = TorndbImpl().mydb
    r = con.query('select * from `user`')
    print r
    con.close()

