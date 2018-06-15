#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
符合WSGI标准的一个HTTP处理函数，它接收两个参数
    environ：一个包含所有HTTP请求信息的dict对象；,可以通过PATH_INFO拿到url路径
    start_response：一个发送HTTP响应的函数。
'''

def application(environ,start_response):
    body = '<h1>hello %s</h1>' % (environ['PATH_INFO'][1:] or 'web')
    start_response('200 OK',[('content-type','text/html')])
    return [body.encode('utf-8')]
