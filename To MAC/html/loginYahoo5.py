# -*- coding:utf-8 -*-
import urllib,urllib2,re,sys
#reload(sys)
#sys.setdefaultencoding('utf-8')
url1='https://edit.bjs.yahoo.com/config/login?.cnrid=ymhp_20000&.challenge=okM.6c3tW7TgxY2GW4HVb0CoE5x1&login=你的用户&passwd=你的密码&.remember=y&.intl=cn&.done=http://mail.cn.yahoo.com/ycn_setcookie_inset.html?.done=http%3A%2F%2Fmail.cn.yahoo.com%2Finset.html%3Frr%3D1482292087%26.remember%3Dy%26.persistent%3D&.src=ym'
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
print len(data2)
print data2.decode('utf-8').encode('gb18030 ')#读进来时是utf8编码的str,先打散成unicode，再以gb18030 进行编码成汉字。
