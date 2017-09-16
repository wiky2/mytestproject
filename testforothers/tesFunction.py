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

@desc:函数名字不能命名为test，否则会进入单元测试

@注意：在Ctrl R运行前先按下 Ctrl+窗口+Alt+V进入Vim模式，如果在keymap在次设置，Run快捷键为Ctrl R,，则不用这么操作，在非vim模式可以用
这个快捷键运行
'''
import os

def fun1():
    '''
    return 必须要写
    '''
    print 'hello'
    return
def fun2(a,b,c,d,e):
    '''
    位置参数
    '''
    return a,b,c,d,e #返回元组
print fun2(1,2,3,4,5)
def fun3( a=4 ):
    '''
    
    :param a: 固定参数
    :return: 无返回
    '''
    return a
print fun3(5)
def fun4(a,b,c,d,return_data='json'):
    '''
    有默认参数
    '''
    if return_data == 'json':
        print 'json'
    elif return_data == 'xml':
        print 'xml'
    return
fun4(1,2,3,4,return_data='xml')

b = 3
def fun5():
    '''
    全局变量
    :return: 
    '''
    b = 4
    return b
def fun6():
    return b
print fun5()
print fun6()

'''
能不用global，就不用gloabal
'''
global b_global#这个定义可以删除，但是方法里面一定要有。
b_global = 3
def fun5_global():
    '''
    全局变量
    :return: 
    '''
    global b_global #如果不在方法里面声明，则下一句的变量为灰色。
    b_global = 4
    return b_global
def fun6_global():
    return b_global
print fun5_global()
print fun6_global()
print b_global
b = [1,2,3]
def fun7(list1):
    '''
    :param list1:可以修改 
    :return: 
    '''
    list1.append(4)
    return list1
b = fun7(b)#函数有返回值
print b
'''
**是字典
*是元组
'''
def fun8(**kr):
    return kr
print fun8(a=1,b=2,c=3,d=4)#返回{'a': 1, 'c': 3, 'b': 2, 'd': 4}
def fun9(*kr):
    return kr
print fun9(1,2,3,4,5,[6,8,8])#{'a': 1, 'c': 3, 'b': 2, 'd': 4}
def fun10(*kr,**kr2):
    return kr,kr2
def fun11(*kr,**kr2):#顺序必须正确。
    return kr,kr2
print fun11(1,2,3,4,5,[6,8,8],a=9,b=10,c=11)#如果a=9放在[6,8,8]前面则报错
def fun12(d,e,f,*kr,**kr2):#定义函数是的参数与调用时的书序要一致，切变量名不要搞混了，前面 定义了d，则后面必须不能定义d
    return kr,kr2
print fun12(1,2,3,4,5,[6,8,8],a=9,b=10,c=11)#如果a=9放在[6,8,8]前面则报错

'''
进阶篇 函数 第一节


1.函数基本概念

2.参数 <=> 抽象

3.参数 分为 可选参数 必须的参数

'''


'''
更复杂的需求



1 + 2 = 3


1 + 2 + 3

1 + 2+ ....+ 1000

def add(*num):
	d = 0
	for i in num:
		d += i
	return d

print add(1,2,3,4,5)



def add(*num):

	d = 0
	for i in num:
		d += i
	return d

print add(1,2,3,4,5)


print add(1,2,3)


print add(2,4,6,8,1,2,3,4,12312,12314,123,123,123)



var1
var2
var3


var1 = None

1.可选参数 是有默认值的

2.必须参数 是没有默认值的

默认值和没有默认值的区别在于  “=”



函数的健壮性

1.你永远知道你的方法会返回什么（异常处理，条件判断）
2.返回你想要的结果

'''
'''
def add(num1 ,num2):

	if isinstance(num1,int) and isinstance(num2, int):
		return num1+num2
	else:
		return '参数里有不是数字的类型'

print add('a',(1,2,3))

print add(1,2)


assert add(1,2) == 3

assert add(2,4) == 3
'''
def add1(*num):#*星号使输入任意多的参数是可以正常求和
    d=0
    for i in num:
        d+=i
    return d
print add1(1,2,3,4)
print add1(1,2,3,4,5,1234,141,5432534,870)