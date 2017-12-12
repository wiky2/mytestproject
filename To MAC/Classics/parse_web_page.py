#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2010-4-3

@author: Administrator
'''
import htmllib, urllib, formatter, sys, re

def parse(url, formatter):
    f = urllib.urlopen(url)
    data = f.read()
    if isinstance(data,unicode)=='true' :
        print data+'is unicode'
    else :
        if data.find('charset=gb2312'):
            print 'charset=gb2312'
            tmp=data.decode('gb2312','ignore')# ignore关键字用来忽略文中不能用来解码的全角空格
            data=tmp.encode('utf-8',)
        print data+'not unicode'
    f.close()
    p = htmllib.HTMLParser(formatter)
    p.feed(data) #取出标签
    p.close()

fmt = formatter.AbstractFormatter(formatter.DumbWriter(sys.stdout))
#parse("http://www.douban.com/",fmt)
parse("http://www.sina.com.cn/",fmt)