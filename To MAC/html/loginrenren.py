#!/usr/bin/python
#filename:loginren.py
import cookielib
import urllib
import urllib2
import re
import os

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
ck = cookielib.CookieJar()
status = urllib2.build_opener(urllib2.HTTPCookieProcessor(ck))

def login():
    print 'login...'
    data_for_login = {'email':'你的邮箱','password':'你的密码'}
    postlogin = urllib.urlencode(data_for_login)
    mainpg = opener.open('http://3g.renren.com/login.do?autoLogin=true',postlogin).read()
    mpg = file('homedo.html','a+')
    mpg.write(mainpg)
    mpg.close()
    print 'success!'

def getu():
    pat = re.compile('.+<form action="http://(.*)Status\.do\?(.*)" method="post">')
    f = open('homedo.html','r')
    for line in f.readlines():
    m = pat.match(line)
    if m:
        sod = m.group(2)
        print sod
        break
    sid = re.sub(r'&amp;','&',sod)
    return sid

def statusup():
    url = 'http://3g.renren.com/status/wUpdateStatus.do?'+getu()
    data_for_statusup = {'status':'你要发的状态'}
    poststatus = urllib.urlencode(data_for_statusup)
    f = status.open(url,poststatus).read()
    print f

def rmfile()
    command = 'rm -r homedo.html'
    os.system(commamd)

login()
statusup()
rmfile()