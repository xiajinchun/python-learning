#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python的函数定义非常简单，但灵活度却非常大
# 除了正常定义的必选参数外，还可以使用默认参数、可变参数和关键字参数

# 必选参数
def power(x):
    return x * x
print power(5)

def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print power(5, 2)

# 默认参数，多个默认参数时，调用的时候，既可以按顺序提供默认参数
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print power(5)
print power(5, 2)

# 不按顺序提供部分默认参数，当不按顺序提供部分默认参数时，需要把参数名写上
def enroll(name, gender, age=6, city='Beijing'):
    print 'name:', name
    print 'gender:', gender
    print 'age:', age
    print 'city:', city
print enroll('Sarah', 'F')
print enroll('Adam', 'M', city='Tianjin')

# 默认参数很有用，但使用不当，也会掉坑里
def add_end(L=[]):
    L.append('END')
    return L

print add_end([1, 2, 3])
print add_end(['x', 'y', 'z'])
# 再次调用add_end()时，结果就不对了
print add_end()
print add_end()

# Python函数在定义的时候，默认参数L的值就被计算出来了，即[]
# 因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容
# 则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了
# 所以，定义默认参数要牢记一点：默认参数必须指向不变对象，我们可以用None这个不变对象来实现
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

# 用list或tuple来实现可变参数
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print calc([1, 2, 3])
print calc((1, 3, 5, 7))

# 可变参数
# 定义可变参数和定义list或tuple参数相比，仅仅在参数前面加了一个*号
# 参数numbers接收到的是一个tuple
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print calc(1, 3, 5, 7)

# 允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去
nums = [1, 2, 3]
14
print calc(*nums)

# 关键字参数
# 关键字参数在函数内部自动组装为一个dict
def person(name, age, **kw):
    print 'name:', name, 'age:', age, 'other:', kw
# 函数person除了必选参数name和age外，还接受关键字参数kw
person('Michael', 30)
person('Adam', 45, gender='M', job='Engineer')

# 和可变参数类似，也可以先组装出一个dict
kw = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, city=kw['city'], job=kw['job'])
person('Jack', 24, **kw)

# 参数组合
# 参数定义的顺序必须是：必选参数、默认参数、可变参数和关键字参数
def func(a, b, c=0, *args, **kw):
    print 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw
func(1, 2, 3, 'a', 'b', x=99)

# 通过一个tuple和dict
args = (1, 2, 3, 4)
kw = {'x': 99}
func(*args, **kw)