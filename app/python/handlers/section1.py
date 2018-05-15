#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from app.base import PageBaseHandler


class PythonPageHandler(PageBaseHandler):
    def initialize(self):
        super(PythonPageHandler, self).initialize()
        self.template = 'python/index.html'

    def get(self, *args, **kwargs):
        # type: (object, object) -> object

        self.render_page()


class IntroduceHandler(PageBaseHandler):
    def initialize(self):
        super(IntroduceHandler, self).initialize()
        self.template = 'python/introduce.html'

    def get(self, *args, **kwargs):
        # type: (object, object) -> object

        self.render_page()

