#!/usr/bin/env python
# coding: utf-8
#声明必须放在前两行，# coding=<encoding name>

'''

@author: 

@license: 

@contact: 

@software: Test

@file: testSinaweibo1.py

@time: 2017/11/19 上午9:50

@desc:
'''
import requests,json,time
from bs4 import BeautifulSoup
url='https://weibo.com/p/aj/v6/mblog/mbloglist?ajwvr=6&domain=100606&topnav=1&wvr=6&topsug=1&is_hot=1&pagebar=0&pl_name=Pl_Official_MyProfileFeed__24&id=1006065460991756&script_uri=/u/5460991756&feed_type=0&page=1&pre_page=(page)&domain_op=100606&__rnd=1511055909973'
for i in xrange(10):
    url=url.format(page=i)
    cookies={'cookie':'输入cookie'}
    # cookies={'cookie':'此处是通过chrome获取的cookie'}
    r=requests.get(url,cookies=cookies)
    print type(r.text)
    data1=json.loads(r.text)#转化为字典
    print type(data1)
    html=data1['data']
    soup=BeautifulSoup(html,'html.parser')
    divs=soup.find_all('div',{"class":"WB_text W_f14"})
    for div in divs:
        print div.get_text()
    time.sleep(1)

