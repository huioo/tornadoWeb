#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import json

import tornado.gen
import tornado.httpclient

from utils.utils import utf8
import utils.httputils


class AliyunIpFinder(object):
    def __init__(self):
        self.api_url = 'https://dm-81.data.aliyun.com/rest/160601/ip/getIpInfo.json?ip={ip}'
        self.headers = {
            "Content-Type": "application/json; charset=utf-8",
            "Authorization": "APPCODE a782089840b44df694085804e1bba491"
        }

    def parse_response_result(self, response):
        """
        :param response:
        :return: city ip对应的城市
        """
        city = ''
        try:
            city = utf8(json.loads(response)['data']['city'])
            city = city.replace('市', '')  # .replace('自治区', '').replace('地区', '')
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
            logging.info('[response] taobao_api_search:{} success, result:{}'.format(url, result))
        except tornado.httpclient.HTTPError as e:
            logging.error('[http] http error:"%s"' % str(e))
            result = ''
        except Exception as e:
            logging.error('[http] http error:"%s"' % str(e))
            result = ''
        raise tornado.gen.Return(result)


class TaobaoIpFinder(object):
    def __init__(self):
        self.api_url = 'http://ip.taobao.com/service/getIpInfo.php?ip={ip}'

    def parse_response_result(self, response):
        """
        :param response:
        :return: city ip对应的城市
        """
        city = ''
        try:
            city = utf8(json.loads(response)['data']['city'])
            city = city.replace('市', '')  # .replace('自治区', '').replace('地区', '')
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
                validate_cert=False
            )
            result = self.parse_response_result(response)
            logging.info('[response] taobao_api_search:{} success, result:{}'.format(url, result))
        except tornado.httpclient.HTTPError as e:
            logging.error('[http] http error:"%s"' % str(e))
            result = ''
        except Exception as e:
            logging.error('[http] http error:"%s"' % str(e))
            result = ''
        raise tornado.gen.Return(result)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    loop = tornado.ioloop.IOLoop.instance()
    city_parse_result = TaobaoIpFinder().find('223.104.175.204')
    city_parse_result = AliyunIpFinder().find('223.104.175.204')
    loop.start()
