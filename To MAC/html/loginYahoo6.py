# -*- coding:utf-8 -*-
import urllib,urllib2,re,sys
url1 = 'http://edit.bjs.yahoo.com/config/login'
values = {
            '.intl' : 'cn',
            '.done' : 'http%3A%2F%2Fmail.cn.yahoo.com%2Finset.html%3Frr%3D1482292087%26.remember%3Dy%26.persistent%3D',
            '.src' : 'ym',
            '.cnrid' : 'ymhp_20000',
            '.challenge' : 'okM.6c3tW7TgxY2GW4HVb0CoE5x1',
            'login' : '你的邮箱',
            'passwd' : '你的密码',
            '.remember' : 'y',
        }
req = urllib2.Request(url1,urllib.urlencode(values))
req.add_header('Referer', 'http://mail.cn.yahoo.com/?cns')
req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 5.1; rv:10.0.1) Gecko/20100101 Firefox/10.0.1')
req.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
# req.add_header('Accept-Language', 'zh-cn,zh;q=0.5')    
# req.add_header('Accept-Encoding', 'gzip, deflate')   
req.add_header('Connection', 'keep-alive')   
# req.add_header('Referer', 'http://mail.cn.yahoo.com/')
response = urllib2.urlopen(req)
url_verify=response.geturl()
print url_verify
url_verify='https://login.yahoo.com/config/login_verify2?'
values_verify={'passwd' : '你的密码',
               '.done': 'http%3A%2F%2Fmy.yahoo.com',
               '.tries':'1',
               '.slogin':'你的用户',
               '.intl' : 'cn',
               '.lang':'zh-Hans-CN',
               '.challenge':'DIKFj59uibpriisaAgn6Ofy6zFOH',
               'hasMsgr':'0',
               '.pd':'_ver%3D0%26c%3D%26ivt%3D%26sg%3D',
               '.u':'9parl2p7ji5eb',
               '.persistent':'y',
               'pad':'6',
               'aad':'6'
            }
req_verify = urllib2.Request(url_verify,urllib.urlencode(values_verify))
req_verify.add_header('Referer', 'http://mail.cn.yahoo.com/?cns')
req_verify.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 5.1; rv:10.0.1) Gecko/20100101 Firefox/10.0.1')
req_verify.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8') 
req_verify.add_header('Connection', 'keep-alive')   
response2 = urllib2.urlopen(req_verify)
data3=response2.read()
print data3.decode('utf-8').encode('gb18030 ')#读进来时是utf8编码的str,先打散成unicode，再以gb18030 进行编码成汉字。