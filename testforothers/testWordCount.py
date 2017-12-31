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
start('https://www.washingtonpost.com/politics/how-the-trump-era-is-changing-the-federal-bureaucracy/2017/12/30/8d5149c6-daa7-11e7-b859-fb0995360725_story.html?utm_term=.48229016b77a')

