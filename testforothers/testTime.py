#!/usr/bin/env python
# coding: utf-8
#声明必须放在前两行，# coding=<encoding name>

'''

@author: 

@license: 

@contact: 

@software: Test

@file: testTime.py

@time: 2017/10/15 下午5:35

@desc:
'''
# python
# time和datetime的常用转换处理
# 一、time
#
# 1、获取当前时间和时区

# 复制代码
import time,datetime
now = time.time()  # 当前时间 float类型
print time.strftime("%Y-%m-%d %H:%M:%S")  # 当前时间 str
# '2016-11-04 15:29:58'

time.ctime()  # 当前时间 english str
# 'Fri Nov 4 15:40:42 2016'
time.time()
1478244363.875308
time.localtime()  # 当前时间 time结构体
# time.struct_time(tm_year=2016, tm_mon=11, tm_mday=4, tm_hour=15, tm_min=26, tm_sec=9, tm_wday=4, tm_yday=309,tm_isdst=0)

time.localtime(now)  # float -> struct_time
# time.struct_time(tm_year=2016, tm_mon=11, tm_mday=4, tm_hour=15, tm_min=26, tm_sec=1, tm_wday=4, tm_yday=309,tm_isdst=0)

time.strftime('%Z', time.localtime())  # 显示当前时区 China standard timezone
'CST'
time.gmtime()  # 显示UTC标准时间 跟中国相差8个钟
# time.struct_time(tm_year=2016, tm_mon=11, tm_mday=4, tm_hour=7, tm_min=26, tm_sec=28, tm_wday=4, tm_yday=309,tm_isdst=0)
# 复制代码
# 其中time.time()
# 返回的一个float型，是从1970年1月1日0时起到当前经过的秒数，注意这里是分时区的

time.localtime()
# 返回的是一个time结构体，其中包括tm_year, tm_mon, tm_mday, tm_hour, tm_min, tm_sec, tm_wday, tm_yday, tm_isdst = 0（夏令时间标志）

# 　　2、时间字符串转成time格式

a = '2016-11-04 15:29:58'
print time.strptime(a, "%Y-%m-%d %H:%M:%S")
# time.struct_time(tm_year=2016, tm_mon=11, tm_mday=4, tm_hour=15, tm_min=29, tm_sec=58, tm_wday=4, tm_yday=309,tm_isdst=-1)
# 　　3、时间字符串转成float类型

a = '2016-11-04 15:29:58'
print time.mktime(time.strptime(a, "%Y-%m-%d %H:%M:%S"))
#
# 　　4、time
# tuple格式转成字符串

time_tuple = (2016, 11, 04, 13, 51, 18, 2, 317, 0)
time.strftime("%Y-%m-%d %H:%M:%S", time_tuple)
'2016-11-04 13:51:18'
# 　　5、float类型转成时间字符串

a = 1478244598.0
b = time.localtime(a)
time.strftime("%Y-%m-%d %H:%M:%S", b)
'2016-11-04 15:29:58'
# 　　6、时间和日期格式化符号说明
#
# 复制代码
# % y
# 两位数的年份表示（00 - 99）
# % Y
# 四位数的年份表示（000 - 9999）
# % m
# 月份（01 - 12）
# % d
# 月内中的一天（0 - 31）
# % H
# 24
# 小时制小时数（0 - 23）
# % I
# 12
# 小时制小时数（01 - 12）
# % M
# 分钟数（00 = 59）
# % S
# 秒（00 - 59）
#
# % a
# 本地简化星期名称
# % A
# 本地完整星期名称
# % b
# 本地简化的月份名称
# % B
# 本地完整的月份名称
# % c
# 本地相应的日期表示和时间表示
# % j
# 年内的一天（001 - 366）
# % p
# 本地A.M.或P.M.的等价符
# % U
# 一年中的星期数（00 - 53）星期天为星期的开始
# % w
# 星期（0 - 6），星期天为星期的开始
# % W
# 一年中的星期数（00 - 53）星期一为星期的开始
# % x
# 本地相应的日期表示
# % X
# 本地相应的时间表示
# % Z
# 当前时区的名称
# % % % 号本身
# 复制代码
#
#
# 　　二、datetime
#
# 　　1、获取当前时间
#
# 复制代码
datetime.datetime.now()  # datetime tuple
datetime.datetime(2016, 11, 4, 15, 52, 17, 680405)

time.mktime(datetime.datetime.now().timetuple())  # float类型
datetime.datetime.now().replace(second=0, microsecond=0)  # 秒数为0 毫秒数为0
datetime.datetime(2016, 11, 4, 15, 54)

datetime.date.today()  # 当前天
datetime.date(2016, 11, 4)
# 复制代码
# 　　2、datetime
# tuple转成时间字符串

now = datetime.datetime.now()
now.strftime("%Y-%m-%d %H:%S:%M")
# '2016-11-04 16:06:00'
# 　　3、datetime
# tuple转成float类型

now = datetime.datetime.now()
time.mktime(now.timetuple())
# 1478246406.0
# 　　4、datetime
# date和time转换

a = datetime.date(2016, 11, 4)
datetime.datetime.strptime(str(a), '%Y-%m-%d')
datetime.datetime(2016, 11, 4, 0, 0)
datetime.date(2016, 11, 4)
# 　　5、获取当前时间的前一段时间

now = datetime.datetime.now()

# 前一小时
a = now - datetime.timedelta(hours=1)
print a.strftime("%Y-%m-%d %H:%S:%M")

# 前一天
b = now - datetime.timedelta(days=1)
print b.strftime("%Y-%m-%d %H:%S:%M")

# 上周日
c = now - datetime.timedelta(days=now.isoweekday())
print c.strftime("%Y-%m-%d %H:%S:%M")  # 上周一
d = c - datetime.timedelta(days=6)
print d.strftime("%Y-%m-%d %H:%S:%M")  # 上个月最后一天
e = now - datetime.timedelta(days=now.day)
print e.strftime("%Y-%m-%d %H:%S:%M")

# 上个月第一天
print datetime.datetime(e.year, e.month, 1)
# 　　6、获取两个时间相差的秒数

print (datetime.datetime.now() - datetime.datetime(1970, 1, 1, 0, 0, 0, 0)).total_seconds()  # 获取的是UTC标准时区的时间float类型