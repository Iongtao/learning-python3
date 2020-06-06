# https://music.163.com/#/user/songs/rank?id=582924692
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait  # 用于页面加载完的插件
from selenium.webdriver.support import expected_conditions as EC
# 提供了一组预定义的条件供WebDriverWait使用。
from selenium.webdriver.common.by import By
import re
import os
import sys

url = 'https://music.163.com/#/user/songs/rank?id=582924692'
driver = webdriver.Chrome()
driver.get(url)

result = []

iframe = driver.switch_to.frame('g_iframe')
WebDriverWait(driver, 5).until(
    lambda diver: driver.find_element_by_css_selector('#m-record > div > div > ul'))

rheader = driver.find_element_by_id('rHeader')
numText = rheader.find_element_by_tag_name('h4').text
num = re.sub(r"\D", "", numText)

print('当前听歌数量：' + str(num))

try:
    # 和缓存文件进行比较 如果没有则创建新的文件
    with open('test/list.txt', 'r+', encoding="utf-8") as file_object:
        backlist = file_object.readlines()
        for i in range(len(backlist)):
            result.append(backlist[i].replace('\n', ''))
        file_object.close()
        # 如果数量没有变化 就没有新增的歌曲
        # if num == re.sub(r"\D", "", result[0]):
        #     print('没有听新的歌曲')

    with open('test/list.txt', 'w+', encoding='utf-8') as write_file:
        write_file.write(numText + '\n')

except FileNotFoundError as err:
    with open('test/list.txt', 'w+', encoding='utf-8') as write_file:
        write_file.write(numText + '\n')


# 获取歌曲列表
ul = driver.find_element_by_css_selector('.j-flag > ul')
lis = ul.find_elements_by_tag_name('li')
newlist = []

for i in range(len(lis)):
    songName = lis[i].find_element_by_class_name('song').text

    with open('test/list.txt', 'a', encoding='utf-8') as write_file:
        write_file.write(songName + '\n')
    if songName not in result[1:]:
        newlist.append(songName)


# 遍历出新增的歌曲
if len(newlist) > 0:
    print('新增%s首歌曲：' % len(newlist))
    for i in range(len(newlist)):
        print(newlist[i])
else:
    print('她没有听新的歌曲')
