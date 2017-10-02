#!/usr/bin/env python
# coding: utf-8
#声明必须放在前两行，# coding=<encoding name>

'''

@author: 

@license: 

@contact: 

@software: Test

@file: testFunction1.py

@time: 2017/10/1 下午2:59

@desc:
'''
def fun1():
    print 'hehe'

test=fun1()
print type(test)
def fun2(*num):
    '''
    接受的参数放入一个tuple 
    '''
    sum1=0
    for i in num:
        sum1=sum1+i
    return sum1
print fun2(1,2,3,4)
print fun2(1,2,3,4,5)
print fun2(1,2,3,4,5,6)
def fun3(num1,num2):
    '''
    接受2个参数，然后判断参数类型 
    '''
    if isinstance(num1,int) and isinstance(num2,int):
        sum2=num1+num2
        return sum2
    else:
        print 'wrong input number'
    return
print fun3(3,5)
# assert fun3(5,8)==14
def fun4(*num):
    '''
    接受人一多参数，返回最大、最小值 
    '''
    for x in num:
        if isinstance(x,int):
            pass
        else:
            return "参数中有非数值类型"
    num=list(num)
    num.sort()#在原有基础上排序
    print 'min:',num[0],'  max:',num[len(num)-1]
fun4(15,13,19,8,7,21,14)
def fun5(*num):
    '''
    接收任意多的参数，返回最长的 
    '''
    num=list(num)
    num.sort(key=lambda x:len(x))
    print num[len(num)-1]
fun5('boy','girl','bike','stupid')
def get_doc(module1):
    '''
    用pydoc获取帮助文档    
    '''
    import os
    command1='pydoc %s' % module1
    doc1=os.popen(command1).read()
    return doc1
print get_doc('open')
print get_doc('list')#获取帮助文档

def get_dir(folder):
    import glob
    dir1 = glob.glob('%s/*.*' % folder)
    if dir1 == []:
        return '文件夹为空或不存在'
    else:
        return dir1


print get_dir('/Users/mateseries/Documents/PycharmProjects/testforothers/')



