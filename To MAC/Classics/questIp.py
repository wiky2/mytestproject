#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Created on 2010-4-1

@author: Administrator
'''
#!C:\\python26\\python.exe
# -*- coding:gbk -*-
# ipfind.py
import sys,re
import urllib2
import socket

def Usage():
    print '''
说明：
  1) 查询本机出口IP地址.
  2) 查询IP地址所在的地域和类型.
  3) 查询域名对应的IP地址.
  0) 退出
'''

def trynet():
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.settimeout(8)
    try:
        sk.connect(('ip138.com',80))
        pass
    except Exception:
        print '*** 请保证您的Internet接入正常!'
        sys.exit()
    sk.close()


def getmyip():
    url = urllib2.urlopen('http://ip138.com/ip2city.asp')
    result = url.read()
    m = re.search(r'(([01]?\d\d?|2[0-4]\d|25[0-5])\.){3}([01]?\d\d?|2[0-4]\d|25[0-5])',result)
    return m.group(0)


def getdomainip(DOMAIN):
    iplist = socket.gethostbyname_ex(DOMAIN)
    return ', '.join(iplist[2])

  
def getnet(IP):
    if re.match(r'^(([01]?\d\d?|2[0-4]\d|25[0-5])\.){3}([01]?\d\d?|2[0-4]\d|25[0-5])$',IP):
        pass
    else:
        print '*** 您输入了错误的IP地址！'
        sys.exit()

    mysearch = "http://ip138.com/ips8.asp?ip=%s&action=2" % (IP)
    url = urllib2.urlopen(mysearch)
    result = url.read()

    m = re.search(r'<li>(.*?)</li>', result)
    return m.group(1).replace('本站主数据：',IP+' => ')


def main():
    trynet()
    Usage()
    while True:
        select = raw_input('*** 请选择您要查看的类型：')
        if select == '1':
            print '\n>>> 您的出口IP是：', getmyip()
        elif select == '2':
            myip = raw_input('*** 请输入您要查询的IP地址：')
            print '\n>>>', getnet(myip)
        elif select == '3':
            domain = raw_input('*** 请输入您要查询的域名：')
            print '\n>>>', getdomainip(domain)
        elif select == '0':
            break
    

if __name__ == '__main__':
    main()