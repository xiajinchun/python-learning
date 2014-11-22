#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 迭代是通过for ... in来完成
d = {'a': 1, 'b': 2, 'c': 3}

# 迭代key
for key in d:
    print key

# 迭代value
for value in d.itervalues():
    print value

# 迭代key和value
for k, v in d.iteritems():
    print 'k =', k, 'v =', v

# 字符串也是可迭代对象
for ch in 'ABC':
    print ch

# 通过collections模块的Iterable类型判断一个对象是可迭代对象
from collections import Iterable

print isinstance('abc', Iterable) # str可迭代
print isinstance([1,2,3], Iterable) # list可迭代
print isinstance(123, Iterable) # 整数不可迭代

# enumerate函数可以把一个list变成索引-元素对
for i, value in enumerate(['a', 'b', 'c']):
    print i, value

# 上面的for循环里，同时引用了两个变量，在Python里是很常见的
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print x, y