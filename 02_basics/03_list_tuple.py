#!/usr/bin/env python
# -*- coding: utf-8 -*-

# list是一种有序的集合，可以随时添加和删除其中的元素
classmates_list = ['Michael','Tracy','Bob']

print len(classmates_list)

# 访问list中的第一个元素
print classmates_list[0]

# 还可以用-1做索引，直接获取最后一个元素
print classmates_list[-1]

# list是一个可变的有序表，所以，可以往list中追加元素到末尾
classmates_list.append('Adam')

# 也可以把元素插入到指定的位置，比如索引号为1的位置
classmates_list.insert(1,'Jack')

# 要删除list末尾的元素，用pop()方法
classmates_list.pop()
classmates_list.pop(1)

# 给list中的元素排序
print classmates_list.sort()

# list里面的元素的数据类型也可以不同
L = ['Apple', 123, True]
s = ['python', 'java', ['asp', 'php'], 'scheme']

# tuple（元祖） tuple和list非常类似，但是tuple一旦初始化就不能修改
classmates_tuple = ('Michael','Bob','Tracy')

# classmates这个tuple不能变了，它也没有append()，insert()这样的方法
print classmates_tuple[0]

# 只有1个元素的tuple定义时必须加一个逗号
t = (1,)