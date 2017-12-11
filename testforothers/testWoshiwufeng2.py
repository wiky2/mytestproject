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
# 你好，世界！
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
#1 + “1” 这行代码在Python中会报错。
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
print seq[::-2] #支持负步长。
print seq[9:1:-1] #支持负步长。
print [1, 2, 3] + [4, 5, 6] # 序列支持相加，这解释了为啥字符串可以相加。
print [1, 2, 3] * 3 #序列支持相乘，这解释了为啥字符串可以相称。
print [None] * 10 #生成一个空序列。
print 1 in [1, 2, 3] #成员判断。
# 复制代码
# 可变的列表
# 复制代码
data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

data[0] = "a" #修改元素。
print data
data[0] = 0

del data[10] #删除元素。
print data

del data[8:] #分片删除。
print data

data[8:] = [8, 9, 10] #分片赋值
print data
# 复制代码
# 不可变的元祖
print (1, 2) #元祖以小括号形式声明。
print (1,) #一个元素的元祖。
# 字符串格式化
# 复制代码
print "% 10s" % "----"

print '''
%(title)s
%(body)s
''' % {"title": "标题", "body": "内容"}
# 复制代码
# 字典
print {"title": "title", "body": "body"}
print dict(title = "title", body = "body")
print dict([("title", "title"), ("body", "body")])
dic = {"title": "title", "body": "body"};
print dic["title"]
del dic["title"]
print dic
print 语句
print 'a', 'b' #print可以接受多个参数，参数的输出之间以空格相隔。
print 'a', #如果逗号之后没有参数，则不会换行。
print 'b'
# 序列解包
# 复制代码
x, y, z = 1, 2, 3
print x, y, z
(x, y, z) = (1, 2, 3)
print x, y, z
(x, y, z) = [1, 2, 3]
print x, y, z
# 复制代码
# bool值
# 复制代码
#下面的输入全部返回False。
print(bool(None))
print(bool(()))
print(bool([]))
print(bool({}))
print(bool(""))
print(bool(0))

#虽然这些值在条件运算中会当做False，但是本身不等于False。
print(True and "")
print(not "")
print(False == "")
print(False == 0) #0除外，bool类型的内部表示就是int类型。
# 复制代码
# bool运算
print(0 < 1 < 10)
print(0 < 1 and 1 < 10)
print(not(0 > 1 > 10))
print(not(0 > 1 or 1 > 10))
# 语句块
# :开始语句快，缩进的所有内容都是一个语句块。
if(10 > 1):
    print("10 > 1")
else:
    print("不可能发生")
# 三元运算符
print("10 > 1" if 10 > 1 else "不可能发生")
# 相等比较
# 复制代码
#== 和 is的差别，==比较的是内容，is比较的是引用。
x = [1, 2, 3]
y = x
z = [1, 2, 3]
print(x == y)
print(x == z)
print(x is y)
print(x is z)
# 复制代码
# 循环
# 复制代码
#for循环类似C#的foreach，注意for后面是没有括号的，python真是能简洁就尽量简洁。
for x in range(1, 10):
    print(x)

for key in {"x":"xxx"}:
    print(key)

for key, value in {"x":"xxx"}.items():
    print(key, value)

for x, y, z in [["a", 1, "A"],["b", 2, "B"]]:
    print(x, y, z)
# 复制代码
# 复制代码
#带索引的遍历
for index, value in enumerate(range(0, 10)):
    print(index, value)

#好用的zip方法
for x, y in zip(range(1, 10), range(1, 10)):
    print(x, y)

#循环中的的else子句
from math import sqrt
for item in range(99, 1, -1):
    root = sqrt(item)
    if(root == int(root)):
        print(item)
        break
    else:
        print("没有执行break语句。")
# 复制代码
#         pass、exec和eval
# 复制代码
#pass、exec、eval
if(1 == 1):
    pass

    exec('print(x)', {"x": "abc"})
    print(eval('x*2', {"x": 5}))
# 复制代码
# 函数部分

# 形参和实参之间是按值传递的，当然有些类型的值是引用（对象、列表和字典等）。
# 复制代码
# 基本函数定义。
def func():
    print("func")

func()

# 带返回值的函数。
def func_with_return():
    return ("func_with_return")

    print(func_with_return())

# 带多个返回值的函数。
def func_with_muti_return():
    return ("func_with_muti_return", "func_with_muti_return")

    print(func_with_muti_return())

# 位置参数
def func_with_parameters(x, y):
    print(x, y)

func_with_parameters(1, 2)

# 收集多余的位置参数
def func_with_collection_rest_parameters(x, y, *rest):
    print(x, y)
    print(rest)

func_with_collection_rest_parameters(1, 2, 3, 4, 5)

#命名参数
def func_with_named_parameters(x, y, z):
    print(x, y, z)

func_with_named_parameters(z = 1, y = 2, x = 3)

#默认值参数
def func_with_default_value_parameters(x, y, z = 3):
    print(x, y, z)

func_with_default_value_parameters(y = 2, x = 1)

#收集命名参数
def func_with_collection_rest_naned_parameters(*args, **named_agrs):
    print(args)
    print(named_agrs)

func_with_collection_rest_naned_parameters(1, 2, 3, x = 4, y = 5, z = 6)

#集合扁平化
func_with_collection_rest_naned_parameters([1, 2, 3], {"x": 4, "y": 4, "z": 6}) #这会导致args[0]指向第一个实参，args[1]指向第二个实参。
func_with_collection_rest_naned_parameters(*[1, 2, 3], **{"x": 4, "y": 4, "z": 6}) #这里的执行相当于func_with_collection_rest_naned_parameters(1, 2, 3, x = 4, y = 5, z = 6)。
# 复制代码
# 作用域
#
# 复制代码
# coding=utf-8

# 只有函数执行才会开启一个作用域。
if(2 > 1):
    x = 1

print(x) # 会输出1。


# 使用vars()函数可以访问当前作用域包含的变量。
x = 1
print(vars()["x"])

# 使用globals()函数可以访问全局作用域。
x = 1

def func():
    print(globals()["x"])

func()

# 使用locals()函数可以访问局部作用域。
def func():
    x = 2
    print(locals()["x"])

func()

# 每个函数定义时都会记住所在的作用域。
# 函数执行的时候会开启一个新的作用域，函数内变量访问的规则是：先访问当前作用域，如果没有就访问函数定义时的作用域，递归直到全局作用域。
x = 1

def func():
    y = 2
    print(x, y) # 输出1 2

func()


# 变量赋值始终访问的是当前作用域。
x = 1

def func():
    x = 2
    y = 2
    print(x, y) # 输出2 2

func()
print(x) #输出 1

# 局部变量会覆盖隐藏全局变量，想访问全局变量可以采用global关键字或globals()函数。
x = 1

def func():
    global x
    x = 2
    y = 2
    print(x, y) # 输出2 2

func()
print(x) #输出 2
# 复制代码
# 复制代码
# python支持闭包
def func(x):
    def inner_func(y):
        print(x + y)

    return inner_func

inner_func = func(10)
inner_func(1)
inner_func(2)
# 复制代码
# 复制代码
#函数作为对象
def func(fn, arg):
    fn(arg)

func(print, "hello")
func(lambda arg : print(arg), "hello")
# 复制代码
# 模块
#
# 几个模块相关的规则：
# /一个文件代表一个模块。
# 可以用import module导入模块，也可以用form module import member导入模块的成员。
# 如果导入的是module，必须使用module.member进行访问；如果导入的member，可以直接访问member。
# 导入的module或member都会变成当前module的member。
# b.py
# 复制代码
# coding=utf-8

print __name__

def say_b():
    print "b"
# 复制代码
# a.py
# 复制代码
# coding=utf-8

import b
from b import *

print __name__

def say_a():
    print "a"
# 复制代码
# test.py
# 复制代码
# coding=utf-8

import a

print __name__

a.say_a();
a.say_b();
a.b.say_b()
# 复制代码
# 输出
# 复制代码
# b
# a
# __main__
# a
# b
# b
# 复制代码
# 异常管理
#
# 复制代码
# coding=utf-8

# 自定义异常
class HappyException(Exception):
    pass

# 引发和捕获异常
try:
    raise HappyException
except:
    print("HappyException")

try:
    raise HappyException()
except:
    print("HappyException")

# 捕获多种异常
try:
    raise HappyException
except (HappyException, TypeError):
    print("HappyException")

# 重新引发异常
try:
    try:
        raise HappyException
    except (HappyException, TypeError):
        raise
except:
    print("HappyException")

#访问异常实例
try:
    raise HappyException("都是我的错")
except (HappyException, TypeError), e:
    print(e)

#按类型捕获
try:
    raise HappyException
except HappyException:
    print("HappyException")
except TypeError:
    print("TypeError")

#全面捕获
try:
    raise HappyException
except:
    print("HappyException")

#没有异常的else
try:
    pass
except:
    print("HappyException")
else:
    print("没有异常")

#总会执行的final
try:
    pass
except:
    print("HappyException")
else:
    print("没有异常")
finally:
    print("总会执行")
# 复制代码
# 面向对象
#
# 先上一张图
#
# 几个规则：
# 一切都是对象，python中一切都是对象，每个对象都包含一个__class__属性以标记其所属类型。
# 每个对象（记得一切都是对象啊）都包含一个__dict__属性以存储所有属性和方法。
# 每个类型都包含一个__bases__属性以标记其父类。
# 属性和方法的访问规则：依次搜索instance、子类、父类、父类的父类、直到object的__dict__，如果找到就返回。
# 属性和方法的设置规则：直接设置instance.__dict__。
# 以上属性和方法访问或设置规则没有考虑“魔法方法”，下文会解释。
# 示例
# 复制代码
# coding=utf-8

__metaclass__ = type

# 类型定义
# 实例方法必的第一个参数代表类型实例，类似其他语言的this。
class Animal:
name = "未知" # 属性定义。

def __init__(self, name): #构造方法定义。
    self.name = name

def getName(self): # 实例方法定义。
    return self.name

def setName(self, value):
    self.name = value

print(Animal.name) # 未知
print(Animal.__dict__["name"]) # 未知

animal = Animal("狗狗")
print(animal.name) # 狗狗
print(animal.__dict__["name"]) # 狗狗
print(Animal.name) # 未知
print(Animal.__dict__["name"]) # 未知
print(animal.__class__.name) # 未知
print(animal.__class__.__dict__["name"]) # 未知
# 复制代码
# 类型定义中的代码会执行，是一个独立的作用域。
class TestClass:
print("类型定义中") #类型定义中
# 绑定方法和未绑定方法
# 复制代码
class TestClass:
    def method(self):
        print("测试方法")

test = TestClass()
print(TestClass.method) #<unbound method TestClass.method>
print(test.method) #<bound method TestClass.method of <__main__.TestClass object at 0x021B46D0>>

TestClass.method(test) #测试方法
test.method() #测试方法
# 复制代码
# 绑定方法已经绑定了对象示例，调用的时刻不用也不能传入self参数了。
# 注：使用对象访问实例方法为何会返回绑定方法？这个还得等到学完“魔法方法”才能解释，内部其实是拦截对方法成员的访问，返回了一个Callable对象。
# 私有成员
# 复制代码
# 私有成员
class TestClass:
    __private_property = 1

def __private_method():
    pass

print(TestClass.__dict__) # {'__module__': '__main__', '_TestClass__private_method': <function __private_method at 0x0212B970>, '_TestClass__private_property': 1
# 复制代码
# 难怪访/问不了了，名称已经被修改了，增加了访问的难度而已。
# 多重继承
# 复制代码
#多重继承
class Base1:
    pass

class Base2:
    pass

class Child(Base2, Base1):
    pass

child = Child()
print(isinstance(child, Child)) # True
print(isinstance(child, Base2)) # True
print(isinstance(child, Base1)) # True
# 复制代码
# 如果继承的多个类型之间有重名的成员，左侧的基类优先级要高，上例子Base2会胜出。
# 接口那里去了，鸭子类型比接口更好用。
# 复制代码
class TestClass1:
    def say(self):
        print("我是鸭子1")

class TestClass2:
    def say(self):
        print("我是鸭子2")

def duck_say(duck):
    duck.say()

duck_say(TestClass1()) # 我是鸭子1
duck_say(TestClass2()) # 我是鸭子2
# 复制代码
# 调用父类
# 复制代码
# 调用父类
class Base:
    def say(self):
        print("Base")

class Child(Base):
    def say(self):
        Base.say(self)
        super(Child, self).say()
        print("Child")

child = Child()
child.say()
# 复制代码
# 魔法方法
#
# 对象构造相关：__new__、__init__、__del__。
# 复制代码
from os.path import join

class FileObject:
'''Wrapper for file objects to make sure the file gets closed on deletion.'''

    def __init__(self, filepath='~', filename='sample.txt'):
# open a file filename in filepath in read and write mode
        self.file = open(join(filepath, filename), 'r+')

    def __del__(self):
        self.file.close()
    del self.file
# 复制代码
# 运算符重载：所有运算符都能重载。
# 复制代码
class Word(str):
'''Class for words, defining comparison based on word length.'''

    def __new__(cls, word):
# Note that we have to use __new__. This is because str is an immutable
# type, so we have to initialize it early (at creation)
        if ' ' in word:
            print "Value contains spaces. Truncating to first space."
            word = word[:word.index(' ')] # Word is now all chars before first space
        return str.__new__(cls, word)

    def __gt__(self, other):
        return len(self) > len(other)

    def __lt__(self, other):
        return len(self) < len(other)

    def __ge__(self, other):
        return len(self) >= len(other)

    def __le__(self, other):
        return len(self) <= len(other)

print(Word("duan") > Word("wei"))
# 复制代码
# 属性访问。
# 复制代码
class AccessCounter:
'''A class that contains a value and implements an access counter.
The counter increments each time the value is changed.'''

    def __init__(self, value):
        super(AccessCounter, self).__setattr__('counter', 0)
        super(AccessCounter, self).__setattr__('value', value)

    def __setattr__(self, name, value):
        if name == 'value':
            super(AccessCounter, self).__setattr__('counter', self.counter + 1)
# Make this unconditional.
# If you want to prevent other attributes to be set, raise AttributeError(name)
        super(AccessCounter, self).__setattr__(name, value)

    def __delattr__(self, name):
        if name == 'value':
            super(AccessCounter, self).__setattr__('counter', self.counter + 1)
        super(AccessCounter, self).__delattr__(name)
# 复制代码
# 集合实现。
# 复制代码
class FunctionalList:
'''A class wrapping a list with some extra functional magic, like head,
tail, init, last, drop, and take.'''

    def __init__(self, values=None):
        if values is None:
            self.values = []
        else:
            self.values = values

    def __len__(self):
        return len(self.values)

    def __getitem__(self, key):
# if key is of invalid type or value, the list values will raise the error
        return self.values[key]

    def __setitem__(self, key, value):
        self.values[key] = value

    def __delitem__(self, key):
    del self.values[key]

    def __iter__(self):
        return iter(self.values)

    def __reversed__(self):
        return FunctionalList(reversed(self.values))

    def append(self, value):
        self.values.append(value)
    def head(self):
# get the first element
        return self.values[0]
    def tail(self):
# get all elements after the first
        return self.values[1:]
    def init(self):
# get elements up to the last
        return self.values[:-1]
    def last(self):
# get last element
        return self.values[-1]
    def drop(self, n):
# get all elements except first n
        return self.values[n:]
    def take(self, n):
# get first n elements
        return self.values[:n]
# 复制代码
# 可调用对象，像方法一样调用对象。
# 复制代码
class Entity:
'''Class to represent an entity. Callable to update the entity's position.'''

    def __init__(self, size, x, y):
        self.x, self.y = x, y
        self.size = size

    def __call__(self, x, y):
'''Change the position of the entity.'''
        self.x, self.y = x, y
        print(x, y)

entity = Entity(5, 1, 1)
entity(2, 2)
# 复制代码
# 资源管理
# 复制代码
class Closer:
    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_val, trace):
        print("清理完成")
        return True;

with Closer() as closer:
    pass
# 复制代码
# 对象描述符。
# 复制代码
class Meter(object):
'''Descriptor for a meter.'''

    def __init__(self, value=0.0):
        self.value = float(value)
    def __get__(self, instance, owner):
        return self.value
    def __set__(self, instance, value):
        self.value = float(value)

class Foot(object):
'''Descriptor for a foot.'''

    def __get__(self, instance, owner):
        return instance.meter * 3.2808
    def __set__(self, instance, value):
        instance.meter = float(value) / 3.2808

class Distance(object):
'''Class to represent distance holding two descriptors for feet and
meters.'''
    meter = Meter()
    foot = Foot()
# 复制代码
# Mixin（也叫掺入）
#
# 掺入模块：playable.py
# coding=utf-8

def paly(self):
    print("游戏中...")
# 掺入目标模块：test.py
# 复制代码
# coding=utf-8

class Animal:
    from playable import paly

animal = Animal()
animal.paly() # 游戏中...
# 复制代码
# Open Class（打开类型，从新定义成员）

# 复制代码
#coding:utf-8

class TestClass:
    def method1(self):
        print("方法1")

    def method2(self):
        print("方法2")

TestClass.method2 = method2

test = TestClass()
test.method1() # 方法1
test.method2() # 方法2
# 复制代码
# Meta Programming（元编程）
#
# 复制代码
TestClass = type("TestClass", (object,), {"say": lambda self : print("你好啊")})

test = TestClass()
test.say()
# 复制代码
# 复制代码
def getter(name):
    def getterMethod(self):
        return self.__getattribute__(name)
    return getterMethod

def setter(name):
    def setterMethod(self, value):
        self.__setattr__(name, value)
    return setterMethod

class TestClass:
    getName = getter("name")
    setName = setter("name")

test = TestClass()
test.setName("段光伟")
print(test.getName())
# 复制代码

