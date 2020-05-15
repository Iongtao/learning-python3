# !/usr/bin/env python3
# coding=utf-8


'''
通过setUp()修改 TestAnonymousSurvey用例
python3 会先执行测试用例中的setUp方法
所以可以在setUp中去创建好需要检测类的实例
'''
import unittest
from demo import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):

    def setUp(self):
        question = '花木兰好看吗'
        self.my_survery = AnonymousSurvey(question)
        self.answers = ['好看', '好好看', '好好好看']

    def test_store_single_response(self):
        self.my_survery.store_responses(self.answers[0])
        self.assertIn(self.answers[0], self.my_survery.responses)

    def test_store_three_response(self):
        for answer in self.answers:
            self.my_survery.store_responses(answer)

        for answer in self.answers:
            self.assertIn(answer, self.my_survery.responses)


unittest.main()
