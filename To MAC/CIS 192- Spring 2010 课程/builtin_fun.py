#!/usr/bin/python


print "-"*10
print "zip"
print "-"*10

#zip()
# zip togeather two sequences
for i,j in zip(range(10),range(9,-1,-1)):
    print i,j

print "-"*10
print "map"
print "-"*10



#map()
#applys a function across a sequnce
def divide_by2(x):
    return float(x)/2

for i in map(divide_by2,range(10)):
    print i

print "-"*10
print "reduce"
print "-"*10

#reduce
def multiply(x,y):
    return x*y

for i in xrange(10):
    print i,reduce(multiply,[1]+range(1,i))
