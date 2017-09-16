#!/usr/bin/env python
# coding: utf-8
#声明必须放在前两行，# coding=<encoding name>

'''

@author: 

@license: 

@contact: 

@software: Test

@file: testList2.py

@time: 2017/8/27 上午12:28

@desc:学习老王python-控制语句
python语句讲解


1.print语句

	1.1 基本输出
	1.2 print的逗号
	1.2 输出到文件 >>为重定向



2.控制流语句（control flow）

	2.1 由条件和执行代码块组成。
		2.1.1 条件可分为决策、循环和分支
	2.2 格式（冒号与4个空格永不忘）
	2.3 if while for 函数，皆为contorl flow


3.布尔值

	3.1 控制流与真假值息息相关
		3.1.1 不要误解了真假与布尔值

	3.2 布尔值的几个最基本运算符
		3.2.1 and
		3.2.2 or
		3.2.3 is 检查共享
		3.2.4 == 检查值
		3.2.5 not
		3.2.6 其他若干比较符号


4. if语句 （控制流语句）

	
	4.1 if的组成 if else elif pass
		4.1.1 if与elif替代了switch
		4.1.2 pass	

	4.2 奇技淫巧 三元表达式
		4.2.1 x if  else
		4.2.2 活用list  
		4.2.3 三元表达式玩玩就好


'''
f=open('printtest.txt','w')
print >>f,'hahahahaha'
print >>f,'hahahahaha'
f.close()
x=3
if x:
    print 4
if x is True:
    print 5# 一个是int ，一个是bool，两个不等,检查是否引用同一个数据对象
print True and False
print True & False
print 4 if True else 3
print [4,3][True]#[假的答案，真的答案][条件]
for x in 'i am lilei':
    print x
for x in 'i am lilei'.split(' '):
    print x
for x in 'i am lilei'.split(' '):
    continue
    print x
else:
    print 'end-----'
print True and False and False and True#从左到右，遇到计算为False则为空。
a='aAsfASD'
print a.swapcase()#大写改小写
a='aA141safd2afa534234vAUJADAWWEGFDfgiuRHIUOIKNLNey52fA78447SD'
print ''.join([s for s in a if s.isdigit()])
a=a.lower()
print dict([(x,a.count(x)) for x in set(a)])#统计字符串的个数。
a_list=list(a)
set_list=list(set(a_list))
set_list.sort(key=a_list.index)#index是个函数
print ''.join(set_list)
print a[::-1]

a='aA141safd2afa534234vAUJADAWWEGFDfgiuRHIUOIKNLNey52fA78447SD'
l=sorted(a)
a_upper_list=[]
a_lower_list=[]

for x in l:
    if x.isupper():
        a_upper_list.append(x)
    elif x.islower():
        a_lower_list.append(x)
    else:
        pass
for y in a_upper_list:
    y_lower=y.lower()
    if y_lower in a_lower_list:
        a_lower_list.insert(a_lower_list.index(y_lower),y)
print ''.join(a_lower_list)

a='aA141safd2afa534234vAUJADAWWEGFDfgiuRHIUOIKNLNey52fA78447SD'
search='boy'
u=set(a)
u.update(list(search))
print len(set(a))== len(u)

a='aA141safd2afa534234vAUJADAWWEGFDfgiuRHIUOIKNLNey52fA78447SD'
search=['boy','girl']
u=set(a)
for s in search:
    u.update(list(s))
print len(set(a))== len(u)

a='aA141safd2afa534234vAUJADAWWEGFDfgiuRHIUOIKNLNey52fA78447SD'
l=([(x,a.count(x)) for x in set(a)])#
l.sort(key=lambda k:k[1],reverse=True)#k[1]代表第二个键,从0开始
print l[0][0]
print l
import os
m=os.popen('python -m this').read()
m=m.replace('\n','')
l=m.split(' ')
print [(x,l.count(x)) for x in ['be','this','than']]

size=1023147201
print '%s kb' % (size >>10)
print '%s mb' % (size >>20)

a=[1,2,3,6,8,9,10,14,17]
print str(a)#[1, 2, 3, 6, 8, 9, 10, 14, 17]
print ''.join(str(a))
print str(a)[1:-1:3]#多位数不行
print str(a)[1:-1].replace(', ','')#先去方括号，再去逗号，空格

a={'key1':'value1','key2':'value2'}
for i in a.keys():
    print i

a={'key1':'value1','key2':'value2'}
for x,y in a.items():
    print x,y

a={'a':'haha','b':'xixi','d':'haha'}
search_value='haha'
key_list=[]
for x,y in a.items():
    if y==search_value:
        key_list.append(x)
print key_list

import string
a='aA141safd2afa534234vAUJADAWWEGFDfgiuRHIUOIKNLNey52fA78447SD'
a=''.join([x for x in a if not x.isdigit()])
print sorted(a,key=string.upper)

a='i am lilei. We need to go'
c=string.maketrans('i','I')#第一个参数，第二个参数，逐一对应。
b=a.translate(c,'lei')#第二个参数是要删除的参数,翻译后要赋值
print b

with open('printtest.txt','a') as g:#不需要自己关闭。
    g.write('xixixi')








