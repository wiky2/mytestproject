# -*- coding:gb18030  -*-
import urllib,urllib2,re	
url0 = 'http://mail.cn.yahoo.com/'
response = urllib2.urlopen(url0)
data0 = response.read()
print data0.decode('utf-8').encode('gb18030 ')#������ʱ��utf8�����str,�ȴ�ɢ��unicode������gb18030 ���б���ɺ��֡�