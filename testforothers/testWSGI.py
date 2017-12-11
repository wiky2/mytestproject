#!/usr/bin/env python
# coding: utf-8
# 声明必须放在前两行，# coding=<encoding name>

'''

@author:

@license:

@contact:

@software: Test

@file: testGenerator.py

@time: 2017/11/11 下午16:59

@desc:
增加异步加载的内容
'''
from wsgiref.simple_server import make_server

def demo_app(environ,start_response):
    from StringIO import StringIO
    stdout=StringIO()
    print >>stdout,"hello laowang %s"%environ['PATH_INFO']
    print >>stdout
    print 'path_info:%s'%environ['PATH_INFO']
    h=environ.items()#获取环境变量
    h.sort()
    for k,v in h:
        print >>stdout,k,'=',repr(v)
    start_response('200 ok',[('Content-Type','text/plain')])
    return [stdout.getvalue()]

httpd=make_server('',8000,demo_app)
sa=httpd.socket.getsockname()#返回一个tuple，ip:port
print 'Serving HTTP on',sa[0],'port',sa[1],'...'
httpd.serve_forever()