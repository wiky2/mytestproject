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
一个进程会创造一个主线程。
一个进程只有一个主线程。
python里的多线程，不是真正意义的多线程。
全局锁，保证任何时候只有一个线程在运行。
'''
import threading
def testthread1():
    print 1
a=threading.Thread(target=testthread1)#这里只用函数名
b=threading.Thread(target=testthread1)
a.start()
b.start()

a.join()
b.join()

