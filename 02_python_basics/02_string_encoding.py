#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 最早的Python只支持ASCII编码，普通的字符串'ABC'在Python内部都是ASCII编码的
# Python提供了ord()和chr()函数，可以把字母和对应的数字相互转换
print ord('A')
print chr(65)

# Python在后来添加了对Unicode的支持，以Unicode表示的字符串用u'...'表示
print u'ABC'

# 把u'xxx'转换为UTF-8编码的'xxx'用encode('utf-8')方法
print u'中文'.encode('utf-8')

# len()函数可以返回字符串的长度
print len(u'ABC')
print len(u'中文')

# 格式化
print 'Hi, %s, you have $%d.' % ('Michael', 1000000)
print '%.2f' % 3.1415926
print 'Age: %s. Gender: %s' % (25, True)

# %%转义成一个%
print 'growth rate: %d%%' % 7

# str.format()
print "{name}".format(name='name：夏锦春')