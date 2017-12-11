#!/usr/bin/env python
# coding: utf-8
#声明必须放在前两行，# coding=<encoding name>

'''

@author: 

@license: 

@contact: 

@software: Test

@file: testNetease_pinglun.py

@time: 2017/11/11 下午4:30

@desc:
'''
import urllib,re
def pinglun_netease(url):
    url_netease=urllib.urlopen(url).read()
    pattern1=re.compile(r'''<div class="item_top">[\s.]*<h2><a href="(.*)">(.*)</a></h2>''')#读取的网页源码不是按照chrome开发模式下整齐的排列，有大量的空格、换行。
    pattern2=re.compile(r'''<span class="time">(.*)</span>''')#读取的网页源码不是按照chrome开发模式下整齐的排列，有大量的空格、换行。
    result1=re.findall(pattern1,url_netease)
    result2=re.findall(pattern2,url_netease)
    result1_list=[]
    for i in result1:
        result1_list.append(list(i))
    print result1_list,result2
    for i in xrange(1,len(result1_list)+1):
        result1_list[i-1].append(result2[i-1])
    print result1_list
    result_list=[]
    for i in result1_list:
        result_list.append({'title':i[1],'created_at':i[2],'url':i[0]})
        # result_list.append({'title':i[1],'url':i[0]})
    return result_list
print pinglun_netease('http://money.163.com/special/pinglun/')
