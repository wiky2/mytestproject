#!/usr/bin/env python
# coding: utf-8

from operator import itemgetter
stocks = [{'ticker': 'Alpha', 'Price': 367},{'ticker': 'Apolo', 'Price': 289}, {'ticker': 'APPL', 'Price': 201}, {'ticker': 'GOOG', 'Price': 800}, {'ticker': 'F', 'Price': 54}, {'ticker': 'MSFT', 'Price': 313}, {'ticker': 'TUNA', 'Price': 68}]
stocks2 = [{'ticker': 'APPL', 'Price': 367},{'ticker': 'APPL', 'Price': 289}, {'ticker': 'APPL', 'Price': 201}, {'ticker': 'GOOG', 'Price': 800}, {'ticker': 'F', 'Price': 54}, {'ticker': 'MSFT', 'Price': 313}, {'ticker': 'TUNA', 'Price': 68}]
for x in sorted(stocks,key=itemgetter('ticker')):
    print x
print '----------------'
for x in sorted(stocks,key=itemgetter('ticker','Price')):
    print x
#对value完全一致的key再进行排序
for x in sorted(stocks2,key=itemgetter('ticker','Price')):
    print x
