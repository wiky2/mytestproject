#!/usr/bin/env python
# coding: utf-8
import heapq,operator
grades=[32,43,654,34,132,66,99,532,995,1021]
grades2={'xiaoming':32,'xiaohong':43,'xiaohua':654,'xiaoqiang':100,'xiaoyang':256}
print heapq.nlargest(3,grades)
print heapq.nsmallest(3,grades2,key=operator.itemgetter(2))
stocks = [ {'ticker': 'APPL', 'Price': 201}, {'ticker': 'GOOG', 'Price': 800}, {'ticker': 'F', 'Price': 54}, {'ticker': 'MSFT', 'Price': 313}, {'ticker': 'TUNA', 'Price': 68}]
print heapq.nsmallest(3,stocks,key=lambda stock:stock['Price'])
