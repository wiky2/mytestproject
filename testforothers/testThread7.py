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
import time


def a():
    print 'a begin!'
    time.sleep(2)
    print 'a end!'


def b():
    print 'b begin!'
    time.sleep(2)
    print 'b end!'


# b_time=time.time()
# a()
# b()
# print time.time()-b_time
import threading

b_time = time.time()
a_thread = threading.Thread(target=a)
b_thread = threading.Thread(target=b)
a_thread.start()
b_thread.start()
a_thread.join()
b_thread.join()
print time.time() - b_time  # 花费时间只是一半。
