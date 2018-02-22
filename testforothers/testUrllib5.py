#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: wiky2
# Created Time : 2018年01月28日 星期日 12时23分53秒
# File Name: testUrllib4.py
# Description:urlopen不支持构造请求
# 构造request，模拟浏览器，防止被封。
"""
import urllib2
url='http://www.baidu.com'
request=urllib2.Request(url)
response=urllib2.urlopen(request)
html=response.read()
print html
