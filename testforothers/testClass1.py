#!/usr/bin/env python
# coding: utf-8
#声明必须放在前两行，# coding=<encoding name>

'''

@author:

@license:

@contact:

@software: Test

@file: testFunction1.py

@time: 2017/10/3 下午12:54

@desc:
面向对象，不是面向类
'''
class test(object):
    '''

    '''
    def get(self,a):#self是默认的参数，第一个永远是self
        return a

t=test()
print t.get(5)

class test2(object):
    '''

    '''
    def __init__(self,a):
        self.a=a
    def get(self,a=None):#self是默认的参数，第一个永远是self
        return self.a

t=test2('I love china')
print t.get()

class Base(object):
    def __init__(self,name):
        self.name=name#一定要加self，初始化类变量

class b(Base):
    def get_name(self):
        return self.name

new_class=b('lilei')
print new_class.get_name()

class boy(object):
    gender=1
    def __init__(self,name):
        self.name=name

class girl(object):
    gender=0
    def __init__(self,name):
        self.name=name

class love(object):
    def __init__(self,first,second):
        self.first=first
        self.second=second
    def meet(self):
        return '这是%s和%s的恋爱'%(self.first.name,self.second.name)
    def marry(self):
        return '这是%s和%s的婚姻'%(self.first.name,self.second.name)
    def children(self):
        return '这是%s和%s的孩子'%(self.first.name,self.second.name)


class normal_love(love):
    '''
    男人和女人的恋爱
    '''
    def __init__(self,first,second):
        if first.gender+second.gender!=1:
            # return '对象引入错误'#init不能返回值
            print '对象引入错误，不是男人和女人'#init不能返回值
        else:
            love.__init__(self,first,second)

class gay_love(love):
    '''
    男人和男人的恋爱
    '''
    def __init__(self,first,second):
        if first.gender+second.gender!=2:
            # return '对象引入错误'
            print '对象引入错误，不是男人和男人'#init不能返回值
        else:
            love.__init__(self, first, second)

class girl_love(love):
    '''
    女人和女人的恋爱
    '''
    def __init__(self,first,second):
        if first.gender+second.gender!=0:
            print '对象引入错误，不是女人和女人'
        else:
            love.__init__(self,first,second)
hanmeimei=girl('韩梅梅')
lilei=boy('李雷')
normal=normal_love(hanmeimei,lilei)
gay=gay_love(hanmeimei,lilei)
girl1=girl_love(hanmeimei,lilei)

print normal.meet()
print gay.meet()
print girl1.meet()

