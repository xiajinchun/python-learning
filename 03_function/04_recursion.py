#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 递归函数
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)
print fact(1)
print fact(5)

# 尾递归，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式
# 尾递归调用时，如果做了优化，栈不会增长，因此，无论多少次调用也不会导致栈溢出。
def fact(n):
    return fact_iter(1, 1, n)

def fact_iter(product, count, max):
    if count > max:
        return product
    return fact_iter(product * count, count + 1, max)
