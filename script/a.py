#!/usr/bin/env python
# -*- coding: utf-8 -*-


class A(object):
    def __init__(self, a):
        self.a = a
        # print a
    pass

a = A('aaa')
b = A('aa')

print id(A('aaa'))  # 45539568  相同
print id(A('aa'))   # 45539568
print id(A('aaa').a)    # 45556440   不同
print id(A('aa').a)     # 45556480
print id(a)  # 45539456     不同
print id(b)  # 45539512

