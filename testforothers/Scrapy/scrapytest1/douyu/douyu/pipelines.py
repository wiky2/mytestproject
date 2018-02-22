# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


from scrapy.utils.project import get_project_settings
from scrapy.pipelines.images import ImagesPipeline
import os,scrapy
class ImagesPipeline(ImagesPipeline):
    #def process_item(self, item, spider):
    #    return item
    IMAGES_STORE=get_project_settings().get("IMAGES_STORE")
    def get_media_requests(self,item,info):
        image_url=item['imageLink']
        yield scrapy.Request(image_url)
    def item_completed(self,result,item,info):
        image_path=[x['path'] for ok ,x in result if ok]#tuple
        os.rename(self.IMAGES_STORE+'/'+image_path[0],self.IMAGES_STORE+'/'+item['nickname']+'.jpg')#照片为nickname.jpg
        item['imagePath']=self.IMAGES_STORE+'/'+item['nickname']#目录为nickname命令
        return item
