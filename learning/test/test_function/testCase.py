# !/usr/bin/env python3
# coding=utf-8

'''
单元测试和测试用例 测试项目是否能正常满足各个方面没有问题
单元测试 用于核实函数的某个方面没有问题
测试用例 是一组单元测试
'''

'''
编写测试用例
需要导入模块unittest 和 需要测试的函数
一个测试用例 就是 一个继承了unittest.TestCase的类 然后 该类中的方法 就是一个个单元测试
'''

import unittest
from demo import get_formatted_name

'''
NamesTestCase类继承unittest.TestCase类 
python才知道这个类是用来编写测试用例的
'''

class NamesTestCase(unittest.TestCase):

    '''定义了一个测试姓和名的方法 只有以 test_ 打头的方法才会自动运行'''
    def test_first_last_name(self):
        '''这里将执行需要去测试的函数 将得到 值为：曹尤进 的结果'''
        name = get_formatted_name('曹', '尤进')

        '''
        assertEqual是unittest类中的一个断言方法 
        用来核实得到的结果是否和期望的结果一直 一直的时候说明测试通过
        '''
        self.assertEqual(name, '曹尤进')


    def test_first_last_hua_name(self):
        '''这里将执行需要去测试的函数 将得到 值为：曹尤进乐进 的结果'''
        name = get_formatted_name('曹', '尤进', '乐进')

        '''
        assertEqual是unittest类中的一个断言方法 
        用来核实得到的结果是否和期望的结果一直 一直的时候说明测试通过
        '''
        self.assertEqual(name, '曹尤进乐进')

'''当执行这个文件的时候 将自动执行NamesTestCase类中的所有 以test_打头的方法'''
unittest.main()


'''
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
'''
'''以上是测试通过的结果'''



'''修改目标方法 新增了hua_name字段 测试时未填写该参数 则会出现测试不通过 如下'''
'''
E
======================================================================
ERROR: test_first_last_name (__main__.NamesTestCase)
这里将执行需要去测试的函数 将得到 值为：曹尤进 的结果
----------------------------------------------------------------------
Traceback (most recent call last):
  File "testCase.py", line 29, in test_first_last_name
    name = get_formatted_name('曹', '尤进')
TypeError: get_formatted_name() missing 1 required positional argument: 'hua_name'

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (errors=1)
'''
'''以上是测试不通过的结果并附上了详细的错误信息'''