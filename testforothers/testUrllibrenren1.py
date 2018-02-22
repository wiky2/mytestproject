#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: 你的名字
# Created Time : 2018年02月16日 星期五 17时18分02秒
# File Name: testUrllibrenren1.py
# Description:
"""
import urllib
import urllib2
import cookielib
import random
cookie=cookielib.CookieJar()
cookie_handler=urllib2.HTTPCookieProcessor(cookie)
opener=urllib2.build_opener(cookie_handler)
ua_list = [
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Mozilla/5.0 (Windows NT 6.1; rv2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
        "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    ]
user_agent=random.choice(ua_list)
fullurl="http://www.renren.com/PLogin.do"
data={"email":"18682460724","password":""}
data=urllib.urlencode(data)
request=urllib2.Request(fullurl,data=data)
request.add_header("User-Agent",user_agent)
response=opener.open(request)
print response.read()

