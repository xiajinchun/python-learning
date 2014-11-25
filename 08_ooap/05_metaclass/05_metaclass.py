#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的

# type()函数可以查看一个类型或变量的类型
# Python解释器载入hello模块时，就会依次执行该模块的所有语句
from hello import Hello
h = Hello()
h.hello()
print type(Hello) # Hello是一个class，它的类型就是type
print type(h) # h是一个实例，它的类型就是class Hello

# class的定义是运行时动态创建的，而创建class的方法就是使用type()函数
# type()函数既可以返回一个对象的类型，又可以创建出新的类型
# 通过type()函数创建出Hello类，而无需通过class Hello(object)...的定义
def fn(self, name = 'world'):
    print 'Hello, %s.' % name

# type()函数依次传入3个参数：
# 1.class的名称；
# 2.继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法
# 3.class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上
Hello = type('Hello', (object,), dict(hello = fn)) # 创建Hello class
h = Hello()
h.hello()
print type(Hello)
print type(h)

# metaclass ———— 除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass
# 先定义metaclass，就可以创建类，最后创建实例

# metaclass可以给我们自定义的MyList增加一个add方法
# metaclass是创建类，所以必须从`type`类型派生
class ListMetaclass(type):
    # __new__()方法接收到的参数依次是：
    # 当前准备创建的类的对象；
    # 类的名字；
    # 类继承的父类集合；
    # 类的方法集合
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

class MyList(list):
    __metaclass__ = ListMetaclass # 指示使用ListMetaclass来定制类
# __metaclass__ = ListMetaclass语句指示Python解释器在创建MyList时，要通过ListMetaclass.__new__()来创建
        
# 测试一下MyList是否可以调用add()方法，普通的list没有add()方法
L = MyList()
L.add(1)
print L

# 利用metaclass完成ORM框架

# 定义Field类，它负责保存数据库表的字段名和字段类型
class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type
    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)

# 在Field的基础上，进一步定义各种类型的Field，比如StringField，IntegerField
class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')

class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')

# 编写ModelMetaclass
class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        mappings = dict()
        for k, v in attrs.iteritems():
            if isinstance(v, Field):
                print 'Found mapping: %s==>%s' % (k, v)
                mappings[k] = v
        for k in mappings.iterkeys():
            attrs.pop(k)
        attrs['__table__'] = name # 假设表名和类名一致
        attrs['__mappings__'] = mappings # 保存属性和列的映射关系
        return type.__new__(cls, name, bases, attrs)

# 基类Model
class Model(dict):
    __metaclass__ = ModelMetaclass
    
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.iteritems():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print 'SQL: %s' % sql
        print 'ARGS: %s' % str(args)

# 当用户定义一个class User(Model)时，Python解释器首先在当前类User的定义中查找__metaclass__
# 如果没有找到，就继续在父类Model中查找__metaclass__，找到了，就使用Model中定义的__metaclass__的ModelMetaclass来创建User类
# 也就是说，metaclass可以隐式地继承到子类，但子类自己却感觉不到
class User(Model):
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

u = User(id = 12345, name = 'Colin', email = 'test@orm.org')
u.password = 'mypwd'
u.save()
print u.name

# 类属性和实例属性

# 直接在class中定义的是类属性
class Student(object):
    name = 'Student'

# 实例属性必须通过实例来绑定
# 创建实例s：
s = Student()
# 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性：
print(s.name)
# 这和调用Student.name是一样的：
print(Student.name)
# 给实例绑定name属性：
s.name = 'Colin'
# 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性：
print(s.name)
# 但是类属性并未消失，用Student.name仍然可以访问：
print(Student.name)
# 如果删除实例的name属性：
del s.name
# 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了：
print(s.name)