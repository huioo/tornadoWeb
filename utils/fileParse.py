#!/usr/bin/env python
# -*- coding: utf-8 -*-
import ConfigParser
from cStringIO import StringIO


class IniTypeUtil(object):
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
                info[section] = r
        return info


def load_configs(column='config', config_ini_path='config.ini'):
    _cp = ConfigParser()
    fp = open(config_ini_path, 'rb')
    content = fp.read()
    fp.close()
    # 替换bom信息
    content = content.replace('\xef\xbb\xbf', '')
    fp = StringIO(content)
    _cp.readfp(fp)
    return _cp.items(column)


def get_config(section, option):
    config = ConfigParser()
    with open('config.ini') as f:
        config.readfp(f)
        return config.get(section, option)

if __name__ == '__main__':
    a = IniTypeUtil(filename=['../conf/config.ini', '../conf/configs.ini'])
    print a.info



