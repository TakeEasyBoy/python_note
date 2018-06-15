#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 从wsgiref模块导入:
from wsgiref.simple_server import make_server
from interfaceWSGi import application
#  创建一个服务器,端口为8888
httpd = make_server('',8888,application)
print ('server http on port 8888')
# 监听http请求
httpd.serve_forever()