# !/usr/bin/env python3
# coding=utf-8


'''
逐行读取
直接对文件对象进行遍历
'''
# with open('text1.txt') as file_object:
#     # result = file_object
#     for line in file_object:
#         # print(line)
#         print(line.strip()) # 除去空格



'''
创建一个包含文件各行内容的列表
'''

with open('text1.txt') as file_object:
    lines = file_object.readlines()

# 然后在with代码块外的地方使用
for line in lines:
    # print(line)
    print(line.strip()) # 除去空格