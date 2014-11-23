#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 判断对象类型，使用type()函数
# 基本类型
print type(123)
print type('str')
print type(None)

# 函数或者类
print type(abs)

class Animal(object):
    def run(self):
        print 'Animal is running...'

a  = Animal()
print type(a)

# type()函数返回的是type类型
print type(123) == type(456)
print type('abc') == type('123')
print type('abc') == type(123)

# Python把每种type类型都定义好了常量，放在types模块里
import types
print type('abc') == types.StringType
print type(u'abc')==types.UnicodeType
print type([])==types.ListType
print type(str)==types.TypeType

# 所有类型本身的类型就是TypeType
print type(int) == type(str) == types.TypeType

# isinstance()判断
class Dog(Animal):
    # 覆盖父类的run()
    def run(self):
        print 'Dog is running...'

    def eat(self):
        print 'Eating meat...'

dog = Dog()
print isinstance(dog, Dog) and isinstance(dog, Animal)

# 能用type()判断的基本类型也可以用isinstance()判断
print isinstance('a', str)
print isinstance(u'a', unicode)
print isinstance('a', unicode)

# 并且还可以判断一个变量是否是某些类型中的一种
print isinstance(123, (str, unicode))
print isinstance('a', (str, unicode))
print isinstance(u'a', (str, unicode))

# 使用dir()函数获得一个对象的所有属性和方法，它返回一个包含字符串的list
print dir('ABC')
print dir(dog)

# 仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态
class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x

obj = MyObject()

print hasattr(obj, 'x')
print hasattr(obj, 'y')

setattr(obj, 'y', 19)
print hasattr(obj, 'y')

print getattr(obj, 'y', -1)

# 也可以获得对象的方法
print hasattr(obj, 'power')
print getattr(obj, 'power')
fn = getattr(obj, 'power')
print fn()

# 只有在不知道对象信息的时候，我们才会去获取对象信息
# 假设我们希望从文件流fp中读取图像，我们首先要判断该fp对象是否存在read方法
# 如果存在，则该对象是一个流，如果不存在，则无法读取。hasattr()就派上了用场
def readImage(fp):
    if hasattr(fp, 'read'):
        return readData(fp)
    return None