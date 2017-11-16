#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib
a = urllib.urlencode({'spam':1,'eggs':2,'bacon':'中国'})
print urllib.unquote_plus(a)