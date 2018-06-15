#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 有汉字存在的情况下一般使用utf-8的编码形式
# with方法会自动调用 close()方法'
# read()一次读取文件较大的文件,内存会吃紧 比如读一片爱情动作片.rmvb就比读一片学习资料.txt要来的更猛些

with open('./python_note/advanced.py','r') as f1:
    print (f1.read())

import os
print ([x for x in os.listdir('.') if os.path.isdir(x)])
print ([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])
