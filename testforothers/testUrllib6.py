#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: wiky2
# Created Time : 2018年01月28日 星期日 12时23分53秒
# File Name: testUrllib4.py
# Description:urlopen不支持构造请求
# 构造request，模拟浏览器，防止被封。
# User-Agent是爬虫、反爬虫的第一步。
"""
import urllib2
ua_headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
url='http://www.baidu.com'
request=urllib2.Request(url,headers=ua_headers)
response=urllib2.urlopen(request)
html=response.read()
print html
