from html.parser import HTMLParser
import urllib.request
import string
class parseLinks(HTMLParser):
    def handle_starttag(self, tag, attrs):#解析后已经有这些参数，只需重载怎么处理这些参数就行了
        if tag == 'a':
            for name,value in attrs:
                if name == 'href':
                    print(value)#连接
                    print(self.get_starttag_text())#获取连接对应的文字
lParser = parseLinks()
lParser.feed(urllib.request.urlopen("http://www.python.org/index.html").read().decode()) 
lParser.close()# 
