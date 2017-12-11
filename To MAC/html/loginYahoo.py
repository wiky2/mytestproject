# -*- coding:gb2312 -*-
import urllib,urllib2,re
def loginYahoo(username, password):	
	url0 = '''
	http://mail.yahoo.com.cn
	'''	
	response = urllib2.urlopen(url0)
	data0 = response.read()
	
	done =re.search( r'(?<=(value=")).*?(?=")', re.search( r'(?<=(name=\.done)).*?(?=>)', data0 ).group()).group()
	challenge = re.search( r'(?<=(value=")).*?(?=")', re.search( r'(?<=(name="\.challenge")).*?(?=>)', data0 ).group()).group()


	url1 = '''
	http://edit.bjs.yahoo.com/config/login
	'''
	values = {
		'.intl' : 'cn',
		'.done' : "%s%s" % (done, "%26.remember%3Dy%26.persistent%3D"),
		'.src' : 'ym',
		'.cnrid' : 'ymhp_20000',
		'.challenge' : '%s' % challenge,
		'login' : '%s@yahoo.cn' % username,
		'passwd' : '%s' % password,
		'.remember' : 'y',
		'submit' : '%B5%C7%C2%BC'
        }
	
	data = urllib.urlencode(values)
	req = urllib2.Request(url1, data)
	req.add_header('Referer', 'http://mail.cn.yahoo.com/')
	
	response = urllib2.urlopen(req)
	data2 =response.read()
	
	folder = re.search( r'(?=(showFolder)).*?(?=")', data2).group()	
	total = re.search( r'(?<=(tt=)).*', folder).group()
	num_per_page = re.search( r'(?<=(pSize=)).*?(?=&)', folder ).group()
	num_per_page = string.atoi(num_per_page)
	mod = string.atoi(total) % num_per_page
	num_times = string.atoi(total) / num_per_page
	if mod > 0 :
		num_times += 1;
	
	index = 0
	for i in xrange(num_times):
		url2 = "http://cn.mc924.mail.yahoo.com/mc/%s&startMid=%d" % (folder, i * num_per_page )
		response = urllib2.urlopen(url2)
		data3 = response.read()	
		
		for match in re.finditer(r'(?<=(showMessage)).*?(?=\>)', data3):#
			index += 1
			part1 = "第%d封邮件" % index
			part2 = "%s" % match.group()
			part1 = part1.decode('utf8').encode('gbk')
			subject = re.search( r'(?<=(title=")).*?(?=")', part2 ).group()
			subject = part1.decode('gbk') + "    " + subject.decode('utf8')
			print( subject.encode('gbk'))
name = 'jery_136510@yahoo.com.cn'
pwd = '13651054931'
loginYahoo(name,pwd)




