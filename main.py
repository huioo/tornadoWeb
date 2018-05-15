#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time
import signal
import os.path
import logging
import tornado.httpserver
import tornado.ioloop
import tornado.autoreload
import tornado.web
import tornado.log

import tornado.options

# import page_base
# import gear
# import insurance.init
import common
# import config
from application import Application
from app.base import DefaultErrorHandler
sys.path.append(os.path.dirname(__file__))
reload(sys)
sys.setdefaultencoding('utf-8')

tornado.options.define("port", default=8080, help="run on the given port", type=int)
tornado.options.define("is_worker", default=0, help="run as the worker", type=int)
tornado.options.define("unit_test", default=0, help="run as the unit tester", type=int)

tornado.web.ErrorHandler = DefaultErrorHandler

APPLICATION = None
HTTP_SERVER = None


def main():
    global APPLICATION
    global HTTP_SERVER

    def sig_handler(sig, frame):
        tornado.ioloop.IOLoop.instance().add_callback(shutdown)

    def shutdown():
        """ 使 Tornado 在退出前先停止接收新请求（由 nginx 分发到其他端口），再尝试处理未完成的回调，最后才退出"""
        global APPLICATION
        global HTTP_SERVER
        # 不接收新的 HTTP 请求
        HTTP_SERVER.stop()

        io_loop = tornado.ioloop.IOLoop.instance()

        deadline = time.time() + 5  # 5 为关闭之前等待处理未完成请求的最大时间

        def stop_loop():
            now = time.time()
            if now < deadline and (io_loop._callbacks or io_loop._timeouts):
                io_loop.add_timeout(now + 1, stop_loop)
            else:
                # 处理完现有的 callback 和 timeout 后，可以跳出 io_loop.start() 里的循环
                io_loop.stop()

        stop_loop()
        APPLICATION.destroy()

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

    # 1.读取命令行参数
    tornado.options.parse_command_line()
    # 2.创建 tornado 应用处理类 Application
    APPLICATION = Application()
    # 3.创建 HTTPServer 对象接受Application对象参数
    HTTP_SERVER = tornado.httpserver.HTTPServer(APPLICATION, xheaders=True)
    # 4.监听指定端口 port
    HTTP_SERVER.listen(tornado.options.options.port)
    # 捕捉TERM和INT信号，使Tornado在退出前先停止接收新请求（由nginx分发到其他端口），再尝试处理未完成的回调，最后才退出
    signal.signal(signal.SIGTERM, sig_handler)
    signal.signal(signal.SIGINT, sig_handler)

    # 给app_log添加handler
    app_log_add_handler()

    logging.info("Tornado's IOLoop Instance Starting")
    # 6.IOLoop对象管理 HTTP 请求
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
