#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: 你的名字
# Created Time : 2018年02月19日 星期一 07时44分36秒
# File Name: testUrllib-bak.py
# Description:我们日常的脚本里会有很大HTTP的请求访问,python也自带了标准的HTTP lib库,比如urllib,urllib2但是这俩个库的API 实在是太不友好了
"""
import urllib
url = "http://www.baidu.com"
data = {"name":"python"}
res = urllib.urlopen(url,urllib.urlencode(data))
print res.read()
