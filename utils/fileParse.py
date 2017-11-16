#!/usr/bin/env python
# -*- coding: utf-8 -*-
import ConfigParser

from schema import singleton


@singleton
class IniType(object):
    """ ini、cfg、cong 等类型文件解析类，文件内容格式为 [section] 和 option 键值对"""
    def __init__(self, filename=[]):
        self.parser = ConfigParser.ConfigParser()
        self.filename = filename
        self.info = self._load_info()

    def _load_info(self):
        """
        :return  结构 {section1:{optuion1:value1, optuion2:value2, ···}, ···}
        """
        info = {}
        success_l = self.parser.read(self.filename)
        if success_l:
            for section in self.parser.sections():  # [sec1, sec2,...]
                r = {}
                for option, value in self.parser.items(section):  # [(o1,v1),(o2,v2),...]
                    r[option] = value
                self.info[section] = r
        return info











if __name__ == '__main__':
    print id(IniType().parser)
    print id(IniType().parser)



