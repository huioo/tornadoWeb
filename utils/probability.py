#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 概率方面的通用工具 """
import random


def is_win_prize(win=0.5):
    """ 按几率中奖，返回结果是否中奖 """
    result = False
    percent = random.random()
    if percent < win:
        result = True
    return result


if __name__ == '__main__':
    print is_win_prize(1.9)
