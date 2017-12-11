# -*- coding: utf-8 -*-
import scrapy


class MeituSpider(scrapy.Spider):
    name = "meitu"
    allowed_domains = ["www.meizitu.com"]
    start_urls = (
        'http://www.www.meizitu.com/',
    )

    def parse(self, response):
        pass
