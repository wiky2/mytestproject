#!/usr/bin/env python
# coding: utf-8
#声明必须放在前两行，# coding=<encoding name>

'''

@author: 

@license: 

@contact: 

@software: Test

@file: testGenerator.py

@time: 2017/11/5 下午6:59

@desc:
'''
L = [x * x for x in range(10)]
g = (x * x for x in range(10))#<generator object <genexpr> at 0x10f54dc30>
print L
print g

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1

fib(30)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
    break