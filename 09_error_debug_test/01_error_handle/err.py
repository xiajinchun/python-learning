#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 如果错误没有被捕获，它就会一直往上抛，最后被Python解释器捕获，打印一个错误信息，然后程序退出
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    bar('0')

#main()

import logging

def main():
    try:
        bar('0')
    except StandardError, e:
        logging.exception(e)

#main()
#print 'END'
# 同样是出错，但程序打印完错误信息后会继续执行，并正常退出

# 要抛出错误，首先根据需要，可以定义一个错误的class，选择好继承关系，然后，用raise语句抛出一个错误
class FooError(StandardError):
    pass

def foo(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value: %s' % s)
    return 10 / n

#print foo(0)
        
# 另一种错误处理的方式
def foo(s):
    n = int(s)
    return 10 / n

def bar(s):
    try:
        return foo(s) * 2
    except StandardError, e:
        print 'Error!'
        # raise语句如果不带参数，就会把当前错误原样抛出
        raise

def main():
    bar('0')

#main()

# except中raise一个Error，还可以把一种类型的错误转化成另一种类型，只要是合理的转换逻辑就可以
try:
    10 / 0
except ZeroDivisionError:
    raise ValueError('input error!')