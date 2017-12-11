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
    x=yield '第一次会直接输出本段文字返回'#每次跑到yield均会输出一个值
    print '哈哈，第一次%s'%x
    x=yield #每次跑到yield均会输出一个值
    print '哈哈，第二次%s'%x
t=testyield()
print t.next()
print t.next()#跑到第二个x=yield
