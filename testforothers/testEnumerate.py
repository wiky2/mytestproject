#!/usr/bin/env python
# coding: utf-8
#声明必须放在前两行，# coding=<encoding name>

'''

@author: 

@license: 

@contact: 

@software: Test

@file: 

@time: 2017/9/9 上午12:28

@desc:enumerate把list的索引和内容包装为dict
'''
myEnumerate_list=["a","b","c","d","e","f"]
for i,s in enumerate(myEnumerate_list):
    print 'test %d:%s'%(i,s)
