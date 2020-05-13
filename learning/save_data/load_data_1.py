# !/usr/bin/env python3
# coding=utf-8



'''
读取数据 json.load()
'''

# 引入json模块
import json

# 文件名
filename = 'name.json'

# 执行读取操作
with open(filename) as file_object:
    data = json.load(file_object)
    print(data)