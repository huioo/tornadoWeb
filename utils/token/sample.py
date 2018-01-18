#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib


def md5_value(content):
    return hashlib.md5(content).hexdigest().upper()