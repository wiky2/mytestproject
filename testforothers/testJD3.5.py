#!/usr/bin/env python
# coding: utf-8
# 声明必须放在前两行，# coding=<encoding name>

'''

@author:

@license:

@contact:

@software: Test

@file: testGenerator.py

@time: 2017/11/11 下午16:59

@desc:
增加异步加载的内容
https://search.jd.com/s_new.php?keyword=%E9%9E%8B&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E9%9E%8B&page=2&s=26&scrolling=y&log_id=1510479918.84232&tpl=3_M&show_items=17187731992,10335871586,1473034949,4653743,2913482,4046199,1024223197,1070604145,12516966516,10127664980,3101039,1374720575,10452153721,4653555,2503123,1656692400,17139491926,1373859646,1696361113,15646552504,5246543,1130236930,11226414488,14273360057,2803594,10520894994,1073629839,10482701133
'''
import urllib,re,bs4
def search_JD(keyword):
    url="https://search.jd.com/Search?keyword="+keyword+"&enc=utf-8&wq="+keyword+"&pvid=096d9c88664a46629a784f039a677f8c"
    content=urllib.urlopen(url).read()
    # e=content.decode('utf-8')
    o=bs4.BeautifulSoup(content,'html.parser')#soup是一种特殊的tag
    div_link=o.find_all('div',class_='p-img')
    for i in div_link:
        img_link1=i.find('img').get('data-lazy-img')
        img_link2=i.find('img').get('src')
        if img_link1:
            print img_link1
        if img_link2:
            print img_link2
    div_data_pid=o.find_all('li',class_='gl-item')
    print 'pid总数量：',len(div_data_pid)
    for i in div_data_pid:
        data_pid=i.get('data-pid')
        print data_pid
search_JD('鞋')


