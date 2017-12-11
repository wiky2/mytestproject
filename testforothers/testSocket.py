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
while True:
    connectin,address=s.accept()#处理下一个连接。
    buf=connectin.recv(10)#最多获取多少字节。不管多少字节进来，只抓取10个
    print buf
    connectin.send(buf)
connectin.close()
