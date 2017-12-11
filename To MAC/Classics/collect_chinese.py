#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Created on 2010-4-2

@author: Administrator
'''
import re
s="""//document.getElementById("zoom").innerHTML = document.getElementById("zoom").innerHTML.replace(/topview/gi,"TopView(<a href='http://topview.eastmoney.com/regfm.html' target='_blank' class='blue'>我们是中国人</a>)");""" 
#rc=re.compile(r'\\\w+',re.DOTALL|re.IGNORECASE)
rc=re.compile(r'\\\w+',re.DOTALL|re.IGNORECASE)
li=list(s)
print li
lis=[x for x in li if rc.search(x.__repr__())]
print lis
cn=reduce(lambda x,y:x+y,lis)
print cn
#结果：我们是中国人
print "\xe6\x88\x91\xe4\xbb\xac"  #每个汉字3个字符