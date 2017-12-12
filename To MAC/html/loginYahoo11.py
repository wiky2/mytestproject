# -*- coding:gb18030  -*-
import urllib,urllib2,re	
url0 = 'http://mail.cn.yahoo.com/'
response = urllib2.urlopen(url0)
data0 = response.read()
print data0.decode('utf-8').encode('gb18030 ')#读进来时是utf8编码的str,先打散成unicode，再以gb18030 进行编码成汉字。