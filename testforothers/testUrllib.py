#!/usr/bin/env python
# coding: utf-8
#声明必须放在前两行，# coding=<encoding name>

'''

@author: 

@license: 

@contact: 

@software: Test

@file: testUrllib.py

@time: 2017/11/3 上午7:39

@desc:我们日常的脚本里会有很大HTTP的请求访问,python也自带了标准的HTTP lib库,比如urllib,urllib2但是这俩个库的API 实在是太不友好了

1.标准库的post 方法
'''

import urllib2
import urllib
url = "http://www.baidu.com"
data = {"name":"python"}
res = urllib.urlopen(url,urllib.urlencode(data))
print res.read()