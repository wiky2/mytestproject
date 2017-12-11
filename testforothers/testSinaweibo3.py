#!/usr/bin/env python
# coding: utf-8
#声明必须放在前两行，# coding=<encoding name>

'''

@author: 

@license: 

@contact: 

@software: Test

@file: testSinaweibo3.py

@time: 2017/11/19 下午10:35

@desc:
'''
#!usr/bin/env python
#coding:utf-8

''''' 
以关键词收集新浪微博 
'''
#import wx
import sys
import urllib
import urllib2
import re
import time
from datetime import datetime
from datetime import timedelta
import random
from lxml import etree
import logging
import simlogin
from main.simlogin import WeiboLogin
from mysql import SqlHelper

class CollectData():
"""数据收集类
利用微博高级搜索功能，按关键字搜集一定时间范围内的微博。
"""
def __init__(self, keyword, startTime, interval='50', flag=True, begin_url_per = "http://s.weibo.com/weibo/"):
    self.begin_url_per = begin_url_per #设置固定地址部分
    self.setKeyword(keyword) #设置关键字
    self.setStartTimescope(startTime) #设置搜索的开始时间
    #self.setRegion(region) #设置搜索区域
    self.setInterval(interval) #设置邻近网页请求之间的基础时间间隔（注意：过于频繁会被认为是机器人）
    self.setFlag(flag)
    self.logger = logging.getLogger('main.CollectData') #初始化日志

##设置关键字
##关键字需解码后编码为utf-8
def setKeyword(self, keyword):
    self.keyword = keyword.decode('utf-8','ignore').encode("utf-8")
    print 'twice encode:',self.getKeyWord()

##关键字需要进行两次urlencode
def getKeyWord(self):
    once = urllib.urlencode({"kw":self.keyword})[3:]
    return urllib.urlencode({"kw":once})[3:]

##设置起始范围，间隔为1天
##格式为：yyyy-mm-dd
def setStartTimescope(self, startTime):
    if not (startTime == '-'):
    self.timescope = startTime + ":" + startTime
    else:
    self.timescope = '-'

##设置搜索地区
#def setRegion(self, region):
# self.region = region

##设置邻近网页请求之间的基础时间间隔
def setInterval(self, interval):
    self.interval = int(interval)

##设置是否被认为机器人的标志。若为False，需要进入页面，手动输入验证码
def setFlag(self, flag):
    self.flag = flag

##构建URL
def getURL(self):
    return self.begin_url_per+self.getKeyWord()+"&typeall=1&suball=1×cope=custom:"+self.timescope+"&page="

##爬取一次请求中的所有网页，最多返回50页
def download(self, url, maxTryNum=4):
    hasMore = True #某次请求可能少于50页，设置标记，判断是否还有下一页
    isCaught = False #某次请求被认为是机器人，设置标记，判断是否被抓住。抓住后，需要，进入页面，输入验证码
    name_filter = set([]) #过滤重复的微博ID

    i = 1 #记录本次请求所返回的页数
    while hasMore and i < 51 and (not isCaught): #最多返回50页，对每页进行解析，并写入结果文件
        source_url = url + str(i) #构建某页的URL
        print source_url
        data = '' #存储该页的网页数据
        goon = True #网络中断标记
        ##网络不好的情况，试着尝试请求三次
        for tryNum in range(maxTryNum):
            try:
                html = urllib2.urlopen(source_url, timeout=12)
                data = html.read()
                break
            except:
                if tryNum < (maxTryNum-1):
                    time.sleep(10)
                else:
                    print 'Internet Connect Error!'
                    self.logger.error('Internet Connect Error!')
                    self.logger.info('url: ' + source_url)
                    self.logger.info('page: ' + str(i))
                    self.flag = False
                    goon = False
                    break
        if goon:
            lines = data.splitlines()
            isCaught = True
            for line in lines:
                ## 判断是否有微博内容，出现这一行，则说明没有被认为是机器人
                if line.startswith('<script>STK && STK.pageletM && STK.pageletM.view({"pid":"pl_weibo_direct"'):
                    isCaught = False
                    n = line.find('html":"')
                    if n > 0:
                        j = line[n + 7: -12].encode("utf-8").decode('unicode_escape').encode("utf-8").replace("\\", "") #去掉所有的\
                        ## 没有更多结果页面
                        if (j.find('<div class="search_noresult">') > 0):
                            hasMore = False
                        ## 有结果的页面
                        else:
                        #此处j要decode，因为上面j被encode成utf-8了
                        page = etree.HTML(j.decode('utf-8'))
                        ps = page.xpath("//p[@node-type='feed_list_content']") #使用xpath解析得到微博内容
                        addrs = page.xpath("//a[@class='W_texta W_fb']") #使用xpath解析得到博主地址
                        addri = 0
                        #获取昵称和微博内容
                        for p in ps:
                            name = str(p.attrib.get('nick-name')) #获取昵称
                            txt = str(p.xpath('string(.)')).lstrip() #获取微博内容
                            addr = str(addrs[addri].attrib.get('href')) #获取微博地址
                            addri += 1
                            if(name != 'None' and str(txt) != 'None' and name not in name_filter): #导出数据到excel中
                                name_filter.add(name)
                                print name,timescope,addr,txt
                                #print "save with same name ok"
                    break
            lines = None
            ## 处理被认为是机器人的情况
            if isCaught:
                print 'Be Caught!'
                self.logger.error('Be Caught Error!')
                #self.logger.info('filePath: ' + savedir)
                self.logger.info('url: ' + source_url)
                #self.logger.info('fileNum: ' + str(fileNum))
                self.logger.info('page:' + str(i))
                data = None
                self.flag = False
                break
            ## 没有更多结果，结束该次请求，跳到下一个请求
                if not hasMore:
                    print 'No More Results!'
                if i == 1:
                    pass
                #time.sleep(random.randint(3,8))
            else:
                pass
                #time.sleep(10)
                data = None
                break
            i += 1
            ## 设置两个邻近URL请求之间的随机休眠时间，防止Be Caught
            sleeptime_one = random.randint(self.interval-25,self.interval-15)
            sleeptime_two = random.randint(self.interval-15,self.interval)
            if i%2 == 0:
                sleeptime = sleeptime_two
            else:
                sleeptime = sleeptime_one
                print 'sleeping ' + str(sleeptime) + ' seconds...'
                time.sleep(sleeptime)
        else:
            break

##改变搜索的时间范围，有利于获取最多的数据
def getTimescope(self, perTimescope):
    if not (perTimescope=='-'):
        times_list = perTimescope.split(':')
        start_date = datetime(int(times_list[-1][0:4]), int(times_list[-1][5:7]), int(times_list[-1][8:10]) )
        start_new_date = start_date + timedelta(days = 1)
        start_str = start_new_date.strftime("%Y-%m-%d")
        return start_str + ":" + start_str
    else:
        return '-'

def main():
    logger = logging.getLogger('main')
    logFile = './collect.log'
    logger.setLevel(logging.DEBUG)
    filehandler = logging.FileHandler(logFile)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler)

    #模拟登录代码在下面
    login = WeiboLogin('用户名', '密码')
    login.login()


while True:
    ## 接受键盘输入
    #keyword = raw_input('Enter the keyword(type \'quit\' to exit ):')
    keyword = '关键字'
    if keyword == 'quit':
    sys.exit()
    startTime = '2017-04-25'#raw_input('Enter the start time(Format:YYYY-mm-dd):')
    #region = raw_input('Enter the region([BJ]11:1000,[SH]31:1000,[GZ]44:1,[CD]51:1):')
    interval = 30#raw_input('Enter the time interval( >30 and deafult:50):')

    ##实例化收集类，收集指定关键字和起始时间的微博
    cd = CollectData(keyword, startTime, interval)
    cd.download(cd.getURL())
    print '---------------'
    break;
    '''
    while cd.flag: 
    #print cd.timescope 
    logger.info(cd.timescope) 
    url = cd.getURL()
    print url 
    cd.download(url) 
    cd.timescope = cd.getTimescope(cd.timescope) #改变搜索的时间，到下一天 
    else: 
    cd = None 
    print '-----------------------------------------------------' 
    print '-----------------------------------------------------' 
    '''
    #else:
    # logger.removeHandler(filehandler)
    # logger = None
if __name__ == '__main__':
    main()

#! /usr/bin/env python
#coding=utf8

import urllib
import urllib2
import cookielib
import base64
import re
import json
import hashlib
import rsa
import binascii

cj = cookielib.LWPCookieJar()
cookie_support = urllib2.HTTPCookieProcessor(cj)
opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
urllib2.install_opener(opener)
postdata = {
     'entry': 'weibo',
     'gateway': '1',
     'from': '',
     'savestate': '7',
     'userticket': '1',
     'ssosimplelogin': '1',
     'vsnf': '1',
      'vsnval': '',
      'su': '',
      'service': 'miniblog',
      'servertime': '',
      'nonce': '',
      'pwencode': 'rsa2', #加密算法
      'sp': '',
      'encoding': 'UTF-8',
      'prelt': '401',
      'rsakv': '',
      'url': 'http://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack',
      'returntype': 'META'
}

class WeiboLogin:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __get_spwd(self):
        rsaPublickey = int(self.pubkey, 16)
        key = rsa.PublicKey(rsaPublickey, 65537) #创建公钥
        message = self.servertime + '\t' + self.nonce + '\n' + self.password #拼接明文js加密文件中得到
        passwd = rsa.encrypt(message, key) #加密
        passwd = binascii.b2a_hex(passwd) #将加密信息转换为16进制。
        return passwd

    def __get_suser(self):
        username_ = urllib.quote(self.username)
        username = base64.encodestring(username_)[:-1]
        return username

    def __prelogin(self):
        prelogin_url = 'http://login.sina.com.cn/sso/prelogin.php?entry=sso&callback=sinaSSOController.preloginCallBack&su=%s&rsakt=mod&client=ssologin.js(v1.4.4)' % self.username
        response = urllib2.urlopen(prelogin_url)
        p = re.compile(r'{.*}')
        strurl = p.search(response.read() ).group()
        dic = dict(eval(strurl)) #json格式的response
        self.pubkey = str(dic.get('pubkey'))
        self.servertime = str(dic.get('servertime'))
        self.nonce = str(dic.get('nonce'))
        self.rsakv = str(dic.get('rsakv'))

    def login(self):
        url = 'http://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.18)'
        self.__prelogin()
        try:
            self.__prelogin() #预登录
        except:
            print 'Prelogin Error'
            return
        global postdata
        postdata['servertime'] = self.servertime
        postdata['nonce'] = self.nonce
        postdata['su'] = self.__get_suser()
        postdata['sp'] = self.__get_spwd()
        postdata['rsakv'] = self.rsakv
        postdata = urllib.urlencode(postdata)
        headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:37.0) Gecko/20100101 Firefox/37.0'} #伪装成浏览器
        req  = urllib2.Request(
        url = url,
        data = postdata,
        headers = headers
        )
        result = urllib2.urlopen(req)
        text = result.read()
        #p = re.compile('location\.replace\'(.∗?)\'')
        p = re.compile(r'location.replace\(\'(.*)\'')
        try:
            #login_url = p.search(text).group()
            login_url = p.findall(text)[0]
            urllib2.urlopen(login_url)
            print "Login Succeed!"
        except:
            print 'Login Error!'
#!usr/bin/env python
#coding:utf-8

import MySQLdb

class SqlHelper:
    def __init__(self,user='root',pwd='123456',database='nepudata',port=3306):
        self.user = user
        self.pwd = pwd
        self.database = database
        self.port = port

    def execute(self,sql):
        conn= MySQLdb.connect(
            host='localhost',
            port = self.port,
            user=self.user,
            passwd=self.pwd,
            db =self.database
        )
        conn.set_character_set('utf8')
        cur = conn.cursor()
        r = cur.execute(sql)
        cur.close()
        conn.commit()
        conn.close()
        '''
        try:
            r = cur.execute(sql)
        except:
            print sql
        finally:
            cur.close()
            conn.commit()
            conn.close()'''
    def execute2(self,sql,params):
        conn= MySQLdb.connect(
            host='localhost',
            port = self.port,
            user=self.user,
            passwd=self.pwd,
            db =self.database
        )
        conn.set_character_set('utf8')
        cur = conn.cursor()
        try:
            r = cur.execute(sql,params)
        except:
            print sql
        finally:
            cur.close()
            conn.commit()
            conn.close()