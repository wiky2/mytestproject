#!/usr/bin/env python
# coding: utf-8
#声明必须放在前两行，# coding=<encoding name>

'''

@author: 

@license: 

@contact: 

@software: Test

@file: start.py.py

@time: 2017/12/3 下午7:05

@desc:
'''
from scrapy import cmdline
cmdline.execute('scrapy crawl 163spider'.split())#把命令切片依次传入程序