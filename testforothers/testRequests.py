#!/usr/bin/env python
# coding: utf-8
#声明必须放在前两行，# coding=<encoding name>

'''

@author: 

@license: 

@contact: 

@software: Test

@file: testRequests.py

@time: 2017/11/3 上午7:45

@desc:只能在urllib3上使用。
'''
import  requests
url ="http://www.baidu.com"
myheader = {"User-Agent":"Intel Mac OS X 10_12_6","Referer":"http://127.0.0.1"}
# res = requests.get(url,headers=myheader)
#get方法
get_res = requests.get(url)
print get_res.text
#post方法
mydata = {"name":"python"}
post_res = requests.post(url,data=mydata)
print post_res.text

#提交json
res = requests.post(url,json=mydata)
#解析json
print res.json()

session = requests.session()
login_res = session.post("http://www.abc.com/login",data={"user":"python","pwd":"123"})
#这时候已经保存了登录的cookie了,可以直接访问个人的信息页了
res = session.get("http://www.abc.com/profile")
print res.text