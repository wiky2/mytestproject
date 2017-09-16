#!/usr/bin/env python
# coding: utf-8
#声明必须放在前两行，# coding=<encoding name>

'''

@author: 

@license: 

@contact: 

@software: Test

@file: testDeleteFile.py

@time: 2017/9/16 下午5:05

@desc:删除Frieds目录下的html文件
本文实例讲述了python实现删除文件与目录的方法。分享给大家供大家参考。具体实现方法如下：
os.remove(path)
删除文件 path. 如果path是一个目录， 抛出 OSError错误。如果要删除目录，请使用rmdir().
remove() 同 unlink() 的功能是一样的
在Windows系统中，删除一个正在使用的文件，将抛出异常。在Unix中，目录表中的记录被删除，但文件的存储还在。
os.removedirs(path)
递归地删除目录。类似于rmdir(), 如果子目录被成功删除， removedirs() 将会删除父目录；但子目录没有成功删除，将抛出错误。
举个例子， os.removedirs(“foo/bar/baz”) 将首先删除 “foo/bar/ba”目录，然后再删除foo/bar 和 foo, 如果他们是空的话
如果子目录不能成功删除，将 抛出 OSError异常
os.rmdir(path)
删除目录 path，要求path必须是个空目录，否则抛出OSError错误
 
递归删除目录和文件（类似DOS命令DeleteTree）：
复制代码 代码如下:
import os
for root, dirs, files in os.walk(top, topdown=False):
    for name in files:
        os.remove(os.path.join(root, name))
    for name in dirs:
        os.rmdir(os.path.join(root, name))
方法2：
复制代码 代码如下:
import shutil
shutil.rmtree()

一行搞定：
复制代码 代码如下:
__import__('shutil').rmtree()
希望本文所述对大家的Python程序设计有所帮助。
Python os.walk文件遍历

os.walk(top, topdown=True, onerror=None, followlinks=False) 

 

可以得到一个三元tupple(dirpath, dirnames, filenames), 

第一个为起始路径，第二个为起始路径下的文件夹，第三个是起始路径下的文件。

dirpath 是一个string，代表目录的路径，

dirnames 是一个list，包含了dirpath下所有子目录的名字。

filenames 是一个list，包含了非目录文件的名字。

这些名字不包含路径信息，如果需要得到全路径，需要使用os.path.join(dirpath, name).

通过for循环自动完成递归枚举
'''

import os
def del_files(path):
    for root , dirs, files in os.walk(path):
        for name in files:
            if name.endswith(".html"):
                os.remove(os.path.join(root, name))
    print "Delete File: ",os.path.join(root, name)
# test
if __name__ == "__main__":
    path = '/Users/hack/Downloads/FriendsSub'
    del_files(path)