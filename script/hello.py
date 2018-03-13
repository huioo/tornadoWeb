#!/usr/bin/env python
# -*- coding: utf-8 -*-
# from __future__ import unicode_literals


class A(dict):
    def __init__(self, a):
        self.a = a
class B(A):
    def __init__(self, b):
        self.b = b


# print B(1).b
import os
# print os.path.dirname(__file__)
import re
p = re.compile(r"industr(?:y|ies)")
r = p.findall("industry|industries|industr|industraaaa")
print r
