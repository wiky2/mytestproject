#!/usr/bin/env python
# coding: utf-8
#声明必须放在前两行，# coding=<encoding name>

'''

@author: 

@license: 

@contact: 

@software: Test

@file: testWoshiwufeng1.py

@time: 2017/11/18 下午9:55

@desc:
'''
# 背景
#
# PHP的$和->让人输入的手疼（PHP确实非常简洁和强大，适合WEB编程），Ruby的#、@、@@也好不到哪里（OO人员最该学习的一门语言）。
# Python应该是写起来最舒服的动态语言了，一下是一些读书笔记，最后会介绍一下高级的用法：Mixin、Open Class、Meta Programming和AOP。
# 文中有些地方是用2.7开发的，如果您安装的是3.x，有几点需要注意：
# print "xxx" 要换成 print("xxx")
# __metaclass__ = type 删除掉。
你好，世界！
# coding=utf-8

print "你好，世界。"
 # 乘方
print 2**10
# 变量
var = 1
print var

var  = "吴峰"
print var
# 注：这里的var = xxxx不叫变量赋值，而叫变量绑定，python维护了一个符号表（变量名）以及符合对应的值，这个对应关系就叫做绑定，一个符号可以绑定任意类型的值。
# 获取用户输入
# 1 #获取用户输入
x = input("x:")
y = input("y:")

print x*y
# 注：input接受的是Python代码，输入中可以访问当前执行环境中的变量，如果想获取原始输入需要使用 raw_input。
# 函数定义
def say_b():
    print "b"
# 强类型
# Javascript和Php是弱类型的，Python和Ruby是强类型的。弱类型允许不安全的类型转换，强类型则不允许。
1 #1 + “1” 这行代码在Python中会报错。
print 1 + int("1")
print str(1) + "1"
# 字符串
# 复制代码
#字符串
print ''''    吴             
            峰'''
print r'C:\log.txt'
print 'C:\\log.txt'
# 复制代码
# 序列
# 这里先介绍三种序列：列表、元祖和字符串。
# 序列通用操作
# 复制代码
seq = "0123456789"
print seq[0] #从0开始编码。
print seq[-1] #支持倒着数数，-1代表倒数第一。
print seq[1:5] #支持分片操作，seq[start:end]，start会包含在结果中，end不会包含在结果中。
print seq[7:] #seq[start:end]中的end可以省略。
print seq[-3:] #分片也支持负数。
print seq[:3] #seq[start:end]中的start也可以省略。
print seq[:] #全部省略会复制整个序列。
print seq[::2] #支持步长。
10 print seq[::-2] #支持负步长。
11 print seq[9:1:-1] #支持负步长。
12 print [1, 2, 3] + [4, 5, 6] # 序列支持相加，这解释了为啥字符串可以相加。
13 print [1, 2, 3] * 3 #序列支持相乘，这解释了为啥字符串可以相称。
14 print [None] * 10 #生成一个空序列。
15 print 1 in [1, 2, 3] #成员判断。
复制代码
 可变的列表
复制代码
 1 data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
 2
 3 data[0] = "a" #修改元素。
 4 print data
 5 data[0] = 0
 6
 7 del data[10] #删除元素。
 8 print data
 9
10 del data[8:] #分片删除。
11 print data
12
13 data[8:] = [8, 9, 10] #分片赋值
14 print data
复制代码
不可变的元祖
1 print (1, 2) #元祖以小括号形式声明。
2 print (1,) #一个元素的元祖。
字符串格式化
复制代码
1 print "% 10s" % "----"
2
3 print '''
4 %(title)s
5 %(body)s
6 ''' % {"title": "标题", "body": "内容"}
复制代码
字典
1 print {"title": "title", "body": "body"}
2 print dict(title = "title", body = "body")
3 print dict([("title", "title"), ("body", "body")])
1 dic = {"title": "title", "body": "body"};
2 print dic["title"]
3 del dic["title"]
4 print dic
print 语句
1 print 'a', 'b' #print可以接受多个参数，参数的输出之间以空格相隔。
2 print 'a', #如果逗号之后没有参数，则不会换行。
3 print 'b'
序列解包
复制代码
1 x, y, z = 1, 2, 3
2 print x, y, z
3 (x, y, z) = (1, 2, 3)
4 print x, y, z
5 (x, y, z) = [1, 2, 3]
6 print x, y, z
复制代码
bool值
复制代码
 1 #下面的输入全部返回False。
 2 print(bool(None))
 3 print(bool(()))
 4 print(bool([]))
 5 print(bool({}))
 6 print(bool(""))
 7 print(bool(0))
 8
 9 #虽然这些值在条件运算中会当做False，但是本身不等于False。
10 print(True and "")
11 print(not "")
12 print(False == "")
13 print(False == 0) #0除外，bool类型的内部表示就是int类型。
复制代码
bool运算
1 print(0 < 1 < 10)
2 print(0 < 1 and 1 < 10)
3 print(not(0 > 1 > 10))
4 print(not(0 > 1 or 1 > 10))
语句块
:开始语句快，缩进的所有内容都是一个语句块。
1 if(10 > 1):
2     print("10 > 1")
3 else:
4     print("不可能发生")
三元运算符
1 print("10 > 1" if 10 > 1 else "不可能发生")
相等比较
复制代码
1 #== 和 is的差别，==比较的是内容，is比较的是引用。
2 x = [1, 2, 3]
3 y = x
4 z = [1, 2, 3]
5 print(x == y)
6 print(x == z)
7 print(x is y)
8 print(x is z)
复制代码
循环
复制代码
 1 #for循环类似C#的foreach，注意for后面是没有括号的，python真是能简洁就尽量简洁。
 2 for x in range(1, 10):
 3     print(x)
 4
 5 for key in {"x":"xxx"}:
 6     print(key)
 7
 8 for key, value in {"x":"xxx"}.items():
 9     print(key, value)
10
11 for x, y, z in [["a", 1, "A"],["b", 2, "B"]]:
12     print(x, y, z)
复制代码
复制代码
 1 #带索引的遍历
 2 for index, value in enumerate(range(0, 10)):
 3     print(index, value)
 4
 5 #好用的zip方法
 6 for x, y in zip(range(1, 10), range(1, 10)):
 7     print(x, y)
 8
 9 #循环中的的else子句
10 from math import sqrt
11 for item in range(99, 1, -1):
12     root = sqrt(item)
13     if(root == int(root)):
14         print(item)
15         break
16 else:
17     print("没有执行break语句。")
复制代码
pass、exec和eval
复制代码
1 #pass、exec、eval
2 if(1 == 1):
3     pass
4
5 exec('print(x)', {"x": "abc"})
6 print(eval('x*2', {"x": 5}))
复制代码
函数部分

形参和实参之间是按值传递的，当然有些类型的值是引用（对象、列表和字典等）。
复制代码
 1 # 基本函数定义。
 2 def func():
 3     print("func")
 4
 5 func()
 6
 7 # 带返回值的函数。
 8 def func_with_return():
 9     return ("func_with_return")
10
11 print(func_with_return())
12
13 # 带多个返回值的函数。
14 def func_with_muti_return():
15     return ("func_with_muti_return", "func_with_muti_return")
16
17 print(func_with_muti_return())
18
19 # 位置参数
20 def func_with_parameters(x, y):
21     print(x, y)
22
23 func_with_parameters(1, 2)
24
25 # 收集多余的位置参数
26 def func_with_collection_rest_parameters(x, y, *rest):
27     print(x, y)
28     print(rest)
29
30 func_with_collection_rest_parameters(1, 2, 3, 4, 5)
31
32 #命名参数
33 def func_with_named_parameters(x, y, z):
34     print(x, y, z)
35
36 func_with_named_parameters(z = 1, y = 2, x = 3)
37
38 #默认值参数
39 def func_with_default_value_parameters(x, y, z = 3):
40     print(x, y, z)
41
42 func_with_default_value_parameters(y = 2, x = 1)
43
44 #收集命名参数
45 def func_with_collection_rest_naned_parameters(*args, **named_agrs):
46     print(args)
47     print(named_agrs)
48
49 func_with_collection_rest_naned_parameters(1, 2, 3, x = 4, y = 5, z = 6)
50
51 #集合扁平化
52 func_with_collection_rest_naned_parameters([1, 2, 3], {"x": 4, "y": 4, "z": 6}) #这会导致args[0]指向第一个实参，args[1]指向第二个实参。
53 func_with_collection_rest_naned_parameters(*[1, 2, 3], **{"x": 4, "y": 4, "z": 6}) #这里的执行相当于func_with_collection_rest_naned_parameters(1, 2, 3, x = 4, y = 5, z = 6)。
复制代码
作用域

复制代码
 1 # coding=utf-8
 2
 3 # 只有函数执行才会开启一个作用域。
 4 if(2 > 1):
 5     x = 1
 6
 7 print(x) # 会输出1。
 8
 9
10 # 使用vars()函数可以访问当前作用域包含的变量。
11 x = 1
12 print(vars()["x"])
13
14 # 使用globals()函数可以访问全局作用域。
15 x = 1
16
17 def func():
18     print(globals()["x"])
19
20 func()
21
22 # 使用locals()函数可以访问局部作用域。
23 def func():
24     x = 2
25     print(locals()["x"])
26
27 func()
28
29 # 每个函数定义时都会记住所在的作用域。
30 # 函数执行的时候会开启一个新的作用域，函数内变量访问的规则是：先访问当前作用域，如果没有就访问函数定义时的作用域，递归直到全局作用域。
31 x = 1
32
33 def func():
34     y = 2
35     print(x, y) # 输出1 2
36
37 func()
38
39
40 # 变量赋值始终访问的是当前作用域。
41 x = 1
42
43 def func():
44     x = 2
45     y = 2
46     print(x, y) # 输出2 2
47
48 func()
49 print(x) #输出 1
50
51 # 局部变量会覆盖隐藏全局变量，想访问全局变量可以采用global关键字或globals()函数。
52 x = 1
53
54 def func():
55     global x
56     x = 2
57     y = 2
58     print(x, y) # 输出2 2
59
60 func()
61 print(x) #输出 2
复制代码
复制代码
 1 # python支持闭包
 2 def func(x):
 3     def inner_func(y):
 4         print(x + y)
 5
 6     return inner_func
 7
 8 inner_func = func(10)
 9 inner_func(1)
10 inner_func(2)
复制代码
复制代码
1 #函数作为对象
2 def func(fn, arg):
3     fn(arg)
4
5 func(print, "hello")
6 func(lambda arg : print(arg), "hello")
复制代码
模块

几个模块相关的规则：
一个文件代表一个模块。
 可以用import module导入模块，也可以用form module import member导入模块的成员。
如果导入的是module，必须使用module.member进行访问；如果导入的member，可以直接访问member。
导入的module或member都会变成当前module的member。
b.py
复制代码
1 # coding=utf-8
2
3 print __name__
4
5 def say_b():
6     print "b"
复制代码
a.py
复制代码
1 # coding=utf-8
2
3 import b
4 from b import *
5
6 print __name__
7
8 def say_a():
9     print "a"
复制代码
test.py
复制代码
1 # coding=utf-8
2
3 import a
4
5 print __name__
6
7 a.say_a();
8 a.say_b();
9 a.b.say_b()
复制代码
输出
复制代码
1 b
2 a
3 __main__
4 a
5 b
6 b
复制代码
异常管理

复制代码
 1 # coding=utf-8
 2
 3 # 自定义异常
 4 class HappyException(Exception):
 5     pass
 6
 7 # 引发和捕获异常
 8 try:
 9     raise HappyException
10 except:
11     print("HappyException")
12
13 try:
14     raise HappyException()
15 except:
16     print("HappyException")
17
18 # 捕获多种异常
19 try:
20     raise HappyException
21 except (HappyException, TypeError):
22     print("HappyException")
23
24 # 重新引发异常
25 try:
26     try:
27         raise HappyException
28     except (HappyException, TypeError):
29         raise
30 except:
31     print("HappyException")
32
33 #访问异常实例
34 try:
35     raise HappyException("都是我的错")
36 except (HappyException, TypeError), e:
37     print(e)
38
39 #按类型捕获
40 try:
41     raise HappyException
42 except HappyException:
43     print("HappyException")
44 except TypeError:
45     print("TypeError")
46
47 #全面捕获
48 try:
49     raise HappyException
50 except:
51     print("HappyException")
52
53 #没有异常的else
54 try:
55     pass
56 except:
57     print("HappyException")
58 else:
59     print("没有异常")
60
61 #总会执行的final
62 try:
63     pass
64 except:
65     print("HappyException")
66 else:
67     print("没有异常")
68 finally:
69     print("总会执行")
复制代码
面向对象

先上一张图

几个规则：
一切都是对象，python中一切都是对象，每个对象都包含一个__class__属性以标记其所属类型。
每个对象（记得一切都是对象啊）都包含一个__dict__属性以存储所有属性和方法。
每个类型都包含一个__bases__属性以标记其父类。
属性和方法的访问规则：依次搜索instance、子类、父类、父类的父类、直到object的__dict__，如果找到就返回。
属性和方法的设置规则：直接设置instance.__dict__。
以上属性和方法访问或设置规则没有考虑“魔法方法”，下文会解释。
 示例
复制代码
 1 # coding=utf-8
 2
 3 __metaclass__ = type
 4
 5 # 类型定义
 6 # 实例方法必的第一个参数代表类型实例，类似其他语言的this。
 7 class Animal:
 8     name = "未知" # 属性定义。
 9
10     def __init__(self, name): #构造方法定义。
11         self.name = name
12
13     def getName(self): # 实例方法定义。
14         return self.name
15
16     def setName(self, value):
17         self.name = value
18
19 print(Animal.name) # 未知
20 print(Animal.__dict__["name"]) # 未知
21
22 animal = Animal("狗狗")
23 print(animal.name) # 狗狗
24 print(animal.__dict__["name"]) # 狗狗
25 print(Animal.name) # 未知
26 print(Animal.__dict__["name"]) # 未知
27 print(animal.__class__.name) # 未知
28 print(animal.__class__.__dict__["name"]) # 未知
复制代码
1 # 类型定义中的代码会执行，是一个独立的作用域。
2 class TestClass:
3     print("类型定义中") #类型定义中
绑定方法和未绑定方法
复制代码
 1 class TestClass:
 2     def method(self):
 3         print("测试方法")
 4
 5 test = TestClass()
 6 print(TestClass.method) #<unbound method TestClass.method>
 7 print(test.method) #<bound method TestClass.method of <__main__.TestClass object at 0x021B46D0>>
 8
 9 TestClass.method(test) #测试方法
10 test.method() #测试方法
复制代码
绑定方法已经绑定了对象示例，调用的时刻不用也不能传入self参数了。
注：使用对象访问实例方法为何会返回绑定方法？这个还得等到学完“魔法方法”才能解释，内部其实是拦截对方法成员的访问，返回了一个Callable对象。
私有成员
复制代码
1 # 私有成员
2 class TestClass:
3     __private_property = 1
4
5     def __private_method():
6         pass
7
8 print(TestClass.__dict__) # {'__module__': '__main__', '_TestClass__private_method': <function __private_method at 0x0212B970>, '_TestClass__private_property': 1
复制代码
难怪访问不了了，名称已经被修改了，增加了访问的难度而已。
多重继承
复制代码
 1 #多重继承
 2 class Base1:
 3     pass
 4
 5 class Base2:
 6     pass
 7
 8 class Child(Base2, Base1):
 9     pass
10
11 child = Child()
12 print(isinstance(child, Child)) # True
13 print(isinstance(child, Base2)) # True
14 print(isinstance(child, Base1)) # True
复制代码
如果继承的多个类型之间有重名的成员，左侧的基类优先级要高，上例子Base2会胜出。
接口那里去了，鸭子类型比接口更好用。
复制代码
 1 class TestClass1:
 2     def say(self):
 3         print("我是鸭子1")
 4
 5 class TestClass2:
 6     def say(self):
 7         print("我是鸭子2")
 8
 9 def duck_say(duck):
10     duck.say()
11
12 duck_say(TestClass1()) # 我是鸭子1
13 duck_say(TestClass2()) # 我是鸭子2
复制代码
调用父类
复制代码
 1 # 调用父类
 2 class Base:
 3     def say(self):
 4         print("Base")
 5
 6 class Child(Base):
 7     def say(self):
 8         Base.say(self)
 9         super(Child, self).say()
10         print("Child")
11
12 child = Child()
13 child.say()
复制代码
魔法方法

对象构造相关：__new__、__init__、__del__。
复制代码
 1 from os.path import join
 2
 3 class FileObject:
 4     '''Wrapper for file objects to make sure the file gets closed on deletion.'''
 5
 6     def __init__(self, filepath='~', filename='sample.txt'):
 7         # open a file filename in filepath in read and write mode
 8         self.file = open(join(filepath, filename), 'r+')
 9
10     def __del__(self):
11         self.file.close()
12         del self.file
复制代码
运算符重载：所有运算符都能重载。
复制代码
 1 class Word(str):
 2     '''Class for words, defining comparison based on word length.'''
 3
 4     def __new__(cls, word):
 5         # Note that we have to use __new__. This is because str is an immutable
 6         # type, so we have to initialize it early (at creation)
 7         if ' ' in word:
 8             print "Value contains spaces. Truncating to first space."
 9             word = word[:word.index(' ')] # Word is now all chars before first space
10         return str.__new__(cls, word)
11
12     def __gt__(self, other):
13         return len(self) > len(other)
14
15     def __lt__(self, other):
16         return len(self) < len(other)
17
18     def __ge__(self, other):
19         return len(self) >= len(other)
20
21     def __le__(self, other):
22         return len(self) <= len(other)
23
24 print(Word("duan") > Word("wei"))
复制代码
属性访问。
复制代码
 1 class AccessCounter:
 2     '''A class that contains a value and implements an access counter.
 3     The counter increments each time the value is changed.'''
 4
 5     def __init__(self, value):
 6         super(AccessCounter, self).__setattr__('counter', 0)
 7         super(AccessCounter, self).__setattr__('value', value)
 8
 9     def __setattr__(self, name, value):
10         if name == 'value':
11             super(AccessCounter, self).__setattr__('counter', self.counter + 1)
12         # Make this unconditional.
13         # If you want to prevent other attributes to be set, raise AttributeError(name)
14         super(AccessCounter, self).__setattr__(name, value)
15
16     def __delattr__(self, name):
17         if name == 'value':
18             super(AccessCounter, self).__setattr__('counter', self.counter + 1)
19         super(AccessCounter, self).__delattr__(name)
复制代码
集合实现。
复制代码
 1 class FunctionalList:
 2     '''A class wrapping a list with some extra functional magic, like head,
 3     tail, init, last, drop, and take.'''
 4
 5     def __init__(self, values=None):
 6         if values is None:
 7             self.values = []
 8         else:
 9             self.values = values
10
11     def __len__(self):
12         return len(self.values)
13
14     def __getitem__(self, key):
15         # if key is of invalid type or value, the list values will raise the error
16         return self.values[key]
17
18     def __setitem__(self, key, value):
19         self.values[key] = value
20
21     def __delitem__(self, key):
22         del self.values[key]
23
24     def __iter__(self):
25         return iter(self.values)
26
27     def __reversed__(self):
28         return FunctionalList(reversed(self.values))
29
30     def append(self, value):
31         self.values.append(value)
32     def head(self):
33         # get the first element
34         return self.values[0]
35     def tail(self):
36         # get all elements after the first
37         return self.values[1:]
38     def init(self):
39         # get elements up to the last
40         return self.values[:-1]
41     def last(self):
42         # get last element
43         return self.values[-1]
44     def drop(self, n):
45         # get all elements except first n
46         return self.values[n:]
47     def take(self, n):
48         # get first n elements
49         return self.values[:n]
复制代码
可调用对象，像方法一样调用对象。
复制代码
 1 class Entity:
 2     '''Class to represent an entity. Callable to update the entity's position.'''
 3
 4     def __init__(self, size, x, y):
 5         self.x, self.y = x, y
 6         self.size = size
 7
 8     def __call__(self, x, y):
 9         '''Change the position of the entity.'''
10         self.x, self.y = x, y
11         print(x, y)
12
13 entity = Entity(5, 1, 1)
14 entity(2, 2)
复制代码
资源管理
复制代码
 1 class Closer:
 2     def __enter__(self):
 3         return self
 4
 5     def __exit__(self, exception_type, exception_val, trace):
 6         print("清理完成")
 7         return True;
 8
 9 with Closer() as closer:
10     pass
复制代码
对象描述符。
复制代码
 1 class Meter(object):
 2     '''Descriptor for a meter.'''
 3
 4     def __init__(self, value=0.0):
 5         self.value = float(value)
 6     def __get__(self, instance, owner):
 7         return self.value
 8     def __set__(self, instance, value):
 9         self.value = float(value)
10
11 class Foot(object):
12     '''Descriptor for a foot.'''
13
14     def __get__(self, instance, owner):
15         return instance.meter * 3.2808
16     def __set__(self, instance, value):
17         instance.meter = float(value) / 3.2808
18
19 class Distance(object):
20     '''Class to represent distance holding two descriptors for feet and
21     meters.'''
22     meter = Meter()
23     foot = Foot()
复制代码
Mixin（也叫掺入）

掺入模块：playable.py
1 # coding=utf-8
2
3 def paly(self):
4     print("游戏中...")
掺入目标模块：test.py
复制代码
1 # coding=utf-8
2
3 class Animal:
4     from playable import paly
5
6 animal = Animal()
7 animal.paly() # 游戏中...
复制代码
Open Class（打开类型，从新定义成员）

复制代码
 1 #coding:utf-8
 2
 3 class TestClass:
 4     def method1(self):
 5         print("方法1")
 6
 7 def method2(self):
 8     print("方法2")
 9
10 TestClass.method2 = method2
11
12 test = TestClass()
13 test.method1() # 方法1
14 test.method2() # 方法2
复制代码
Meta Programming（元编程）

复制代码
1 TestClass = type("TestClass", (object,), {
2     "say": lambda self : print("你好啊")
3 })
4
5 test = TestClass()
6 test.say()
复制代码
复制代码
 1 def getter(name):
 2     def getterMethod(self):
 3         return self.__getattribute__(name)
 4     return getterMethod
 5
 6 def setter(name):
 7     def setterMethod(self, value):
 8         self.__setattr__(name, value)
 9     return setterMethod
10
11 class TestClass:
12     getName = getter("name")
13     setName = setter("name")
14
15 test = TestClass()
16 test.setName("段光伟")
17 print(test.getName())
复制代码

