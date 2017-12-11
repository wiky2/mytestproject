# -*- coding: utf-8 -*-

# Scrapy settings for fun project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'fun'

SPIDER_MODULES = ['fun.spiders']
NEWSPIDER_MODULE = 'fun.spiders'

ITEM_PIPELINES = {'fun.pipelines.ImageDownloadPipeline': 1}

IMAGES_STORE = r'.'


DOWNLOAD_DELAY = 0.25    # 250 ms of delay

USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36'
DOWNLOADER_MIDDLEWARES = {
    'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
    'pythontab.middlewares.ProxyMiddleware': 100,
}