# -*- coding:gb2312 -*-
 
if __name__=='__main__':
    print "-------------code 1----------------"
    a = "和谐b你b可爱女人"
    print a
    print a.find("你")   #index=5,对于一般字符串,按照了
                        #指定的编码方式(这里为gb2312)
                        #并不像unicode字符串一样,把任何字符视为长度1,
                        #而是视为字节长度(5=2+2+1).
    b = a.replace("爱", "喜欢")
    print b
    print "--------------code 2----------------"
    x = "和谐b你b可爱女人"
    print a.find("你")
    y = unicode(x) #此处将x解码(成字符串),如果有编码第二参数,应该和第一行指示编码相同,gb2312格式的unicode
    print y
    print y.encode("utf-8") #若和指示编码不一样,则会打印乱码,把gb2312格式的unicode以utf-8编码，会打印乱码
    print y.encode("gb2312")
    
    print y.find(u"你")  #index=3,因为unicode字符都视为1长度
    z = y.replace(u"爱", u"喜欢小")
    print z.encode("utf-8")
    print z.encode("gb2312")
    print "---------------code 3----------------"
    print y
    newy = unicode(x,"gb2312") #如果和指示编码行的指示不一样的话,将报错
    print newy

