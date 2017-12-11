#!/usr/bin/env python
# coding: utf-8
#声明必须放在前两行，# coding=<encoding name>

'''

@author: 

@license: 

@contact: 

@software: Test

@file: testXpath.py

@time: 2017/11/26 下午5:33

@desc:
'''

# articles = selector.xpath('//ul[@class="article-list thumbnails"]/li')
#
#     for article in articles:
#         title = article.xpath('div/h4/a/text()').extract()
#         url = article.xpath('div/h4/a/@href').extract()
#         author = article.xpath('div/p/a/text()').extract()

import urllib2
from lxml import etree
crawl_url = "http://blog.chinaunix.net/uid-28266791-id-5754271.html"
req = urllib2.Request(crawl_url)
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36')
response = urllib2.urlopen(req)
html = response.read()
selector = etree.HTML(html)
# 核心部分
bloger = selector.xpath("//div[@class='Blog_left']/div/div/p/a")[0].text.encode('utf-8').strip()

print bloger #打印出夏寥寥