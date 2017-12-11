#!/usr/bin/env python
# coding: utf-8
#声明必须放在前两行，# coding=<encoding name>

'''

@author: 

@license: 

@contact: 

@software: Test

@file: testUrllib2.py

@time: 2017/11/3 上午7:43

@desc:
'''

import urllib2
import cookielib
cookie = cookielib.CookieJar()
handler=urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)
res = opener.open('http://www.baidu.com')
print res.read()
