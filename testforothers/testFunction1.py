#!/usr/bin/env python
# coding: utf-8
#声明必须放在前两行，# coding=<encoding name>

'''

@author: 

@license: 

@contact: 

@software: Test

@file: testFunction1.py

@time: 2017/10/1 下午2:59

@desc:
'''
def fun1():
    print 'hehe'

test=fun1()
print type(test)
def fun2(*num):
    '''
    接受的参数放入一个tuple 
    '''
    sum1=0
    for i in num:
        sum1=sum1+i
    return sum1
print fun2(1,2,3,4)
print fun2(1,2,3,4,5)
print fun2(1,2,3,4,5,6)
def fun3(num1,num2):
    '''
    接受2个参数，然后判断参数类型 
    '''
    if isinstance(num1,int) and isinstance(num2,int):
        sum2=num1+num2
        return sum2
    else:
        print 'wrong input number'
    return
print fun3(3,5)
# assert fun3(5,8)==14
def fun4(*num):
    '''
    接受人一多参数，返回最大、最小值 
    '''
    for x in num:
        if isinstance(x,int):
            pass
        else:
            return "参数中有非数值类型"
    num=list(num)
    num.sort()#在原有基础上排序
    print 'min:',num[0],'  max:',num[len(num)-1]
fun4(15,13,19,8,7,21,14)
def fun5(*num):
    '''
    接收任意多的参数，返回最长的 
    '''
    num=list(num)
    num.sort(key=lambda x:len(x))
    print num[len(num)-1]
fun5('boy','girl','bike','stupid')
def get_doc(module1):
    '''
    用pydoc获取帮助文档    
    '''
    import os
    command1='pydoc %s' % module1
    doc1=os.popen(command1).read()
    return doc1
print get_doc('open')
print get_doc('list')#获取帮助文档

def get_dir(folder):
    import glob
    dir1 = glob.glob('%s/*.*' % folder)
    if dir1 == []:
        return '文件夹为空或不存在'
    else:
        return dir1


print get_dir('/Users/mateseries/Documents/PycharmProjects/testforothers/')



def get_text(module1):
    '''
    用cat获取文本内容
    '''
    import os
    if os.path.exists(module1):
        command1='cat %s' % module1
        doc1=os.popen(command1).read()
    else:
        return '文件不存在'
# print get_text('help_string.txt')
print get_text('121.txt')

def func6(args1,args2):
    return args1+args2
print dir(func6.__code__)#可以看到属性
print func6.__code__.co_varnames#输出参数名称到一个列表。
print func6.__code__.co_filename#看到在哪个文件定义的。
print dir(func6) #与上面不一样

def func7(args1):
    args1[0]=1
    return args1
print func7([5,4,3])# 可变参数支持自修改。
templist=[7,6,5]
print func7(templist)# 可变参数支持自修改。

def func8(numlist):
    '''
    返回偶数类型
    '''
    result=[]
    for i in numlist:
        if isinstance(i,int):
            if i%2==0:
                result.append(i)
    return result
print func8([1,2,3,4,5,6,7,8])

def func9(url):
    import urllib
    if url.startswith('http://') or url.startswith('https://'):
        f=urllib.urlopen(url)
        s=f.read()
        f.close()
    return s
# print func9('http://www.baidu.com')

func10=lambda x:x+1 if x>0 else "error"#类似于函数,隐藏了一个return功能
print func10(2)
print func10(3)
print func10(4)
print func10(-1)
print func10(-2)

func11=lambda x:[(x,i) for i in range(0,10) ]if x>0 else "error"#类似于函数
print func11(5)

t=[1,2,3,4,5,6]
func12 = filter(lambda x:x>3,t)#对可迭代对象放入x，执行lambda运算。这种方式最常用。
print func12#输出运算后的输入值

t=[1,2,3,4,5,6]
func13 = map(lambda x:x>3,t)#对可迭代对象放入x，执行lambda运算。这种方式最常用。
print func13#输出执行运算后的输出值（布尔值）。

def func14(arg1,arg2,arg3):
    return arg1,arg2,arg3
print func14(1,2,3)#函数参数位置匹配

def func15(arg1='',arg2=None,arg3=''):
    return arg1,arg2,arg3

print func15(arg3=5,arg1=4,arg2=3)#函数参数字典匹配

#带*函数参数tuple匹配，带**的函数参数用dic匹配，如果匹配不到，则输出为空
def func16(*kargs,**kwargs):
    return kargs#
print func16(2,3,4,[11,12,31],{15,17,18})#所有参数放入一个dic,会优先过滤。
def func17(*kargs,**kwargs):
    return kwargs#
print func17(2,3,4,[11,12,31],{15,17,18})#空dic，因为没有dic
def func18(a,*kargs,**kwargs):
    return kargs#
print func18(2,3,4,[11,12,31],{15,17,18})#tuple少一个元素，因为被a提前匹配走了。
def func19(a,d,b=4,*kargs,**kwargs):
    return kargs#
print func19(2,3,4,[11,12,31],{15,17,18})#先匹配位置，再匹配关键字
# def func20(a,b=4,d,*kargs,**kwargs):#先匹配位置，再匹配关键字，tuple，dic，所以这里报语法错误。
#     return kargs#
# print func20(2,3,4,[11,12,31],{1:15,2:16},{15,17,18})
def func21(a,d,b=4,*kargs,**kwargs):
    return kargs#
print func21(2,3,4,[11,12,31],{1:15,2:16},{15,17,18})#先匹配位置，再匹配关键字，tuple，dic,
def func22(a,d,b=4,*kargs,**kwargs):
    return kargs,kwargs#kwargs为空
print func22(2,3,4,[11,12,31],{15,17,18},{1:15,2:16})#先匹配位置，再匹配关键字，tuple，dic,结果同上
def func23(a,d,b=4,*kargs,**kwargs):
    return kargs,kwargs#kwagrs不为空
print func23(2,3,4,[11,12,31],{15,17,18},{1:15,2:16},e=18,f=17,g=23)#先匹配位置，再匹配关键字，tuple，dic,所以最后字典参数全部收集到一个字典里

def func24(a):
    '''
    阶乘
    '''
    if a>0:
        return func24(a-1)*a
    else:
        return 1
print func24(5)#先匹配位置，再匹配关键字，tuple，dic,所以最后字典参数全部收集到一个字典里

def func25(*kargs):
    str1 = filter(lambda x:isinstance(x,str),kargs)
    return str1

print func25(1,2,3,'lilei',4,5,6,'hanmeimei')#输出字符串

def func26(name,**kargs):
    '''
    比较笨的拼接方法
    '''
    student_info=[name]
    for key,value in kargs.items():
        student_info.extend([','+key+":"+str(value)])
    student_info_line=''.join(student_info)
    return student_info_line


print func26('lilei',years=4,weight=20)#lilei收集到name,而years=4,weight=20收集到**kargs

def func27(name,**kargs):
    '''
    正确的快速方法
    '''
    student_info = [("%s:%s,")%(k,v) for k,v in kargs.items()]#将逗号连接的字典，格式化为冒号连接的字典
    student_info.insert(0,name+",")
    return ''.join(student_info)
print func27('lilei',years=4,weight=20)

# def func28(name,**kargs):
#     '''
#     错误的方法
#     '''
#     student_info = [(k,v) for k,v in kargs.items()]#
#     print student_info
#     student_info.insert(0,name+",")
#     return ''.join(student_info)
# print func28('lilei',years=4,weight=20)

def get_dir2(folder):
    import os
    dir_list = []
    if os.path.exists(folder):
        if os.path.isdir(folder):
            for i in os.listdir(folder):
                dir_list.append(i)
            return dir_list
        else:
            return '不是目录'
    else:
        return '路径不存在'


print get_dir2('/Users/mateseries/Documents/PycharmProjects/testforothers/')#正确输出
print get_dir2('FriendsSub')#正确输出

def func29(url,folder_path=None):
    '''
    读取网页，保存到一个文件夹下，随机名字
    '''
    import urllib
    try:
        if not ((url.startswith('http://')) or url.startswith('https://')):
            return u'地址不符'
        if not os.path.isdir(folder_path):
            return u'folder_path非文件夹'
        d=urllib.urlopen(url)
    except Exception as e:
        return u'网页无法打开'
    else:
        content=d.read()
        import os
        if not os.path.isdir(folder_path):
            return '非文件夹'
        else:
            import random
            random_filename=random.randint(1,1000)
            file_path="%s%s.txt"%(folder_path,random_filename)
            # file_path=os.path.join(folder_path,random_filename)#报错
            d=open(file_path,'w')
            d.write(content)
            d.close()
            return file_path
print func29('http://www.163.com','/Users/mateseries/Documents/PycharmProjects/testforothers/')

def get_url_list(url):
    '''
    分析url里面有多少链接,用split方法
    '''
    import urllib,os
    if not ((url.startswith('http://')) or url.startswith('https://')):
        return u'地址不符'
    d = urllib.urlopen(url)
    content = d.read()
    return len(content.split('<a href='))-1
# print get_url_list('http://www.baidu.com')

def merge(folder_path):
    import os
    for f in os.listdir(folder_path):
        file_path = os.path.join(folder_path,f)
        if os.path.isdir(file_path):
            merge(file_path)
        else:
            merge_file=open('/Users/mateseries/Documents/PycharmProjects/testforothers/mergetest/mergetest.txt','ab+')
            content=open(file_path,'r').read()
            merge_file.write(content)
            merge_file.close()
# merge('/Users/mateseries/Documents/PycharmProjects/testforothers/mergetest/')

def qs(url):
    import urlparse
    query=urlparse.urlparse(url).query
    q=urlparse.parse_qs(query)
    return dict(([(k,v[0]) for k,v in q.items()]))
print qs('http://www.baidu.com/')
print qs('http://www.baidu.com/pan?name=wiky&pw=1234567')

def delete_test(folder_path):
    import os
    if not os.path.exists(folder_path):
        return u'路径不存在'
    for f in os.listdir(folder_path):
        file_path = os.path.join(folder_path,f)
        if os.path.isdir(file_path):
            delete_test(file_path)
            os.rmdir(file_path)#删除目录
        else:
            os.remove(file_path)#删除文件路径，如果是目录，则要删除目录中的文件,目录保留。
delete_test('/Users/mateseries/Documents/PycharmProjects/testforothers/mergetest2/')



