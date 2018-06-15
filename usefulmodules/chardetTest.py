#!/usr/bin/python3
# -*- coding: utf-8 -*-
import chardet
# 用于检测编码
data ='离离原上草，一岁一枯荣'
print (chardet.detect(data))    # {'confidence': 0.99, 'language': '', 'encoding': 'utf-8'}
