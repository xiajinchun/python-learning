#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 函数是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数
def now():
    print '2014-11-22'

f = now
f()

# 函数对象有一个__name__属性
print now.__name__
print f.__name__

# 在函数调用前后自动打印日志，但又不希望修改now()函数的定义
# 这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）
# 本质上，decorator就是一个返回函数的高阶函数
def log(func):
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper

# log是一个decorator，所以接受一个函数作为参数
# 用Python的@语法，把decorator置于函数的定义处
@log
def now():
    print '2014-11-22'

# 调用now()函数，不仅会运行now()函数本身，还会在运行now()函数前打印一行日志
now()

# 由于log()是一个decorator，返回一个函数，所以，原来的now()函数仍然存在
# 只是现在同名的now变量指向了新的函数，于是调用now()将执行新函数，即在log()函数中返回的wrapper()函数
# wrapper()函数的参数定义是(*args, **kw)，因此，wrapper()函数可以接受任意参数的调用

# 如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print '%s %s():' % (text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator

# 3层嵌套decorator用法
@log('execute')
def now():
    print '2014-11-22'
now()

# Python内置的functools.wraps()把原始函数的__name__等属性复制到wrapper()函数中
import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper

@log
def now():
    print '2014-11-22'

print now()

# 针对带参数的decorator
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print '%s %s():' % (text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute')
def now():
    print '2014-11-22'

print now()

# 函数调用的前后执行的decorator
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print 'begin call'
        func(*args, **kw)
        print 'end call'
    return wrapper
@log
def now():
    print '2014-11-22'
now()

# 既支持无参又支持有参的decorator
# def log(func):
#     if not isinstance(func, (function)):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kw):
#             print '%s %s():' % (text, func.__name__)
#             return func(*args, **kw)
#         return wrapper
#     return decorator
# print 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
# @log
# def now():
#     print '2014-11-22'
# now()