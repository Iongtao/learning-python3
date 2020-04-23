# !/usr/bin/env python3
# coding=utf-8

# 函数
"""
定义一个函数
以def关键词开头 后接函数名称和圆括号() 函数内容以冒号起始，并且缩进
def 函数名(参数列表):
    函数体
"""
# def getName(name):
#     print(name)
# getName('乐进')
'''
getName是函数名
name是函数接收的参数
该函数内容是打印了接收的参数

形参和实参的概念
形参：以一种形式存在的信息 用于函数内部使用的参数
实参：实际传递给函数的信息
如上面的getName(name)中的 name 即是形参
getName('乐进')中的 '乐进' 即是实参
'''


# # 多个形参的函数 and 默认值
# def getRealName(stage_name='乐进', real_name='曹尤进'):
#     print(stage_name+'的真实名称叫：' + real_name)
# # 如果形参有默认值 不传递实参的时候 会以默认值显示
# getRealName()
# # 顺序传参 实参需按照形参的顺序传递
# getRealName('乐进', '曹尤进')
# # 形参名-值 传递参数 不在乎形参顺序
# getRealName(real_name='高云霞', stage_name='花木兰')


'''
返回值
函数可以返回一个或一组值
使用 return 关键字 
返回值将作用于函数调用处
'''
# def getYourName():
#     your_name = '花木兰'
#     return your_name

# name = getYourName()
# print(name) # 打印 花木兰


'''
函数返回 字典等复杂类型
'''
# def getYourNameInfo(stage_name, real_name):
#     name_info = {"stage_name": stage_name, "real_name": real_name}
#     return name_info

# info = getYourNameInfo('lejin', 'caoyoujin')
# print(info)


# report = {
#     'lejin': 'i like it',
#     'humulan': 'i hate it'
# }
'''处理字典 返回列表'''
# def dealList(target):
#     new_list = []
#     for item in target.items():
#         new_list.append(item)
    
#     return new_list
'''用于打印的方法'''
# def printAll(my_list):
#     for item in my_list:
#         print(item)

# 函数的返回值作为实参
# printAll(dealList(report))

'''
使用函数修改 调查报告
'''
# report = {}
# actived = True

# def checkInput():
#     result = True
#     while result:
#         again = input('\n是否还有其他人需要反馈的吗？\n请输入yes/no：')
#         # 当输入的值 不是 yes no 则一直重复问题
#         if again not in ['yes', 'no']:
#             print('请输入 yes/no：')
#         # 如果是 就跳出循环
#         else:
#             result = False
#             # 把用户输入的值 返回
#             return again

# while actived:
#     name = input('请输入你的姓名：')
#     message = input('请输入你对我们平台的意见：')
#     report[name] = message

#     # 检查用户输入是否正确
#     again = checkInput()
#     # 跳出result循环后 去校验输入的结果 控制是否继续调查
#     if again == 'no':
#         actived = False

# # 打印报告
# print('\n调差报告如下：')
# for name, message in report.items():
#     print(name + '：' + message)


'''
传递任意数量的实参
使用 * 跟着形参names 代表 把实参统一包裹到了names中
*names 相当于创建了一个名为names的元组
'''
# def add_name(*names):
#     print(names)
#     print(names[0]) # 像是以元组的形式存在

# add_name('lejin', 'lvmeng', 'jiaxu')

'''
结合位置实参和任意数量的实参
'''
# def plan(date, *activtiy):
#     print(str(date) + '号，你有以下活动：')
#     for item in activtiy:
#         print(item)

# plan(14, '打篮球','唱歌','聚餐')

'''
任意数量的关键字实参
**形参名 创建一个字典 把剩余的实参统一包裹到了names中
**others 创建了一个others的字典
'''
def your_info(first_name, last_name, **others):
    info = {}
    info['first_name'] = first_name
    info['last_name'] = last_name
    # 这里是做了遍历others字典的操作
    for key, value in others.items():
        info[key] = value
    return info

print(your_info('cao', 'youjin', age=18, height=175, weight=128))