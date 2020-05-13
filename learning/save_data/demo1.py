# !/usr/bin/env python3
# coding=utf-8


'''
模拟一个用户登录的场景
用户输入名字后 保存起来
等下次的时候 去读取用户的名字
'''
# 引入必要模块
import json

# 定义一个文件名
filename = 'username.json'

try:
    with open(filename) as file_object:
        name = json.load(file_object)
except FileNotFoundError as error:
    # 没有找到文件 是第一次执行程序
    # 开始 用户登录的操作
    name = input('请创建一个昵称')
    # 把输入的内容存储到指定文件中
    with open(filename, 'w') as file_object:
        json.dump(name, file_object)
else:
    print(name + '欢迎回来~')
