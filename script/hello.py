#!/usr/bin/env python
# -*- coding: utf-8 -*-


class A(object):
    a = 0
    @classmethod
    def aa(cls):
        print cls.a
        print A.a
class B(A):
    pass
class C(A):
    pass

B.a = 1
C.a = 1
B.aa()
C.aa()