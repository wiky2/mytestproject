Code highlighting produced by Actipro CodeHighlighter (freeware)http://www.CodeHighlighter.com/--> 1 #encoding=gbk
 
 import sys
 import re
 import cookielib
 import urllib2
 import urllib
 
  
 
 class Renren(object):
 
     def __init__(self):
         self.name=self.pwd=self.domain=self.origURL=self.operate=""
         self.cj=cookielib.LWPCookieJar()
         try:
             self.cj.revert('renren.cookie')
         except Exception,e:
             print e
         self.opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj))
         urllib2.install_opener(self.opener)
 
     def setinfo(self,username,pwd,domain,origURL):
         """设置登陆参数"""
         self.name=username
         self.pwd=pwd
         self.domain=domain
         self.origURL=origURL
 
     def login(self):
         """登陆人人网"""
         params={'domain':self.domain,'origURL':self.origURL,'email':self.name,
                 'password':self.pwd}
         print 'login......'
         req=urllib2.Request(
             'http://www.renren.com/PLogin.do',
             urllib.urlencode(params))
         self.operate = self.opener.open(req)
         if self.operate.geturl() == 'http://www.renren.com/Home.do':
             print 'logged on successfully!'
             self.cj.save("renren.cookie")
             self.__viewinfo()
         else:
             print 'login error.....'
 
     def __viewinfo(self):
         """查看个人的状态"""
         print "正在获取信息......"
         self.__caiinfo()
         
     def __caiinfo(self):
         h3patten=re.compile('^<meta.*/>$')#正则匹配，这里假设匹配元信息
         incontent=self.operate.readlines()#读取整个网页内容
         #print incontent
         for i in incontent:
             content=h3patten.findall(i)
             if len(content)!=0:
                 for ok in content:           
                     print ok.decode("utf-8").encode("gbk")   #进行编码的转换，否则显示是十六进制的数     
         print "已完成！"         
 if __name__=='__main__':
             ren=Renren()
             ren.setinfo("xxxx@gmail.com",'xxxx',
                         "renren.com","http://www.renren.com/SysHome.do")
             ren.login()

