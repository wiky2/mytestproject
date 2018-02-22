#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: 你的名字
# Created Time : 2018年02月14日 星期三 07时49分28秒
# File Name: testUrllib10.py
# Description:不通过urllib.open,而是通过自定义方式
"""
import urllib2
http_handler=urllib2.HTTPHandler(debuglever=1)#输出提调试信息:
opener=urllib2.build_opener(http_handler)
request=urllib2.Request("http://www.baidu.com")
response=opener.open(request)
print response.read()
