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
        price=tag.contents[1].contents[5]#有些商品位置放置广告，影响搜索，而且奇数下标对应价格。这是所有标签的一个列表。报错。有（换行）也是contents的元素
        print price
print search_JD('鞋')

