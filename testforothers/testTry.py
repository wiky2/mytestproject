#!/usr/bin/env python
# coding: utf-8
#声明必须放在前两行，# coding=<encoding name>

'''

@author: 

@license: 

@contact: 

@software: Test

@file: testTry.py

@time: 2017/10/15 下午4:47

@desc:
'''
try:
    print 1
except:
    print u'haha'
else:
    print 'hello'
finally:#不管前面是否有异常，总会执行
    print 'xixi'#执行完后就结束了。

import urllib
sth_url='http://www.baidu.com'
try:
    d=urllib.urlopen(sth_url)
except IOError:
    print '哈哈，出错了，第一种错误'
except 2:
    print '第二种错误'
else:
    content=d.read()
    print content
finally:
    d.close()

import sys
try:
    a=3
    assert a==4
except:
    exc=sys.exc_info()#tuple
    print exc

assert 1>2,'1>2,错误'