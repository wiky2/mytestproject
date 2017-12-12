import sys, urllib2, urllib, cookielib
import urlparse
import re, os, string
from stat import *

cookie = cookielib.LWPCookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
#opener = urllib2.build_opener(urllib2.HTTPHandler())
opener.add_handler(urllib2.HTTPHandler())
urllib2.install_opener(opener)def login126(username, password):
	url1 = '''
	https://reg.163.com/logins.jsp?type=1&product=mail126&url=http://entry.mail.126.com/cgi/ntesdoor?hid%3D10010102%26lightweight%3D1%26verifycookie%3D1%26language%3D0%26style%3D-1
	'''
	values = {
		'domain' : '126.com',
		'language' : '0',
		'bCookie' : '',
		'username' : '%s@126.com' % username,
		'savelogin' : '',
		'url2' : 'http%3A%2F%2Fmail.126.com%2Ferrorpage%2Ferr_126.htm',
		'user' : '%s' % username,
		'password' : '%s' % password,
		'style' : '-1',
		'secure' : '',
		'enter.x' : '%B5%C7%A1%A1%C2%BC'
	}

	data = urllib.urlencode(values)
	req = urllib2.Request(url1, data)
	response = opener.open(req)
	data2 =response.read()

	url2 = re.search(r'(?<=(replace\(")).*?(?=")', data2).group()
	response = opener.open(url2)
	data3 = response.read()

	url3 = re.search(r'(?<=(replace\(")).*?(?=")', data3).group()
	response = opener.open(url3)
	data4 = response.read()

	url4 = re.sub(r'main', 'index', response.url )
	response = opener.open(url4)
	data5 = response.read()

	url5 = re.sub(r'/index.jsp', '', url4)
	part1 = re.search(r'(http://).*?(?=/)', url4).group()
	part2 = re.search(r'sid.+', url4).group()
	url5 = '%s/a/s?%s&func=mbox:listMessages' % (part1, part2)

	received_xml = '''
	<?xml version="1.0"?>
	<object>
		<int name="fid">1</int>
		<string name="order">date</string>
		<boolean name="desc">true</boolean>
		<boolean name="topFirst">false</boolean>
		<int name="start">0</int>
		<int name="limit">20</int>
	</object>
	'''

	draft_xml = '''
	<?xml version="1.0"?>
	<object>
		<int name="fid">2</int>
		<string name="order">date</string>
		<boolean name="desc">true</boolean>
		<boolean name="topFirst">false</boolean>
		<int name="start">0</int>
		<int name="limit">20</int>
	</object>
	'''
	sent_xml = '''
	<?xml version="1.0"?>
	<object>
		<int name="fid">3</int>
		<string name="order">date</string>
		<boolean name="desc">true</boolean>
		<boolean name="topFirst">false</boolean>
		<int name="start">0</int>
		<int name="limit">20</int>
	</object>
	''' 
	delete_xml = '''
	<?xml version="1.0"?>
	<object>
		<int name="fid">4</int>
		<string name="order">date</string>
		<boolean name="desc">true</boolean>
		<boolean name="topFirst">false</boolean>
		<int name="start">0</int>
		<int name="limit">20</int>
	</object>
	'''
	data = draft_xml

	req = urllib2.Request(url5, data)
	response = opener.open(req)
	data6 = response.read()

	index = 0
	for match in re.finditer(r'(?<="subject"\>).*?(?=\<)',data6):
		index += 1
		print ("第%d封邮件   %s" % ( index, match.group().decode('utf8').encode('gbk')))

