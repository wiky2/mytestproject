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
    x=yield '这是第一次yield,第一次会直接输出本段文字返回'#每次跑到yield均会输出一个值
    print '哈哈，第一次%s'%x
    x=yield '这是第二次yield'#每次跑到yield均会输出一个值
    print '哈哈，第二次%s'%x
    x=yield '这是第三次yield'
    print '哈哈，这是第三次send!%s'%x
t=testyield()
print t.next()#跑到第一个x=yield
print t.send('第一次send')#生产者获取send的值，并且第二次yield
print t.next()#生产者第3次yield
print t.send('第二次send')
