#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: 你的名字
# Created Time : 2018年02月16日 星期五 21时14分14秒
# File Name: testRE3.py
# Description:爬去内涵段子
"""
import urllib2
import re
import random
class Spider:
    def __init__(self):
        self.page=2
        self.switch=True
    def loadPage(self):
        print "正在下载数据"
        fullurl="http://www.neihanpa.com/article/index_"+str(self.page)+'.html'
        print fullurl
        ua_list = [
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv2.0.1) Gecko/20100101 Firefox/4.0.1",
                "Mozilla/5.0 (Windows NT 6.1; rv2.0.1) Gecko/20100101 Firefox/4.0.1",
                "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
                "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
        ]
        user_agent=random.choice(ua_list)
        request=urllib2.Request(fullurl)
        request.add_header("User-Agent",user_agent)
        # request.get_header("User-agent")#第一个字母大写
        response=urllib2.urlopen(request)
        html=response.read()
        pattern=re.compile('<div class="text-column-item box box-790">(.*?)</div>',re.S)
        content_list=pattern.findall(html)
        for content in content_list:
            print content
        self.dealPage(content_list)
    def writePage(self,item):
        print "正在写入数据\n"
        with open("duanzi.txt", 'a') as f:
            f.write(item)
    def dealPage(self,content_list):
        for item in content_list:
            item=item.replace("<h3>","").replace("</h3>","").replace("</div>","").replace("</a>","")#replace不能用正则表达式
            pattern=re.compile('<div(.*?)>',re.S)
            item=pattern.sub("",item)
            pattern=re.compile('<a(.*?)>',re.S)
            item=pattern.sub("",item)
            # print item
            self.writePage(item)
    def startWork(self):
        while self.switch:
            command=raw_input("继续爬取请回车")
            if command=="quit":
                self.switch=False
            self.loadPage()
            self.page+=1
        print "谢谢使用"
if __name__ == '__main__':
    duanziSpider=Spider()
    # duanziSpider.loadPage()
    duanziSpider.startWork()





