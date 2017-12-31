import requests
from bs4 import BeautifulSoup
import operator
def start(url):
    word_list=[]
    headers = requests.utils.default_headers()
    headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    source_code=requests.get(url,headers=headers).text
    soup=BeautifulSoup(source_code,'lxml')
    for post_text in soup.findAll('a',{'class':'event'}):
        content=post_text.string
        words=content.lower().split()
        for each_word in words:
            print each_word
            word_list.append(each_word)
start('http://www.163.com')

