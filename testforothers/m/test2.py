#!/usr/bin/env python
# coding: utf-8
#声明必须放在前两行，# coding=<encoding name>

'''

@author: 

@license: 

@contact: 

@software: Test

@file: test.py

@time: 2017/10/15 下午3:36

@desc:
'''
# from testforothers.m import m1
#
# print m1.hash()
import m2.url
from m2 import url#同上
# from m2 import url.get_page as get_page#报错

print dir(m2)#没有url
print m2.__file__#导入/Users/mateseries/Documents/PycharmProjects/testforothers/m/m2/__init__.pyc
print m2.url#ok,包中的模块，不能直接只导入包后，由包调用，必须要把模块也导入，即导入代码。

from m2 import *#从包里导入所有模块，先查询__all__变量，如果有，可以导入，否则不可以。