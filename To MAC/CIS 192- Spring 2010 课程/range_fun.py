#!/usr/bin/python
#range_fun.py

#forwards
for i in range(10): print i,
print

#backwards
for i in range(10,0,-1): print i,
print

#by multiples
for i in range(0,20,2): print i,
print

#both directions at once, glue the lists togeather using zip()
for i,j in zip(range(9,-1,-1),range(10)): print (i,j),

