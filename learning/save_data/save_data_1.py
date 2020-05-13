# !/usr/bin/env python3
# coding=utf-8

'''
程序一般会在初始化的时候 或者 需要记录用户数据的时候 从某种存储内容中读取需要的数据

python中 从文件中去存储数据和读取数据 需要用到 json模块
存储数据对应 json.dump() 接收两个参数 1要存储数据 2用于存储的文件对象
读取数据对应 json.load() 接收一个参数 为读取的文件对象
'''

# 引入json模块
import json

# 接收存储数据的文件
filename = 'name.json'

# 需要存储的数据
names = ['caoyoujin', 'gaoyunxia']

# 执行存储操作
with open(filename, 'w') as file_object:
    json.dump(names, file_object)
