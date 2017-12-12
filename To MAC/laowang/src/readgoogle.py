#-*- coding:UTF-8 -*-
# -*- coding: utf-8 -*-
import urllib,urllib.request,http.cookiejar
'''
Created on 2012-1-10

@author: Administrator
'''
import unittest


class Test(unittest.TestCase):

    username='曼青'
    header = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}

    def testName(self):
        postdata = {
            'q':self.username
            }
        postdata = urllib.parse.urlencode (postdata)
        req = urllib.request.Request(
                url='http://www.google.com.hk/',
                data= postdata,#��������
                headers = self.header #����ͷ
            )
        result = urllib.request.urlopen(req).read()
        result = str(result)
        print(result)
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()