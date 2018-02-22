#!/usr/bin/env python
# coding: utf-8
#声明必须放在前两行，# coding=<encoding name>

'''

@author: 

@license: 

@contact: 

@software: Test

@file: testXpath3.py

@time: 2018/2/21

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
# with open('tieba_chuanzhi.html','r') as f:
with open('tieba1.html','r') as f:
    html = f.read()
    selector = etree.HTML(html)
    # 核心部分
    link = selector.xpath("//div[@class='t_con cleafix']/div/div/div/a/@href")
    # link = selector.xpath("//div[@class='t_con cleafix']/div/div/div/a/@href")
    # link = selector.xpath("//a[@class='j_th_tit']/@href")[0].text.encode('utf-8').strip()
    # link = selector.xpath("//div[@class='threadlist_title pull_left j_th_tit']//a[@class='j_th_tit']/@href")[0].text.encode('utf-8').strip()
    # link = selector.xpath("//div[@class='threadlist_lz clearfix']//a[@class='j_th_tit ']/@href")[0].text.encode('utf-8').strip()

    print link #打印出链接