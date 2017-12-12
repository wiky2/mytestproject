#!/usr/bin/env python
print 12*34+78-132/6
import time
thisyear=time.localtime()[0]
if thisyear %400==0 or thisyear %4==0 and thisyear %100<>0:
    print 'this year %s is a leap year' % thisyear
else:
    print 'this year %s is not a leap year' % thisyear
time.localtime

#find SuShu
from math import sqrt
N=100
result1=[]
for num in range(2,N):
    f= True
    for snu in range(2,int(sqrt(num))+1):
        if num % snu==0:
            f=False
            break
    if f:
        result1.append(num)
print result1

result2 = [ p for p in range(2, N) if 0 not in [ p% d for d in range(2, int(sqrt(p))+1)] ]
print result2

