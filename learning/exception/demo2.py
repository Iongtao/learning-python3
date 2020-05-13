# !/usr/bin/env python3
# coding=utf-8


'''
else 代码块

try:
    ...
except:
    ...
else:
    ...

'''


print('请输入两个整数，将把第一个数做为被除数，第二个数作为除数，计算它们的商值')
print('输入 "q" 则退出程序')

while True:
    num_one = input('请输入被除数：')
    if num_one == 'q':
        break
    num_two = input('请输入除数：')
    if num_two == 'q':
        break
    try:
        # try 代码块中
        # 可能会出现的异常代码
        result = int(num_one)/int(num_two)
    except ZeroDivisionError as err:
        # 出现异常时的错误处理
        print('错误',err)
        print('请不要用0作为除数')
    else:
        # 没有异常
        print(result)

print('程序已停止')
