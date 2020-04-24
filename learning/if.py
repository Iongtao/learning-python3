# !/usr/bin/env python3
# coding=utf-8

# == 比较运算符
# print('a' == 'b') # False

# a = 'Cars'
# print(a == 'cars') # 条件表达式 区分大小写
# if(a.lower() == 'cars'):
#   print(a)

# 不等于 !=
# print('a' != 'b') # True

# 比较数字
# >、>=、<、<= 比较运算符
# print(20 > 20) # False
# print(20 >= 20)  # True
# print(20 < 20)  # False
# print(20 <= 20)  # True

# 多个条件判断
# 使用 or 或 and   or: 或 运算，and: 且 运算
# 一般有这几种情况：
# 条件a or 条件b 或有多个or运算 只要有一个满足 则为返回True
# 条件a or 条件b 只要一个不满足 则为返回False
# print((2 > 3) or ( 2 < 3)) # False or True => True
# print((2 > 3) and (2 < 3)) # False and True => False
# 关于 and 运算的问题
# 当使用一个有意义（为隐式转为False）的值 去 and 另一个 有意义的值时 会返回最后一个有意义的值
# 如果 多个 and 关联 其中有False的值则会 返回这个False的值
# 默认表示False的关键字或值有 0, 0.0, '', "", False, None, (), [], {}
# print(2 and 3) # 3
# print(2 and 2 and 4 and 5) # 5
# print(2 and False and 4 and 5) # False
# 关于 or 运算的问题
# 当使用一个或多个 or 运算 知道返回隐式转为True的那个值
# 如果每一项的值 都是False 则 返回最后一个为False的值
# print(2 or 3 or 4 or 5) # 2
# print(0 or False or 4 or 5) # 4
# print('' or 0 or {}) # {}

# 检测特定值是否存在列表中 使用 in 关键字
# names = ['lejin', 'jiaxu', 'lvmeng']
# print('lejin' in names) # True
# print('hml' in names) # False

# 检测特定知不存在列表中 使用 not in 关键字
# names = ['lejin', 'jiaxu', 'lvmeng']
# print('hml' not in names) # True

# 布尔表达式
# isActived = False
# isLogin = True


# if语句
# if conditional_test:
#     do_something
# 每一个if语句的核心是 一个值为True或Falst条件表达式 这样的表达式 称为条件测试
# conditional_test 即是条件测试（一个布尔表达式）
# do_something 为满足条件后 执行的操作
# True和False 为Boolean类型（布尔类型）

# if..else..
# if conditional_test:
# do_something
# else:
# do_something
# 相对if语句 多了一个未满足条件时所执行的语句
# if True:
#   print('True')
# else:
#   print('False')

# if..elif..else 多个条件判断
# if False:
#   print('if')
# elif True:
#   print('elif')
# else:
#   print('else')

# 在列表中 使用条件判断
# names = ['lejin', 'jiaxu', 'lvmeng']
# for name in names:
#   if(name == 'lejin'):
#     # 针对值为 lejin 的元素 可以做特殊的处理
#     print(name + 'ta 不在')
#   else:
#     print(name + 'ta 在的')

# 在遍历 列表前进行列表的非空判断 以避免 额外的错误
# names = []
# if len(names) > 0:
#   for name in names:
#     print(name)
# else:
#   print("names'length is " + str(len(names)))

# 使用多个列表
# good_mans = ['lejin']
# names = ['lejin', 'jiaxu', 'lvmeng']
# for name in names:
#   if name in good_mans:
#     print('这里有个好男人是：' + name)
# print('已经没有其他好男人了')
