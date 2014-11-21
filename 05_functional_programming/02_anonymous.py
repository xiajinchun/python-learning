#!/usr/bin/env python
# -*- coding: utf-8 -*-

# map()函数直接传入匿名函数
print map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])

# 匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果

# 关键字lambda表示匿名函数，冒号前面的x表示函数参数
# 匿名函数lambda x: x * x实际上就是
def f(x):
    return x * x

# 匿名函数是一个函数对象，可以把匿名函数赋值给一个变量，再利用变量来调用该函数
f = lambda x: x * x
print f
print f(5)

# 把匿名函数作为返回值返回
def build(x, y):
    return lambda: 'result : ' + str(x * x + y * y)
print build(1, 2)
print build(1, 2)()