#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from functools import partial

# 分离路径，返回文件名:'/usr/path/s.txt' ==> 's.txt'
filename = lambda path: os.path.basename(path)

# 分离路径，返回目录:'/usr/path/s.txt' ==> '/usr/path'
current_path = lambda path: os.path.dirname(path)

# 路径下所有文件夹和文件:['__init__.py', '__init__.pyc', ...]
all_files = lambda path: os.listdir(current_path(path))

# 路径下所有文件
files = lambda path: [file for file in all_files(path) if os.path.isfile(file)]

# 路径下所有文件夹
dirs = lambda path: [file for file in all_files(path) if os.path.isdir(file)]

# path
#   1)__file__;  D:/tornadoWeb/utils/pathUtils.py
#   2)os.path.abspath(__file__);  路径格式化成绝对路径，当前目录 :D:\tornadoWeb\utils\pathUtils.py
#   3)os.path.realpath(__file__);  同上
# os.path.split(path)       分离目录、文件名：('D:/tornadoWeb/utils', 'pathUtils.py')
# os.path.splitext(path)    分离路径名、扩展名；('D:/tornadoWeb/utils/pathUtils', '.py')


HERE = os.path.abspath(os.path.dirname(__file__))
UPLOAD_FOLDER = 'permdir'
get_file_path = partial(os.path.join, HERE, UPLOAD_FOLDER)  # 绑定前2个传参

if __name__ == '__main__':
    path = os.path.realpath(__file__)
    print os.path.realpath('a.s')
    print __file__
