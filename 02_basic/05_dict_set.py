#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python内置了字典：dict的支持，键-值（key-value）存储，具有极快的查找速度，dict的key必须是不可变对象
score = {'Michael': '95', 'Bob': 75, 'Tracy': 85}
print score['Michael']

# 通过in判断key是否存在
print 'Michael' in score

# dict提供的get方法，如果key不存在，可以返回None，或者自己指定的value
print score.get('Bob')
print score.get('Boba',-1)

# 删除一个key，用pop(key)方法，对应的value也会从dict中删除
score.pop('Michael')

# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key
s = set([1,2,2,3])
print s

# 通过add(key)方法可以添加元素到set中
s.add(4)
print s

# 通过remove(key)方法可以删除元素
s.remove(2)
print s

# 两个set可以做数学意义上的交集、并集等操作
s1 = set([1,2,3])
s2 = set([2,3,4])

print s1 & s2
print s1 | s2

# str是不变对象，而list是可变对象

# 对于可变对象，比如list，对list进行操作，list内部的内容是会变化的
a = ['c', 'b', 'a']
a.sort()
print a

# 对于不可变对象，比如str
a = 'abc'
a.replace('a','A')
print a

# 虽然字符串有个replace()方法，也确实变出了'Abc'，但变量a最后仍是'abc'
a = 'abc'
b = a.replace('a','A')
print a
print b