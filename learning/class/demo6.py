# !/usr/bin/env python3
# coding=utf-8


# 类的模块化
'''
与函数的模块化基本一致
'''

# 这里引用class/demo5.py 中的类


# 类名引入 and 别名
from demo5 import HuntingDog as HuntingDog2

a = HuntingDog2('杜高', 1)

print(a.name)
a.sit()
a.hunting.desciption()


# 文件引入 调用
import demo5
b = demo5.Dog('贾诩',1)
b.sit()