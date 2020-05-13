# !/usr/bin/env python3
# coding=utf-8

'''
文件类的异常错误 FileNotFoundError
当读取一个不存在的文件 会抛出异常
'''


filename = 'hml.txt'
try:
    with open(filename) as file_object:
        content = file_object.read()
        print(content)
except FileNotFoundError as error:
    print('找不到名为' + filename + '的文件')
