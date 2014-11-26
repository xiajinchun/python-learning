#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python内置的os模块也可以直接调用操作系统提供的接口函
import os
print os.name
# uname()函数在Windows上不提供，也就是说，os模块的某些函数是跟操作系统相关的
print os.uname()

# 在操作系统中定义的环境变量，全部保存在os.environ这个dict中
print os.environ

# 要获取某个环境变量的值，可以调用os.getenv()函数
print os.getenv('PATH')

# 操作文件和目录
# 操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中

# 查看当前目录的绝对路径
print os.path.abspath('.')

# 在某个目录下创建一个新目录
# 首先把新目录的完整路径表示出来
# 把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数
print os.path.join('/Users/Colin', 'testdir')
# 然后创建一个目录
os.mkdir(os.path.join('/Users/Colin', 'testdir'))
# 删掉一个目录
os.rmdir(os.path.join('/Users/Colin', 'testdir'))

# 要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数
# 这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名
print os.path.split('/Users/Colin/testdir/file.txt')

# os.path.splitext()可以直接让你得到文件扩展名，很多时候非常方便
print os.path.splitext('/path/to/file.txt')

# 对文件重命名
#os.rename('test.txt', 'test.py')
# 删掉文件
#os.remove('test.py')

# 可以在shutil模块中找到很多实用函数，它们可以看做是os模块的补充
import shutil
# shutil模块提供了copyfile()的函数来复制文件

# 利用Python的特性来过滤文件，比如我们要列出当前目录下的所有目录
print [x for x in os.listdir('.') if os.path.isdir(x)]

# 要列出所有的.py文件，也只需一行代码
print [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']