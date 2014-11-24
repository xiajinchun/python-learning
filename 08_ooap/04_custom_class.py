#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 看到类似__slots__这种形如__xxx__的变量或者函数名就要注意，这些在Python中是有特殊用途的
# __slots__我们已经知道怎么用了，__len__()方法我们也知道是为了能让class作用于len()函数
# 除此之外，Python的class中还有许多这样有特殊用途的函数，可以帮助我们定制类

# __str__
class Student(object):
    def __init__(self, name):
        self.name = name

print Student('Colin')

# 定义__str__()方法
class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name: %s)' % self.name

print Student('Colin')

# __str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串
# 定义__repr__()
class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name: %s)' % self.name
    __repr__ = __str__

# __iter__
# 类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1
    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己
    def next(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100:
            raise StopIteration()
        return self.a # 返回下一个值

for n in Fib():
    print n

# __getitem__
# Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行
# 要表现得像list那样按照下标取出元素，需要实现__getitem__()方法
class Fib(object):
    def __getitem__(sefl, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a
f = Fib()
print f[0], f[1], f[2]

# __getitem__()传入的参数可能是一个int，也可能是一个切片对象slice
class Fib(object):
    def __getitem__(sefl, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L
print Fib()[0:5]
# 与之对应的是__setitem__()方法，把对象视作list或dict来对集合赋值
# 还有一个__delitem__()方法，用于删除某个元素

# __getattr__动态返回一个属性
class Student(object):
    def __init__(self):
        self.name = 'Colin'
    
    def __getattr__(self, attr):
        if attr == 'score':
            return 99

# 当调用不存在的属性时，比如score，Python解释器会试图调用__getattr__(self, 'score')来尝试获得属性
s = Student()
print s.name
print s.score

# 返回函数也是完全可以的
class Student(object):
    def __init__(self):
        self.name = 'Colin'
   
    def __getattr__(self, attr):
        if attr == 'age':
            return lambda: 25
s = Student()
print s.age
print s.age()
# 只有在没有找到属性的情况下，才调用__getattr__，已有的属性，比如name，不会在__getattr__中查找

# 注意到任意调用如s.abc都会返回None，这是因为我们定义的__getattr__默认返回就是None
# 要让class只响应特定的几个属性，我们就要按照约定，抛出AttributeError的错误
class Student(object):
    def __init__(self):
        self.name = 'Colin'
   
    def __getattr__(self, attr):
        if attr == 'age':
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)

# 利用完全动态的__getattr__，我们可以写出一个链式调用
class Chain(object):
    def __init__(self, path = ''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

print Chain().status.user.timeline.list

# 任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用
class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)

s = Student('Colin')
print s()

# 能被调用的对象就是一个Callable对象，比如函数和我们上面定义的带有__call()__的类实例
# 通过callable()函数，我们就可以判断一个对象是否是“可调用”对象
print callable(Student('Colin'))
print callable(max)
print callable([1, 2, 3])
print callable(None)
print callable('string')

# 支持Chain().users('colinxia').repos这样的链式调用
class Chain(object):
    def __init__(self, path = ''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    def users(self, user_name):
        return Chain('%s/user/%s' % (self._path, user_name))

print Chain().users('colinxia').repos 