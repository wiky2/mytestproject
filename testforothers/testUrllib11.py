#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: 你的名字
# Created Time : 2018年02月14日 星期三 07时58分17秒
# File Name: testUrllib11.py
# Description:加入代理处理功能
"""
import urllib2
proxyswitch=True
httpproxy_handler=urllib2.ProxyHandler({'https': '61.135.217.7:80'})
nullproxy_handler=urllib2.ProxyHandler({})
if proxyswitch:
    opener=urllib2.build_opener(httpproxy_handler)
else:
    opener=urllib2.build_opener(nullproxy_handler)
urllib2.install_opener(opener)#用了install_opener，就不用opener.open,直接yong urllib2.urlope(
request=urllib2.Request("http://www.baidu.com")
response=urllib2.urlopen(request)
print response.read()#如果是GPK，则要decode('gbk')

