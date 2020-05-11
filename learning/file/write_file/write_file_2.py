# !/usr/bin/env python3
# coding=utf-8


'''
附加模式
向已有的文件末尾 继续添加内容
'''
with open('write_file.txt', 'a') as write_file:
    write_file.write('我喜欢你\n')