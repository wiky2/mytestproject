# -*- coding:gb18030-*-
#能够正确解析网页，读取邮件
import urllib,urllib2,re,string
def loginYahoo(username, password):
    cookies = urllib2.HTTPCookieProcessor()
    opener = urllib2.build_opener(cookies)    
    url0 = 'http://mail.cn.yahoo.com/'
    response = opener.open(url0)
    data0 = response.read()
    data0 = data0.decode('utf-8').encode('gb18030 ')#读进来时是utf8编码的str,先打散成unicode，再以gb18030 进行编码成汉字。
    print type(data0)
    done1 =re.search(r'(?<=(name=\.done)).*?(?=>)', data0).group()  
    done= re.search(r'(?<=(value=")).*?(?=")',done1).group()
    challenge1 = re.search(r'(name="\.challenge").*?(?=>)',data0).group() #firbug's sourcecode is different from IE source code
    challenge = re.search(r'(?<=(value=")).*?(?=")',challenge1).group()
    url1 = 'http://edit.bjs.yahoo.com/config/login'
    values = {
		'.intl' : 'cn',
		'.done' : "%s%s" % (done, "%26.remember%3Dy%26.persistent%3D"),#%26.remember%3Dy%26.persistent%3D
		'.src' : 'ym',
		'.cnrid' : 'ymhp_20000',
		'.challenge' : '%s' % challenge,
		'login' : '%s@yahoo.com.cn' % username,
		'passwd' : '%s' % password,
		'.remember' : 'y',
#		'submit' : '%B5%C7%C2%BC'
        }
    url1='http://edit.bjs.yahoo.com/config/login'+'?'+'.intl=cn'+'&'+'.done='+done+'%26.remember%3Dy%26.persistent%3D'+'&'+'.src=ym&.cnrid=ymhp_20000'+'&'+'.challenge='+challenge+'&'+'login='+username+'&'+'passwd='+password+'&'+'.remember=y'
    req = urllib2.Request(url1)
    req.add_header('Referer', 'http://mail.cn.yahoo.com/?cns')
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 5.1; rv:10.0.1) Gecko/20100101 Firefox/10.0.1')
    req.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
#    req.add_header('Accept-Language', 'zh-cn,zh;q=0.5')    
#    req.add_header('Accept-Encoding', 'gzip, deflate')   
    req.add_header('Connection', 'keep-alive')   
#    req.add_header('Referer', 'http://mail.cn.yahoo.com/')
    response = opener.open(req)
#    response = urllib2.urlopen(url1)
    data2 =response.read()
    print data2.decode('utf-8').encode('gb18030 ')#读进来时是utf8编码的str,先打散成unicode，再以gb18030 进行编码成汉字。
    folder = re.search(r'(?<=(showFolder)).*?(?=" ><em>)', data2).group()
    print folder
    folder='showFolder'+folder
    total =re.search(r'(?<=(tt=)).*?(?=&)',data2).group()
    num_per_page = re.search(r'(?<=(pSize=)).*?(?=&)',data2).group()
    num_per_page = string.atoi(num_per_page)
    print num_per_page
    mod = string.atoi(total) % num_per_page
    num_times = string.atoi(total) / num_per_page
    if mod > 0 :
        num_times += 1
        index = 0
    for i in xrange(num_times):
        url2 = "http://cn.mc150.mail.yahoo.com/mc/showFolder?fid=Inbox&sort=date&order=down&startMid=%d" % (num_times*i)
        response = opener.open(url2)
        data3 = response.read()
        data3=data3.decode('utf-8').encode('gb18030 ')#读进来时是utf8编码的str,先打散成unicode，再以gb18030 进行编码成汉字。
        print data3
        fb=open('data3.txt','w+')
        fb.write(data3)
        for match in re.finditer(r'(?<=(showMessage)).*?(?=\>)',data3):#showmessage
            index += 1
            part1 = "第%d封邮件" % index
            part2 = "%s" % match.group()#
            subject = re.search( r'(?<=(title=")).*?(?=")', part2 ).group()
            print subject
name = 'jerry_136510'
pwd = '13651054931'
loginYahoo(name,pwd)
