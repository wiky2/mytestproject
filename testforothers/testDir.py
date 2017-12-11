#!/usr/bin/env python
# coding: utf-8
#声明必须放在前两行，# coding=<encoding name>

'''

@author: 

@license: 

@contact: 

@software: Test

@file: testDir.py

@time: 2017/10/15 下午2:57

@desc:
'''

import linecache#把所有函数导入到命名空间。import也是一种赋值。把所有的函数赋值到linecache里面。
print dir(linecache)
print help(dir)
from linecache import getline#从module里面导入函数，可以直接使用getline
print getline#可以直接使用。
from linecache import *#从module里面导入所有函数，可以直接使用getline
print clearcache
#如果__all__=[]这个变量里面有值，则里面的值无法被调用，只是模块的测试用例。

#包就是文件夹

