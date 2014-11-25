#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 需要引入Python自带的unittest模块
import unittest

from mydict import Dict

# 单元测试时，我们需要编写一个测试类，从unittest.TestCase继承
class TestDict(unittest.TestCase):
    # 以test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法，测试的时候不会被执行
    def test_init(self):
        d = Dict(a = 1, b = 'test')
        self.assertEquals(d.a, 1)
        self.assertEquals(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEquals(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEquals(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        # 期待抛出指定类型的Error，比如通过d['empty']访问不存在的key时，断言会抛出KeyError
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty
        
# 最简单的运行方式是在mydict_test.py的最后加上两行代码
if __name__ == '__main__':
    unittest.main()

# setUp与tearDown
# 这两个方法会分别在每调用一个测试方法的前后分别被执行
class TestDict(unittest.TestCase):

    def setUp(self):
        print 'setUp...'

    def tearDown(self):
        print 'tearDown...'