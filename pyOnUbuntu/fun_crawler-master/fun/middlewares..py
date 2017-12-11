# Importing base64 library because we'll need it ONLY in case if the proxy we are going to use requires authentication
# -*- coding: utf-8 -*-
import base64
from proxy import Getip
import  logging
# from bs4 import BeautifulSoup
from xml.etree import ElementTree as ET
import requests

# Start your middleware class
class ProxyMiddleware(object):
    http_n=0
    https_n = 0

    # overwrite process request

    def process_request(self, request, spider):
        # Set the location of the proxy
        ips = get_ips()
        #request.meta['proxy'] = "http://YOUR_PROXY_IP:PORT"
        request.meta['proxy'] = "http://%s:%d"%(ips[n][1],int(ips[n][2]))
        logging.info('Sequence - http:%s-%s'%(n,str(ips[n])))
        ProxyMiddleware.http_n=n+1

        # Use the following lines if your proxy requires authentication
        #proxy_user_pass = "USERNAME:PASSWORD"
        # setup basic authentication for the proxy
        #encoded_user_pass = base64.encodestring(proxy_user_pass)
        #request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass
    def get_ips(self):
        html=requests.get('http://www.xicidaili.com/nn/').content
        # soup=BeautifulSoup(html,'html.parser',from_encoding='utf-8')
        # tr_nodes = soup.find_all('tr', class_=True)
        # lists=[[0 for j in range(10)] for i in range(10)]
        # i = 0,j=0
        # for tr_node in tr_nodes:
        #     for item in tr_node.find_all('td'):
        #         lists[i][j]=item.string
        #         print lists[i][j]
        #         j=j+1
        #     i=i+1
        # return lists
        proxy_list={} #字典
        proxy_line=[]
        tree=ET.parse(html)
        trs=tree.xpath('/html/body/div[1]/div[2]/table/tbody/tr')
        for tr in trs:
            if tr.xpath('/td[1]/text()')[0].extract()!="IP地址":
                proxy_line["Addr"]=tr.xpath('/td[1]/text()')[0].extract()
                proxy_line["Port"]=tr.xpath('/td[2]/text()')[0].extract()
                proxy_list.append(proxy_line)
        print proxy_list


