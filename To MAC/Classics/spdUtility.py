
# -*- coding: utf-8 -*-
'''
Created on 2010-4-3

@author: Administrator
'''
#filename:spdUtility.py


import bisect

import string

import htmllib

import formatter

class PriorityQueue(list):
#    "优先级队列,用于存储url,及它的优先级"
    def __init__(self):

        list.__init__(self)

        self.map = {}

        

    def push(self, item):

        # 按顺序插入，防止重复元素;若要按升序排列，可使用bisect.insort_left

        if self.count(item) == 0:

            bisect.insort(self, item)

            self.map[ item[1] ] = item

        

    def pop(self):

        r = list.pop(self)

        del self.map[ r[1] ]

        return r

        

    def getitem(self,url):

        if self.map.has_key( url ):

            return self.map[url]

        else :

            return None

        

    def empty(self):

        return len(self) == 0

        

    def remove(self,item):

        list.remove(self, item)

        del self.map[ item[1] ]

    

    def count(self,item):

        if len(self) == 0 :

            return 0

        #二分查找

        left = 0

        right = len(self)-1

        mid = -1

        while left <= right:

            mid = (left+right)/2

            if self[mid] < item :

                left = mid + 1

            elif self[mid] > item :

                right = mid -1

            else :

                break

        return self[mid] == item and 1 or 0

        

class Parser(htmllib.HTMLParser):

    # HTML分析类    

    def __init__(self, verbose=0):

        self.anchors = {}

        f = formatter.NullFormatter()

        htmllib.HTMLParser.__init__(self, f, verbose)

    

    def anchor_bgn(self, href, name, type):

        self.save_bgn()

        self.anchor = href

    

    def anchor_end(self):

        text = string.strip(self.save_end())

        if self.anchor and text:

            self.anchors[text] = self.anchors.get(text, []) + [self.anchor]

            

def main(): #just for test

    pq = PriorityQueue()

    # add items out of order

    pq.push( (1,'http://www.baidu.com') )

    pq.push( (2,'http://www.sina.com') )

    pq.push( (3,'http://www.google.com') )

    pq.push( (1,'http://www.163.com') )

    

    item = pq.getitem('http://www.sina.com')

    print item

    print pq.count(item)

    pq.remove( item )

    print pq.count(item)

    # print queue contents

    while not pq.empty():

        print pq.pop()

        

if __name__ == '__main__':

    main()
