# -*- coding:utf-8 -*-
import urllib,urllib2,re
def loginYahoo(username, password):	
    url1 = 'https://edit.bjs.yahoo.com/config/login'
    url2='?.intl=cn&.done=http%3A%2F%2Fmail.cn.yahoo.com%2Fycn_setcookie_inset.html%3F.done%3Dhttp%253A%252F%252Fmail.cn.yahoo.com%252Finset.html%253Frr%253D1119943579&.src=ym&.cnrid=ymhp_&.challenge=Hl0SCh5DsLQdfH5wvIIRuZKFjM_V&'
    url3='login=%s'% username
    url4='%40yahoo.com.cn&passwd='
    url5='%s&submit=' % password
    url1=url1+url2+url3+url4+url5
    req = urllib2.Request(url1)
    response = urllib2.urlopen(req)
    data2 =response.read()
    print data2
    total =re.search(r'(?<=(tt=)).?(?=&)', data2).group()
    total =re.search(r'(?<=(tt=)).*?(?=&)',data2).group()
    num_per_page = re.search(r'(?<=(pSize=)).*?(?=&)',data2).group()
    num_per_page = string.atoi(num_per_page)
    mod = string.atoi(total) % num_per_page
    num_times = string.atoi(total) / num_per_page
    if mod > 0 :
		num_times += 1
    index = 0
    for i in xrange(num_times):
        url2 = "http://cn.mc150.mail.yahoo.com/mc/showFolder?fid=Inbox&order=down&tt=707&pSize=25&.rand=834624389&.jsrand=4161406&acrumb=3.UESYeTVYn&op=dat"
        response = urllib2.urlopen(url2)
        data3 = response.read()	
        for match in re.finditer(r'(?<=(showMessage)).*?(?=\>)',data3):#匹配showmessage后面的内容
            index += 1
            part1 = "第%d封邮件" % index
            part2 = "%s" % match.group()#第一封邮件后所有的字符串
            part1 = part1.decode('utf8').encode('gbk')
            subject = re.search( r'(?<=(title=")).*?(?=")', part2 ).group()
            subject = part1.decode('gbk') + "    " + subject.decode('utf8')
            print subject.encode('gbk')
name = '你的邮箱'
pwd = '你的密码'
loginYahoo(name,pwd)

