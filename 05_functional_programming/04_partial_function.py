#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python的functools模块提供了很多有用的功能，其中一个就是偏函数（Partial function）

# int()函数可以把字符串转换为整数，当仅传入字符串时，int()函数默认按十进制转换
print int('12345')

# 但int()函数还提供额外的base参数，默认值为10
print int('12345', base = 8)
print int('12345', 16)

# 定义int2()函数，默认把base=2传进去
def int2(x, base = 2):
    return int(x, base)
print int2('1000000')
print int2('1000001')

# functools.partial的作用就是，把一个函数的某些参数（不管有没有默认值）给固定住（也就是设置默认值）
# 然后返回一个新的函数，调用这个新函数会更简单
import functools
int2 = functools.partial(int, base = 2)
print int2('1000000')
print int2('1000000', base = 10)