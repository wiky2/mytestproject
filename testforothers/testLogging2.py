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
'''
import logging
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
logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')
