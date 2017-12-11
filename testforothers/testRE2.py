#!/usr/bin/env python
# coding: utf-8
# 声明必须放在前两行，# coding=<encoding name>

'''

@author:

@license:

@contact:

@software: Test

@file: testGenerator.py

@time: 2017/11/26 下午3:47

@desc:
'''
'''
多个单一 分隔符 时 ，”[]”与 “|”的 效果是一样的，但是 请注意 使用 “|”时 mouxie某些字符 需要转义 
多个 长短 不一 的的分隔符的分隔符时， 就应该使用 “|” 
适用 “（）”则是 将分隔后的结果保留分隔符（在split中，分隔符理应是被刨除的，所以这里有点难理解）
'''
import re
re.split('_#|','this_is#a|test')


# 将正则表达式编译成Pattern对象
pattern = re.compile(r'hello')

# 使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None
match = pattern.match('hello world!')

if match:
    # 使用Match获得分组信息
    print match.group()

    ### 输出 ###
    # hello

import re

m = re.match(r'(\w+) (\w+)(?P<sign>.*)', 'hello world!')

print "m.string:", m.string
print "m.re:", m.re
print "m.pos:", m.pos
print "m.endpos:", m.endpos
print "m.lastindex:", m.lastindex
print "m.lastgroup:", m.lastgroup

print "m.group(1,2):", m.group(1, 2)
print "m.groups():", m.groups()
print "m.groupdict():", m.groupdict()
print "m.start(2):", m.start(2)
print "m.end(2):", m.end(2)
print "m.span(2):", m.span(2)
print r"m.expand(r'\2 \1\3'):", m.expand(r'\2 \1\3')

import re

p = re.compile(r'(\w+) (\w+)(?P<sign>.*)', re.DOTALL)

print "p.pattern:", p.pattern
print "p.flags:", p.flags
print "p.groups:", p.groups
print "p.groupindex:", p.groupindex

pattern = re.compile(r'world')

# 使用search()查找匹配的子串，不存在能匹配的子串时将返回None
# 这个例子中使用match()无法成功匹配
match = pattern.search('hello world!')

if match:
    # 使用Match获得分组信息
    print match.group()

    ### 输出 ###
    # world

p = re.compile(r'\d+')
print p.split('one1two2three3four4')
p = re.compile(r'\d+')
print p.findall('one1two2three3four4')

p = re.compile(r'\d+')
for m in p.finditer('one1two2three3four4'):
    print m.group()

p = re.compile(r'(\w+) (\w+)')
s = 'i say, hello world!'

print p.sub(r'\2 \1', s)


def func(m):
    return m.group(1).title() + ' ' + m.group(2).title()


print p.sub(func, s)

p = re.compile(r'(\w+) (\w+)')
s = 'i say, hello world!'

print p.subn(r'\2 \1', s)


def func(m):
    return m.group(1).title() + ' ' + m.group(2).title()


print p.subn(func, s)



line = "word;Word;temp"
"""
单一分隔符，str.split()与 re.split()zuoy作用一致 
"""
print line.split("; ")
# ['word', 'Word', 'temp']
print re.split(r"; ", line)
# ['word', 'Word', 'temp']


"""
多个单一 分隔符 时 ，"[]"与 "|"的 效果是一样的，但是 请注意 使用 “|”时 mouxie某些字符 需要转义  
"""
line1 = "word;Word,emp?hahaha"
print re.split(r";|,|\?", line1) #别忘了转义"?",如果双引号括起来，则用|分割，如果用中括号括起来，则不用分隔
# ['word', 'Word', 'emp', 'hahaha']
print re.split(r"[;,?]", line1)
# ['word', 'Word', 'emp', 'hahaha']

## 当 空格 出现 时 ，就 十分讨厌了(ノω<。)ノ))☆.。
"""
多个 长短 不一 的的分隔符的分隔符时， 就应该使用 "|"
"""
line2 = "word;Word,emp? hahaha; whole, cai"
print re.split(r";|,|\?\s|;\s|,\s", line2)
# ['word', 'Word', 'emp', 'hahaha', ' whole', ' cai']

## 以上 只是 为了 说明这些的吗的适用情况 ，还有 更加渐变简便 的 用法 是
print re.split(r"\W+", line)
print re.split(r"\W+", line1)
print re.split(r"\W+", line2)

"""
适用 “（）”则是 将 分隔 后的 结果 连同分隔符均 有所 保留 
"""
print re.split(r"(\W+)", line2)
# ['word', ';', 'Word', ',', 'emp', '? ', 'hahaha', '; ', 'whole', ', ', 'cai']
# 注意： 连 空格 都 保留了

"""
在 正则中 具有 含义 的 符号 也将 作为 分隔符 的 通用 解决 办法 ，请不要 在 尝试 要有 多少个 ‘\’
"""

delimiters = "a", "...", "(C)"
regexPattern = '|'.join(map(re.escape, delimiters)) # 'a|\\.\\.\\.|\\(C\\)',escape将字符进行转义
line = "stackoverflow (C) is awesome... isn't it?"
print re.split(regexPattern,line) # ['st', 'ckoverflow ', ' is ', 'wesome', " isn't it?"]



"""
一些 更 复杂 的 就 需要 你对 正则 表达式 的更 深入 的 了解了 
以下是 stackoverflow的 关于 re.split的 问题 
"""
##split a string like "HELLO there HOW are YOU" by uppercase, thus the result is ['HELLO there', 'HOW are', 'YOU']
line1 = "HELLO there HOW are YOU"
re.split(r"\s+(?=[A-Z]+)", line1) # 后向匹配

# i want to split “400-IF(3>5,5,5)+34+IF(4>5,5,6)” by string 'IF(3>5,5,5)', so re.split() should give list with length: 2  ['400-', '+34+']
line2 = "400-IF(3>5,5,5)+34+IF(4>5,5,6)"
' '.join(re.split(r'IF\(.*?\)',line2)).split()  # 贪婪模式


def mySplit(s,ds):
    res =[s]
    for d in ds:
        t =[]
        map(lambda x:t.extend(x.split(d)),res)
        res = t
    #当s中存在连续的分隔符时，就会出现空格的，下面是去除空格
    return [x for x in res if x]
s = "abcd,1313|;gg2*hhh"
res = ',|;*'
print mySplit(s,res)