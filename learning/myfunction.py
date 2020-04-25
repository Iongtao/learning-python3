# !/usr/bin/env python3
# coding=utf-8

if __name__ == '__main__':
    print('直接 python 当前这个文件时候 出发')
else: 
    print('在别的文件中引用执行的时候 触发')

def get_user_name(name):
    print('该用户的名称是：' + name)
