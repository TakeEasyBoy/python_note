#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 文件名不能命名为requests 模块名,否则报错
import requests
# 获取网页内容  r为resonse对象
#request对象 可以发起 get post option put head 等请求
# 返回的就是一个response对象,可以查看各种状态码 status_code 等
r = requests.get('https://www.douban.com/')
# print (r.text)
# 转换json对象
res = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
print(res.content)
'''
# data可以是一个json格式的参数
payload = {'key':'value','key1':'value2'}
res1 = requests.get('https://api.github.com/events',data={'key':'value'})
# url参数传递
res1 = requests.get('https://api.github.com/events',params=payload)
'''