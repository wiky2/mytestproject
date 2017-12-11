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
def is_p(t_int):
    '''
   判断是否是素数
   质数（prime number）又称素数，有无限个。
质数定义为在大于1的自然数中，除了1和它本身以外不再有其他因数。
    '''
    if t_int==1:
        return False
    elif t_int==2:
        return True
    else:
        for i in xrange(2,t_int):
            if t_int%i==0:#能够整除
                return False
        return True
print is_p(3)
print is_p(13)
print is_p(15)
print is_p(21)

for i in xrange(1,101):
    if is_p(i):
        print i
a=[i for i in xrange(1,101) if is_p(i)]
print a

def get_prime(max_num):
    return [i for i in xrange(1,max_num+1) if is_p(i)]
print get_prime(101)

def get_prime_after_num(num):
    i=0
    prime_num=[]
    for i in xrange(1,5):#不包括stop数
        num=num+1
        while is_p(num)==False:
            num=num+1
        prime_num.append(num)
    return prime_num
print get_prime_after_num(100)
print get_prime_after_num(5)