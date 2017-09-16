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

@desc:学习老王python-基础篇，基础数据类型,list，dict是可以变化的

'''

a="abcde'"#双引号里面写单引号
b='abcd"'#单引号里面写双引号
c="""
三个双引号是可以写多行字符串，
里面可以写多行字符串
"hanmeimei,I'm happy to see you!'
里面可以随便写单引号，双引号
"""
print a,b,c
a='this is world'
print a.replace('this','that')#新建字符串
print a.find('world')#a[index:],返回的是索引，从0开始
a= 'i like %s and %s'%('pear','apple')#按照顺序，元组中的元素要按照顺序。
print a
a= 'i like {} and {}'.format('pear','apple')#format不能用占位符。
print a
a= 'i like {1} and {0}'.format('pear','apple')#一切从0开始，{}中的是tuple中元素的位置
print a
a= 'i like %(fruit2)s and %(fruit1)s' % {"fruit1":'pear',"fruit2":'apple'}#占位符+标识符+字典
print a

import linecache
print linecache.getline('a.txt',1)
print linecache.getline('a.txt',2)
lines=linecache.getlines('a.txt')
print lines

s='i,am,lilei'
print s[2:4]
print s.split(',')[1]
print bool('2012'==2012)
f=open('a.txt','r')
content=f.read()
decode_content=content.decode('utf-8')
print content
print len(decode_content)#一个中文字符长度为1
print len(content)#一个中文字符长度为2
print decode_content[len(decode_content)/2:len(decode_content)/2+5].encode('utf-8')
print decode_content[-2:].encode('utf-8')#取出最后2个字符
f.close()

import sys
cinfo='1234'
print id(cinfo)
print sys.getrefcount('1234')#引用计数起始值为3，这里引用了一次，所以加1，4
dinfo=cinfo
print id(dinfo)
print sys.getrefcount('1234')#引用计数起始值为3，这里引用了一次，所以加1，5
ainfo=cinfo
print id(ainfo)#id是一样的
print sys.getrefcount('1234')#引用计数起始值为3，这里引用了一次，所以加1，6
ainfo='5678'
print sys.getrefcount('1234')#ainfo引用了别的字符串，所以'1234'的引用减1，5

import string,sys#sys中有help
print string.digits
print string.lowercase
print string.punctuation
print string.ascii_letters
strinfo=[]
strinfo.append(string.digits)
strinfo.append(string.lowercase)
print ''.join(strinfo)
a='china'
print a.find('i')#2
print a.index('i')#2
print a.find('z')#-1
# print a.index('z')#error
print dir("__builtin__.print")
a='i am a good boy'
print a.find('o',a.find('boy'))#boy中o的位置
print a.rfind('o')#从右到左
f=open('help_string.txt','w')
sys.stdout=f
print help(string)#成功写入
f.close()


