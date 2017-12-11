#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Created on 2010-4-2

@author: Administrator
'''
import win32com.client, pythoncom
import time

ie = win32com.client.DispatchEx('InternetExplorer.Application.1')
ie.Visible = 1
ie.Navigate("http://news.sina.com.cn")
while ie.Busy:
  time.sleep(0.05)

doc = ie.Document
for i in doc.images:
    print i.src, i.width, i.height