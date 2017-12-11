#!/usr/bin/env python
# coding: utf-8
#声明必须放在前两行，# coding=<encoding name>

'''

@author: 

@license: 

@contact: 

@software: Test

@file: testNetease_pinglun.py

@time: 2017/11/11 下午4:30

@desc:
'''
import urllib,re,bs4
def pinglun_netease(url):
    content=urllib.urlopen(url).read()
    e=content.decode('gbk')
    o=bs4.BeautifulSoup(e,'html.parser')#soup是一种特殊的tag
    tags=o.find_all('div',class_='list_item clearfix')#为了与关键字进行区分，加下划线
    result=[]
    for tag in tags:
     #'# 可以在查找的 tag 下继续使用 find_all()'
        link=tag.div.h2.a['href']
        title=tag.div.h2.a.get_text()
        created_at=tag.div.p.span.get_text()
        print link,title,created_at
        # result.append([link,title])
    # return result
print pinglun_netease('http://money.163.com/special/pinglun/')
