# 使用 __slots__动态定义类的属性
# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
class Student(object):
    __slots__ = ('name','age')  # 用tuple申明可以添加的属性名
s = Student()
s.name = 'sputid'
s.age = 220
# s.gender = 'nv'   # 不能定义未在 __slots__中申明的属性


# 使用@property,相当于定义勒一个 getter和setter
class Person(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
p = Person()
p.score = 23
print (p.score)