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
import threading,time
def testthread1(p):
    time.sleep(0.001)
    print p
ts=[]
for i in xrange(0,15):
    th=threading.Thread(target=testthread1,args=[i])#args时函数的参数。
    ts.append(th)
for i in ts:
    i.start()#如果没有join，主线程启动后，子线程也启动，并行。
# for i in ts:
#     i.join()
print 'end threading'
