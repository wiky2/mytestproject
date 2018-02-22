#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: wiky2
# Created Time : 2018年01月28日 星期日 12时23分53秒
# File Name: testUrllib8.py
# Description:urlopen不支持构造请求
# 构造request，模拟浏览器，防止被封。
# User-Agent是爬虫、反爬虫的第一步。
"""
import urllib
import urllib2
import random
ua_list = [
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Mozilla/5.0 (Windows NT 6.1; rv2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
        "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
]
user_agent=random.choice(ua_list)
url='http://www.baidu.com'
keyword=raw_input("请输入需要查询的字符:")
wd={"wd":keyword}
wd=urllib.urlencode(wd)
fullurl=url+"?"+wd
request=urllib2.Request(fullurl)
request.add_header("User-Agent",user_agent)
# request.get_header("User-agent")#第一个字母大写
response=urllib2.urlopen(request)
html=response.read()
print html
