#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python提供了__future__模块，把下一个新版本的特性导入到当前版本，于是我们就可以在当前版本中测试一些新版本的特性

# 可以通过unicode_literals来使用Python 3.x中字符串的新的语法
from __future__ import unicode_literals

# Python 2.7的代码中直接使用Python 3.x的除法，可以通过__future__模块的division实现
from __future__ import division

print '\'xxx\' is unicode?', isinstance('xxx', unicode)
print 'u\'xxx\' is unicode?', isinstance(u'xxx', unicode)
print '\'xxx\' is str?', isinstance('xxx', str)
print 'b\'xxx\' is str?', isinstance(b'xxx', str)

print '10 / 3 =', 10 / 3
print '10.0 / 3 =', 10.0 / 3
print '10 // 3 =', 10 // 3