#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 在Python中，这种一边循环一边计算的机制，称为生成器（Generator）
# generator的工作原理是在for循环的过程中不断计算出下一个元素，并在适当的条件结束for循环
# 对于函数改成的generator来说，遇到return语句或者执行到函数体最后一行语句，就是结束generator的指令，for循环随之结束

# 把一个列表生成式的[]改成()创建generator
L = [x * x for x in range(10)]
print L

g = (x * x for x in range(10))
print g

# 获取generator中的元素，generator保存的是算法，每次调用next()，就计算出下一个元素的值
print g.next()
print g.next()
print g.next()

# generator是可迭代对象，通过for来迭代
for n in g:
    print n

# 斐波拉契数列生成函数
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print b
        a, b = b, a + b
        n = n + 1
fib(6)

# 斐波拉契数列生成器，如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
fib_generator = fib(6)
print fib_generator

# 函数是顺序执行，遇到return语句或者最后一行函数语句就返回
# 而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行
def odd():
    print 'step 1'
    yield 1
    print 'step 2'
    yield 3
    print 'step 3'
    yield 5
o = odd()
# 在执行过程中，遇到yield就中断，下次又继续执行
o.next()
o.next()
o.next()

# 把函数改成generator后，我们基本上从来不会用next()来调用它，而是直接使用for循环来迭代
for n in fib_generator:
    print n