# !/usr/bin/env python3
# coding=utf-8


'''
将类的实例作为属性
当一个类中的属性和方法越来越多 变的复杂 会不利于维护
将类中的特性或公共部分提取成一个新的类 会显得直观明了

下面 定义了一个Dog类 一个Hunting类 一个HuntingDog类
这里将Hunting类的实例 赋值给了 HuntingDog中的hunting属性的值 

'''


class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name + "坐下了")


class Hunting():
    def __init__(self, name):
        self.speed = 100
        self.name = name

    def desciption(self):
        print('猎狗' + self.name + '的速度可以达到' + str(self.speed) + '千米/小时')


class HuntingDog(Dog):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.hunting = Hunting(name)


if __name__ == '__main__':
    dugao = HuntingDog('杜高犬', 2)
    dugao.hunting.desciption()
    print('直接 python 当前这个文件时候 触发')
else:
    print('在别的文件中引用执行的时候 触发')
