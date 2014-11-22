#!/usr/bin/env python
# -*- coding: utf-8 -*-

# range函数生成list
print range(1, 11)

L = []
for x  in range(1, 11):
    L.append(x * x)
print L

# 列表生成式生成list
print [x * x for x in range(1, 11)]

# 加上if判断
print [x * x for x in range(1, 11) if x % 2 ==0]

# 使用两层循环，可以生成全排列
print [m + n for m in 'ABC' for n in 'XYZ']

# 运用列表生成式，列出当前目录下的所有文件和目录名
import os
print [d for d in os.listdir('.')]

# for循环其实可以同时使用两个甚至多个变量，比如dict的iteritems()可以同时迭代key和value
d = {'x': 'A', 'y': 'B', 'z': 'C'}
for k, v in d.iteritems():
    print k, '=', v

# 列表生成式也可以使用两个变量来生成list
print [k + '=' + v for k, v in d.iteritems()]

# 把一个list中所有的字符串变成小写
L = ['Hello', 'World', 'IBM', 'Apple']
print [s.lower() for s in L]

# 把一个list中所有的字符串变成小写（判断是否为整数）
L = ['Hello', 'World', 18, 'Apple', None]
print [s.lower() if isinstance(s, str) else s for s in L]