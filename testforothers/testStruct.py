#!/usr/bin/env python
# coding: utf-8
# 声明必须放在前两行，# coding=<encoding name>

from struct import *
packd_data=pack('iif',6,19,4.73)# 两个整形，一个float
print packd_data
print calcsize('i')
print calcsize('f')
print calcsize('iif')
original_data=unpack('iif',packd_data)
original_data2=unpack('iif',')\@')
print original_data
print original_data2
