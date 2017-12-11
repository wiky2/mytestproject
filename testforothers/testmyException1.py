#!/usr/bin/env python
# coding: utf-8
#声明必须放在前两行，# coding=<encoding name>

'''

@author:

@license:

@contact:

@software: Test

@file: testLogging.py

@time: 2017/10/15 下午9:06

@desc:
#需要注意的是：
1.在上面所示的完整语句中try/except/else/finally所出现的顺序必须是try-->except X-->except-->else-->finally，即所有的except必须在else和finally之前，else（如果有的话）必须在finally之前，而except X必须在except之前。否则会出现语法错误。
2.对于上面所展示的try/except完整格式而言，else和finally都是可选的，而不是必须的，但是如果存在的话else必须在finally之前，finally（如果存在的话）必须在整个语句的最后位置。

3.在上面的完整语句中，else语句的存在必须以except X或者except语句为前提，如果在没有except语句的try block中使用else语句会引发语法错误。也就是说else不能与try/finally配合使用。
'''
import logging,urllib
logger=logging.getLogger()


# logfile='test.log'
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.FileHandler('sendlog.txt')#terminal不输出，写入文件。
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

# 'application' code
# logger.debug('debug message')
# logger.info('info message')
# logger.warn('warn message')
# logger.error('error message')
# logger.critical('critical message')

def func(urllist):
    for i in urllist:
        try:
            u=urllib.urlopen(i)
            str=u.read()
            print str
            print u.info()
            print u.getcode()
        except IOError as e:
            logging.error('错入地址:%s',i)
        else:
            print u.read()
        finally:
            print '结束'
func(['http://www.baidu.com','http://www.163.com','http://www.12312313.com','http://www.12306.cn'])   #一定要加上http
