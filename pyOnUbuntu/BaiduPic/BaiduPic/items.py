# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from PIL import Image

class BaidupicItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pic_name=scrapy.Field()
    file_urls=scrapy.Field()

