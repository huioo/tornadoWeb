#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 概率方面的通用工具 """
import random


def is_win_prize1(win=0.5):
    """    按几率中奖，返回结果是否中奖
    :param win: 中奖几率，取值范围0~1
    :return: True / False
    """
    result = False
    percent = random.random()
    if percent < win:
        result = True
    return result


def is_win_prize2(win=0.5, percent=0.5):
    """    克扣中奖
    :param win: 中奖几率
    :param percent: 中奖克扣百分比
    :return: True / False
    """
    result = False
    if is_win_prize1(win):
        return is_win_prize1(1-percent)
    return result


def is_win_prize3(rule={}, precision=100):
    """    多种奖品，按概率抽取其中一个
    :param rule: 奖品中奖概率规则 prize_name/win_percent 字典映射
    :param precision: 抽奖概率精度，配合中奖百分比，如0.01/100,0.281/1000
    :return: prize_name 奖品名
    """
    pond = []
    for k, v in rule.iteritems():
        for _ in xrange(int(v * precision)):
            pond.append(k)
    return random.choice(pond)


if __name__ == '__main__':
    print is_win_prize3({'a':0.3,'b':0.5,'c':0.2})
