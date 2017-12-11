#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2010-4-3

@author: Administrator
'''
import urllib
url='http://www.douban.com/'
f = urllib.urlopen(url)
data = f.read()
print data