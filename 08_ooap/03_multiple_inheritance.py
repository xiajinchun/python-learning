#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 通过多重继承，一个子类就可以同时获得多个父类的所有功能
# 不需要复杂而庞大的继承链，只要选择组合不同的类的功能，就可以快速构造出所需的子类

class Animal(object):
    pass

# 大类:
class Mammal(Animal):
    pass

class Bird(Animal):
    pass

# 各种动物:
class Dog(Mammal):
    pass

class Bat(Mammal):
    pass

class Parrot(Bird):
    pass

class Ostrich(Bird):
    pass

# 给动物再加上Runnable和Flyable的功能，只需要先定义好Runnable和Flyable的类
class Runnable(object):
    def run(self):
        print('Running...')

class Flyable(object):
    def fly(self):
        print('Flying...')

# 需要Runnable功能的动物，就多继承一个Runnable
class Dog(Mammal, Runnable):
    pass

# 需要Flyable功能的动物，就多继承一个Flyable
class Bat(Mammal, Flyable):
    pass

# 通过多重继承就可以实现，这种设计通常称之为Mixin
# 为了更好地看出继承关系，我们把Runnable和Flyable改为RunnableMixin和FlyableMixin
class RunnableMixin(object):
    def run(self):
        print('Running...')

class FlyableMixin(object):
    def fly(self):
        print('Flying...')

class CarnivorousMixin(object):
        def eat(self):
        print('Carnivorous...')
        
class Dog(Mammal, RunnableMixin, CarnivorousMixin):
    pass

# Mixin的目的就是给一个类增加多个功能
# 这样，在设计类的时候，我们优先考虑通过多重继承来组合多个Mixin的功能，而不是设计多层次的复杂的继承关系