#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app.base import BasePageHandler


class IndexPageHandler(BasePageHandler):
    def initialize(self):
        super(IndexPageHandler, self).initialize()
        self.is_wap = 0
        self.is_ios = False

    def get(self, *args, **kwargs):
        self.write('hello world!')
