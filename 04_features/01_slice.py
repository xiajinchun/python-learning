#!/usr/bin/env python
# -*- coding: utf-8 -*-

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

# L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3。即索引0，1，2
print L[0:3]
print L[1:3]

# 如果第一个索引是0，还可以省略
print L[:3]

# 倒数切片
print L[-2:]
# 倒数第一个元素的索引是-1
print L[-2:-1]

L = range(100)

# 前10个数
print L[:10]
# 后10个数
print L[-10:]
# 前11-20个数
print L[10:20]
# 前10个数，每两个取一个
print L[:10:2]
# 所有数，每5个取一个
print L[::5]
# 什么都不写，只写[:]就可以原样复制一个list
print L[:]

# uple也是一种list，唯一区别是tuple不可变。tuple也可以用切片操作，只是操作的结果仍是tuple
print (0, 1, 2, 3, 4, 5)[:3]

# 字符串切片操作，针对字符串提供了很多各种截取函数，其实目的就是对字符串切片
print 'ABCDEFG'[:3]
print 'ABCDEFG'[::2]