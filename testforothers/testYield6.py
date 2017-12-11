#!/usr/bin/env python
# coding: utf-8
#声明必须放在前两行，# coding=<encoding name>

'''

@author: 

@license: 

@contact: 

@software: Test

@file: testYield5.py

@time: 2017/11/5 下午6:12

@desc:
'''
def Fibonacci(num):
    '''
   输出Num以内的斐波那契数列
    '''
    f=[1,1]
    a=1
    b=1
    while (a+b)<=num:
        temp=a+b
        a=b
        b=temp
        yield temp

print Fibonacci(30)
for i in Fibonacci(30):
    print i