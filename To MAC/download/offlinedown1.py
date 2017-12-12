#作者：   陈仲才   《Python核心编程》 
#本人做了一点修改，并打算从此基础上继续开发出更实用、功能更丰富的Web   下载#查询工具。 
#
#!/bin/python 
#   功能目标： 
#           实时获取web信息　，如股票行情，天气预报 
#   　　　指定站点的信息搜索 
#   　　　网页收集，离线浏览 

#   v0.1 
#   date:   2004-3-24   16:53 

from   sys   import   argv 
from   os   import   makedirs,   unlink,sep 
from   os.path   import   dirname,exists,isdir,splitext 
import   string 

import   formatter 
import   cStringIO 

import   htmllib 
import   urlparse 
import   urllib 


def   downloadHooker(block_cnt,block_size,total_size): #进度显示
        print   block_cnt, '- ',block_size, '- ',total_size, '--- ',(block_size   *   block_cnt   *   1.0)/total_size 

class   Retriever: 
        def   __init__(self,url): 
                self.url   =   url 
                self.file   =   self.filename(url) 

        def   filename(self,url,deffile   =   'index.htm '): #
                parsedurl   =   urlparse.urlparse(url, 'http: ',0) 
                
                path   =   parsedurl[1]     +   parsedurl[2] #www.***.com:80/***/index.html
                file_name   =   string.split(path, '/ ')[-1] #[0]是起点，-1为反向第一个元素，即文件名
                dir   =   dirname(path[:len(path)-len(file_name)]) #获取path中出去文件名的部分，即/***/,dirname已经引入，可以直接使用

                if   sep   !=   '/ ': #如果分隔符不是/,他是系统参数
                        dir   =   string.replace(dir, '/ ',sep) #用/替换sep

                if   not   isdir(dir): #判断dir是否是存在的文件目录
                        if   exists(dir):unlink(dir) #移除dir
                        makedirs(dir) 

                return   path   
                
        def   download(self): #获取文件
                try: 
                        retval   =   urllib.urlretrieve(self.url,self.file) #获取文件对象
                except: 
                        retval   =   ( '***   ERROR:   invalid   URL   "%s " '   %   self.url,) 

                return   retval 
        
        def   parseAndGetLinks(self): 
                self.parser   =   htmllib.HTMLParser(formatter.AbstractFormatter(formatter.DumbWriter(cStringIO.StringIO())))#在python3.2中变为了html.parser.HTMLParser(#strict=True),而cStringIO.StringIO变成io.StringIO ，参考http://nullege.com/codes/search/formatter.DumbWriter
                self.parser.feed(open(self.file).read()) ##打开文件，给分析器喂食。在由完整元素构成的情况下工作；不完整数据情况下，会进行缓冲知道更多数据加进来或者 close() 被调用
                self.parser.close()# 
                return   self.parser.anchorlist 
        

class   Crawler: 
        count   =   0 

        def   __init__(self,url): 
                print   'init ',url 
                
                self.q   =   [url] 
                self.seen   =   [] #空的
                self.dom   =   urlparse.urlparse(url)[1] #解析一个网页地址为6个部分，如
#scheme='', netloc='www.cwi.nl:80', path='/%7Eguido/Python.html', 把【1】给dom,即www.cwi.nl:80
#           params='', query='', fragment=''

        def   getPage(self,url): 
                r   =   Retriever(url) 
                retval   =   r.download() 
                if   retval[0]   ==   '* ': 
                        print   retval, '...   skipping   parse ' #如果遇到*,则跳过解析
                        return 
                Crawler.count   =   Crawler.count   +   1 
                print   '\n( ',Crawler.count, ') ' 
                print   'URL: ',url 
                print   'File: ',retval[0] 
                self.seen.append(url) #将url添加到[]中

                links   =   r.parseAndGetLinks() #把网页文件下下来，解析里面的连接
                for   eachLink   in   links: 
                        if   eachLink[:4]   !=   'http '   and string.find(eachLink,':// ')   ==   -1: #find在没有找到时返回-1，现在python3.2中变为str.find
                                eachLink   =   urlparse.urljoin(url,eachLink) #如urljoin('http://www.cwi.nl/%7Eguido/Python.html', 'FAQ.html')得到'http://www.cwi.nl/%7E#guido/FAQ.html'
                                print   '* ',eachLink, 

                                if   string.find(string.lower(eachLink), 'mailto: ')   !=   -1: #如果是mail link则放弃
                                        print   '...   discarded,   mailto   link ' 
                                        continue 

                                if   eachLink   not   in   self.seen: #没有获取过
                                        if   string.find(eachLink,self.dom)   ==   -1: #如果没有www.cwi.nl:80
                                                print   '...discarded,   not   in   domain ' 
                                        else: 
                                                if   eachLink   not   in   self.q: 
                                                        self.q.append(eachLink) #没有处理过的，则添加到q
                                                        print   '...   new,added   to   Q ' 
                                                else: 
                                                        print   '..   discarded,   already   in   Q ' 
                                else: 
                                        print   '...   discarded,   already   processed. ' ##已经处理过的，则放弃
        def   go(self): 
                print   "go " 
                while   self.q: 
                        url   =   self.q.pop() 
                        self.getPage(url) 
                

def   main(): 
        if   len(argv)   >   1: 
                url   =   argv[1] 
        else: 

                try: 
                        url   =   raw_input( 'Enter   starting   URL: ') 
                except(KeyboardInterrupt,EOFError): 
                        url   =   ' ' 


        if   not   url   :   return 
        robot   =   Crawler(url) 
        robot.go() 
        
if   __name__== "__main__ ": 
        print   'main ' 
        main() 

