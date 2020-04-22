# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# 列表 list

# 向列表为末尾添加一条元素 append()
# names = ['lejin', 'jiaxu', 'lvmeng']
# names.append('hml')
# print(names)

# insert(index, value) 向指定位置添加元素
# names = ['lejin', 'jiaxu', 'lvmeng']
# names.insert(2, 'hml')  # 想索引为2的位置插入元素
# print(names)

# del关键字 删除列表指定位置的元素
# names = ['lejin', 'jiaxu', 'lvmeng']
# del names[1]
# print(names)

# pop(index) 删除列表一条元素 返回删除的元素
# 参数index: 列表索引
# 不提供则默认列表最后一条元素
# names = ['lejin', 'jiaxu', 'lvmeng']
# names.pop()  # 默认最后一条
# names.pop(2)  # 删除 第三条元素
# print(names)

# 根据值删除元素
# names = ['lejin', 'jiaxu', 'lvmeng']
# remove(value)
# names.remove('lejin')
# print(names)

# sort() 列表排序 默认 首字母a-z 数字从小到大 会改变原列表
# sorted() 同上 但不会改变原列表 返回新列表
# names = ['lejin', 'jiaxu', 'lvmeng']
# nums = [34, 52, 12, 46, 2]
# nums.sort(reverse=True)  # reverse=True 倒序
# print(sorted(nums, reverse=True))  # 接收需要排序的列表作为参数 返回排序后的列表
# print(nums)

# reverse() 列表翻转顺序 改变原列表
# names = ['lejin', 'jiaxu', 'lvmeng']
# names.reverse()
# print(names)

# len() 获取列表长度
names = ['lejin', 'jiaxu', 'lvmeng']
print(len(names))
