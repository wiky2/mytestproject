#!/usr/bin/env python
# coding: utf-8
#声明必须放在前两行，# coding=<encoding name>

'''

@author:

@license:

@contact:

@software: Test

@file: testDir.py

@time: 2017/10/15 下午3:57

@desc:__all__会制约from linecache import *可以导入的函数
'''
import linecache#模块
dir(linecache)
print linecache.__file__
print linecache.getline

from linecache import getline#从模块导入函数
print getline

import urllib
print dir(urllib)
print help(urllib)
d=urllib.urlopen('http://www.baidu.com')
print d.read()

import time,datetime
t1=time.time()
print t1
print time.localtime()
print time.gmtime()
print time.strftime("%Y-%m-%d %H:%M:%S")
print time.localtime()
print time.strftime('%Z', time.localtime())
print time.strftime('%a, %d %b %Y %H:%M:%S +0000', time.localtime())

import pickle#用于数据对象序列化。
print help(pickle)
print type(pickle.dumps(t1))
print pickle.dumps(t1)
g=pickle.dumps(t1)
l1=pickle.loads(g)
print dir(l1)

#bsddb，轻量级数据库
