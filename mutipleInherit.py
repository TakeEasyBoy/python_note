# 多重继承  使用 MixIn
# 定义一个annimal类
class Animal(object):
    pass
#定义哺乳动物
class BuruAnimal(Animal):
    pass
# 定义胎生动物
class EggAnimal(Animal):
    pass
# 定义是否会飞类
class FlyableMixIn(Animal):
    pass
# 定义不会飞类
class LushengMixIn(Animal):
    pass
# 通过继承 哺乳动物,lushengMixIn来实现多重继承
class Dog(BuruAnimal,LushengMixIn):
    pass
class Bird(EggAnimal,FlyableMixIn):
    pass


