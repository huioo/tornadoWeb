#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from app.base import BasePageHandler


class PythonPageHandler(BasePageHandler):
    def initialize(self):
        super(PythonPageHandler, self).initialize()
        self.template = 'python/index.html'

    def get(self, *args, **kwargs):

        self.render_page()


class IntroduceHandler(BasePageHandler):
    def initialize(self):
        super(IntroduceHandler, self).initialize()
        self.template = 'python/introduce.html'

    def get(self, *args, **kwargs):

        self.render_page()

