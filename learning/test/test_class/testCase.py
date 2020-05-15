# !/usr/bin/env python3
# coding=utf-8

import unittest
from demo import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    def test_store_single_response(self):
        question = '花木兰好看吗'
        my_survery = AnonymousSurvey(question)
        my_survery.store_responses('好看呀')

        self.assertIn('好看呀', my_survery.responses)


    def test_store_three_response(self):
        question = '花木兰好看吗'
        my_survery = AnonymousSurvey(question)
        answers = ['好看', '好好看', '好好好看']
        for answer in answers:
            my_survery.store_responses(answer)

        for answer in answers:
            self.assertIn(answer, my_survery.responses)


unittest.main()
