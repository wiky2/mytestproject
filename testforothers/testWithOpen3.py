#!/usr/bin/env python
# coding: utf-8
#声明必须放在前两行，# coding=<encoding name>

'''

@author: 

@license: 

@contact: 

@software: Test

@file: testWithOpen.py

@time: 2017/11/1 上午8:00

@desc:进入时调用__enter__，退出时调用__exit__方法
'''

with open('1.txt','r') as a:
    e=a.read()
print 4

class sth(object):
    def __init__(self,xixi):
        self.a=xixi
    def __enter__(self):
        print '进来'
        return self.a
    def __exit__(self, exc_type, exc_val, exc_tb):
        print '退出'
with sth('调用的参数') as s:
    print '调用开始'
    print s

class myException(Exception):
    def __init__(self,error,msg):
        self.args=(error,msg)
        self.error=error
        self.msg=msg
try:
    raise myException(1,'my exception')
except Exception as e:
    print str(e)
