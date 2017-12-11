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
'''
import urllib,re,bs4
def search_JD(keyword):
    url="https://search.jd.com/Search?keyword="+keyword+"&enc=utf-8&wq="+keyword+"&pvid=096d9c88664a46629a784f039a677f8c"
    content=urllib.urlopen(url).read()
    # e=content.decode('utf-8')
    o=bs4.BeautifulSoup(content,'html.parser')#soup是一种特殊的tag
    tags=o.find_all('li',class_='gl-item')#为了与关键字进行区分，加下划线
    # print tags
    # print len(tags)
    result=[]
    for tag in tags:
        link=tag.contents[1].contents[1].a['href']#可以输出链接
        print len(tag.contents[1])#先看所有标签的列表的长度，比如第12个位置放的是广告，所有这里长度只有5，而其他的都在17以上
        # print price
print search_JD('鞋')

