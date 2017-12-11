# coding=utf-8

from lxml import *
import lxml.html
import urllib2
import lxml.html as H

def getjarinfo(url):
    c=urllib2.urlopen(url)
    
    f=c.read()
    #print f
    doc = H.document_fromstring(f)#返回rootnode
    tables=doc.xpath("//table[@id='line_height_25']")  #//表示选取所有元素，不管它在哪  
    pinpais=doc.xpath("//td[@id='lanmu']")
    print pinpais
    jixings=doc.xpath("//div[@id='hot']")
    print jixings
    jars = doc.xpath("//li[@id='width_75']")
    for j in range(len(jars)):
        print jars[j].text_content()
    #r = doc.xpath("//table[@id='xiazai']//tr[2]/td[1]/a[1]")[0]
    #jarurl=r.get('href')
    
if __name__ == '__main__':
    url='http://game.3533.com/game/30862.htm'
    getjarinfo(url)

