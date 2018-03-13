#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app.index import handler as index
from python import handler as python

HANDLERS = {
    (r'/python', python.PythonPageHandler),
    (r'/python/introduce', python.IntroduceHandler),
    (r'/python/introduce.html', python.IntroduceHandler),

    # 实验
    (r'/test', index.IndexTestPageHandler),
}