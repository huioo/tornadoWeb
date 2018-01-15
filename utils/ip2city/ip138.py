#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import logging
import time
import signal

import tornado.gen
import tornado.httpclient

from utils.utils import utf8
import utils.httputils

area_regex = re.compile('(?is)<li>本站数据：([^<]*?)</li>')


class Ip138Finder(object):
    def __init__(self):
        self.api_url = 'http://www.ip138.com/ips1388.asp?ip={ip}&action=2'
        self.headers = {
            "User-Agent": "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Referer": "http://www.ip138.com/",
        }

    def parse_response_result(self, response):
        """
        :param response:
        :return: city ip对应的城市
        """
        city = ''
        try:
            response = utf8(response.decode('gb18030', 'ignore'))
            result = area_regex.findall(response)
            city = result[0] if result else ''
            city = city.split(' ')[0].replace('新疆维吾尔自治区', '').replace('广西壮族自治区', '')
            city = city.replace('宁夏回族自治区', '').replace('西藏自治区', '').replace('内蒙古自治区', '')
            city = city.split('省')[-1].replace('市', '')
        except:
            logging.info('taobao ip request error, response:{}'.format(response))
        return city

    @tornado.gen.coroutine
    def find(self, ip):
        result = ''
        try:
            url = self.api_url.format(ip=ip)
            response = yield utils.httputils.async_http_fetch(
                url=url,
                timeout=15,
                method='GET',
                headers=self.headers,
                validate_cert=False
            )
            result = self.parse_response_result(response)
            logging.info('[response] ip138_api_search:{} success, result:{}'.format(url, result))
        except tornado.httpclient.HTTPError as e:
            logging.error('[http] http error:"%s"' % str(e))
            result = ''
        except Exception as e:
            logging.error('[http] http error:"%s"' % str(e))
            result = ''
        raise tornado.gen.Return(result)


class TestHandler(object):

    def shutdown(self):
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

    @tornado.gen.coroutine
    def work(self):
        print 'work in'
        handler = Ip138Finder()
        ip_dict = {
            '124.117.66.2': '乌鲁木齐',
            '219.159.235.101': '南宁',
            '222.75.147.51': '银川',
            '220.182.50.226': '拉萨',
            '218.21.128.51': '赤峰',
        }
        for ip, city in ip_dict.items():
            city_result = yield handler.find(ip)
            assert city == city_result

        tornado.ioloop.IOLoop.instance().add_callback(self.shutdown)

    def sig_handler(self, sig, frame):
        tornado.ioloop.IOLoop.instance().add_callback(self.shutdown)

    def main(self):
        loop = tornado.ioloop.IOLoop.instance()
        signal.signal(signal.SIGTERM, self.sig_handler)
        signal.signal(signal.SIGINT, self.sig_handler)

        tornado.ioloop.IOLoop.current().add_timeout(
            time.time() + 2, self.work
        )
        loop.start()


if __name__ == '__main__':
    TestHandler().main()
