# -*- coding: utf-8 -*-
import scrapy
from scrapy import optional_features
optional_features.remove('boto')
from PIL import Image
from BaiduPic.items import BaidupicItem

class BaidupicspiderSpider(scrapy.Spider):
    name = "baidupicspider"
    allowed_domains = ["http://www.fsbus.com"]
    start_urls = (
        'http://www.fsbus.com/sheyingjiaocheng/23753.html'
    )

    def parse(self, response):
        items["file_urls"] = response.xpath('/html/body/div[4]/div[1]/div[2]/div/div[1]/img/@src')[0].extract()
        items["pic_name"]=response.xpath('/html/body/div[4]/div[1]/div[2]/div/div[1]/img/@title')[0].extract()
        yield items