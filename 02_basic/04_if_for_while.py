#!/usr/bin/env python
# -*- coding: utf-8 -*-

# if、if-else 注意不要少写了冒号:
# 要是非零数值、非空字符串、非空list等，就判断为True，否则为False
age = 3
if age >= 18:
    print 'adult'
elif age >= 6:
    print 'teenager'
else:
    print 'kid'

# Python的循环有两种，一种是for...in循环，依次把list或tuple中的每个元素迭代出来
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print name

# range()函数，可以生成一个整数序列，range(101)生成的序列是从0开始小于101的整数
sum = 0
for x in range(101):
    sum = sum + x
print sum

# 第二种循环是while循环，只要条件满足，就不断循环，条件不满足时退出循环
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print sum

# 用raw_input()读取用户的输入，输入1982，结果却显示00后
birth = raw_input('birth: ')
if birth < 2000:
    print '00前'
else:
    print '00后'

# raw_input()读取的内容永远以字符串的形式返回,把字符串和整数比较就不会得到期待的结果，必须先用int()把字符串转换为我们想要的整型
birth = int(raw_input('birth: '))