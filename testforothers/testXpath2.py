#!/usr/bin/env python
# coding: utf-8
#声明必须放在前两行，# coding=<encoding name>

'''

@author: 

@license: 

@contact: 

@software: Test

@file: testXpath2.py

@time: 2017/11/26 下午5:37

@desc:
'''
import urllib2
from lxml import etree
crawl_url = "http://www.jianshu.com/p/e2c4ebd2eeb3"
req = urllib2.Request(crawl_url)
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36')
response = urllib2.urlopen(req)
html = response.read()
selector = etree.HTML(html)
# 核心部分
bloger = selector.xpath("//div[@class='author']/div[@class='info']//span[@class='name']/a/text()")#['mrlevo520'],不包括a标签,不能用extract
bloger2= selector.xpath("//div[@class='author']/div[@class='info']//span[@class='name']/a")#包括a标签

print bloger,bloger2
bloger3 = selector.xpath("//div[@class='author']/div[@class='info']//span[@class='name']")#['mrlevo520']
bloger3 = selector.xpath("//div[@class='author']/div[@class='info']//span[@class='name']")#['mrlevo520']

info = bloger3[0].xpath('string(.)').strip()#text()是一个node test，而string()是一个函数，data()是一个函数且可以保留数据类型。此外，还有点号（.）表示当前节点。
print info #打印出mrlevo
