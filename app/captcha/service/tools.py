#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import threading

from app.captcha.service.check_input import check_phone


class CaptchaManager(object):
    _instance_lock = threading.Lock()

    def __init__(self, storge):
        """

        :param storge:
        """
        super(CaptchaManager, self).__init__()
        self.storge = storge

    @staticmethod
    def instance(*args, **kwargs):
        """Returns a global `CaptchaManager` instance.

        Most applications have a single, global `CaptchaManager` running on the
        main thread.  Use this method to get this instance from
        another thread.
        """
        if not hasattr(CaptchaManager, "_instance"):
            with CaptchaManager._instance_lock:
                if not hasattr(CaptchaManager, "_instance"):
                    # New instance after double check
                    CaptchaManager._instance = CaptchaManager(*args, **kwargs)
        return CaptchaManager._instance

    def verify_random_string(self, r):
        key = 'captcha_r_' + r
        value = self.redis_server.get(key)
        if value == None:
            return
        self.redis_server.incr(key)
        # 验证完保留，用户可以不刷新页面再次获取验证码
        value = int(value) + 1
        if value >= self.random_valid:
            logging.info('delete key:%s' % key)
            self.redis_server.delete(key)
        return

    def gen_captcha(self, phone, remote_ip, r):
        logging.info('gen captcha, phone:%s' % phone)

        if check_phone(phone) > 0:
            return None


if __name__ == '__main__':
    print id(CaptchaManager('a').storge), CaptchaManager('c').storge
    print id(CaptchaManager('c').storge), CaptchaManager('c').storge
    print id(CaptchaManager('b').storge), CaptchaManager('b').storge


