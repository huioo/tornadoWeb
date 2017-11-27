#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app.base import BasePageHandler


class IndexPageHandler(BasePageHandler):
    def initialize(self):
        super(IndexPageHandler, self).initialize()

    def get(self, *args, **kwargs):
        self.write('hello world!')
