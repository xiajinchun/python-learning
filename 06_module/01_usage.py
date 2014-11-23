#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 第1行注释可以让这个hello.py文件直接在Unix/Linux/Mac上运行
# 第2行注释表示.py文件本身使用标准UTF-8编码

# 该字符串表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释
' a test module '

# __author__变量为作者名
__author__ = 'Colin Xia'

# 导入sys模块
import sys
# 导入sys模块后，我们就有了变量sys指向该模块，利用sys这个变量，就可以访问sys模块的所有功能

def test():
    # sys模块有一个argv变量，用list存储了命令行的所有参数。argv至少有一个元素为该.py的文件名称
    args = sys.argv
    if len(args) == 1:
        print 'Hello, world!'
    elif len(args) == 2:
        print 'Hello, %s!' % args[1]
    else:
        print 'Too many arguments!'

if __name__ == '__main__':
    test()
# 在命令行运行hello模块文件时，Python解释器把一个特殊变量__name__置为__main__
# 如果在其他地方导入该hello模块时，if判断将失败
# 这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试

# 导入模块时，还可以使用别名，这样，可以在运行时根据当前环境选择最合适的模块

# Python标准库一般会提供StringIO和cStringIO两个库，这两个库的接口和功能是一样的
# 但是cStringIO是C写的，速度更快，所以，你会经常看到这样的写法：
try:
    # import ... as ...指定了别名StringIO，因此，后续代码引用StringIO即可正常工作
    import cStringIO as StringIO
except ImportError: # 导入失败会捕获到ImportError
    import StringIO

# 作用域 —— 外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义为public

# 在一个模块中，我们可能会定义很多函数和变量，但有的函数和变量我们希望给别人使用，有的函数和变量我们希望仅仅在模块内部使用
# 在Python中，是通过_前缀来实现的
# 正常的函数和变量名是公开的（public），可以被直接引用
# 类似__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途
# 类似_xxx和__xxx这样的函数或变量就是非公开的（private），不该被直接引用
def _private_1(name):
    return 'Hello, %s' % name

def _private_2(name):
    return 'Hi, %s' % name

def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)
# 在模块里公开greeting()函数，而把内部逻辑用private函数隐藏起来了
# 这样，调用greeting()函数不用关心内部的private函数细节，这也是一种非常有用的代码封装和抽象的方法