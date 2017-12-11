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
    def __enter__(self):
        print '进来'
    def __exit__(self, exc_type, exc_val, exc_tb):
        print '退出'
with sth() as s:
    print '调用开始'
