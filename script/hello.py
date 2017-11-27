#!/usr/bin/env python
# -*- coding: utf-8 -*-


class A(dict):
    def __init__(self, a):
        self.a = a
class B(A):
    def __init__(self, b):
        self.b = b


print B(1).a
