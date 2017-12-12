# -*- coding:utf-8 -*-
import urllib,urllib2,re,sys
#reload(sys)
#sys.setdefaultencoding('utf-8')
url1='https://login.yahoo.com/config/login?.tries=1&.src=&.md5=&.hash=&.js=&.last=&promo=&.intl=us&.lang=zh-Hans-CN&.bypass=&.partner=&.u=5qkcncp7ji7j1&.v=0&.challenge=s0D0_yPEgrqoKEJiPtVtiuzS3qIt&.yplus=&.emailCode=&pkg=&stepid=&.ev=&hasMsgr=0&.chkP=Y&.done=http%3A%2F%2Fmy.yahoo.com&.pd=_ver%3D0%26c%3D%26ivt%3D%26sg%3D&.ws=1&.cp=0&pad=5&aad=6&login=你的邮箱&passwd=你的密码&.persistent=y&.save=&passwd_raw='
req = urllib2.Request(url1)
#req.add_header('Referer', 'http://mail.cn.yahoo.com/?cns')
#req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 5.1; rv:10.0.1) Gecko/20100101 Firefox/10.0.1')
req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.8.1.14) Gecko/20080404 (FoxPlus) Firefox/2.0.0.14')
#req.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
#req.add_header('Accept-Language', 'zh-cn,zh;q=0.5')# don't make too many fake image #导致乱码
#req.add_header('Accept-Encoding', 'gzip, deflate')   
#req.add_header('Connection', 'keep-alive')   
#response = urllib2.urlopen(req)
response = urllib2.urlopen(url1)
data2 =response.read()
url_redirect='https://login.yahoo.com/config/verify?.done=http%3a//my.yahoo.com'
response = urllib2.urlopen(url_redirect)
data_redirect =response.read()
print len(data_redirect)
print data_redirect.decode('utf-8').encode('gb18030 ')#读进来时是utf8编码的str,先打散成unicode，再以gb18030 进行编码成汉字。
