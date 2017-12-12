'''
Created on 2010-4-3

@author: Administrator
'''
import chilkat #商业的字符集模块

#  The Chilkat Spider component/library is free.
spider = chilkat.CkSpider()

#  The spider object crawls a single web site at a time.  As you'll see
#  in later examples, you can collect outbound links and use them to
#  crawl the web.  For now, we'll simply spider 10 pages of chilkatsoft.com
spider.Initialize("www.chilkatsoft.com")

#  Add the 1st URL:
spider.AddUnspidered("http://www.sina.com.cn/")

#  Begin crawling the site by calling CrawlNext repeatedly.

for i in range(0,10):

    success = spider.CrawlNext()
    if (success == True):
        #  Show the URL of the page just spidered.
        print spider.lastUrl()
        #  The HTML is available in the LastHtml property
    else:
        #  Did we get an error or are there no more URLs to crawl?
        if (spider.get_NumUnspidered() == 0):
            print "No more URLs to spider"
        else:
            print spider.lastErrorText()

    #  Sleep 1 second before spidering the next URL.
    spider.SleepMs(1000)
