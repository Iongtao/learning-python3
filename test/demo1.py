# !/usr/bin/env python3
# coding=utf-8


class AnonymousSurvey():
    '''收集匿名调查问卷的答案'''

    def __init__(self, question):
        self.question = question
        self.responses = []

    def show_question(self):
        '''显示调查问卷'''
        print(self.question)

    def store_responses(self, new_response):
        '''存储单份调查答卷'''
        self.responses.append(new_response)

    def show_results(self):
        '''显示收集到的所有答案'''
        for response in self.responses:
            print('-' + response)




question = '你觉得花木兰好看吗'
my_survey = AnonymousSurvey(question)

my_survey.show_question()
print('输入 q 退出问卷')

while True:
    answer = input('你是怎么认为的？请输入你的回答：')
    if answer == 'q':
        break
    my_survey.store_responses(answer)

print('本次以《' + question + '》为题的调查结果如下：')
my_survey.show_results()
