# !/usr/bin/env python3
# coding=utf-8

# 字典 用花括号 包裹的键值对形式存在
# me = {
#     "name": "lejin",
#     "age": 18,
#     "speed": "medium"
# }
# print(me)
# print(me['name'])  # 输出me中的name字段 lejin
# print(me['age'])  # 18
# 添加键值对
# me['favorite'] = 'gyx'
# print(me)
# 修改键值对
# if me['speed'] == 'slow':
#     x_increment = 1
# elif me['speed'] == 'medium':
#     x_increment = 2
# elif me['speed'] == 'fast':
#     x_increment = 3
# me['x_position'] = x_increment
# print(me)
# 删除键值对 del
# del me['speed']
# print(me)


# 遍历字典
# print(me.items()) 返回的数据是 列表包含元组这样的结构
# [('age', 18), ('speed', 'medium'), ('name', 'lejin')]
# for 定义两个变量key, value（变量名可自定义）接收列表每一项中的key, value
# for a, b in me.items():
#     print('\nkey:' + a)
#     print('value:' + str(b))


# 遍历字典的键 xxx.keys()
# print(me.keys())  # ['age', 'speed', 'name']
# for key in me.keys():
#     print(key)

# 遍历字典中的值 xxx.values()
# print(me.values())
# for value in me.values():
#     print(value)

# set() 列表去重
# books = ['python', 'java', 'javascript', 'java']
# for item in set(books):
#     print(item)


# 嵌套 字典列表
# one = {"name": 'one', "age": 18}
# two = {"name": "two", "age": 23}
# three = {"name": "three", "age": 22}
# mylist = [one, two, three]
# for item in mylist:
#     print(item)

# 如何自动生成多个人物
# 使用range()创建一个列表
# persons = []
# for i in range(0, 30):
#     persons.append({'name': 'pserson' + str(i), "age": i})
# # 去针对前5个人 添加额外的属性
# for person in persons[0:5]:
#     person['work'] = 'coder'
# print(persons[0:6])

# 列表作为字典中key的值
# 例1 购物车
# order = {
#     "name": '曹尤进',
#     "cars": ['苹果', '蔬菜', '鸡蛋']
# }
# print(order["name"] + "的购物车里有以下商品：")
# for item in order['cars']:
#     print(item)
# 例2 不同人喜欢的东西
# 嵌套循环
# favorites = {
#     '乐进': ['土豆', '肉', '肉'],
#     '贾诩': ['海鲜', '鸡肉'],
#     '吕蒙': ['shit', '💩', '便便']
# }
# for name, favorite in favorites.items():
#     print('\n'+name+'喜欢的东西：')
#     for value in favorite:
#       print(value)

# 嵌套字典（字典中存储字典信息）
person = {
  "name": "曹尤进",
  "age": 18,
  "stature": {
    "height": 175,
    "weight": 128
  }
}
print(person['stature']['height'])
