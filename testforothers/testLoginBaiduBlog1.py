#!/usr/bin/env python
# coding: utf-8
#声明必须放在前两行，# coding=<encoding name>

'''

@author: 

@license: 

@contact: 

@software: Test

@file: testLoginBaiduBlog1.py

@time: 2017/12/3 下午11:40

@desc:
'''
# -*- coding: utf-8 -*-
import re
import urllib
import urllib2
import cookielib
#获取CSDN博客标题和正文
url = "http://blog.csdn.net/[username]/archive/2010/07/05/5712850.aspx"
sock = urllib.urlopen(url)
html = sock.read()
sock.close()
content = re.findall('(?<=blogstory">).*(?=<p class="right artical)', html, re.S)
content = re.findall('<mce:script.*><!--.*// --></mce:script>(.*)', content[0], re.S)
title = re.findall('(?<=<title>)(.*)-.* - CSDN.*(?=</title>)', html, re.S)
#根据上文获取内容新建表单值
blog = {'spBlogTitle': title[0].decode('utf-8').encode('gbk'), #百度博客标题
        'spBlogText': content[0].decode('utf-8').encode('gbk'),#百度博客内容
        'ct': "1",
        'cm': "1"}
del content
del title
#模拟登录
cj = cookielib.CookieJar()
#用户名和密码
post_data = urllib.urlencode({'username': '[username]', 'password': '[password]', 'pwd': '1'})
#登录路径
path = 'https://passport.baidu.com/?login'
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent', 'Opera/9.23')]
urllib2.install_opener(opener)
req = urllib2.Request(path, post_data)
conn = urllib2.urlopen(req)
#获取百度发布博客的认证令牌
bd = urllib2.urlopen(urllib2.Request('http://hi.baidu.com/[username]/creat/blog')).read()
bd = re.findall('(?<=bdstoken/" value=/").*(?=ct)', bd, re.S)
blog['bdstoken'] = bd[0][:32]
#设置分类名
blog['spBlogCatName'] = 'php'
#比较表单发布博客
req2 = urllib2.Request('http://hi.baidu.com/[username]/commit', urllib.urlencode(blog))
#查看表单提交后返回内容
print urllib2.urlopen(req2).read()
#请将[username]/[password]替换为您的真实用户名和密码
#搞定收工……