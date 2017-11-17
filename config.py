#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os


from utils.schema import singleton

SERVER_PORT = 8080
IS_WORKER = 0
UNIT_TEST = 0


@singleton
class ConfigServer(object):
    pass


