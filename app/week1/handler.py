#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app.base import BasePageHandler


class FirstPageHandler(BasePageHandler):
    def initialize(self):
        super(FirstPageHandler, self).initialize()
        self.template = 'week1/first.html'

    def get(self, *args, **kwargs):
        self.body['param'] = 'i\'m the first param!'
        self.body['title'] = 'Python Studying At NO.1 Week'
        self.render_page()
