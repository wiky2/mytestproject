#!/usr/bin/env python
# coding: utf-8
#声明必须放在前两行，# coding=<encoding name>

'''

@author: 

@license: 

@contact: 

@software: Test

@file: Login.py

@time: 2017/11/19 下午10:42

@desc:
'''
# -*- coding: utf-8 -*-
import WeiboLogin
import urllib2
import re
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

def login():
    username = 'username'
    pwd = 'pwd'      #我的新浪微博的用户名和密码
    weibologin = WeiboLogin.WeiboLogin(username, pwd)   #调用模拟登录程序
    if weibologin.Login():
        print "登陆成功..！"  #此处没有出错则表示登录成功