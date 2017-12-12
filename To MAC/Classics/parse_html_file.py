#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2010-4-3

@author: Administrator
'''
import re
filename = "douban.htm"

newContent = "大家的豆瓣"

filehandle = open(filename, "r")

data = filehandle.read()     #可以读取中文
filehandle.close()

matching = re.subn("豆瓣", newContent, data)

if matching[1] == 0:
    print "Error while parsing HTML template"
print "Content-Type: text/html\n\n"
print matching[0]