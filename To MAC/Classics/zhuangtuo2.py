#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2010-3-31

@author: Administrator
'''
import htmlentitydefs
import httplib
import locale
import math
import netrc
import os
import os.path
import re
import socket
import string
import sys
import time
import urllib
import urllib2
from operator import itemgetter 
def myopenurl(request):
    res1=''
    try:
        data = urllib2.urlopen(request)
        res1=data.read()
    except (urllib2.HTTPError, ), err:
        if err.code != 416: #  416 is 'Requested range not satisfiable'
            #raise 
            pass
    return res1
std_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.2) Gecko/20090729 Firefox/3.5.2',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
    'Accept': 'text/xml,application/xml,application/xhtml+xml,text/html;q=0.9,text/plain;q=0.8,image/png,*/*;q=0.5',
    'Accept-Language': 'en-us,en;q=0.5',
}
url='http://guba.eastmoney.com/topic,002122.html'
request = urllib2.Request(url, None, std_headers)
stream = None
open_mode = 'ab'
params_Con=None
count = {} 
IPS=[]
word=''
res=myopenurl(request)
for i in range(2,10):
    url="http://guba.eastmoney.com/topic,002122_%d.html" % i
    request1 = urllib2.Request(url, None, std_headers)
    res=res+myopenurl(request1)
    
IPS=re.compile(r'\d+\.\d+\.\d+\.\*').findall(res)
for word in IPS:
    count[word] = 1 + count.get(word, 0)
print sorted(count.iteritems(), key=itemgetter(1), reverse=True)[0:5]  
