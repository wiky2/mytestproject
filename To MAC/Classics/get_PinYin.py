# -*-coding:utf-8-*- 
# ���غ��ֵ�ƴ�� 
def Return_pinyin(word): 
    global reslist 
    for line in reslist: 
        if (word==line[0]+line[1]) or (word==line[2]+line[3]): 
                str = line 
                break 
# ȡ�ٺ͢�֮������� 
    s = str.find(u'��')+4 
    e = str.find(u'��')+3 
    return str[s:e] 
def GetPy(word): 
#����װ����Դ�ļ� 
    i=0 
    allstr = '' 
    while i<len(word): 
        if ord(word[i])>127: 
            if allstr: 
                allstr += Return_pinyin(word[i]+word[i+1]) 
            else: 
                allstr = Return_pinyin(word[i]+word[i+1]) 
                i +=2 
        else: 
            if allstr: 
                allstr += word[i] 
            else: 
                allstr = word[i] 
                i +=1 
    return allstr 
if __name__=='__main__': 
    f = open('wbtext1.txt','r') 
    reslist = f.readlines() 
    f.close() 
    word = raw_input(u'�����뺺��: ') 
    print GetPy(word).lower() 