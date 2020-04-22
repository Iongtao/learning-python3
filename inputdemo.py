# !/usr/bin/env python3
# coding=utf-8

qanda = [
    {
        "q": "为什么会喜欢你",
        "a": "因为你迷人可爱。因为你那不拒绝的性格，让我很很害怕你受到不好的人的侵犯，我想保护你"
    },
    {
        "q": "我什么时候开始喜欢的你",
        "a": "在去大明山之前一天晚上，我问你明天去不去，你回答的起得来就去。那天我很希望你去的"
    },
    {
        "q": "我为什么不放弃你？",
        "a": "因为你那天晚上 给我的一个拥抱 真的一直在温暖着我"
    }
]


message = '请输入你想问的问题的序号，例如：1\n'

indexs = []
for i in range(0, len(qanda)):
    indexs.append(i + 1)
    message += str(i + 1) + '：' + qanda[i]['q'] + '\n'
print(message)

message = input(message)
if message in indexs:
    print(qanda[message - 1]['a'])
else:
    print('请输入以下序号噢' + str(indexs))
