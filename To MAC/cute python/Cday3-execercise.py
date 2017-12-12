#!/usr/bin/env python
   #coding:utf-8
   '''cdays-3-exercise-2.py 
        @not: 
        @see: sys
    '''
    
import sys                                          #
import chardet
def _smartcode(stream):
"""smart recove stream into UTF-8
"""
    ustring = stream
    codedetect = chardet.detect(ustring)["encoding"]
    print codedetect
    try:
        print ustring
        ustring = unicode(ustring, codedetect)
        print ustring
        return "%s %s"%("",ustring.encode('utf8'))
    except:
        return u"bad unicode encode try!"
def collect(file):
       ''' 改变 key-value对为value-key对
       @param file: 
       @return: 一个dict包含value-key对
       '''
       result = {}
       for line in file.readlines(): 
           left, right = line.split()   
           if result.has_key(right):            
               result[right].append(left)            
           else:
               result[right] = [left]                 
       return result
collect(open('cdays-3-test.txt','r'))   
   if __name__ == "__main__":
       if len(sys.argv) == 1:                         
           print 'usage:\n\tpython cdays-3-exercise-2.py cdays-3-test.txt'
       else:
           result = collect(open(sys.argv[1], 'r'))   
           for (right, lefts) in result.items():      
               print "%d '%s'\t=>\t%s" % (len(lefts), right, lefts)

