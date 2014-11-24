#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Animal类
class Animal(object):
    def run(self):
        print 'Animal is running...'

# 编写Dog和Cat类直接从Animal类继承
class Dog(Animal):
    pass

class Cat(Animal):
    pass        

# Dog和Cat拥有Animal的run()方法
dog = Dog()
dog.run()

cat = Cat()
cat.run()

# 对Dog类增加一些方法
class Dog(Animal):
    # 覆盖父类的run()
    def run(self):
        print 'Dog is running...'

    def eat(self):
        print 'Eating meat...'

dog = Dog()
dog.run()
dog.eat()

# 同时修改Cat类
class Cat(Animal):
    # 覆盖父类的run()
    def run(self):
        print 'Cat is running...'

    def eat(self):
        print 'Eating meat...'

# 多态 dog是Dog也是Animal
print isinstance(dog, Dog)
print isinstance(dog, Animal)

# 多态的运用
def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Animal())
run_twice(Dog())
run_twice(Cat())

# 再定义一个Tortoise类型继承Animal
class Tortoise(Animal):
    def run(self):
        print 'Tortoise is running slowly'

run_twice(Tortoise())

# 多态的好处就是，当我们需要传入Dog、Cat、Tortoise……时，我们只需要接收Animal类型就可以
# 然后，按照Animal类型进行操作即可。由于Animal类型有run()方法
# 因此，传入的任意类型，只要是Animal类或者子类，就会自动调用实际类型的run()方法