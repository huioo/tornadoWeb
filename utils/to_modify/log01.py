#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import logging.handlers
import threading


class LoanLogger(object):
    _instance_lock = threading.Lock()

    @staticmethod
    def instance():
        if not hasattr(LoanLogger, "_instance"):
            with LoanLogger._instance_lock:
                if not hasattr(LoanLogger, "_instance"):
                    LoanLogger._instance = LoanLogger()
        return LoanLogger._instance

    def __init__(self):
        self.logger = logging.getLogger('heiniubao.daikuan')
        self.logger.setLevel('INFO')
        formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')

        file_handler = logging.handlers.TimedRotatingFileHandler(
            filename='./log.log',
            when='d',
            interval=1,
            backupCount=100
        )

        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)
        console = logging.StreamHandler()
        console.setFormatter(formatter)
        self.logger.addHandler(console)


if __name__ == "__main__":
    LoanLogger.instance().logger.info('test')



