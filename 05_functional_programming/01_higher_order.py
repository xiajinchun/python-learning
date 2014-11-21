#!/usr/bin/env python
# -*- coding: utf-8 -*-

# map()函数接收两个参数，一个是函数，一个是序列，map将传入的函数依次作用到序列的每个元素，并把结果作为新的list返回
# 像map()函数这种能够接收函数作为参数的函数，称之为高阶函数

# 把f(x)=x2函数作用在一个list上，就可以用map()实现
def f(x):
    return x * x
print map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])

# reduce把一个函数作用在一个序列[x1, x2, x3...]上
# reduce函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算

# 一个序列求和，就可以用reduce实现
def add(x, y):
    return x + y
print reduce(add, [1, 3, 5, 7, 9])

# 用sum()函数完成求和
print sum([1, 3, 5, 7, 9])

# 把序列[1, 3, 5, 7, 9]变换成整数13579
def fn(x, y):
    return x * 10 + y
print reduce(fn, [1, 3, 5, 7 ,9])

# str转换为int
def fn(x, y):
    return x * 10 + y

def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
print reduce(fn, map(char2num, '13579'))

# 整理成一个str2int的函数
def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn, map(char2num, s))
print str2int('13579')

# 用lambda函数进一步简化
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))
print str2int('13579')

# 排序算法

# sorted()函数就对list进行排序
print sorted([36, 5, 12, 9, 21])

# sorted()是一个高阶函数，可以接受一个比较函数来实现自定义的排序，定义reversed_cmp()倒序排序函数
def reversed_cmp(x, y):
    if x > y:
        return -1
    if x < y:
        return 1
    return 0
print sorted([36, 5, 12, 9, 21], reversed_cmp)

# 字符串排序
print sorted(['about', 'bob', 'Zoo', 'Credit'])

# 忽略大小写按照字母排序
def cmp_ignore_case(s1, s2):
    u1 = s1.upper()
    u2 = s2.upper()
    if u1 < u2:
        return -1
    if u1 > u2:
        return 1
    return 0
print sorted(['about', 'bob', 'Zoo', 'Credit'], cmp_ignore_case)

# 函数作为返回值

# k可变参数求和
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax
print calc_sum(*range(101))

# 如果不需要立刻求和，可以不返回求和的结果，而是返回求和的函数
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

# 调用lazy_sum()返回求和函数
f = lazy_sum(*range(101))
print f

# 调用函数f()时，返回真正的结果
print f()

# 内部函数sum()可以引用外部函数lazy_sum()的参数和局部变量
# 当lazy_sum()返回函数sum时，相关的参数和变量都保存在返回的函数中，称为“闭包”

# 当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数
# 即f1和h2的调用结果互不影响，f1和f2都有自己的作用域

f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print f1 == f2

# 自定义my_map()函数实现map()功能
def my_map(function, *iterable):
    result = []
    for value in iterable:
        result.append(function(value))
    return result

def f(x):
    return x * x
print my_map(f, *[1, 2, 3, 4, 5, 6, 7, 8, 9])

# 自定义prod()函数求积
def prod(*list):
    def multiply(x, y):
        return x * y
    return reduce(multiply, list)
print prod(1, 2, 3, 4)
