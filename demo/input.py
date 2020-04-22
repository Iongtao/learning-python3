# !/usr/bin/env python3
# coding=utf-8

qanda = [
    {
        "q": "1+1等于几？",
        "a": "2"
    },
    {
        "q": "你是几号入职的？例如：9月24号",
        "a": "11月2号"
    },
    {
        "q": "我和你认识多久了",
        "a": "不知道"
    }
]


# 声明一个变量作为 提示信息
question = '请输入你想回答的问题序号，例如：1\n'

# indexs用来去得到序号列表
indexs = []

# 把问题遍历出来
# += 运算： a += b 与 a = a + b 运算形式是一致的
for i in range(0, len(qanda)):
    # 向indexs列表添加索引值
    indexs.append(i + 1)
    # 进行字符串拼接操作 遍历出问题列表
    question += str(i + 1) + '：' + qanda[i]['q'] + '\n'
# 额外的提示输入
question += '请输入序号：'

# 开始提出问题
# print(question)

# message 接收输入的内容 message的类型为字符串
# input返回用户输入的类型默认为字符串
message = input(question)
# 如果想要接收的类型是整数型 需要使用int()去强转
message = int(message)
# 得到输入内容 后 进行校验输入内容的正确性
if message in indexs:
    if message == 1:
        answer = input('请输入你的回答: ')
        if answer != int(qanda[message - 1]['a']):
            print('你回答错误了，正确答案是：' + qanda[message - 1]['a'])
        else:
            print('恭喜你，回答正确')

    if message == 2:
        answer = input('请输入你的回答：')
        if answer != qanda[message - 1]['a']:
            print('你可能记错你的入职时间噢')
        else:
            print('哎哟，不错哦')

    if message == 3:
        answer = input('请输入你的回答：')
        print(answer)

else:
    print('\n你输入的序号' + '[' + str(message) + ']' + '不在以下列表中哦：' + str(indexs))
