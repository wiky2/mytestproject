#!/usr/bin/env python
# coding: utf-8
#声明必须放在前两行，# coding=<encoding name>

'''

@author: 

@license: 

@contact: 

@software: Test

@file: testJD4.py

@time: 2017/11/12 上午8:42

@desc:
'''
import urllib
import json
import re
class JdPrice(object):
    """
    对获取京东商品价格进行简单封装
        """
    def __init__(self, url):
        self.url = url
        self._response = urllib.urlopen(self.url)
        self.html = self._response.read()
    def get_product(self):
        """
    获取html中，商品的描述(未对数据进行详细处理，粗略的返回str类型)
    :return:
    """
        product_re = re.compile(r'compatible: true,(.*?)};', re.S)
        product_info = re.findall(product_re, self.html)[0]
        return product_info
    def get_product_skuid(self):
        """
    通过获取的商品信息，获取商品的skuid
    :return:
    """
        product_info = self.get_product()
        skuid_re = re.compile(r'skuid: (.*?),')
        skuid = re.findall(skuid_re, product_info)[0]
        return skuid
    def get_product_name(self):
        pass
    def get_product_price(self):
        """
    根据商品的skuid信息，请求获得商品price
    :return:
    """
        price = None
        skuid = self.get_product_skuid()
        url = 'http://p.3.cn/prices/mgets?skuIds=J_' + skuid + '&type=1'
        price_json = json.load(urllib.urlopen(url))[0]
        if price_json['p']:
            price = price_json['p']
        return price
# 测试代码
if __name__ == '__main__':
    url = 'http://item.jd.com/1310118868.html'
    url = 'http://item.jd.com/1044773.html'
    jp = JdPrice(url)
    print jp.get_product_price()
# htm.decode('gb2312', 'ignore').encode('utf-8')
# f = open('jjs.html', 'w')
# f.write(htm)
# f.close()