#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Created on 2010-4-2

@author: Administrator
'''
import re   
s="""//document.getElementById("zoom").innerHTML = document.getElementById("zoom").innerHTML.replace(/topview/gi"TopView(<a href='http://topview.eastmoney.com/regfm.html' target='_blank' class='blue'>我们都是中国人</a>)");"""
s=s.__repr__()   
w=re.findall(r'\\\w+',s,re.DOTALL|re.IGNORECASE)
#w
print w #['\\xe6', '\\x88', '\\x91', '\\xe4', '\\xbb', '\\xac', '\\xe9', '\\x83', '\\xbd', '\\xe6', '\\x98', '\\xaf', '\\xe4', '\\xb8', '\\xad', '\\xe5', '\\x9b', '\\xbd', '\\xe4', '\\xba', '\\xba']
print "\xe6\x88\x91"