import timeimport pcapimport dpktfrom dpkt.ip 
import IP from dpkt.tcp 
import TCP from dpkt.udp 
import UDP from dpkt.http 
import *from dpkt.ethernet 
import Ethernet pc=pcap.pcap()    
#注，参数可为网卡名，如eth0#pc.setfilter('tcp port 80')    
#设置监听过滤器#
ip = IP() 
def formattime(t): #日期字段格式化     
    return time.strftime('%c',time.gmtime(t+8*3600)) 
    for ptime,i in pc:    
        #ptime为收到时间，pdata为收到数据    
        p=Ethernet(pdata)    
try:        
    sStr1 = p.data.data.data        
    srcip='%d.%d.%d.%d'%tuple(map(ord,list(p.data.src)))        
    ip='%d.%d.%d.%d'%tuple(map(ord,list(p.data.dst)))        
    print '========================================================='        
    print 'time = ',formattime(ptime)        
    print p.data.__class__.__name__        
    print p.data.data.__class__.__name__        
    print '%s------->%s,PORT:%d' %(srcip,ip,p.data.data.dport)        
    print 'data = ',sStr1    
except:        
    pass
