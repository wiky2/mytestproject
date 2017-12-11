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
从文中获取page数量。
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

reload(sys)
sys.setdefaultencoding('utf-8')
if (len(sys.argv)==2):
    user_id = (int)(sys.argv[1])
else:
    user_id = (int)(raw_input(u"请输入user_id: "))#鹿晗id：5460991756

cookie = {"Cookie": "你的cookie"}
url = 'https://weibo.com/p/aj/v6/mblog/mbloglist?ajwvr=6&domain=100606&is_search=0&visible=0&is_hot=1&is_tag=0&profile_ftype=1&page=1&pagebar=1&pl_name=Pl_Official_MyProfileFeed__24&id=1006065460991756&script_uri=/u/%d&feed_type=0&pre_page=1&domain_op=100606&__rnd=1511695180950' % user_id

# html = requests.get(url, cookies=cookie).content.decode('gb2312').encode('utf-8')#万能中文处理方法，A和B分别可以使gbk, gb2312,utf-8,它们排列组合一下，一共只有6种组合方式
html = requests.get(url, cookies=cookie).content
print html
# html = requests.get(url, cookies=cookie).content
selector = etree.HTML(html)
pageNum = selector.xpath('//*[@id="Pl_Official_MyProfileFeed__24"]/div/div[47]/div/span/a/text()')
print pageNum
pageNum=re.findall(u'\d',pageNum)#或者先compile成pattern对象，由模式对象调用findall来查找。否则直接用re调用findall
#
result = ""
urllist_set = set()
word_count = 1
image_count = 1

print u'爬虫准备就绪...'

for page in range(1, pageNum + 1):

    # 获取lxml页面
    url = 'http://weibo.cn/u/%d?filter=1&amp;page=%d' % (user_id, page)
    lxml = requests.get(url, cookies=cookie).content

    # 文字爬取
    selector = etree.HTML(lxml)
    content = selector.xpath('//span[@class="ctt"]')
    for each in content:
        text = each.xpath('string(.)')
        if word_count == 4:
            text = "%d :" % (word_count - 3) + text + "\n\n"
        else:
            text = text + "\n\n"
        result = result + text
        word_count += 1

    # 图片爬取
    soup = BeautifulSoup(lxml, "lxml")
    urllist = soup.find_all('a', href=re.compile(r'^http://weibo.cn/mblog/oripic', re.I))
    first = 0
    for imgurl in urllist:
        urllist_set.add(requests.get(imgurl['href'], cookies=cookie).url)
        image_count += 1

fo = open("/Users/Personals/%s" % user_id, "wb")
fo.write(result)
word_path = os.getcwd() + '/%d' % user_id
print u'文字微博爬取完毕'

link = ""
fo2 = open("/Users/Personals/%s_imageurls" % user_id, "wb")
for eachlink in urllist_set:
    link = link + eachlink + "\n"
fo2.write(link)
print u'图片链接爬取完毕'

if not urllist_set:
    print u'该页面中不存在图片'
else:
    # 下载图片,保存在当前目录的pythonimg文件夹下
    image_path = os.getcwd() + '/weibo_image'
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

print u'原创微博爬取完毕，共%d条，保存路径%s' % (word_count - 4, word_path)
print u'微博图片爬取完毕，共%d张，保存路径%s' % (image_count - 1, image_path)