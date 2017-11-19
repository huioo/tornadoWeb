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
    def initialize(self):
        super(BasePageHandler, self).initialize()
        self.is_wap = 0
        self.is_ios = False
        # self.re_user_agent = re.compile(r'(iPhone|iPod|Android|ios|iPad)')
        # self.re_ios_user_agent = re.compile(r'(iPhone|iPod|ios|iPad)')
        # self._check_is_wap()
        # self.http_referer = self.request.headers.get('Referer', '')
        # self.cnzz_site_id = 1257406960
        #
        # self.remote_ip = self.request.remote_ip
        # self.uri = self.request.uri
        # self.user_agent = self.request.headers.get('user-agent', '')
        #
        # self.hn_uv_key = self.get_cookie(USER_SIGN_COOKIE_NAME)
        # if not self.hn_uv_key:
        #     self.hn_uv_key = self._gen_uv_key_by_uuid()
        #     self.set_cookie(USER_SIGN_COOKIE_NAME, self.hn_uv_key, expires_days=365, httponly=True)
        # self.first_referer = self.get_cookie(FIRST_REFERER_COOKIE_NAME, '')
        # if not self.first_referer:
        #     if self.http_referer:
        #         self.first_referer = self.http_referer
        #     else:
        #         self.first_referer = self.request.path
        #     try:
        #         self.set_cookie(FIRST_REFERER_COOKIE_NAME, self.first_referer, expires_days=1, httponly=True)
        #     except:
        #         logging.error(traceback.format_exc())

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