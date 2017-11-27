#!/usr/bin/env python
# -*- coding: utf-8 -*-
from week1 import handler as week1

HANDLERS = {
    (r'/week1/first', week1.FirstPageHandler)
}