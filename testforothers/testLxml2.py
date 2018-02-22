#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: 你的名字
# Created Time : 2018年02月16日 星期五 21时14分14秒
# File Name: testRE3.py
# Description:爬取百度贴吧：
"""
import urllib
import urllib2
# import re
# import random
from lxml import etree
class tiebaSpider:
    def __init__(self):
        self.page=2
        self.switch=True
    def loadPage(self,keyword,page=1):
        print "正在下载数据"
        thread_number=(page-1)*50
        fullurl="https://tieba.baidu.com/f?"+keyword+'&pn='+str(thread_number)
        print fullurl
        proxyswitch=True#打开网页要挂代理，不能用User-agent.
        httpproxy_handler=urllib2.ProxyHandler({'http': '122.114.31.177:808'})
        nullproxy_handler=urllib2.ProxyHandler({})
        if proxyswitch:
                opener=urllib2.build_opener(httpproxy_handler)
        else:
                opener=urllib2.build_opener(nullproxy_handler)
        urllib2.install_opener(opener)#用了install_opener，就不用opener.open,直接yong urllib2.urlope()
        request = urllib2.Request(fullurl)
        html = urllib2.urlopen(request).read()
        print html
        content=etree.HTML(html)
        # link_list=content.xpath('//div[@class="t_con cleafix"]')
        # link_list = content.xpath('//div[@class="t_con cleafix"]/div/div/div/a/@href')
        # link_list=content.xpath("//li[@class='j_thread_list clearfix']/text()")
        # link_list=content.xpath('//div[@class="t_con cleafix"]//div[@class="col2_right j_threadlist_li_right"]//div[@class="threadlist_lz clearfix"]//div[@class="threadlist_title pull_left j_th_tit"]//a[@class="j_th_tit"]/@href')#无法匹配
        # link_list=content.xpath("//div[@class='t_con cleafix']//div[@class='col2_right j_threadlist_li_right']//div[@class='threadlist_lz clearfix']//div[@class='threadlist_title pull_left j_th_tit']//a[@class='j_th_tit']/@href")#无法匹配
        # link_list=content.xpath("//div[@class='t_con cleafix']/div[@class='col2_right j_threadlist_li_right']/div[@class='threadlist_lz clearfix']/div[@class='threadlist_title pull_left j_th_tit']/a[@class='j_th_tit']/@href")#无法匹配
        link_list=content.xpath("//div[@class='t_con cleafix']/div/div/div/a/@href")
        print len(link_list)
        # print link_list[0]
        full_link_list=[("http://tieba.baidu.com"+v) for v in link_list]
        print full_link_list
        for link in (full_link_list):
            print "帖子链接是"+link
            self.loadImage(link)
    def loadImage(self,link):
        print "正在下载图片"
        proxyswitch=False#下载图片的时候不能挂代理
        httpproxy_handler=urllib2.ProxyHandler({'http': '122.114.31.177:808'})
        nullproxy_handler=urllib2.ProxyHandler({})
        if proxyswitch:
                opener=urllib2.build_opener(httpproxy_handler)
        else:
                opener=urllib2.build_opener(nullproxy_handler)
        urllib2.install_opener(opener)#用了install_opener，就不用opener.open,直接yong urllib2.urlope()
        headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
        # 文件写入
        request = urllib2.Request(link, headers = headers)
        html = urllib2.urlopen(request).read()
        content=etree.HTML(html)
        with open('tieba2.html','w') as f:
            f.write(html)
        # link_list = content.xpath('//div[@class="d_post_content j_d_post_content "]/img/@src')
        page_number=content.xpath("//li[@class='l_reply_num']/span[2]/text()")[0]
        print page_number
        for next_page in range(1,2):
        # for next_page in range(1,int(page_number)+1):
            next_page_url=link+"/?pn="+str(next_page)
            proxyswitch=False
            httpproxy_handler=urllib2.ProxyHandler({'http': '122.114.31.177:808'})
            nullproxy_handler=urllib2.ProxyHandler({})
            if proxyswitch:
                    opener=urllib2.build_opener(httpproxy_handler)
            else:
                    opener=urllib2.build_opener(nullproxy_handler)
            urllib2.install_opener(opener)#用了install_opener，就不用opener.open,直接yong urllib2.urlope()
            request=urllib2.Request(next_page_url)
            # request.add_header("User-Agent",user_agent)
            # request.get_header("User-agent")#第一个字母大写
            response=urllib2.urlopen(request)
            html=response.read()
            content=etree.HTML(html)
            with open('tieba3.html','w+') as f:
                f.write(html)
                f.write(next_page_url)
            link_list=content.xpath("//div[@class='d_author']/ul/li[1]/div/a/img/@src")#如果找不到某个标签，可能与浏览器有关,往上级找，多试几种方法,比如加代理，去代理，加user_agent,去user_agent,把网页打印出来看看。
            link_list2=[]
            for link in link_list:
                if not link.startswith("http"):
                    link_list2.append("https:"+link)
                else:
                    link_list2.append(link)
            username_list=content.xpath("//div[@class='d_author']/ul/li[1]/div/a/img/@username")
            username_list2=[]
            # for username in username_list:
                # username_list2.append(username.decode('utf-8'))
            # print len(link_list)
            # print len(username_list)
            link_name_list=zip(link_list2,username_list)
            print link_name_list
            for (link,username) in (link_name_list):
                # # fulllink="https://tieba.baidu.com"+link
                self.writeImage(link,username)
    def writeImage(self,url,username):
        headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; rv2.0.1) Gecko/20100101 Firefox/4.0.1"}
        request=urllib2.Request(url,headers=headers)
        image=urllib2.urlopen(request).read()
        print "正在写入数据\n"
        folder='/home/python/Documents/Pycharmproject/testforothers/tieba_face_image'
        with open(folder+'/'+username+'.jpg', 'wb') as f:
            f.write(image)
        print "*"*30

    def startWork(self):
        # while self.switch:
        tieba_name=raw_input("请输入爬取的贴吧名")
        begin_page=int(raw_input("请输入起始页"))
        end_page=int(raw_input("请输入结束页"))
        tieba_name_code=urllib.urlencode({'kw':tieba_name})
        while begin_page<=end_page:
            self.loadPage(tieba_name_code,begin_page)
            begin_page+=1
        print "谢谢使用"

if __name__ == '__main__':
    duanziSpider=tiebaSpider()
    # duanziSpider.loadPage()
    duanziSpider.startWork()





