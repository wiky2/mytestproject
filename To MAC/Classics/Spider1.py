'''
Created on 2010-4-2

@author: Administrator
'''
import urllib2

from sgmllib import SGMLParser #�򵥵�html����ģ��

class URLLister(SGMLParser):
    def reset(self):                             
        SGMLParser.reset(self)
        self.urls = []

    def start_a(self, attrs):                     
        href = [v for k, v in attrs if k=='href'] 
        if href:
            self.urls.extend(href)

f = urllib2.urlopen("http://www.donews.com")

if f.code == 200:
    parser = URLLister()
    parser.feed(f.read())
    f.close()
    for url in parser.urls: print url