#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 使用Python Imaging Library将图片生成缩略图
import Image
im = Image.open('test.png')
print im.format, im.size, im.mode
im.thumbnail((200, 100))
im.save('thumb.jpg', 'JPEG')

# 默认情况下，Python解释器会搜索当前目录、所有已安装的内置模块和第三方模块
# 搜索路径存放在sys模块的path变量中
print sys.path

# 如果我们要添加自己的搜索目录，一是直接修改sys.path，这种方法是在运行时修改，运行结束后失效
sys.path.append('Users/Colin/my_py_scripts')

# 第二种方法是设置环境变量PYTHONPATH，该环境变量的内容会被自动添加到模块搜索路径中
# 只需要添加你自己的搜索路径，Python自己本身的搜索路径不受影响