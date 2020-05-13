# !/usr/bin/env python3
# coding=utf-8

'''
如何遇到错误 不做任何处理？
在try或者except或者else中 使用pass关键字 来略过相关处理
'''

try:
    print(1/0)
except:
    pass
else:
    print('else')
