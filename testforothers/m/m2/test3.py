#!/usr/bin/env python
# coding: utf-8
#声明必须放在前两行，# coding=<encoding name>

'''

@author: 

@license: 

@contact: 

@software: Test

@file: test3.py

@time: 2017/10/15 下午3:54

@desc:引用保外的模块
'''
# import m1#报错
import sys
sys.path.append('/Users/mateseries/Documents/PycharmProjects/testforothers/m')#添加搜索路径
import m1
print m1.hash()