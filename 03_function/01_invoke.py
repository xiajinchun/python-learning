#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python内置了很多有用的函数，我们可以直接调用

# abs()求绝对值
print abs(-100)

# 比较函数cmp(x, y)需要两个参数
print cmp(1,2)
print cmp(2,1)
print cmp(3,3)

# 数据类型转换
print int('123')
print str(1.23)
print unicode(100)
print bool(1)

# 函数名赋值给变量
func_abs = abs
print func_abs(-100)