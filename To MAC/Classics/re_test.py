'''
Created on 2010-4-1

@author: Administrator
'''
import re
#p=r'(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])' #OK
p=r'((2[0-4]\d|25[0-5]|[01]?\d\d?)\.){3}(2[0-4]\d|25[0-5]|[01]?\d\d?)' #wrong，只适用于search
#p=r'\b((2[0-4]\d|25[0-5]|[01]?\d\d?)\.){3}(2[0-4]\d|25[0-5]|[01]?\d\d?)\b' #wrong
#p=r'^([1]?\d\d?|2[0-4]\d|25[0-5])\.([1]?\d\d?|2[0-4]\d|25[0-5])\.([1]?\d\d?|2[0-4]\d|25[0-5])\.([1]?\d\d?|2[0-4]\d|25[0-5])$' #wrong
#p=r'^(\d{1,3}\.){3}\d{1,3}$' #wrong

#p=r'\d+.\d+.\d+.\d+' #OK，适用于findall
t='11.22.33.44.55.66 1234.567.890.123 aaa111.222.333.444bbb 999.888.777.666ccc' 
t = open('full IP.txt','rb').read()
#print re.findall(p,t) #wrong
#print re.search(r'(([01]?\d\d?|2[0-4]\d|25[0-5])\.){3}([01]?\d\d?|2[0-4]\d|25[0-5])',t).group(0) #OK
print re.search(p,t).group(0) #OK
text = 'JGood is a handsome boy, he is cool, clever, and so on' 
print re.findall(r' \w*oo\w*', text)
