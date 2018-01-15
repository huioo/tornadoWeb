#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import logging
import jwt


class JWTToken(object):
    def __init__(self):
        super(JWTToken, self).__init__()
        self.secret = '2026#we&free"!'
        self.algorithm = 'HS256'

    def gen_encryption_jwt_token(self, encryption, expiration_time=100 * 60 * 60):
        time_str = int(time.time()) + expiration_time
        payload = {
            'iss': 'hnb&cxl',
            'exp': time_str,
            'encryption': encryption
        }
        jwt_message = jwt.encode(payload, self.secret)
        return jwt_message

    def verify_encryption_jwt_token(self, encryption, jwt_token):
        try:
            p = jwt.decode(jwt_token, self.secret, algorithms=[self.algorithm])

        except Exception, e:
            logging.error('Exception: %s' % str(e))
            logging.error('decode jwt token fail, encryption:%s, token:%s' % (encryption, jwt_token))
            return False
        return p['encryption'] == encryption

    def gen_jwt_token(self, phone, expiration_time=100 * 60 * 60):
        time_str = int(time.time()) + expiration_time
        payload = {
            'iss': 'mjk&ztt',
            'exp': time_str,
            'phone': phone
        }
        jwt_message = jwt.encode(payload, self.secret)
        return jwt_message

    def verify_jwt_token(self, phone, jwt_token):
        try:
            p = jwt.decode(jwt_token, self.secret, algorithms=[self.algorithm])

        except Exception, e:
            logging.error('Exception: %s' % str(e))
            logging.error('decode jwt token fail, phone:%s, token:%s' % (phone, jwt_token))
            return False
        return p['phone']
