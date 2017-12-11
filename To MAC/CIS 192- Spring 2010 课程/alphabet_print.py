#/usr/bin/python
#alphabet_print.py

"""Prints the alphabet in caps and lower case using different control
flow structures and a function"""

print

#for loop
for i in range(ord("a"),ord("a")+26):
    print chr(i),

print
print "-"*70


ord_a = ord("a")
for i in xrange(ord_a,ord_a+26):
    print chr(i),

print
print "-"*70



char = "A"
while cmp(char,"Z") <= 0:
    print char,
    char = chr(ord(char) + 1)
print
print

def print_alpha(upper):

    if upper:
        char = "A"        
    else:
        char = "a"
        
    
    while cmp(char,"Z") <= 0:
        print char,
        char = chr(ord(char) + 1)
    print


print "print_alpha(True):",
print_alpha(True)
print "print_alpha(0):",
print_alpha(0)
print "print_alpha([]):",
print_alpha([])

    

