#!/usr/bin/env python
# -*- coding: GBK -*-

import urllib

from sgmllib import SGMLParser

class URLLister(SGMLParser):
    def reset(self):
        SGMLParser.reset(self)
        self.urls = []
        
    def start_a(self, attrs):
        href = [v for k, v in attrs if k == 'href']
        if href:
            self.urls.extend(href)
    
url = r'http://www.sinc.sunysb.edu/Clubs/buddhism/JinGangJingShuoShenMo/'
sock = urllib.urlopen(url)
htmlSource = sock.read()
sock.close()
#print htmlSource
f = file('jingangjing.html', 'w')
f.write(htmlSource)
f.close()

mypath = r'http://www.sinc.sunysb.edu/Clubs/buddhism/JinGangJingShuoShenMo/'

parser = URLLister()
parser.feed(htmlSource)

for url in parser.urls:
    myurl = mypath + url
    print "get: " + myurl
    sock2 = urllib.urlopen(myurl)
    html2 = sock2.read()
    sock2.close()
    
    # 保存到文件
    print "save as: " + url
    f2 = file(url, 'w')
    f2.write(html2)
    f2.close()
