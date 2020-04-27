# !/usr/bin/env python3
# coding=utf-8

# 类的继承

'''
一个类继承另一个类时，自动获得另一个类的所有属性和方法
A类 extends B类
把 A类 称为子类，把 B类 称为父类
A类 将包含 B类 的所有属性和方法 且 A类 还可以定义自己的属性和方法
'''


class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self):
        print('hello hml')


'''
子类如何继承父类
class B(): ... 
class A(B): ...
申明类的时候在 类名后面的括号中 传入父类的名称
其次在子类的 __init__ 中调用父类的__init__方法 
如: super().__init__(传入父类中的属性) 
就能在创建子类对象的时候 初始化 父类的属性和方法
即可 在子类对象中调用父类的属性和方法
'''
class SaleMan(Person):
    def __init__(self, name, age):
        super().__init__(name, age)

    def speciality(self):
        print('销售能力特别强')


li4 = Person('李四', 18)
print(li4.name)
li4.say()


zhang3 = SaleMan('张三', 20)
zhang3.say()
zhang3.speciality()
print(zhang3.name)
