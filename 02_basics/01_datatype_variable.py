#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 基本数据类型包括整数、浮点数、字符串、布尔值和空值

# 整数
v_int = 1
v_int = 0xff00

# 浮点数
v_float = 1.23
v_float = 1.23e9

# 字符串
v_string = 'abc'
v_string = "I'm OK."

# 转义字符
print 'I\'m learning\nPython.'

# 用r''表示''内部的字符串默认不转义
print '\\\t\\'
print r'\\\t\\'

# 用'''...'''代替\n换行转义字符
print '''Line1
Line2
Line3''' 

# 布尔值 True、False（区分大小写）
v_bool = True
v_bool = 3 > 2

# 布尔值的 and、or、not 运算
print True and False
print True or False
print not True

# 空值，None表示。None不为0，是一个特殊的空值
v_none = None

# 变量 变量名必须是大小写英文、数字和_的组合，且不能用数字开头

a = 123 # a是整数
print a
a = 'ABC' # a变为字符串
print a

x = 10
x = x + 2

# 常量 常量就是不能变的变量，比如常用的数学常数π就是一个常量。在Python中，通常用全部大写的变量名表示常量
PI = 3.14159265359
# 但事实上PI仍然是一个变量，Python根本没有任何机制保证PI不会被改变，所以，用全部大写的变量名表示常量只是一个习惯上的用法，如果你一定要改变变量PI的值，也没人能拦住你