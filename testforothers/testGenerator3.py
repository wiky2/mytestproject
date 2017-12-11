#!/usr/bin/env python
# coding: utf-8
# 声明必须放在前两行，# coding=<encoding name>

'''

@author: 

@license: 

@contact: 

@software: Test

@file: testGenerator.py

@time: 2017/11/5 下午6:59

@desc:
'''


def triangles(num):
    '''
    杨辉三角
    '''
    a = [1, 1]
    b = []
    n = 2
    # print a
    while n < num:
        n = n + 1
        b=[]
        for i in xrange(1, n + 1):#一层的每一个元素
            if i == 1:
                b.append(1)
            elif i > 1 and i!=n:
                b.append(a[i - 1] + a[i - 2])
            elif i == n:
                b.append(1)
        yield b
        a=b


for x in triangles(10):
    print x
