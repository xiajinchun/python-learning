#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 第一种方法简单直接粗暴有效，就是用print把可能有问题的变量打印出来看看
def foo(s):
    n = int(s)
    print '>>> n = %d' % n
    return 10 / n

def main():
    foo('0')

#main()

# 断言 ———— 凡是用print来辅助查看的地方，都可以用断言（assert）来替代
def foo(s):
    n = int(s)
    # assert的意思是，表达式n != 0应该是True，否则，后面的代码就会出错
    assert n != 0, 'n is zero'
    return 10 / n

def main():
    foo('0')

#main()

# logging ———— 把print替换为logging是第3种方式，和assert比，logging不会抛出错误，而且可以输出到文件
import logging
# logging允许你指定记录信息的级别，有debug，info，warning，error等几个级别
logging.basicConfig(level = logging.INFO)

s = '0'
n = int(s)
logging.info('n = %d' % n)
print 10 / n

# pdb ———— 启动Python的调试器pdb，让程序以单步方式运行，可以随时查看运行状态
s = '0'
n = int(s)
print 10 / n

# pdb.set_trace()这个方法也是用pdb，但是不需要单步执行
# 我们只需要import pdb，然后，在可能出错的地方放一个pdb.set_trace()，就可以设置一个断点
import pdb

s = '0'
n = int(s)
pdb.set_trace() # 运行到这里会自动暂停
print 10 / n
# 程序会自动在pdb.set_trace()暂停并进入pdb调试环境