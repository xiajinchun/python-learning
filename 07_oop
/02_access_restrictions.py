#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量
# 比如_name，这样的实例变量外部是可以访问的
# 但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。

# 在Class内部，可以有属性和方法，而外部代码可以通过直接调用实例变量的方法来操作数据，就隐藏了内部的复杂逻辑
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print '%s: %s' % (self.name, self.score)

# 但是，外部代码还是可以自由地修改Student实例的name、score属性
bart = Student('Bart Simpson', 98)
print bart.score
bart.score = 59
print bart.score

# 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，
# 在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print '%s: %s' % (self.__name, self.__score)

bart = Student('Bart Simpson', 98)
bart.print_score()
#print bart.__score # AttributeError: 'Student' object has no attribute '__score'

# 可以给Student类增加get_name和get_score这样的方法，让外部代码获取name和score
class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print '%s: %s' % (self.__name, self.__score)

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

bart = Student('Bart Simpson', 98)
print bart.get_name()
print bart.get_score()

# 可以给Student类增加set_name和set_score这样的方法，让外部代码修改name和score
class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print '%s: %s' % (self.__name, self.__score)

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_name(self, name):
        self.__name = name

    def set_score(self, score):
        # 原先那种直接通过bart.score = 59也可以修改，这样做是因为可以对参数做检查，避免传入无效的参数
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

bart = Student('Bart Simpson', 98)
print bart.get_name()
print bart.get_score()
bart.set_name('Bart')
bart.set_score(99)
print bart.get_name()
print bart.get_score()

# 双下划线开头的实例变量不是一定不能从外部访问，可以通过_Student__name来访问__name变量
print bart._Student__name