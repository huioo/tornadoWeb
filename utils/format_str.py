#!/usr/bin/env python
# -*- coding: utf-8 -*-


def format2sting(template, template2, cmp, *args, **kwargs):
    """
        按指定判断格式化 string
    >>> format2sting('{}{}{}', '{}_{}_{}', lambda x: x>0, 4,1,2,3)
    '412'
    >>> format2sting('{}{}{}', '{}_{}_{}', lambda x: x>0, -1,1,2,3)
    '1_2_3'
    >>> format2sting('{}{}{}', '{}_{}_{}', lambda x: x>0, *[-1,1,2,3])
    '1_2_3'
    >>> format2sting('{}{}{}', '{}_{}_{}', lambda x: x>0, 1,*[-1,1,2,3])
    '1-11'
    >>> format2sting('{}{}{a}', '{}_{}_{a}', lambda x: x>0, 1,*[-1,1,2,3],**{'a':10, 'b': 20})
    '1-110'
    :param template: 默认模板
    :param template2: 特殊模板
    :param cmp: 判断使用何模板的判断方法
    :return: str
    """
    if template2 and cmp:
        if cmp(args[0]):
            return template.format(*args[1:], **kwargs)
        return template2.format(*args[1:], **kwargs)


