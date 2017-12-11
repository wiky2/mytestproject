'''
Created on 2010-4-1

@author: Administrator
'''
'''
Created on 2010-4-1

@author: Administrator
'''
import re
#p=r'(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])' #OK
p=r'((2[0-4]\d|25[0-5]|[01]?\d\d?)\.){3}(2[0-4]\d|25[0-5]|[01]?\d\d?)' #wrong
#p=r'^([1]?\d\d?|2[0-4]\d|25[0-5])\.([1]?\d\d?|2[0-4]\d|25[0-5])\.([1]?\d\d?|2[0-4]\d|25[0-5])\.([1]?\d\d?|2[0-4]\d|25[0-5])$' #wrong
#p=r'^(\d{1,3}\.){3}\d{1,3}$' #wrong

#p=r'\d+.\d+.\d+.\d+' #OK
t='11.22.33.44.55.66 1234.567.890.123 aaa111.222.333.444bbb 999.888.777.666ccc' 
for t in open('full IP.txt','rb').readlines():
    if re.search(p,t) is None :
        print "wrong"
    else :
        print re.search(p,t).group(0)
