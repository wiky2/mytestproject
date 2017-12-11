#!/usr/bin/env python
# coding: utf-8
#声明必须放在前两行，# coding=<encoding name>

'''

@author: 

@license: 

@contact: 

@software: Test

@file: testRequests2.py

@time: 2017/11/19 上午10:03

@desc:
'''
# 二、发送请求与传递参数
#
# 先来一个简单的例子吧！让你了解下其威力：
#
# 复制代码
import requests

r = requests.get(url='http://www.itwhy.org')  # 最基本的GET请求
print(r.status_code)  # 获取返回状态
r = requests.get(url='http://dict.baidu.com/s', params={'wd': 'python'})  # 带参数的GET请求
print(r.url)
print(r.text)  # 打印解码后的返回数据
# 复制代码
# 很简单吧！不但GET方法简单，其他方法都是统一的接口样式哦！

requests.get('https://github.com/timeline.json')  # GET请求
requests.post('https://github.com/timeline.jsonpos')  # POST请求
requests.put('https://github.com/timeline.json')  # PUT请求
requests.delete('https://github.com/timeline.json')  # DELETE请求
requests.head('https://github.com/timeline.json')  # HEAD请求
requests.options('https://github.com/timeline.json')  # OPTIONS请求

# PS：以上的HTTP方法，对于WEB系统一般只支持
# GET
# 和
# POST，有一些还支持
# HEAD
# 方法。
# 带参数的请求实例：

# import requests

requests.get('http://www.dict.baidu.com/s', params={'wd': 'python'})# GET参数实例
requests.post('http://www.itwhy.org/wp-comments-post.php', data={'comment': '测试POST'}) # POST参数实例
# POST发送JSON数据：

import requests
import json

r = requests.post('https://api.github.com/some/endpoint', data=json.dumps({'some': 'data'}))
print(r.json())
# 定制header：
#
# 复制代码
import requests
import json

data = {'some': 'data'}
headers = {'content-type': 'application/json',
           'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}

r = requests.post('https://api.github.com/some/endpoint', data=data, headers=headers)
print(r.text)
# 复制代码
# 三、Response对象
#
# 使用requests方法后，会返回一个response对象，其存储了服务器响应的内容，如上实例中已经提到的
# r.text、r.status_code……
# 获取文本方式的响应体实例：当你访问
# r.text
# 之时，会使用其响应的文本编码进行解码，并且你可以修改其编码让
# r.text
# 使用自定义的编码进行解码。

r = requests.get('http://www.itwhy.org')
print(r.text, '\n{}\n'.format('*' * 79), r.encoding)
r.encoding = 'GBK'
print(r.text, '\n{}\n'.format('*' * 79), r.encoding)
# 其他响应：

r.status_code  # 响应状态码
r.raw  # 返回原始响应体，也就是 urllib 的 response 对象，使用 r.raw.read() 读取
r.content  # 字节方式的响应体，会自动为你解码 gzip 和 deflate 压缩
r.text  # 字符串方式的响应体，会自动根据响应头部的字符编码进行解码
r.headers  # 以字典对象存储服务器响应头，但是这个字典比较特殊，字典键不区分大小写，若键不存在则返回None
# *特殊方法*#
r.json()  # Requests中内置的JSON解码器
r.raise_for_status()  # 失败请求(非200响应)抛出异常

# 案例之一：
#
# 复制代码
import requests

URL = 'http://ip.taobao.com/service/getIpInfo.php'  # 淘宝IP地址库API
try:
    r = requests.get(URL, params={'ip': '8.8.8.8'}, timeout=1)
    r.raise_for_status()  # 如果响应状态码不是 200，就主动抛出异常
except requests.RequestException as e:
    print(e)
else:
    result = r.json()
    print type(result), result, sep='\n'
    # 复制代码
    # 四、上传文件
    #
    # 使用
    # Requests
    # 模块，上传文件也是如此简单的，文件的类型会自动进行处理：
    #
    # 复制代码
    import requests

    url = 'http://127.0.0.1:5000/upload'
    files = {'file': open('/home/lyb/sjzl.mpg', 'rb')}
    # files = {'file': ('report.jpg', open('/home/lyb/sjzl.mpg', 'rb'))}     #显式的设置文件名

    r = requests.post(url, files=files)
    print(r.text)
    # 复制代码
    # 更加方便的是，你可以把字符串当着文件进行上传：
    #
    # 复制代码
    import requests

    url = 'http://127.0.0.1:5000/upload'
    files = {'file': ('test.txt', b'Hello Requests.')}  # 必需显式的设置文件名

    r = requests.post(url, files=files)
    print(r.text)
    # 复制代码
    # 五、身份验证
    #
    # 基本身份认证(HTTP
    # Basic
    # Auth):

    import requests
    from requests.auth import HTTPBasicAuth

    r = requests.get('https://httpbin.org/hidden-basic-auth/user/passwd', auth=HTTPBasicAuth('user', 'passwd'))
    # r = requests.get('https://httpbin.org/hidden-basic-auth/user/passwd', auth=('user', 'passwd'))    # 简写
    print(r.json())
    # 另一种非常流行的HTTP身份认证形式是摘要式身份认证，Requests对它的支持也是开箱即可用的:
    #
    # requests.get(URL, auth=HTTPDigestAuth('user', 'pass'))
    # 六、Cookies与会话对象
    #
    # 如果某个响应中包含一些Cookie，你可以快速访问它们：

    import requests

    r = requests.get('http://www.google.com.hk/')
    print(r.cookies['NID'])
    print(tuple(r.cookies))
    # 要想发送你的cookies到服务器，可以使用
    # cookies
    # 参数：
    #
    # 复制代码
    import requests

    url = 'http://httpbin.org/cookies'
    cookies = {'testCookies_1': 'Hello_Python3', 'testCookies_2': 'Hello_Requests'}
    # 在Cookie Version 0中规定空格、方括号、圆括号、等于号、逗号、双引号、斜杠、问号、@，冒号，分号等特殊符号都不能作为Cookie的内容。
    r = requests.get(url, cookies=cookies)
    print(r.json())
    # 复制代码
    # 会话对象让你能够跨请求保持某些参数，最方便的是在同一个Session实例发出的所有请求之间保持cookies，且这些都是自动处理的，甚是方便。
    # 下面就来一个真正的实例，如下是快盘签到脚本：
    #
    # 复制代码
    import requests

    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
               'Accept-Encoding': 'gzip, deflate, compress',
               'Accept-Language': 'en-us;q=0.5,en;q=0.3',
               'Cache-Control': 'max-age=0',
               'Connection': 'keep-alive',
               'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}

    s = requests.Session()
    s.headers.update(headers)
    # s.auth = ('superuser', '123')
    s.get('https://www.kuaipan.cn/account_login.htm')

    _URL = 'http://www.kuaipan.cn/index.php'
    s.post(_URL, params={'ac': 'account', 'op': 'login'},
           data={'username': '****@foxmail.com', 'userpwd': '********', 'isajax': 'yes'})
    r = s.get(_URL, params={'ac': 'zone', 'op': 'taskdetail'})
    print(r.json())
    s.get(_URL, params={'ac': 'common', 'op': 'usersign'})
    # 复制代码
    # 七、超时与异常
    #
    # timeout
    # 仅对连接过程有效，与响应体的下载无关。
requests.get('http://github.com', timeout=0.001)