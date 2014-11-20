#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 函数定义
# 在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:
def myabs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
# 参数检查，用isinstance函数来判断参数格式是否正确
    if x >= 0:
        return x
    else:
        return -x
# 如果没有return语句，函数执行完毕后也会返回结果，只是结果为None，return None可以简写为return
print myabs(-5)
print myabs('abs')

# 定义空函数， 可以用pass语句
def nop():
    pass

import math

# 返回多个值，游戏中经常需要从一个点移动到另一个点，给出坐标、位移和角度，就可以计算出新的新的坐标
def move(x,y,step,angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

xy = move(100,100,60,math.pi/6)
# Python的函数返回多值其实就是返回一个tuple（可以省略括号），多个变量可以同时接收一个tuple，按位置赋给对应的值
print xy