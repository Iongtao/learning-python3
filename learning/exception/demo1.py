# !/usr/bin/env python3
# coding=utf-8

'''
异常
python使用 异常对象 来管理程序在运行过程中出现的错误
python项目在运行中出现错误 会中断项目运行
使用 异常处理 则可以使项目继续运行下去并且抛出相关错误
'''

# 当以任意一个数字去除以0 则会抛出一个 traceback（回溯）
# print(4/0)

try:
  print(4/0)
except ZeroDivisionError as e:
  print(e)









# ZeroDivisionError错误类型 是０为除数时候的异常
# 如果 错误类型 与 错误的原因不符合时 是无法捕获异常的 项目运行将会中断

# 例如 使用了一个 找不到模块的类型错误 ModuleNotFoundError

try:
    print(4/0)
except ModuleNotFoundError as e:
    # 依然会报错
    print(e)
