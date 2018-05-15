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


class BaseRequestHandler(tornado.web.RequestHandler):
    def __init__(self, application, request, **kwargs):
        """
        每次访问 结果都不一致，表示不是同一个线程
        print id(self)
        """
        super(BaseRequestHandler, self).__init__(application, request, **kwargs)

    def data_received(self, chunk):
        pass


class InterfaceAccessBaseHandler(BaseRequestHandler):
    def __init__(self, application, request, **kwargs):
        """
        每次访问 结果都不一致，表示不是同一个线程
        print id(self)
        """
        # self.referer = None
        super(InterfaceAccessBaseHandler, self).__init__(application, request, **kwargs)

    def initialize(self):
        super(InterfaceAccessBaseHandler, self).initialize()
        # self.referer = self.request.headers.get('Referer', '')


class PageBaseHandler(BaseRequestHandler):

    # 初始化私有常量
    def _private_constant(self):
        self.page_intro = {}
        self.header = {}
        self.body = {}
        self.footer = {}
        self.params = {}
        self.template = 'base.html'

    # functions for initiating all pages' introduce
    def _gen_page_tdk(self):
        """title、description、keywords"""
        self.page_intro['title'] = 'huioo'
        self.page_intro['description'] = 'huioo@850628572'
        self.page_intro['keywords'] = 'huioo'

    def initialize(self):
        super(PageBaseHandler, self).initialize()
        self._private_constant()
        self._gen_page_tdk()

    # before render , integrate all parameters what need to be used
    def _integrate_parameters(self):
        """ 整合self.params变量 """
        self.params['page_intro'] = self.page_intro
        self.params['header'] = self.header
        self.params['body'] = self.body
        self.params['footer'] = self.footer

    def render_page(self):
        self._integrate_parameters()
        self.render(self.template, **self.params)


class DefaultErrorHandler(PageBaseHandler):
    """Generates an error response with ``status_code`` for all requests."""
    def initialize(self, status_code):
        self.set_status(status_code)

    def prepare(self):
        raise tornado.web.HTTPError(self._status_code)

    def write_error(self, status_code, **kwargs):
        error_msg = str(status_code) + ' 抱歉！页面出错'
        self.render('wap/wap_error.html', error_msg=error_msg)