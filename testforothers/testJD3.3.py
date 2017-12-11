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
        if len(tag.contents[1])>5:#先判断是否是广告位，如果大于5，基本就是正常的。
            price = tag.contents[1].contents[5].strong.i.get_text()#tag.contents[1].contents[0],tag.contents[1].contents[2]是空白（换行）
            # print price
        if len(tag.contents[1])>5:
            title=tag.contents[1].contents[7].get_text()#get_text是标签，get_text()是内容
            # print title
        print link,price,title
        result.append([link,price,title])
    # print result
search_JD('鞋')


