#-*- coding: GB2312 -*-    


#百度歌曲MP3 top 500批量下载 


import urllib, re,sys,os,os.path,getopt    
threadNum = 45    #线程数    
toDownNum=75   #要下载的mp3的数目，不要超过500哦    
savePath = "mp3-2" 
if (not    os.path.exists(savePath)): 
    os.makedirs(savePath) 


url = "http://list.mp3.baidu.com/topso/mp3topsong.html"    
def getUrlData(url): 
    num    = 0 
    while (num<3): 
        num = num+1 
    try : 
        f =    urllib.urlopen(    url ) 
        data = f.readlines() 
        f.close() 
        return data    
    except:    
        pass 
    return [] 


data = getUrlData(url) 
pattern    = re.compile( r'class="border"><a href="(.*)"' ) 
target = []; 
i=0; 
for line in data: 
    items = pattern.findall( line ) 
    for    item in    items: 
        item=item.replace("lm=-1","lm=0") 
        target.append( item ) 
        i+=1 
        if i>toDownNum:  break; 


print len( target )," mp3 to down " 


mp3Pattern = re.compile( r' (http\:\/\/.*?\.mp3) ' ) 
titlePattern = re.compile( r'<title>.*?_(.*?)\s+</title>' ) 


import threading 
lock = threading.Lock()    
def getMp3(): 
    while True:    
    t = "" 
    lock.acquire() 
    if ( len( target )>0 ):    
        t =    target[0] 
        target.remove( t ) 
    else : 
        return 
    lock.release() 
    tempUrl    = t 
    data = getUrlData(tempUrl) 
    mp3Target = [] 
    title =    ""; 
    for line in data: 
        if ( line.find( "title" )!=-1 ): 
        m = titlePattern.search( line )    
        if ( m ): 
            title = m.group( 1 ) 
            break 
    for line in data: 
        if ( len( mp3Target    )>10 ):    
        break 
        if ( line.find( ".mp3 " )!=-1 ): 
        items =    mp3Pattern.findall( line ) 
        for item in items: 
            mp3Target.append( item ) 
    filename = savePath+"/"+title+".mp3" 
    for t in mp3Target: 
        try    : 
        print "try to get "+title+".mp3,url=",t    
        ret = urllib.urlretrieve( t, filename )    
        size = os.path.getsize(filename) 
        if (size>1024*1024): 
            print "done:"+title+".mp3 from url:    "+t 
            break 
        except : 
        print "fail to get "+title+".mp3 with url: "+t 
        pass 


for num    in range(threadNum): 
    thread = threading.Thread( None, getMp3 ) 
    thread.start() 
    print "start thread    ",num 


