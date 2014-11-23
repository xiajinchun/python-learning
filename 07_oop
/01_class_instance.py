#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 定义Student类，所有类最终都会继承object类
class Student(object):
    pass

# 根据Student类创建出Student的实例
bart = Student()
print bart
print Student

# 可以自由地给一个实例变量绑定属性
bart.name = 'Bart Simpson'
print bart.name

# 通过定义一个特殊的__init__方法，在创建实例的时候，绑定属性
class Student(object):
    # __init__方法的第一个参数永远是self，表示创建的实例本身
    def __init__(self, name, score):
        self.name = name
        self.score = score
# 和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，并且，调用时，不用传递该参数

# 再次创建Student类的时候需要传入参数
bart  = Student('Bart Simpson', 59)
print bart.name
print bart.score

# 数据封装

# 通过函数来访问bart中的数据，打印学生的成绩
def print_score(std):
    print '%s: %s' % (std.name, std.score)
print_score(bart)

# 可以直接在Student类的内部定义访问数据的函数，这样，就把“数据”给封装起来了
# 这些封装数据的函数是和Student类本身是关联起来的，我们称之为类的方法
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

# 要定义一个方法，除了第一个参数是self外，其他和普通函数一样
    def print_score(self):
        print '%s: %s' % (self.name, self.score)

bart  = Student('Bart Simpson', 59)
# 要调用一个方法，只需要在实例变量上直接调用，除了self不用传递，其他参数正常传入
bart.print_score()

# 封装的另一个好处是可以给Student类增加新的方法，比如get_grade
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print '%s: %s' % (self.name, self.score)

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

bart  = Student('Bart Simpson', 59)
# get_grade方法可以直接在实例变量上调用，不需要知道内部实现细节
print bart.get_grade()

# Python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同
bart  = Student('Bart Simpson', 59)
lisa  = Student('Lisa Simpson', 87)
bart.age = 8
print bart.age
print lisa.age # AttributeError: 'Student' object has no attribute 'age'
        