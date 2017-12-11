# -*- coding: utf-8 -*-

#author:Keengle(http://www.kgblog.net)

from spdUtility import PriorityQueue,Parser

import urllib2

import sys

import os

 

def updatePriQueue( priQueue, url ):

    "更新优先级队列"

    extraPrior = url.endswith('.html') and 2 or 0 #这里优先下载以html结尾的url

    extraMyBlog = 'www.kgblog.net' in url and 5 or 0 #优先抓取含有指定内容的网页，竞价抓取排名？？

    item = priQueue.getitem(url)

    if item :

        newitem = ( item[0]+1+extraPrior+extraMyBlog, item[1] )

        priQueue.remove(item)

        priQueue.push( newitem )

    else :

        priQueue.push( (1+extraPrior+extraMyBlog,url) )

 

def getmainurl(url):

    "获得该url的主站地址，用于添加在相对url地址的开头"

    ix = url.find('/',len('http://') )

    if ix > 0 :

        return url[:ix]

    else :

        return url

 

def analyseHtml(url,html, priQueue,downlist):

    "分析html的超链接，并更新优先级队列"

    p = Parser()

    try :

        p.feed(html)

        p.close()

    except:

        return

    mainurl = getmainurl(url)

    for k, v in p.anchors.items():

        for u in v :

            if not u.startswith('http://'):  #处理相对地址的url

                u = mainurl + u       

            if not downlist.count(u) :    #如果该url已经下载，就不处理了

                updatePriQueue( priQueue, u )

        

def downloadUrl(id, url, priQueue , downlist,downFolder):

    "下载指定url内容，并分析html超链接"

    downFileName = downFolder+'/%d.html' % (id,)

    print 'downloading',url,'as', downFileName ,

    try:

        fp = urllib2.urlopen(url)

    except:

        print '[ failed ]'

        return False

    else :

        print '[ success ]'

        downlist.push( url )  #把已下载的url添加到列表中

        op = open(downFileName,"wb")

        html = fp.read()

        op.write( html )

        op.close()

        fp.close()

        

        analyseHtml(url,html,priQueue,downlist)

        return True

    

def spider(beginurl, pages,downFolder):

    "爬虫主程序，循环从优先级队列中取出最高优先级的结点处理"

    priQueue = PriorityQueue()

    downlist = PriorityQueue() #已下载url的集合，防止重复下载

    priQueue.push( (1,beginurl) )

    i = 0

    while not priQueue.empty() and i < pages :

        k, url = priQueue.pop()

        if downloadUrl(i+1, url, priQueue , downlist,downFolder):

            i += 1

    print '\nDownload',i,'pages, Totally.'

            

def main():

    "主函数，设定相关参数：开始url，抓取的网页数目，保存的文件夹"

    beginurl = 'http://www.kgblog.net'  #开始抓取的URL地址

    pages = 20   #抓取网页的数目

    downloadFolder = './spiderDown' #指定保存网页的文件夹

    if not os.path.isdir( downloadFolder ):

        os.mkdir( downloadFolder )

    spider( beginurl, pages, downloadFolder)

 

if __name__ == '__main__':

    main()

