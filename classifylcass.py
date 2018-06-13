#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 定制类 意思就是重定义类中的一些默认方法,覆盖其默认行为
# __xxx__这样的方法一般都是类中的默认方法,有时候需要自己定义
class Student(object):
    def __init__(self, name):
         self.name = name
    def __str__(self):    #重写str方法,打印的时候就会显得好看些,而不是显示   <__main__.Student object at 0xxxxxxx>
         return 'Student object (name: %s)' % self.name
    __repr__ = __str__     #  s = Student('heh)  print(s)  <__main__.Student object at 0x109afb310>  __repr__()是给程序猿看到的字符串
print (Student('CHaoge'))

#应用 在进行一些restfulApi设计的时候可以使用

class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))
    # 可以传递参数,直接调用 chain('hh')
    def __call__(self,path):
        return Chain('%s/:%s'%(self._path, path))
    def __str__(self):
        return self._path
    __repr__ = __str__
print (Chain().user.test.hehe)      # /user/test/hehe
print (Chain().user.login.info)     # /user/login/info
print (Chain().user('hehe').login('haha').info)     # /user/login/info
