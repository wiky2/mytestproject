# -*- coding: utf-8 -*-
import urllib, urllib2, cookielib, hashlib,threading

import re, os, time, random
import sys
reload(sys)
sys.setdefaultencoding('utf8')
def log(s):
s = "\n" + str(s)
f = open('log.txt', 'a+')
f.write(s)
f.close()

015     sys.stdout.write(s)

016     sys.stdout.flush()

017

018

019 class WeiboCn:

020     all = ('��ע����~~~~','���Ϲ�ע~','��֪������û�з�����ķ�˿����һ��?,������')

021     url = 'http://www.weibo.com'

022     header = {

023         'User-Agent' : 'Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',

024     }

025     def __init__(self, username, password, keyword = None, *args):

026         self.user = username

027         self.keyword = keyword

028         self.all = args or self.all

029         self.cj = cookielib.LWPCookieJar()

030         self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj))

031         urllib2.install_opener(self.opener)

032         self.tryLogin(username, password)

033

034     def tryLogin(self, username, password):

035         bodies = dict(_=int(time.time()),callback='sinaSSOController.preloginCallBack',client='ssologin.js(v1.3.12)',entry='miniblog',user='jiangjia@1616.net')

036         print "Ԥ��¼����ȡservertime & nonce����(����������������)"

037         preloadurl = 'http://login.sina.com.cn/sso/prelogin.php?' + urllib.urlencode(bodies)

038         content = self._request(preloadurl)[1].read()

039         bodies = eval(re.findall('\{.*?\}',content)[0])

040         password = hashlib.sha1(hashlib.sha1(hashlib.sha1(password).hexdigest()).hexdigest() + str(bodies['servertime']) + bodies['nonce']).hexdigest()

041         print "���ܻ������<%s>" % password

042         bodies.update(dict(client='ssologin.js(v1.3.12)',encoding='utf-8',entry='miniblog',gateway='1',password=password,pwencode='wsse',returntype='META',savestate='7',service='miniblog',ssosimplelogin='1',url='http://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack',username=username,useticket=1))

043         response = self._request('http://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.3.12)', bodies)[1]

044         content = response.read()

045         moreurl = re.findall('replace\([\'|"](.*?)[\'|"]\)', content)

046         if len(moreurl) == 0: print "��¼ʧ��!"

047         content = self._request(moreurl[0], dict(Referer='http://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.3.12)',Host='weibo.com'))[1].read()

048         if username in content:

049             print "��¼�ɹ���"

050             self.afterLogin()

051

052     def afterLogin(self):

053         content = self._request('http://weibo.com')[1].read()

054         self.uid = re.findall('\$uid.*?"(\d+)"', content)[0]

055

056     def care(self):

057         url = 'http://weibo.com/pub/news?source=toptray'

058         if self.keyword:

059             url = 'http://weibo.com/k/%s?Refer=Index_header' % urllib.quote(urllib.quote(self.keyword))

060         log(url)

061         content = self._request(url)[1].read()

062         match = re.findall('loadCommentByRid\((.*?)\)', content)

063         for x in match:

064             ownerUid,productId,productName,resourceId,resTitle,resInfo,some,listInDiv,forward,some2 = eval("(%s)" % x)

065             bodies = dict(uid=ownerUid,fromuid=self.uid,refer_sort='profile',atnId='profile')

066             result = self._request('http://weibo.com/attention/aj_addfollow.php?refer_sort=profile&atnId=profile&rnd=%f' % random.random(), bodies, dict(Referer = 'http://weibo.com/'))[1].read()

067             if 'A00006' in result:

068                 log("<%s>��ע<%d>�ɹ���" % (self.user,ownerUid))

069                 content = self.all[random.randint(0, len(self.all)-1)]

070                 bodies = dict(content=content,uid=self.uid,ownerUid=ownerUid,productId=productId,productName=productName,resourceId=resourceId,resTitle=resTitle,resInfo=resInfo,some=some,listInDiv=listInDiv,forward=forward,some2=some2)

071                 result = self._request('http://weibo.com/comment/addcomment.php?f=1&rnd=%f' % random.random(), bodies, dict(Referer='http://weibo.com/pub/news?source=toptray'))[1].read()

072                 if 'A00006' in result:

073                     log("<%s>����<%d>�ɹ���<%s>" % (self.user,ownerUid, content))

074                 else:

075                     log("<%s>����<%d>ʧ�ܣ�" % (self.user,ownerUid))

076                 time.sleep(random.randint(30, 4 * 60))

077             else:

078                 log("<%s>��ע<%d>ʧ�ܣ�" % (self.user,ownerUid))

079                 raise Exception,"��ע<%d>ʧ�ܣ�" % ownerUid

080

081     def unCare(self):

082         content = self._request('http://weibo.com/%s/follow' % str(self.uid))[1].read()

083         pages = re.findall('<em>(\d+)<\/em>', content)

084         log(pages)

085         if len(pages) == 0:

086             return

087         p = apply(max,[int(i) for i in pages])

088         for i in range(p,0,-1):

089             log(i)

090             content = self._request('http://weibo.com/attention/att_list.php?action=0&tag=&page=%d' % i)[1].read()

091             cancel = re.findall('��˿<strong>(.*?)</strong>.*?followcancel\(\'(\d+)', content, re.S)

092             headers = {'Content-Type':'application/x-www-form-urlencoded', 'Origin':'http://weibo.com','Referer':'http://weibo.com/attention/att_list.php?action=0&tag=&page=%d' % i}

093             url = 'http://weibo.com/attention/aj_delfollow.php?rnd=%f' % random.random()

094             for fans,id in cancel:

095                 if int(fans) > 2000:

096                     log("ȡ����ע%sʧ�ܣ�ԭ�򣺷�˿��%s����2000" % (id, fans))

097                     continue

098                 result = self._request(url, dict(touid=id,fromuid=self.uid),headers)[1].read()

099                 if 'A00006' in result:

100                     log("ȡ����ע%s�ɹ���" % id)

101                 else:

102                     log("ȡ����ע%sʧ�ܣ�" % id)

103             time.sleep(10)

104

105     def _request(self, url, bodies = {}, headers = {}):

106         request = urllib2.Request(url, urllib.urlencode(bodies), headers = headers)

107         return (request, self.opener.open(request))

108

109     def _readMainPage(self):

110         return self._request(self.url)[1].read()

111

112 class timer(threading.Thread):

113

114     def __init__(self, weibo):

115         threading.Thread.__init__(self)

116         self.weibo = weibo

117

118     def run(self):

119         #log (">>>>>>��ǰ�û�<%s>�߳�<%s>" % (self.weibo.user,self.getName()))

120         #t = int(time.strftime('%H'))

121         #looptime = 6 * 6 if t < 22 and t > 8 else 60 * 60 * 5

122         '''

123         try:

124             self.weibo.care()

125             log ("��ǰ�û�<%s>�߳�<%s>��ע��һҳ, ��Ϣ%dСʱ���Ժ����~~" % (self.weibo.user,self.getName(), looptime/3600))

126         except Exception, e:

127             log(str(e))

128             log ("��ǰ�û�<%s>�߳�<%s>�����쳣�������ǹ�ע��������, ��Ϣ%dСʱ���Ժ��������~~" % (self.weibo.user,self.getName(), looptime/3600))

129         '''

130         self.weibo.unCare()

131         #time.sleep(looptime)

132         #self.run()

133

134 def run(userinc):

135     f = open(userinc).readlines()

136     if len(f) < 1 : log("�����ļ�Ϊ�գ�")

137     m = re.compile('\|')

138     userlist = []

139     for line in f:

140         if line.startswith('#'):continue

141         line = m.split(line.strip())

142         userlist.append(line)

143     allWeibo = [apply(WeiboCn,u) for u in userlist]

144     pound = []

145     for w in allWeibo:

146         w = timer(w)

147         w.setDaemon(True)

148         w.start()

149         pound.append(w)

150     #time.sleep(10)

151     for x in pound:

152         x.join()

153

154

155 if __name__ == '__main__':

156     run(os.path.join(os.path.dirname(__file__), 'user.txt'))

157     '''

158     while True:

159         m.runtimes += 1

160         m.run()

161     '''
