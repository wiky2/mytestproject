#!/usr/bin/env python
# coding: utf-8
#声明必须放在前两行，# coding=<encoding name>

'''

@author: 

@license: 

@contact: 

@software: Test

@file: 163Spider.py

@time: 2017/12/3 下午6:47

@desc:
'''
import scrapy
from mySpider.items import MyspiderItem
class my163Spider(scrapy.Spider):
    name='163spider'#执行的时候用到 scrapy crawl name
    allowed_domains=['http://www.163.com']
    start_urls=['http://money.163.com/special/pinglun/']
    def parse(self,response):#名字不能乱改
        with open('pinglun.html','w') as f:
            f.write(response.body)#这是scrapy的用法,urllib2是text或者content.
        news_list=response.xpath('//div[@class="item_top"]')
        newsItem=[]
        for each in news_list:
            item=MyspiderItem()
            title=each.xpath('./h2/a/text()').extract()
            time=each.xpath('./p/span/text()').extract()
            abstract=each.xpath('./p/text()').extract()
            item['title']=title[0]
            item['time']=time[0]
            item['abstract']=abstract[0]
            yield item#拿到一个数据，就交给管道文件处理。不用把他放到一个list里面集中处理。yield还可以处理请求


