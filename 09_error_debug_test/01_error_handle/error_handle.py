#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 用错误码来表示是否出错十分不便，因为函数本身应该返回的正常结果和错误码混在一起，造成调用者必须用大量的代码来判断是否出错
def foo():
    r = some_function()
    if r==(-1):
        return (-1)
    # do something
    return r

def bar():
    r = foo()
    if r==(-1):
        print 'Error'
    else:
        pass

# Python内置了try...except...finally...的错误处理机制
try:
    print 'try...'
    r = 10 / 0
    print 'result:', r
except ZeroDivisionError, e:
    print 'except:', e
finally:
    print 'finally...'
print 'END'
# 当我们认为某些代码可能会出错时，就可以用try来运行这段代码
# 如果执行出错，则后续代码不会继续执行，而是直接跳转至错误处理代码，即except语句块
# 执行完except后，如果有finally语句块，则执行finally语句块，至此，执行完毕

# 可以有多个except来捕获不同类型的错误
try:
    print 'try...'
    r = 10 / int('a')
    print 'result:', r
except ValueError, e:
    print 'ValueError:', e
except ZeroDivisionError, e:
    print 'ZeroDivisionError:', e
finally:
    print 'finally...'
print 'END'

# 如果没有错误发生，可以在except语句块后面加一个else，当没有错误发生时，会自动执行else语句
try:
    print 'try...'
    r = 10 / int('a')
    print 'result:', r
except ValueError, e:
    print 'ValueError:', e
except ZeroDivisionError, e:
    print 'ZeroDivisionError:', e
else:
    print 'no error!'
finally:
    print 'finally...'
print 'END'

# Python的错误其实也是class，所有的错误类型都继承自BaseException
try:
    foo()
except StandardError, e:
    print 'StandardError'
except ValueError, e:
    print 'ValueError'
# 第二个except永远也捕获不到ValueError，因为ValueError是StandardError的子类，如果有，也被第一个except给捕获了

# 使用try...except捕获错误还有一个巨大的好处，就是可以跨越多层调用
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except StandardError, e:
        print 'Error!'
    finally:
        print 'finally...'