# !/usr/bin/env python3
# coding=utf-8

qanda = [
    {
        "q": "为什么还不放下",
        "a": "考虑过很多回，想想还是喜欢好了"
    },
    {
        "q": "为什么行为很奇怪",
        "a": "理性的看待这个问题的时候，我也觉得很奇怪，我很抱歉"
    },
    {
        "q": "以后该怎么做",
        "a": "做的更好"
    }
]


message = '请输入你想问的问题的序号，例如：1\n'

indexs = []
for i in range(0, len(qanda)):
    indexs.append(i + 1)
    message += str(i + 1) + '：' + qanda[i]['q'] + '\n'
print(message)

message = int(input(message))
if message in indexs:
    print(qanda[message - 1]['a'])
else:
    print('请输入以下序号噢' + str(indexs))
