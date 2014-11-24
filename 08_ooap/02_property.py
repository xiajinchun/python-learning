#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @property广泛应用在类的定义中，可以让调用者写出简短的代码，同时保证对参数进行必要的检查，这样，程序运行时就减少了出错的可能性

# 绑定属性，检查参数
class Student(object):
 
    def get_score(self):
        return self._score
        
    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer')
        if value < 0 or value > 100:
            raise ValueError('score must be between 0 ~ 100!')
        self._score = value

# @property装饰器负责把一个方法变成属性调用
# 把一个getter方法变成属性，只需要加上@property就可以了
# 此时，@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值
class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer')
        if value < 0 or value > 100:
            raise ValueError('score must be between 0 ~ 100!')
        self._score = value

s = Student()
s.score = 60 # OK，实际转化为s.set_score(60)
print s.score # OK，实际转化为s.get_score()
#s.score = 9999 # ValueError: score must be between 0 ~ 100!

# 可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性
class Student(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2014 - self._birth
# 上面的birth是可读写属性，而age就是一个只读属性，因为age可以根据birth和当前时间计算出来
s = Student()
s.birth = 1992
print s.birth
print s.age
s.age = 22 # AttributeError: can't set attribute