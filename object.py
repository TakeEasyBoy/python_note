class Student(object):
    # 初始化方法,__init__,所有的类都需要这样进行初始化,且其第一个参数永远都是self
    def __init__(self,name,score,gender):
        self.name = name
        self.score = score
        # 属性前面添加两个 __ 表示该属性为私有变量,外部无法访问
        self.__gender = gender
    def print_score(self):
        print ('%s:%d'%(self.name,self.score))
    def print_class(self):
        if(self.score > 80):
            print ('A')
        else:
            print ('foolish!')
    def getgender(self):
        return self.__gender
    def setGender(self,gender):
        self.__gender = gender
chaoge = Student('chaoge',110,'male')
chaoge.print_score()
chaoge.print_class()
# chaoge.__gender   #报错  AttributeError: 'Student' object has no attribute '__gender'
# 通过一个特权方法返回,获取内部私有变脸
chaoge.getgender()
chaoge.setGender('haha')
print (isinstance(chaoge,Student))  # true
print (hasattr(chaoge,'gender'))   # 判断是否含有某个属性
print (getattr(chaoge,'name'))    # chaoge 获取某个属性的值,如果不存在 则会抛出错误
print (getattr(chaoge,'name1','qianjie'))    # 可以传入一个default参数，如果属性不存在，就返回默认值
