#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from app.base import PageBaseHandler

from utils.db import DataBasebUtil


class IndexPageHandler(PageBaseHandler):
    def initialize(self):
        super(IndexPageHandler, self).initialize()

    def get(self, *args, **kwargs):
        # type: (object, object) -> object
        print self.get_argument('a', '')
        self.write('hello world!')

        """ 导出 Django """
        # begin_date = request.GET['begin_date']
        # end_date = request.GET['end_date']
        # username = request.session['username']
        #
        # today = datetime.date.today().strftime('%Y/%m/%d')
        # names, data = _get_sales_info(begin_date, end_date, models.SalesDaily, username)
        # filename = '推广数据日报-{}.csv'.format(today)
        #
        # response = HttpResponse(content_type='text/csv')
        # response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)
        #
        # # 防止csv中文乱码
        # response.write(codecs.BOM_UTF8)
        #
        # writer = csv.writer(response)
        # names.insert(0, u'日期')
        # writer.writerow(names)
        # for each_day_data in data:
        #     row = [each_day_data['date']] + each_day_data['info']
        #     writer.writerow(row)
        #
        # return response


class PythonStudyIndexPageHandler(PageBaseHandler):
    def initialize(self):
        super(PythonStudyIndexPageHandler, self).initialize()
        self.template = 'index/templates/python.html'

    def get(self, *args, **kwargs):
        # type: (object, object) -> object
        # 标题
        self.body['title'] = 'learning python'.title()
        # 简介
        self.body['introduce'] = '全栈工程师'
        # 纲要
        self.body['outline'] = [
            'Python初识',
            'Python语法基础',
            'Python控制流与小实例',
            'Python函数详解',
            'Python模块实战',
            'Python文件操作实战',
            'Python异常处理实战',
            'Python面向对象编程',
        ]
        # 内容
        self.body['content'] = [
            {'title': 'Python初识', 'content': [
                {'name': 'aaaa', 'lines': []},

            ]},
            {'title': 'Python语法基础', 'content': [
                {'name': 'aaaa', 'lines': []},

            ]},
            {'title': 'Python控制流与小实例', 'content': [
                {'name': 'aaaa', 'lines': []},

            ]},
            {'title': 'Python函数详解', 'content': [
                {'name': 'aaaa', 'lines': []},

            ]},
            {'title': 'Python模块实战', 'content': [
                {'name': 'aaaa', 'lines': []},

            ]},
            {'title': 'Python文件操作实战', 'content': [
                {'name': 'aaaa', 'lines': []},

            ]},
            {'title': 'Python异常处理实战', 'content': [
                {'name': 'aaaa', 'lines': []},

            ]},
            {'title': 'Python面向对象编程', 'content': [
                {'name': 'aaaa', 'lines': []},

            ]},
        ]
        self.body['content'] = []

        # 案例
        self.body['case'] = '文档内数字批量删除程序：知识点 Python语法基础、Python控制流、函数、面向对象。'

        # 总结
        self.body['summary'] = ''

        self.render_page()


class IndexTestPageHandler(PageBaseHandler):
    def initialize(self):
        super(IndexTestPageHandler, self).initialize()
        self.template = 'demo/checked.html'

    def get(self, *args, **kwargs):
        # type: (object, object) -> object
        # self.body['is_checked'] = ''
        self.render_page()