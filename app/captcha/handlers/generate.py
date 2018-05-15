#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app.base import InterfaceAccessBaseHandler
from app.captcha.service.check_input import check_valid_request
from common.db import RedisImpl


class BaseHandler(InterfaceAccessBaseHandler):
    def initialize(self):
        self.captcha_store = RedisImpl()

    def post(self, *args, **kwargs):
        referer = self.request.headers.get('Referer', '')
        check_valid_request(referer, self.request.uri)

        # generate captcha


        # send sms


        # return response













