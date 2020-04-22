# !/usr/bin/env python3
# coding=utf-8

# for循环(for...in...)

# names = ['lejin', 'jiaxu', 'lvmeng', 'humulan']
# for name in names:
#     print(name)

# range(start, stop, ?step)
# 创建一个整数列表 start: 起始索引 stop：结束索引（不包括）step：步长 默认1

# for i in range(0, 6, 2):
#     print(i)

# list()将元组类型转为列表
# list(range(1, 5)) 使用 list将range()转化为整数列表

# 整数列表 sum() 求和  min() 求最小值 max 求最大值
# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# print(sum(list))
# print(max(list))
# print(min(list))

# 列表解析[表达式 for循环]
# list = [value**2 for value in range(0, 10)]
# print(list)

# list = list(range(1, 20, 2))  # 奇数列表
# print(list)


# 什么是切片
# 将一个列表 分为多个列表 分出来的每个列表即为切片
# 数组名[start index:end index] end不是包含关系
# names = ['lejin', 'jiaxu', 'lvmeng', 'huaml']
# print(names[1:4])
# print(names[:4])  # 没有起始索引时 默认从0开始
# print(names[2:])  # 没有结束索引时 默认最后一个元素结束
# print(names[-2:])  # 打印最后两个元素

# 遍历切片
# for name in names[:3]:
#     print(name)

# names = ['lejin', 'jiaxu', 'lvmeng', 'huaml']
# name2 = names  # 直接赋值新变量 会导致处理name2会影响names列表 概念：引用类型或指针引用
# name2 = names[:]  # 使用切片相当于创建了新的列表 不会影响names列表
# name2.append('luban') # 添加元素操作 都会影响names列表
# del name2[0] # 删除元素操作 都会影响names列表
# print(names)
# print(name2)
