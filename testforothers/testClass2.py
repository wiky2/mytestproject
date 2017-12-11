#!/usr/bin/env python
# coding: utf-8
#声明必须放在前两行，# coding=<encoding name>

'''

@author:

@license:

@contact:

@software: Test

@file: testClass2.py

@time: 2017/10/15 下午12:54

@desc:
先实现再优化，过早优化是万恶之源。
'''
class test(object):
    @property#把函数当属性。
    def d(self):
        return 4
t=test()
print t.d#不用t.d()

class test1(object):
    @staticmethod#把静态方法当公共属性。
    def d(self):
        return 4
print test1.d

