#!/usr/bin/env python
# -*- coding: utf-8 -*-
from fabric.api import run
from fabric.operations import local
from fabric.context_managers import remote_tunnel


def hello():
    print("Hello fab!")

def hostname():
    run('hostname')

def ls(path='.'):
    local('ls {}'.format(path))

# 内存，磁盘使用，mysql，redis，日志





