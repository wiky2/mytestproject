'''
Created on 2010-4-1

@author: Administrator
'''
from time import time  
from operator import itemgetter    
def test():      
    count = {}      
    for line in open("test.txt"):          
        for word in line.split():              
            count[word] = 1 + count.get(word, 0)      
    print sorted(count.iteritems(), key=itemgetter(1), reverse=True)[0:30]    
if __name__ == "__main__":      
    t1 = time()      test()      
    print time()-t1