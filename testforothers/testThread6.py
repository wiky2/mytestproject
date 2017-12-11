#!/usr/bin/env python
# coding: utf-8
#声明必须放在前两行，# coding=<encoding name>

'''

@author:

@license:

@contact:

@software: Test

@file: testLogging.py

@time: 2017/11/04 下午9:06

@desc:
推荐使用多个进程，可以使用多个cpu。
但是多线程，只能使用1个cpu
多线程复杂度高，不建议使用
'''
import time
def a():
    print 'a begin!'
    time.sleep(2)
    print 'a end!'

def b():
    print 'b begin!'
    time.sleep(2)
    print 'b end!'
b_time=time.time()
a()
b()
print time.time()-b_time

