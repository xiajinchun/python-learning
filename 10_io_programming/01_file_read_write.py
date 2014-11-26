#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python内置了读写文件的函数，用法和C是兼容的

# 读文件
# 以读文件的模式打开一个文件对象，使用Python内置的open()函数，传入文件名和标示符
f = open('test.txt', 'r')
# 标示符'r'表示读，这样，我们就成功地打开了一个文件
# 如果文件不存在，open()函数就会抛出一个IOError的错误，并且给出错误码和详细的信息告诉你文件不存在
#f = open('notfound.txt', 'r')

# 如果文件打开成功，接下来，调用read()方法可以一次读取文件的全部内容，Python把内容读到内存，用一个str对象表示
print f.read()
# 最后一步是调用close()方法关闭文件
f.close()

# 由于文件读写时都有可能产生IOError，一旦出错，后面的f.close()就不会调用
# 使用try ... finally来保证无论是否出错都能正确地关闭文件
try:
    f = open('test.txt', 'r')
    print f.read()
finally:
    if f:
        f.close()

# Python引入了with语句来自动帮我们调用close()方法
with open('test.txt', 'r') as f:
    print f.read()

# 用read(size)方法，每次最多读取size个字节的内容
# 调用readline()可以每次读取一行内容
# 调用readlines()一次读取所有内容并按行返回list
with open('test.txt', 'r') as f:
    for line in f.readlines():
        print(line.strip()) # 把末尾的'\n'删掉

# file-like Object
# 像open()函数返回的这种有个read()方法的对象，在Python中统称为file-like Object
# 除了file外，还可以是内存的字节流，网络流，自定义流等等。file-like Object不要求从特定类继承，只要写个read()方法就行

# 二进制文件
# 要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可
with open('test.png', 'rb') as f:
    print f.read()

# 字符编码
# 要读取非ASCII编码的文本文件，就必须以二进制模式打开，再解码。比如GBK编码的文件
with open('test.txt', 'rb') as f:
    print f.read().decode('utf-8')

# 写文件
# 写文件和读文件是一样的，唯一区别是调用open()函数时，传入标识符'w'或者'wb'表示写文本文件或写二进制文件
f = open('test.txt', 'w')
f.write('Hello, world again!')
f.close()

# 用with语句防止数据丢失
with open('test.txt', 'w') as f:
    f.write('Hello, world with!')

# 在Python中，文件读写是通过open()函数打开的文件对象完成的。使用with语句操作文件IO是个好习惯