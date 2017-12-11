#!/usr/bin/env python
# coding: utf-8
# 声明必须放在前两行，# coding=<encoding name>

'''

@author:

@license:

@contact:

@software: Test

@file: testLogging.py

@time: 2017/11/05 上午11:52

@desc:
'''
def testyield():
    '''包含yield的函数是一个可迭代对象
    需要时才执行
    '''
    i=0
    a=4
    while i<a:
        x=yield i#每次跑到yield均会输出一个值
        i=i+1
t=testyield()
print t
print t.next()
print t.next()
print t.next()
print t.next()

print range(0,5)#[0, 1, 2, 3, 4]
print xrange(0,5)#生成器
for i in range(0,5):
    pass
