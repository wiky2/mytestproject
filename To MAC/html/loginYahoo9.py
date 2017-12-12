# -*- coding:utf-8 -*-
import urllib,urllib2,re,sys
# fail
#reload(sys)
#sys.setdefaultencoding('utf-8')
cookies = urllib2.HTTPCookieProcessor()
opener = urllib2.build_opener(cookies)
url1='https://edit.bjs.yahoo.com/config/login?.cnrid=ymhp_20000&.challenge=okM.6c3tW7TgxY2GW4HVb0CoE5x1&login=你的邮箱&passwd=你的密码&.remember=y&.intl=cn&.done=http://mail.cn.yahoo.com/ycn_setcookie_inset.html?.done=http%3A%2F%2Fmail.cn.yahoo.com%2Finset.html%3Frr%3D1482292087%26.remember%3Dy%26.persistent%3D&.src=ym'
response = opener.open(url1)
data2 =response.read()
print data2.decode('utf-8').encode('gb18030 ')#读进来时是utf8编码的str,先打散成unicode，再以gb18030 进行编码成汉字。
