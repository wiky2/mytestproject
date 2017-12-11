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
import threading
num=0
def testthread1():
    global num
    num+=1
    print num
for i in xrange(0,10):
    d=threading.Thread(target=testthread1)
    d.start()



