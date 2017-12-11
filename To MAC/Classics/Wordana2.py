'''
Created on 2010-4-1

@author: Administrator
'''
'''
Created on 2010-3-15

@author: Administrator
'''
import re
import timeit
 
#uncomment if test with psyco
#import psyco
#psyco.full()
 
def top10word():
    '''return 10 most frequently used word in python 2.6.4 docs'''
    txt = open('full IP.txt','rb').read()
    #lst = re.compile(r'\b((2[0-4]\d|25[0-5]|[01]?\d\d?)\.){3}((2[0-4]\d|25[0-5]|[01]?\d\d?)\.)\b').findall(txt)
    lst=re.compile(r'(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])').findall(txt)
    #print lst
    d = {}
    for word in lst:
        word = word.lower()
        if d.has_key(word):
            d[word] += 1
        else:
            d[word] = 1
    sd = sorted(d.items(),cmp=lambda x,y:cmp(y[1],x[1]))
    return sd[:10]
 
if __name__ == '__main__':
    print top10word()
    t = timeit.Timer('top10word()','from __main__ import top10word')
    print t.timeit(number=1)