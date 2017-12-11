#!/usr/bin/env python
# coding: utf-8
#声明必须放在前两行，# coding=<encoding name>

'''

@author: 

@license: 

@contact: 

@software: Test

@file: testUrllib3.py

@time: 2017/11/12 下午6:46

@desc:
使用urllib2，
'''
import urllib, urllib2
def get_page_source(url):
    headers = {'Accept': '*/*',
               'Accept-Language': 'en-US,en;q=0.8',
               'Cache-Control': 'max-age=0',
               'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
               'Connection': 'keep-alive',
               'Referer': 'http://www.baidu.com/'
               }
    req = urllib2.Request(url, None, headers)
    response = urllib2.urlopen(req)
    page_source = response.read()
    return page_source
print get_page_source('http://www.163.com')