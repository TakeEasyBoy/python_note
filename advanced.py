import os
# 高级特性
# 1.切片
L = list(range(1,100))
print (L[:10])      #取前10个元素
print (L[-10:])      #取最后10个元素
print (L[10:20])    #取 10 - 20个元素
print (L[::5])         #所有范维内,每5个去一个
print (L[:10:2])      #取前10个元素每两个娶一个
# 字符串也可以使用这样的操作
def my_trim(s):
    if not s[0] == ' ':
        return s[0:-1]
    elif s[-1] == ' ':
        return s[:-1]
    else:
        return s
print (my_trim(' python!!'))

# 2.迭代
#  for index,item in target

# 3.列表生成式
print ([x * x for x in range(1, 11)])
print ([m + n for m in 'ABC' for n in 'XYZ'])
print ([d for d in os.listdir('.')])

#4. 生成器 :generator ,可以遍历
g = (x * x for x in range(1, 11))
print ('generater----',g)
for i in g:
    print(i)
