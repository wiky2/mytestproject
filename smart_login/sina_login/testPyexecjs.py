#!/usr/bin/env python
# coding: utf-8
#声明必须放在前两行，# coding=<encoding name>

'''

@author: 

@license: 

@contact: 

@software: Test

@file: testPyexecjs.py

@time: 2017/12/3 下午1:19

@desc:
'''
import execjs
import os
default = execjs.get()
print default.eval("1+2")
print execjs.get().name
print os.environ
# print os.environ["EXECJS_RUNTIME"]
# import execjs.runtime_names
# jscript = execjs.get(execjs.runtime_names.JScript)
# print jscript.eval("1+2")
