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
        if len(tag.find_all('div',class_='gl-i-wrap'))>0:
            print tag.find_all('div',class_='gl-i-wrap')[0].find_all('div',class_='p-img')[0].a['href']
            print tag.find_all('div',class_='gl-i-wrap')[0].find_all('div',class_='p-price')[0].get_text()
            print tag.find_all('div',class_='gl-i-wrap')[0].find_all('div',class_='p-name p-name-type-2')[0].get_text()
    # return result
print search_JD('鞋')

