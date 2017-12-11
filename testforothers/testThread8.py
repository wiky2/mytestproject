#!/usr/bin/env python
# coding: utf-8
# 声明必须放在前两行，# coding=<encoding name>

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
IO操作用到多线程，必须要lock,acquire,release

'''
import threading
mylock=threading.Lock()
num=0
def testthread1():
    global num
    mylock.acquire()#加锁
    num+=1#独占操作
    mylock.release()#释放锁
    print num
for i in xrange(0,10):
    d=threading.Thread(target=testthread1)
    d.start()