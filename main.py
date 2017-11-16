#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time
import signal
import os.path
import logging
# import web
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.autoreload
import tornado.web
import tornado.log

# import page_base
# import gear
# import insurance.init
import config
from app.base import DefaultErrorHandler
from app.index.handler import IndexPageHandler

sys.path.append(os.path.dirname(__file__))
reload(sys)
sys.setdefaultencoding('utf-8')

SERVER_PORT = 8080
APPLICATION = None
HTTP_SERVER = None

tornado.options.define("port", default=SERVER_PORT, help="run on the given port", type=int)
tornado.options.define("is_worker", default=0, help="run as the worker", type=int)
tornado.options.define("unit_test", default=0, help="run as the unit tester", type=int)

tornado.web.ErrorHandler = DefaultErrorHandler


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", IndexPageHandler),
        ]
        config_instance = config.ConfigServer.instance()
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            debug=False,
            xsrf_cookies=False,
            cookie_secret="xFllasd120i0safsa;dfk.,';@%^&!)--=",
            login_url="/login",
            # pycket={
            #     'engine': config_instance.pycket.get('engine'),
            #     'storage': {
            #         'host': config_instance.pycket.get('storage_host'),
            #         'port': int(config_instance.pycket.get('storage_port')),
            #         'password': config_instance.pycket.get('storage_password'),
            #         'db_sessions': int(config_instance.pycket.get('storage_db_sessions')),
            #         'db_notifications': int(config_instance.pycket.get('storage_db_notifications')),
            #         # 'max_connections': int(config_instance.pycket.get('storage_max_connections')),
            #     },
            #     'cookies': {
            #         'expires_days': int(config_instance.pycket.get('cookies_expires_days')),
            #         # 'expires': int(config_instance.pycket.get('cookies_expires')),
            #     },
            # }
        )

        tornado.web.Application.__init__(self, handlers, **settings)

        # if tornado.options.options.unit_test == 1:
        #     self.add_handlers(r".*", [(r"/test", page_base.TestPageHandler)])

        self.shutdown_listener = []
        # add init handlers here
        # gear.init()
        # insurance.init.init(self)
        # web.init(self)

    def destroy(self):
        for listener in self.shutdown_listener:
            listener.destroy()

    def register_shutdown(self, listener):
        self.shutdown_listener.append(listener)


def sig_handler(sig, frame):
    tornado.ioloop.IOLoop.instance().add_callback(shutdown)


def shutdown():
    global APPLICATION
    global HTTP_SERVER
    # 不接收新的 HTTP 请求
    HTTP_SERVER.stop()

    io_loop = tornado.ioloop.IOLoop.instance()

    deadline = time.time() + 5

    def stop_loop():
        now = time.time()
        if now < deadline and (io_loop._callbacks or io_loop._timeouts):
            io_loop.add_timeout(now + 1, stop_loop)
        else:
            # 处理完现有的 callback 和 timeout 后，可以跳出 io_loop.start() 里的循环
            io_loop.stop()

    stop_loop()
    APPLICATION.destroy()


def main():
    global APPLICATION
    global HTTP_SERVER

    tornado.options.parse_command_line()

    # config_instance = config.ConfigServer.instance()
    # config_instance.initialize(tornado.options.options.unit_test == 1)

    APPLICATION = Application()
    HTTP_SERVER = tornado.httpserver.HTTPServer(APPLICATION, xheaders=True)
    HTTP_SERVER.listen(tornado.options.options.port)

    signal.signal(signal.SIGTERM, sig_handler)
    signal.signal(signal.SIGINT, sig_handler)

    # 给app_log添加handler
    app_log_add_handler()

    loop = tornado.ioloop.IOLoop.instance()
    tornado.autoreload.start(loop)
    loop.start()


def app_log_add_handler():
    if tornado.options.options.log_file_prefix:
        file_path = tornado.options.options.log_file_prefix
        file_path = '{}_error.log'.format(file_path)
        log_handler = logging.handlers.TimedRotatingFileHandler(
            filename=file_path,
            when='midnight',
            interval=1,
            backupCount=10
        )
        log_handler.setFormatter(tornado.log.LogFormatter(color=False))
        tornado.log.app_log.setLevel('INFO')
        tornado.log.app_log.addHandler(log_handler)
    if tornado.options.options.unit_test == 1:
        tornado.log.app_log.root.setLevel('DEBUG')
        tornado.log.app_log.setLevel('DEBUG')
        tornado.log.gen_log.setLevel('DEBUG')
        tornado.log.access_log.setLevel('DEBUG')


if __name__ == "__main__":
    main()
