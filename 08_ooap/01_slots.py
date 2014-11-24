#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 创建了一个class的实例后，我们可以给该实例绑定任何属性和方法，这就是动态语言的灵活性

class Student(object):
    pass

s = Student()
# 动态给实例绑定一个属性
s.name = 'Colin'
print s.name

# 给实例绑定一个方法
def set_age(self, age):
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s, Student)
s.set_age(25)
print s.age

# 给一个实例绑定的方法，对另一个实例是不起作用的
s2 = Student()
#s2.set_age(25) # AttributeError: 'Student' object has no attribute 'set_age'

def set_score(self, score):
    self.score = score

# 为了给所有实例都绑定方法，可以给class绑定方法
Student.set_score = MethodType(set_score, None, Student)

s.set_score(100)
print s.score

s2.set_score(200)
print s2.score

# Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class能添加的属性
class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称
        
s = Student()
s.name = 'Colin'
print s.name
s.age = 22
print s.age

# 'score'没有被放到__slots__中，所以不能绑定score属性
# s.score = 22 # AttributeError: 'Student' object has no attribute 'score'

# __slots__定义的属性仅对当前类起作用，对继承的子类是不起作用的
class GraduateStudent(Student):
    pass

g = GraduateStudent()
g.score = 999
print g.score