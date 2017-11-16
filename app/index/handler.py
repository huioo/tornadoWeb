#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tornado.web


class IndexPageHandler(tornado.web.RequestHandler):
    def initialize(self):
        super(IndexPageHandler, self).initialize()
        self.is_wap = 0
        self.is_ios = False

    def get(self, *args, **kwargs):
        self.write('hello world!')
