#!/usr/bin/env python
# coding: utf-8
#声明必须放在前两行，# coding=<encoding name>

'''

@author: 

@license: 

@contact: 

@software: Test

@file: testSelenium1.py

@time: 2017/12/3 下午11:22

@desc:
'''
#coding:utf-8
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://weibo.com/u/5460991756?is_search=0&visible=0&is_hot=1&is_tag=0&profile_ftype=1&page=2')
time.sleep(1)
for i in range(10):
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(1)
print driver.find_element_by_class_name('list').text#第 2 页c
