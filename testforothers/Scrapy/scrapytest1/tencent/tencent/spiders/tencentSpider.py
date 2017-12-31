# -*- coding: utf-8 -*-
#http://hr.tencent.com/position.php
import scrapy
from tencent.items import TencentItem

class TencentspiderSpider(scrapy.Spider):
    name = 'tencentSpider'
    allowed_domains = ['tencent.com']
    url='http://hr.tencent.com/position.php?start='
    offset=0
    start_urls = [url+str(offset)]

    def parse(self, response):
        for each in response.xpath("//tr[@class='even'] | //tr[@class='odd']"):
            item=TencentItem()
            positionName = each.xpath('./td[1]/a/text()').extract()#xpath是一个选择器,要用extract()取出文本列表
            positionLink = each.xpath('./td[1]/a/text()').extract()#xpath是一个选择器,要用extract()取出文本列表
            # print type(each.xpath('./td[1]/a/text()'))
            positionType = each.xpath('./td[2]/text()').extract()
            positionNum = each.xpath('./td[3]/text()').extract()
            workLocation = each.xpath('./td[4]/text()').extract()
            publishTime = each.xpath('./td[5]/text()').extract()
            item['positionName']=positionName[0]
            item['positionLink']=positionLink[0]
            # if positionType=='':
            if positionType:
                item['positionType']=positionType[0]
            else:
                item['positionType']='空'
            item['positionNum']=positionNum[0]
            item['workLocation']=workLocation[0]
            item['publishTime']=publishTime[0]
            yield item#拿到一个数据，就交给管道文件处理。不用把他放到一个list里面集中处理。yield还可以处理请求
        if self.offset <2700:
            self.offset+=10
        yield scrapy.Request(self.url+str(self.offset),callback=self.parse)#将下一个连接传递给回调函数。调度器拿到请求后先入队列，出队列后交给下载器，下载器将响应文件交给parse函数继续处理。

