#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
localIP = socket.gethostbyname(socket.gethostname())
print("local ip:"+localIP)
print("local ip:%s"%localIP)
ipList = socket.gethostbyname_ex(socket.gethostname())
#print("iplist:"+ipList[0])
print(type(ipList[0]))
print("external IP:"+ipList[0])
