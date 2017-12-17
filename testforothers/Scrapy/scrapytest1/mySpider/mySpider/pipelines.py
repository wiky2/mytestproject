# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

#
# class MyspiderPipeline(object):
#     def process_item(self, item, spider):
#         return item
import json
class my163Pipeline(object):
    def __init__(self):#可选的初始化方法
        self.filename=open('pinglun.json','w')
    def process_item(self,item,spider):#必写
        jsontext=json.dumps(dict(item),ensure_ascii=False)+'\n'#转成json格式
        self.filename.write(jsontext.encode('utf-8'))
    def close_file(self,spider):#可选
        self.filename.close()