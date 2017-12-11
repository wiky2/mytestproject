#!/usr/bin/env python
#-*- coding:utf-8 -*-
import os

#print os.listdir("J:\VBA")
#for root, dirs, files in os.walk('J:\VBA'):
#    print root,dirs, files
for root,dirs,files in os.walk('J:\VBA'):
   print root
for root,dirs,files in os.walk('J:\VBA'):
   print dirs
for root,dirs,files in os.walk('J:\VBA'):
   print files   
#print '%s %s %s %s' % ("String",["Str","ing"],("T","uple"),{'Dictionary':123})
for root, dirs, files in os.walk('J:\VBA'):
#    for s in root
#        s=s.decode('utf-8').encode('gbk')
    print root
#    root=root.decode('utf-8').encode('gbk')
#    dirs=dirs.decode('utf-8').encode('gbk')

#    open('mycd.cdc', 'a').write("%s %s %s" % (root,dirs,files))
print "中文"
ss="   i love you   "#取出首尾空格
print ss.strip()
print range(2,10)
