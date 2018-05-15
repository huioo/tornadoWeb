#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import tornado.web

import common
from app.handler_map import HANDLERS
from app.index.handler import IndexPageHandler


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", IndexPageHandler),
        ]
        # config_instance = config.ConfigServer.instance()
        settings = dict(
            # template_path=os.path.join(os.path.dirname(__file__), "templates"),
            # static_path=os.path.join(os.path.dirname(__file__), "static"),
            template_path=os.path.join(os.path.dirname(__file__), "app"),
            static_path=os.path.join(os.path.dirname(__file__), "app"),
            # debug=False,
            debug=True,
            xsrf_cookies=False,
            cookie_secret="xFllasd120i0safsa;dfk.,';@%^&!)--=",
            login_url="/login",
        )
        tornado.web.Application.__init__(self, handlers, **settings)
        self.add_handlers(r'.*', HANDLERS)
        self.shutdown_listener = []

    def destroy(self):
        for listener in self.shutdown_listener:
            listener.destroy()

    def register_shutdown(self, listener):
        self.shutdown_listener.append(listener)

    def add_extra_headlers(self):
        self.add_transform()
