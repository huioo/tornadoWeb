#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app.index import handler as index
from app.python.handlers import section1 as python

HANDLERS = {
    (r'/python', python.PythonPageHandler),
    (r'/python/introduce', python.IntroduceHandler),
    (r'/python/introduce.html', python.IntroduceHandler),

    # test
    (r'/test1', index.IndexTestPageHandler),
    (r'/test2', index.PythonStudyIndexPageHandler),

    # captcha


}