#!/usr/bin/env python
# coding: utf-8
# 声明必须放在前两行，# coding=<encoding name>

'''

@author:

@license:

@contact:

@software: Test

@file: testGenerator.py

@time: 2017/11/11 下午6:59

@desc:
'''
import socket,string
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',8125))
data = s.recv(1024)
if data:
    print data
else:
    print '连接错误'
while True:
    str1=raw_input('已连接上服务器，请输入:\n')
    if str1=='':
        break
    s.send(str1)
    data=s.recv(1024)
    if data:
        print data
    else:
        break
s.close()

