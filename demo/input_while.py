# !/usr/bin/env python3
# coding=utf-8

# 使用while循环 让用户选择是否退出游戏
# tips = '请随意输入一段话，如果不想继续了，请输入exit\n'
# tips += '请输入你的话：'

# message = ''
# while message != 'exit':
#     message = input(tips)

# 使用标记
# actived = True
# while actived:
#     message = input(tips)
#     if message == 'exit':
#         actived = False
#     else:
#         print(message)

# 使用break关键字跳出循环
# beark 可以用于python中 任何循环语句中
# while True:
#     message = input(tips)
#     if message == 'exit':
#         break
#     else:
#         print(message)

report = {}
actived = True
while actived:
    name = input('请输入你的姓名：')
    message = input('请输入你对我们平台的意见：')
    report[name] = message

    # result 控制内部的while循环
    result = True
    while result:
        again = input('\n是否还有其他人需要反馈的吗？\n请输入yes/no：')
        # 当输入的值 不是 yes no 则一直重复问题
        if again not in ['yes', 'no']:
            print('请输入 yes/no：')
        # 如果是 就跳出循环
        else:
            result = False

    # 跳出result循环后 去校验输入的结果 控制是否继续调查
    if again == 'no':
        actived = False

# 打印报告
print('\n调差报告如下：')
for name, message in report.items():
    print(name + '：' + message)
