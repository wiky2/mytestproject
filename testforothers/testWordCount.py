#!/usr/bin/env python
# coding: utf-8
import requests
from bs4 import BeautifulSoup
import operator
def start(url):
    word_list=[]
    headers = requests.utils.default_headers()
    headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    source_code=requests.get(url,headers=headers).text
    soup=BeautifulSoup(source_code,'lxml')
    text=soup.find_all('article',{'class':'paywall'})
    for post_text in text:
        content=post_text.get_text()
        words=content.lower().split()
        for each_word in words:
            print each_word
            word_list.append(each_word)
    clean_up_list(word_list)
def clean_up_list(word_list):
    #clean data
    clean_up_list=[]
    for word in word_list:
        symbols="!@#$%^&*()_<>?[]-=+{}|\""
        for i in range(0,len(symbols)):
            word=word.replace(symbols[i],"")
        if len(word)>0:
            print word
            clean_up_list.append(word)
    print clean_up_list
    create_dictionary(clean_up_list)
def create_dictionary(clean_up_list):
    word_count={}
    for word in clean_up_list:#判断是否在liszt中
        if word in word_count:
            word_count[word]+=1
        else:
            word_count[word]=1
    for key ,value in sorted(word_count.items(),key=operator.itemgetter(1)):
        print key,value

start('https://www.washingtonpost.com/politics/how-the-trump-era-is-changing-the-federal-bureaucracy/2017/12/30/8d5149c6-daa7-11e7-b859-fb0995360725_story.html?utm_term=.48229016b77a')

