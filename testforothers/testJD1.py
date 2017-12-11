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
     #'# 可以在查找的 tag 下继续使用 find_all()'
     #通过点取属性的方式只能获得当前名字的第一个tag。直接 soup.find_all('a') 就能找到所有 a 标签了。官网有详细中文文档。
        # link=tag.div.div[1].a['href']
        for i in tag.find_all('div',class_='gl-i-wrap'):#打印所有链接
            for j in i.find_all('div',class_='p-img'):
                print j.a['href']
        # print type(tag.contents[0])#<class 'bs4.element.NavigableString'>
        # print type(tag.contents[1])#<class 'bs4.element.Tag'>
        # print tag.contents#
        # print
        # price=tag.div.div[2].strong.i.get_text()
        # title=tag.div.div[3].a.em.get_text()
        # created_at=tag.div.p.span.get_text()
        # print link,title,created_at
        # result.append([link,title])
    # return result
print search_JD('鞋')

