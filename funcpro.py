#高阶函数
#1. map
'''
map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
'''
def f(x):
    return x * x
r = map(f,[x * x for x in range(1,10)])
print (r,list(r))
def ff(x):
    return
#2.reduce
'''
reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
.reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
'''
## str2int
from functools import reduce
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def str2int(s):
    def fn(x,y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn,map(char2num,s))
print (str2int("108611"))

# example
def nom(s):
    return s.capitalize()
r = list(map(nom,['adam', 'LISA', 'barT']))
print (r)

# example map + reduce
def prod(L):
    def f(x,y):
        return x * y
    return reduce(f,L)
print (prod([3, 5, 7, 9]))


# 3.filter
'''
和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素
'''

#sorted
'''
sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，
'''
print (sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.lower))
'''
要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True
'''
print (sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.lower,reverse=True))


# 返回函数
def calc_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
f = calc_sum(1,2,3,4,5)
print (f())

# 匿名函数  lamda
def str2intplus(s):
    def char2num(s):
        return DIGITS[s]
    return reduce(lambda x,y:x * 10 +y,map(char2num,s))
print (str2intplus('123654'))

# 装饰器 decorator
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
@log  #  相当于 now = log(now)
def now():
    print ('2018-06-11')
now()
