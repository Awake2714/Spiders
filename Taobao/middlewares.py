# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html
from fake_useragent import UserAgent
import requests
from scrapy import signals
import time

class UserAgentMiddleware(object):
    def process_request(self, request, spider):
        ua = UserAgent()
        request.headers['User-Agent'] = ua.random

class ProxyMiddleware(object):
    def process_request(self, request, spider):
        proxy_url = 'http://piping.mogumiao.com/proxy/api/get_ip_al?appKey=50cb3f42af0c4abd917e887172843888&count=1&expiryDate=0&format=2&newLine=2'
        res = requests.get(proxy_url, timeout=10)
        time.sleep(5)
        ip = res.text.strip('\n\r')
        request.meta['proxy'] = 'http://' + ip