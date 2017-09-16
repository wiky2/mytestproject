#!/usr/bin/env python
# coding: utf-8
#声明必须放在前两行，# coding=<encoding name>

'''

@author: 

@license: 

@contact: 

@software: Test

@file: testList2.py

@time: 2017/8/18 上午12:28

@desc:学习老王python-基础篇2

'''
import sys
d="testhaha"
print sys.getrefcount('testhaha')#python内部的机理，增加他自己的引用计数
e="testhaha"
print sys.getrefcount('testhaha')#引用计数+1
d=1
print sys.getrefcount('testhaha')#引用计数-1,直到减少为0
e=2
print sys.getrefcount('testhaha')#引用计数-1,直到减少为0
e=3
print sys.getrefcount('testhaha')#引用计数不变，每个变量只能是引用计数少1

a,b,c='str','str1',4#多重赋值
a,b,c=('str','str1',4)#同上
del a#删除一个变量
#print a#报错
del b,c#联合删除
#伴随一生的函数#
a=1
print type(a)
import time
print help(time)#查询包的用法，方便自己学习别人的模块，使用前先importprint
print dir(time)#查询内置函数

print id(a)#身份证，唯一标识符
b='str'
print type(b)
c=True
print type(c)
#不可变类型：int,str,tuple
#可变类型：list,dict
e=[1,2,3]
print id(e)
e.append(4)
print id(e)#id一样
a='1234'
print int(a)+1#类型转换
print 1==1#比较操作符
print bool(1==1)
a='1234'
print len(a)
a='哈哈我是中国人'
print len(a)
a='哈'#默认是ASII，3个字节
print len(a)
a=u'哈'#为了计算中文长度，转化为unicode码
print len(a)#1个
a='哈哈哈哈'
print len(a.decode('utf-8'))#4个
print 'abcd\''#转义
print '\n'#回车
print r'\n'#不转义
a='abcde'
print a[0],a[4]#用下标操作字符串
print a[0:],a[1:],a[2:],a[:-1]#a:b,不包括b
print a[:-1]#正向、反向结合
print a[3:5]#不包括最后一个
a='abc'
print a.replace('a','ccccc')#产生一个新的对象，原始字符串是不会变的。
b='cde'
print a+b#字符串拼接，浪费资源，丑陋，违反python特性。
print 'my name is %s lilei' % 'hanmeimei'#模板拼接，占位符
print 'my name is %s lilei' % 1#数字转字符串
print '''my name is %s I'm %s''' % ('hanmeimei','ten-years hold')#按顺序对应
print ''.join([a,b])#最优秀的字符串拼接,参数是可迭代的对象。
print '.'.join([a,b])#用.拼接
d=open('a.txt','w')
d.write('hi,\n second hi.')
d.close()
d=open('a.txt','r')
print d.readline()
print d.read(5)#读取5个字节，逗号换行不算
d.close()
d=open('a.txt','r')
print d.readline()
print d.read(20)#读取5个字节，逗号换行不算
d.seek(0)#指针移动到头部
d.close()