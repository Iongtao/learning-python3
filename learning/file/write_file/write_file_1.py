# !/usr/bin/env python3
# coding=utf-8


'''
写入文件
open方法接受两个实参 第一个为文件名 第二个为操作
操作行为有 "r"读取模式 "w"写入模式 "a"附加模式 "r+"读取和写入模式
如果写入的文件不存在 则会创建目标的空文件 需要注意的是 已存在的文件会被删除重建
python只能将字符串写入文件 如果遇到了整数类型 则需要str()转为字符串
'''
with open('write_file.txt', 'w') as write_file:
    write_file.write('今夜月色真美')