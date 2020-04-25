# !/usr/bin/env python3
# coding=utf-8


# 如何去修改属性值 和 调用方法

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.merits = []

    def print_info(self):
        print(self.name + '今年已经' + str(self.age) + '周岁了')

    def merits_description(self):
        if self.merits:
            str_merits = ''
            for i in range(len(self.merits)):
                if(i == len(self.merits) - 1):
                    str_merits += self.merits[i]
                else:
                    str_merits += self.merits[i] + '、'
            print(self.name + str_merits)
        else:
            print(self.name + '没有啥优点')
    
    # 通过调用方法修改属性值
    def update_merits(self, *merits):
        # 这里定义了一个新的数组 用于接收传入的值
        new_list = []
        for merit in merits:
            new_list.append(merit)
        self.merits = new_list

    def add_merits(self, merits):
        # 往现有的属性中追加新的值
        self.merits.append(merits)


lejin = Person('乐进', 18)
lejin.print_info()
lejin.merits_description()
# 修改属性值 实例.属性名 = 属性值
lejin.merits = ['耍刀弄枪', '长的帅', '又温柔']
lejin.merits_description()

hml = Person('花木兰', 18)
# 通过 方法调用修改属性
hml.update_merits('可爱', '迷人', '大方', '智慧')
hml.merits_description()
hml.add_merits('漂亮')
hml.merits_description()