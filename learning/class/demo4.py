# !/usr/bin/env python3
# coding=utf-8

# 重写父类方法
'''
有时候 可能存在特殊的子类 它没有父类中的属性或某个行为（方法）
这时候 就应该在子类中去重写父类的方法 达到覆盖父类的方法
'''


class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.feature = '可爱'

    def run(self):
        print(self.name + '跑的很快')


wangcai = Dog('旺财', 1)
wangcai.run()


# 可能有的狗狗 跑不起来（假如）
class Keji(Dog):
    def __init__(self, name, age):
        super().__init__(name, age)

    # 此处 重写父类的 run方法
    def run(self):
        print('这只名为' + self.name + '的柯基, 跑不动的')


duantui = Keji('小短腿', 1)
duantui.run()
