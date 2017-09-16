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

@desc:学习老王python-基础篇，list
课程内容

列表：

1 有序的集合

2 通过偏移来索引，从而读取数据

3 支持嵌套

4 可变的类型

 

1 切片：

 
a = [1,2,3，4，5，6，7］

正向索引
反向索引
默认索引


2添加操作：

+ 生成一个新的列表

Extend  接受参数并将该参数的每个元素都添加到原有的列表中，原地修改列表而不是新建列表

Append :添加任意对象到列表的末端

Insert: 插入任意对象到列表中，可以控制插入位置。

 

3 修改：

修改列表本身只需要直接赋值操作就行。

A = [1,2,3]

A[0]=’haha’

 

4 删除操作：

Del ：我们通过索引删除指定位置的元素。

Remove：移除列表中指定值的第一个匹配值。如果没找到的话，会抛异常。

Pop：返回最后一个元素，并从list中删除它。

 

5 成员关系：

In not in我们可以判断一个元素是否在列表里。 

返回一个bool类型，元素在列表里返回true，否则返回fasle.

 

6 列表推导式：


[expr for iter_var in iterable] 

1首先迭代iterable里所有内容，每一次迭代，都把iterable里相应内容放到iter_var中，再在表达式中应用该iter_var的内容，最后用表达式的计算值生成一个列表。

比如我们要生成一个包含1到10的列表

[x for x in range(1,11)]

Range(1,11)


[expr for iter_var in iterable if cond_expr]

2加入了判断语句，只有满足条件的内容才把iterable里相应内容放到iter_var中，再在表达式中应用该iter_var的内容，最后用表达式的计算值生成一个列表。

要生成包含1到10的所有奇数列表。

range(1,11,2)

[x for x in range(1,11) if x % 2 == 1]

 

7 排序翻转：sort,reverse

 
a = [33,11,22,44]


这个方式直接修改原列表。他的返回值为none，所以

b = a.sort()

print b 输出的内容是None

我们直接输出a列表变量


list的reverse函数：反转一个list, 他的返回值为none

比如上面的列表a

b = a. reverse()

print b 输出的内容是None


直接看a列表变量能看到翻转的效果。
'''
a=[1,2,3]
b=[1,2,3,[4,5,6]]
print b
a=[1,2,3,4,5,6,7]
print a[0:4:1]#起始：终点（不含）：步长
print a[-1:-4:-1]#反向索引
print a[0::2]#没有终点，步长为2
a=[1,2,3]
b=[4,5,6]
print a+b#生成一个新列表
a.extend(b)#把b列表的每一个元素加到a中，不创建新列表
print a
a.append(4)
print a##参数加到a中，不创建新列表
a.insert(1,'ab')#在索引为1，也是第二个位置插入ab
print a
del a[0]
print a
a.remove(4)#先查找，在删除
print a
a.pop()#删除最后一个元素
a.pop(1)
print a
print 5 in a
print 8 in a
print range(11)#从0开始
print range(2,11,1)#从2开始
a=[33,11,22,44,55]
b=a.sort()#
print b#none
print a#对原先的列表进行排序，不会创建
a.reverse()
print a#对原先的列表进行翻转，不会创建
a='abc'
print list(a)
b=(1,2)
print list(b)
# print list(123)#报错，list（）参数必须是可以迭代对象。
a=xrange(1,10)#xrange对象
b=range(1,10)#list,默认起始为0
print a#xrange对象,是一个生成器，用多少，生成多少
print b#list
print a[0]#1
print b[0]#1
for m in range(1000):#先生成所有的数值
    if m==10:
        print 'sss'
        break
for m in range(1000):#只生成到10
    if m==10:
        print 'sss'
        break
print [x*x for x in range(100)]#外面的括号表示生成的是list，列表推导式
print ['No.%s' % x for x in range(100)]#外面的括号表示生成的是list，列表推导式
print [(x,y) for x in range(4) for y in range(5)]#外面的括号表示生成的是list，列表推导式
print dict([(x,y) for x in range(4) for y in range(5)])#liszt中的tuple转dict元素,每次一个tuple，tuple的第一个元素是key，第二个元素是value，后面的元素会覆盖前面的元素。
a=[1,2,3]
b=a
del a#删除a的引用关系
print b
# print a#报错
del b[:]#清空元素
print b#空列表

# '''
# 一 元组：
#
# 特点：
#
# 1 有序的集合
#
# 2 通过偏移来取数据
#
# 3 属于不可变的对象，不能在原地修改内容，没有排序，修改等操作。
#
# tuple类型转换
#
# 那为什么有列表还要有元组呢
#
#  元组不可变的好处。保证数据的安全，比如我们传给一个不熟悉的方法或者数据接口，
#  确保方法或者接口不会改变我们的数据从而导致程序问题。
#
# def info(a):
#     '''一个我们不熟悉的方法'''
#     a[0] = 'haha'
#
# a = [1,2,3]
#
# info(a)
#
# print a
#
#
# 二 集合：集合是没有顺序的概念。所以不能用切片和索引操作。
#
# 1 创建集合。set():可变的 不可变的frozenset()：
# 2 添加操作： add，update
# 3 删除 remove
# 4 成员关系 in,not in
# 6 交集，并集，差集 & | -
# 7 set去重  列表内容元素重复
#
#
# #encoding=utf-8
#
#
# ##可变集合
#
# info = set('abc')
# info.add('python')##添加单个对象到集合里
#
# print info
#
# info.update('python')##把对象里的每个元素添加到集合里
#
# print info
#
# info.remove('python')
#
# print info
#
#
# ##不可变集合
#
# t = frozenset('haha')##不能进行添加，修改和删除的操作。
#
# ##成员操作 in,not in
#
# print 'a' in info
#
# print 'h' in t
#
# print 'jay' not in info
#
# ##判断2个集合是否相等，之和元素本身有关，和顺序无关。
#
# print set('abc') == set('cba')
#
# ##并集,交集，差集
#
# print set('abc') | set('cbdef')##并集
#
# print set('abc') & set('cbdef')##交集
#
# print set('abc') - set('cbdef')##差集
#
#
# liststr = ['haha','gag','hehe','haha']
# #for循环
#
# m = []
#
# for i in liststr:
#     if i not in m:
#         m.append(i)
#
# print m
#
# m = set(liststr)
#
# print list(m)
# '''
a=(1,2,3)#tuple不可变
print a[0]#索引
print a[1:3]#切片
print dir(a)
b=list(a)#要想修改tuple，必须先转换为list
b[0]=5
a=tuple(b)#list转化为tuple
print a

def info(a):
    print 'id:%d'% id(a)
a=[1,2,3]
print 'begin------'
print id(a)
info(a)
def info2(a):
    print 'id:%d'% id(a)
    a[0]='haha'
a=[1,2,3]
print 'begin------'
print id(a)
info2(a)
print a
# def info3(a):
#     print 'id:%d'% id(a)
#     a[0]='haha'#报错
# a=(1,2,3)
# print 'begin------'
# print id(a)
# info3(a)
# print a
def info4(a):
    b=a[:]#创建一个内存区域，把a的元素赋值过去
    b[0]='haha'
    return
a=[1,2,3]
print 'begin------'
print id(a)
info4(a)
print a
a=set('abc')#参数是可迭代的对象如list,tupe,string，含有__iter__内置函数
b=set(['d','e','f'])
c=set(('g','h','i'))
a.add('python')#无返回值
print a
a.update('china')#先拆分，在添加
print a
a.remove('a')#无返回值
print a
print 'c' in a
print a & b #交集，与运算
print a & c #交集
print a | c #并集，或运算
print a - c #差集
a=[1,2,3,3,4,4,1,5,6,3,2,4]
print set(a)
print list(set(a))#去重复
a=frozenset(a)#不可变
print a
# a.add('222')#报错
# a.remove(1)
'''
字典：

字典是无序的，它不能通过偏移来存取，只能通过键来存取。

字典 = {'key':value} key：类似我们现实的钥匙，而value则是锁。一个钥匙开一个锁

特点：

内部没有顺序，通过键来读取内容，可嵌套，方便我们组织多种数据结构，并且可以原地修改里面的内容，

属于可变类型。

组成字典的键必须是不可变的数据类型，比如，数字，字符串，元组等，列表等可变对象不能作为键.

1 创建字典。{},dict()

info = {'name':'lilei', 'age': 20}

info  = dict(name='lilei',age=20)

2 添加内容 a['xx'] = 'xx'

比如  info['phone'] = 'iphone5'

3 修改内容 a['xx'] = 'xx' ,

info['phone'] = 'htc'

update 参数是一个字典的类型，他会覆盖相同键的值

info.update({'city':'beijing','phone':'nokia'})

htc 变成了nokia了

4 删除 del,clear,pop

del info['phone'] 删除某个元素

info.clear()删除字典的全部元素

info.pop('name')
 
5 in 和 has_key() 成员关系操作

比如：

1 phone in info

2  info.has_key('phone')

6 keys(): 返回的是列表，里面包含了字典的所有键

values():返回的是列表，里面包含了字典的所有值

items：生成一个字典的容器：[()]

7 get：从字典中获得一个值

info.get('name')

info.get('age2','22')
'''
dic1={'a':1,'b':2,'c':3}#注意冒号不要写成等号
print dic1
dic2={'a':[1,2,3],'b':2,'c':3}
print dic2['a'][1]
dic2['a'][1]=5#value可变，key不可变，必须用string，int，tuple等不可变对象,list不可作为key,tuple中的元素也必须为不可变。

dict3={(1,2,3):[1,2,3],(4,5,6):2,'c':3}
dict4={1:[1,2,3],2:2,'c':3}
print dict3,dict4
dict5=dict(name='lilei',age='four')#用等号后,key酒不可以用分号，类似赋值
dict5['name']='hanmeimei'
print dict5
dict5['place']='beijing'
print dict5
dict5.update(dict(name='zhoujielun',age='twenty'))#更新dict
print dict5
dict5.pop('name')
print dict5
dict5.update(dict(name='zhoujielun',age='twenty'))#更新dict
del dict5['name']
print dict5
dict5.clear()
print dict5
print 'name' in dict5
dict5.update(dict(name='zhoujielun',age='twenty'))#更新dict
print dict5.has_key('name')
print dict5.keys()
print dict5.values()
print dict5.items()#返回list，每个元素是一个tuple
print dict5.get('name')#取数据，传入key，返回值
print dict5.get('abc','none exist')
print type(dict5.get('22'))#返回<type 'NoneType'>
print dict5['name']
print dict5.pop('name','age')#如果没有找到name则返回默认的age
print dict5.pop('gender','Wrong')#如果没有找到name则返回默认的字符。列表没有这个功能。
a=[11,22,24,29]
a.append(28)
print a
a.insert(4,57)
print a
a[0]=6
print a
a.pop()
print a
a.sort()
print a
a.sort(reverse=True)
print a
b=[1,2,3,4,5]
c=b+[6,7,8]
print c
b.extend([6,7,8])#原地追加
print b
b=[1,2,3,4,5]
print b[-1:-3:-1]#不含-3
d=[]
d.append(b.pop())
d.append(b.pop())
print d
b=[1,2,3]
print 2 in b
print 6 in b
b=[23,45,22,44,25,66,78]
print [m for m in b if m%2 == 1]
print ["the content %s" % m for m in b[0:2:1]]
print [m+2 for m in b]
print range(11,34,11)#终点是想保留的数的位置+1
print [m*11 for m in range(1,4,1)]
a=(1,4,5,6,7)
print 4 in a
b=list(a)
del b[2]
print b
c=tuple(b)
print c
setinfo = set('acbdfem')
setinfo.add('abc')
print setinfo
setinfo.remove('m')
print setinfo
finfo=set('sabcdef')
print setinfo & finfo
print setinfo | finfo
studentinfo={'liming':{'name':'黎明','age':25,'fenshu':{'Chinese':89,'Math':99,'English':102}}}
print studentinfo
studentinfo['zhangqiang']={'name':'张强','age':23,'fenshu':{'Chinese':95,'Math':133,'English':135}}
print studentinfo['liming']['fenshu']['English']
b=studentinfo['zhangqiang']['fenshu'].values()
b.sort()#原地排序
print b
print studentinfo.pop('city','beijing')
print 3>>1#3的二进制往右移1位
print bin(3)
print bin(3<<4)#左移
print True & False#与运算
a=[(1,3),(2,123),(3,7886)]#把tuple的list转化为dict
print dict(a)
a=[1,2,3,4]
a=sorted(a,reverse=True)#sorted完要赋值
print a
a.sort(reverse=False)
print a
a=['123','2345','12','45','98']
a.sort(key=int,reverse=True)#排序前先用int处理
print a
a=[('a',2),('b',3),('c',4)]
a.sort(key=lambda x:x[1],reverse=True)#x代表元素，x[1]代表第2个元素。
print cmp(3,2)#(x>y)-(x<y)
print cmp(2,3)
import operator
a=[(1,2,3),(3,4,5),(23,51,12),(873,123,2)]
a.sort(key=operator.itemgetter(1,2))#以第2，3位作为索引排序
print a