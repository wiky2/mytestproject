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
import threading,time
mylock=threading.Lock()
num=500
def testthread1():
    global num
    for i in xrange(1,101):
        mylock.acquire()#加锁,锁放的位置对性能有影响。
        num+=1#独占操作
        mylock.release()#释放锁
    # print num
start=time.time()
l=[]
for i in xrange(0,10):
    d=threading.Thread(target=testthread1)
    d.start()
    l.append(d)
for i in l:
    i.join()
print num
print time.time()-start