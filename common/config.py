#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os


from utils.schema import singleton
from utils.fileParse import IniTypeUtil
from utils.pathUtils import current_path


@singleton
class ConfigServer(object):
    SERVER_PORT = 8080
    IS_WORKER = 0
    UNIT_TEST = 0

    def __init__(self):
        self.config_info = self.__gen_config_info()

    @property
    def mydb(self):
        return self.config_info['mydb']

    def __gen_config_info(self):
        filenames = self.__gen_config_file_list()
        return IniTypeUtil(filename=filenames).info

    @staticmethod
    def __gen_config_file_list():
        """ config 文件路径列表 """
        result = []
        path = os.path.dirname(__file__)
        config_dir_path = os.path.join(current_path(path), 'conf')

        result.append(os.path.join(config_dir_path, 'config.ini'))
        print result
        return result

if __name__ == '__main__':
    print ConfigServer().config_info


