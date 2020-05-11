# !/usr/bin/env python3
# coding=utf-8

'''
读取文件（相对路径）
读取当前路径文件
'''
# with open('text1.txt') as file_object:
#     result = file_object.read()
#     print(result)

'''
读取当前路径中文件夹中的文件 （相对路径）
'''
# with open('textfiles/text1.txt') as file_object:
#     result = file_object.read()
#     print(result)


'''
以绝对路径读取文件
'''
# windows操作系统下的路径类似："C:\user\花木兰\xxx\xxx\xxx.txt"
# 以下路径时Macos（苹果系统）的文件的绝对路径

with open('/Users/longtao/Desktop/text1.txt') as file_object:
    result = file_object.read()
    print(result)