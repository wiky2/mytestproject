#!/usr/bin/env python
# coding: utf-8
# 声明必须放在前两行，# coding=<encoding name>

'''

@author:

@license:

@contact:

@software: Test

@file: testGenerator.py

@time: 2017/11/5 下午6:59

@desc:
'''
import re
print help(re)
c="4567"
print re.match(r'\d',c)##sre.SRE_Match object,match值匹配开头,search匹配任意位置
print re.match(r'\d','4')#sre.SRE_Match object
print re.match(r'\d','a4')#none，开头不是数字
print re.match(r'\d','a4a')#none
print re.match(r'\d$','a4a')#none
print re.match(r'\d$','a4')#none
print re.match(r'\d$','4')#sre.SRE_Match object
print re.match(r'\d$','44')#none,匹配不成功，因为有2个数字，因为\d只代表一个数字，而实际是2个数字结尾。
print re.match(r'\d+$','4')#sre.SRE_Match object
print re.match(r'\d+$','424134123')#sre.SRE_Match object
print re.match(r'\d+$','a424134123')#none,把"a424134123"看成一整个词，要求纯数字结尾。
print re.match(r'\d+$','a,424134123')#none
print re.match(r'\d?$','424134123')#none，？代表重复0次或者1次，实际超过这个数字，故报错。
print re.match(r'\d?$','a424134123')#none,不能有字幕
print re.match(r'\d?$','4')#sre.SRE_Match object，？代表重复0次或者1次，即没有数字或者只有1个，而且不重复，实际超过这个数字，故报错。
print re.match(r'\d?$','')#sre.SRE_Match object，？代表重复0次或者1次，即没有数字或者只有1个，而且不重复，实际超过这个数字，故报错。
print re.match(r'\d.$','424134123')#none，.代表任意字符，只代表一个位，但实际超过这个数字，故报错。
print re.match(r'\d.$','42')#sre.SRE_Match object，.代表任意字符，只代表一个位，但实际超过这个数字，故报错。
print re.match(r'\d*$','42')#sre.SRE_Match object，.代表任意字符，只代表一个位，但实际超过这个数字，故报错。
print re.match(r'^$','42')#none，.代表任意字符，只代表一个位，但实际超过这个数字，故报错。
print re.match(r'^(\w+).*(\w+)$','hello,my darling son')#sre.SRE_Match object，
d=re.match(r'^(\w+) (\w+)$','hello world')#sre.SRE_Match object，.代表任意字符
print dir(d)
print d.group()#hello world
print d.groups()#('hello', 'world')
d=re.match(r'^(\w+).*(\w+)$','hello world son')#sre.SRE_Match object，.代表任意字符
print dir(d)
print d.group()#hello world son
print d.groups()#('hello', 'n')#先匹配hello,在匹配任意字符，最后走到末尾的时候，发下结尾的字符，只倒退1位。
print re.match(r'^(\w+).* (\w+)$','hello world son')#sre.SRE_Match object，
print d.groups()#('hello', 'n')#
d=re.match(r'^\w+ (\w+)$','hello world')#sre.SRE_Match object，.代表任意字符
print dir(d)
print d.group()#hello world
print d.groups()#('world',)
e='a1b2c3d4e'
print re.split('\d',e)
print re.findall('\d',e)#['1', '2', '3', '4']
print re.findall('\d','a4')#匹配任意位置，['4']
