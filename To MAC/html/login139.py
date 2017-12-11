# -*- coding:gb2312 -*-
def login139(username, password):
	url1 = '''
	https://mail.10086.cn/Login/Login.ashx?s=0&u=MTU4Mjc0MjgxMjk=&m=1
	'''
	
	values = {
		'UserName' : '%s' % username,
		'Password' : '%s' % password,
		'VerifyCode' : ''
	}
	
	data = urllib.urlencode(values)
	req = urllib2.Request(url1, data)
	response = opener.open(req)
	data2 =response.read()
	
	url2 = re.search(r'(?<=(href="\" target="_blank" rel="nofollow">)',data2).group()
	response = opener.open(url2)
	data3 = response.read()
	
	received_xml = '''
	<object>
		<int name="fid">1</int>
		<string name="order">receivedDate</string>
		<boolean name="desc">true</boolean>
		<int name="start">0</int>
		<int name="limit">20</int>
		<string name="topFlag">top</string>
	</object>
	'''
	
	getfolder_xml = '''
	<object>
		<boolean name="stats">true</boolean>
	</object>
	'''
	sid = re.search(r'sid.+', url2).group()
	url3 = '''
	http://wmsvr2.mail.10086.cn/c/s?func=mbox:listMessages&%s
	''' % sid
	
	data = received_xml

	req = urllib2.Request(url3, data)
	response = opener.open(req)
	data4 = response.read()
	
	index = 0
	for match in re.finditer(r'(?<="subject"\>).*?(?=\<)',data4):
		index += 1
		

