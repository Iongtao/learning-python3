# !/usr/bin/env python3
# coding=utf-8

# while循环

# 定义一个num
# num = 0
# 当表达式为True的时候就会一直循环下去
# 以下是个死循环
# while True:
#     print(num)
#     num += 1
#     if num >= 20:
#       break # break 可以跳出循环

# 有条件判断的循环
# num = 0
# 当 num < 10 条件不满足 则跳出while循环
# while num < 10:
#     print(num)
#     num += 1


# for循环 和 while循环 区别只是在于形式上 而且 while循环的条件可以为True， for循环必须会有一个有长度的列表


# 使用continue关键字 直接进行下一个操作
# num = 0
# while num < 10:
#     num += 1
#     if num % 2 == 0:  # 偶数 不会被打印
#         continue
#     print(num)

# 使用while 在列表之间移动元素
# good_names = ['lejin', 'jiaxu', 'lvmeng']
# bad_names = []
# while good_names:
#    name = good_names.pop()
#    bad_names.append(name)

# print('\n以下是不好的名单列表：')
# for name in bad_names:
#     print(name)

# 删除数组中 特定值
# 如果数组中的特定值有多个 则用while循环来删除
# tags = ['name', 'age', 'computer', 'foods', 'age', 'age', 'foods']
# while 'age' in tags:
#     tags.remove('age')
# print('结果：' + str(tags))