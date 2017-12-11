def loginTom(username, password):
	url1 = '''
	http://login.mail.tom.com/cgi/login
	'''
	
	values = {
		'type' : '0',
		'user' : '%s' % username,
		'in_username' : '%s@tom.com' % username,
		'pass' : '%s' % password,
		'style' : '21',
		'verifycookie' : 'y'
	}
	
	data = urllib.urlencode(values)
	req = urllib2.Request(url1, data)
	response = opener.open(req)
	data2 =response.read()
	
	sid = re.search(r'(?<=(sid=)).*?(?=&)', data2).group()
	
	url3 = '''
	http://bjapp6.mail.tom.com/cgi/ldapapp?funcid=mails&sid=%s&fid=1
	''' % sid
	response = opener.open(url3)
	data3 = response.read()
	
	b = re.search(r'(?<=nTotalMailCount).*?(?=;)', data3).group()
	c = re.search(r'\d.+', b).group()
	num_per_page = 20
	num_times = string.atoi(c) / 20
	print( num_times )
	
	index = 0
	for match in re.finditer(r'(?<="Mbox_Td_Subject"\>).*?(?=\</)', data3):
		index += 1
		part1 = "第%d封邮件" % index
		part2 = " %s" % match.group()
		part1 = part1.decode('utf8').encode('gbk')
		subject = re.search(r'(?<=\>).+', part2).group()
		subject = part1.decode('gbk') + "    " + subject.decode('gbk')
		print( subject.encode('gbk'))
	
	for i in xrange(num_times - 1):
		url3 = '''
		http://bjapp6.mail.tom.com/cgi/ldapapp?funcid=mails&sid=%s&fid=1&start=%d
		''' % (sid, (i + 1) * num_per_page )
		response = opener.open(url3)
		data3 = response.read()
				
		for match in re.finditer(r'(?<="Mbox_Td_Subject"\>).*?(?=\</)', data3):
			index += 1
			part1 = "第%d封邮件" % index
			part2 = " %s" % match.group()
			part1 = part1.decode('utf8').encode('gbk')
			subject = re.search(r'(?<=\>).+', part2).group()
			subject = part1.decode('gbk') + "    " + subject.decode('gbk')
			print( subject.encode('gbk'))

