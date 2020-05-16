# !/usr/bin/env python3
# coding=utf-8

'''
什么是类？
类一个用于模拟生活现实场景的抽象的方法
也是编程中用于面向对象编程的最有效的编程方式
根据类创建的对象称之为实例化
类的概念需要慢慢理解
'''

'''
使用 class 关键字 跟上 类名（首字母需大写）:
类的内容 由许多函数 和 属性（变量）构成
在类里面定义的函数 又被称为 方法 
类中有一个特殊的方法 名为 __init__() 用于构建实例时传递属性值
self 关键字 指 当前类的实例对象 让构建的实例 可以访问当前类的 属性和方法
类的方法的第一个形参必须是self 但在调用方法的时候 不需要传递self 内部将默认关联self

class Dog():
    __init__(self, name, age):

'''

# 例1
class Dog():
    high = 10  # 类变量
    # 创建时会执行
    # 将 创建时 传入的 name 和 age 赋值给 创建的实例的name和age相关联
    def __init__(self, name, age):
        # name age 都是实例属性（实例变量）
        self.name = name
        self.age = age
    
    # 对狗狗的描述
    def desc(self):
        print('狗狗的名字叫' + self.name + '，今年已经' + str(self.age) + '周岁了')

    # 让狗狗坐下
    def sit(self):
        print(self.name.title() + '坐下了')

# 创建了一直名为旺财，年龄1岁的狗狗
dog_1 = Dog('旺财', 1)
dog_1.desc()
dog_1.sit()

# 你可以使用Dog类 创建多个实例对象
dog_2 = Dog('汪汪', 2)
dog_2.desc()

print(Dog.high)