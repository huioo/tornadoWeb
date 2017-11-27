#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import time
import uuid
import random
import urllib
import hashlib
import logging
import traceback
import tornado.web


class BasePageHandler(tornado.web.RequestHandler):
    def __init__(self, application, request, **kwargs):
        self.page_intro = {}
        self.header = {}
        self.body = {}
        self.footer = {}
        self.params = {}
        self.template = 'base.html'

        super(BasePageHandler, self).__init__(application, request, **kwargs)

    def initialize(self):
        super(BasePageHandler, self).initialize()
        self._gen_page_title()
        self._gen_page_description()
        self._gen_page_keywords()

    def render_page(self):
        self._integrate_parameters()
        self.render(self.template, **self.params)

# functions for initiating all pages' introduce
    def _gen_page_title(self):
        self.page_intro['title'] = 'huioo'

    def _gen_page_description(self):
        self.page_intro['description'] = 'huioo@850628572'

    def _gen_page_keywords(self):
        self.page_intro['keywords'] = 'huioo'

# before render , integrate all parameters what need to be used
    def _integrate_parameters(self):
        """ 整合self.params变量 """
        self.params['page_intro'] = self.page_intro
        self.params['header'] = self.header
        self.params['body'] = self.body
        self.params['footer'] = self.footer

    def data_received(self, chunk):
        pass


class DefaultErrorHandler(BasePageHandler):
    """Generates an error response with ``status_code`` for all requests."""
    def initialize(self, status_code):
        self.set_status(status_code)

    def prepare(self):
        raise tornado.web.HTTPError(self._status_code)

    def write_error(self, status_code, **kwargs):
        error_msg = str(status_code) + ' 抱歉！页面出错'
        self.render('wap/wap_error.html', error_msg=error_msg)