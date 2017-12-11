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

import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',8125))
s.listen(8)
connection,address=s.accept()#处理下一个连接。
print '有客户端连接成功'
connection.send("欢迎来到服务器")

while True:#针对一个连接，不断收发消息
    buf=connection.recv(10)#最多获取多少字节。不管多少字节进来，只抓取10个
    print buf
    connection.send(buf)
connectin.close()
