#!/usr/bin/env python
# coding: utf-8
#声明必须放在前两行，# coding=<encoding name>

'''

@author: 

@license: 

@contact: 

@software: Test

@f

@time: 2017/11/26 下午5:00ile: testSinaweibo4.py

@desc:
http://m.blog.csdn.net/my__oracle/article/details/42293249
http://mp.weixin.qq.com/s?src=3&timestamp=1511108725&ver=1&signature=at24GKibwNNoE9VsETitURyMHzXYeytp1MoUyAFx-2U8j784OgTtvTy7U4FryNyU0E2wp5QQiXJM0CWnzvBFpoy*3R8Vl5-b62wCr7AJt7MZr2IvOsrq2Ax73xcz6xoT4Tuo7YI7EtiCmnsg0WdcGg==
http://blog.csdn.net/zhaolina004/article/details/28699095
爬取微博PC端
需要手工键入page数量
从ajax里面解析出加载的网页里面的page
'''
import re
import string
import sys
import os
import urllib
import urllib2
from bs4 import BeautifulSoup
import requests
from lxml import etree
import json
import time

reload(sys)
sys.setdefaultencoding('utf-8')
if (len(sys.argv)==2):
    user_id = (int)(sys.argv[1])
else:
    user_id = (int)(raw_input(u"请输入user_id: "))#鹿晗id：5460991756

cookie = {"Cookie": "输入cookie"}
url = 'https://weibo.com/p/aj/v6/mblog/mbloglist?ajwvr=6&domain=100606&is_search=0&visible=0&is_hot=1&is_tag=0&profile_ftype=1&page=1&pagebar=1&pl_name=Pl_Official_MyProfileFeed__24&id=1006065460991756&script_uri=/u/%d&feed_type=0&pre_page=1&domain_op=100606&__rnd=1511695180950' % user_id

# html = requests.get(url, cookies=cookie).content.decode('gb2312').encode('utf-8')#万能中文处理方法，A和B分别可以使gbk, gb2312,utf-8,它们排列组合一下，一共只有6种组合方式
html = requests.get(url, cookies=cookie).content
pageNum = int(raw_input(u'请输入爬取页数pageNum：'))
#
result = ""
urllist_set = set()
word_count = 1
image_count = 1

print u'爬虫准备就绪...'

for page in range(1, pageNum + 1):

    print '第%d页'% page
    # 获取lxml页面
    url = 'https://weibo.com/p/aj/v6/mblog/mbloglist?ajwvr=6&domain=100606&is_search=0&visible=0&is_hot=1&is_tag=0&profile_ftype=1&page=1&pagebar=1&pl_name=Pl_Official_MyProfileFeed__24&id=1006065460991756&script_uri=/u/%d&feed_type=0&pre_page=%d&domain_op=100606&__rnd=1511695180950' % (user_id, page)
    print url
    lxml = requests.get(url, cookies=cookie)
    data1 = json.loads(lxml.text)  # 转化为字典
    html=data1['data']
    print html
    selector = etree.HTML(html)
    print selector
    # titles = selector.xpath('//div[@class="WB_text W_f14"]/text()')
    # # 文字爬取
    # for title in titles:
    #     print title

    # 图片爬取
    soup = BeautifulSoup(html, "lxml")
    urllist = soup.find_all('li', {"class":"WB_pic li_1 S_bg1 S_line2 bigcursor li_n_h"})
    first = 0
    for imgurl in urllist:
        # print imgurl.img['src']
        imgurl="http:"+imgurl.img['src']
        urllist_set.add(imgurl)
        image_count += 1
    urllist = soup.find_all('li', {"class":"WB_pic li_1 S_bg1 S_line2 bigcursor"})
    for imgurl in urllist:
        # print imgurl.img['src']
        imgurl="http:"+imgurl.img['src']
        urllist_set.add(imgurl)
        image_count += 1
    time.sleep(1)

fo = open("/Users/mateseries/Downloads/Weibo/%s_text" % user_id, "wb+")
fo.write(result)
word_path = os.getcwd() + '/%d' % user_id
fo.close()
print u'文字微博爬取完毕'

link = ""
fo2 = open("/Users/mateseries/Downloads/Weibo//%s_imageurls" % user_id, "wb+")
for eachlink in urllist_set:
    link = link + eachlink + "\n"
fo2.write(link)
fo2.close()
print u'图片链接爬取完毕'

if not urllist_set:
    print u'该页面中不存在图片'
else:
    # 下载图片,保存在当前目录的pythonimg文件夹下
    image_path = '/Users/mateseries/Downloads/Weibo/weibo_image'
    if os.path.exists(image_path) is False:
        os.mkdir(image_path)
    x = 1
    for imgurl in urllist_set:
        temp = image_path + '/%s.jpg' % x
        print u'正在下载第%s张图片' % x
        try:
            urllib.urlretrieve(urllib2.urlopen(imgurl).geturl(), temp)
        except:
            print u"该图片下载失败:%s" % imgurl
        x += 1

# print u'原创微博爬取完毕，共%d条，保存路径%s' % (word_count - 4, word_path)
print u'微博图片爬取完毕，共%d张，保存路径%s' % (image_count - 1, image_path)