import math
# 函数定义方式  def
'''
python 会自动检查函数输入的个数是否与定义的相匹配
'''
def myfunc(s):
    print (s)
myfunc('你好哇,倩猪')

#定义一个空函数,在不清楚业务逻辑的时候,可以使用空函数将代码跑通
def func():
    pass

# 定义一个移动函数,
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    '''
    python中的返回多个值其实就是一个tuple类型,按照给定位置进行取值使用
    没有返回值时,自动 return None
    '''
    return nx, ny
print (type(move(5,5,10,math.pi/6)))  #<class 'tuple'>
print (move(5,5,10,math.pi/6))  #<class 'tuple'>

# 一元二次方程的解
def quadratic(a, b, c):
    x1 = x2 = 0
    if (a == 0):
        x1 = x2 = -c/b
        return x1, x2
    else :
        if(b * b - 4 * a * c) < 0:
            return " no real root"
        x1 = (-b + math.sqrt(b * b - 4 * a * c)/(2 * a))
        x2 = (-b - math.sqrt(b * b - 4 * a * c)/(2 * a))
        return x1, x2
print (quadratic(4,-2,1))

# 为什么要设计str、None这样的不变对象呢？因为不变对象一旦创建，对象内部的数据就不能修改，
# 这样就减少了由于修改数据导致的错误。此外，由于对象不变，多任务环境下同时读取对象不需要加锁，
# 同时读一点问题都没有。我们在编写程序时，如果可以设计一个不变对象，那就尽量设计成不变对象。


# 传参,可变参数,接收参数为tuple
def calc(*num):
    sum = 0
    for n in num:
        sum = sum + n * n
    return sum
print ('可变参数',calc(1,2,3,4,5))

#关键字参数 **prop  ,用于函数扩展,接收的参数为dict
'''
在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
'''
def person(name,age,**extra):
    print ('name:',name,'age:',age,'other',extra)
person('gege',20,birth='1922-3-12')
extra = {'birth':'1992-2-23','gender':'male'}
person('gege',20,**extra)

#hano tower  n代表的是需要移动的汉诺塔的层数
def move(n,a,b,c):
    if n == 1:
        print (a, '--->', c)   #移动a中的最后一个到最右层
    else:
        move(n-1,a,c,b)         #将最顶层n-1个盘子的移动到b,不需要管怎么实现
        move(1,a,b,c)           #将a最底层的盘子移动到c      将最大的盘子,移动到c
        move(n-1,b,a,c)         #最后将中间的盘子移动到c
move (3,'A','B','C')
