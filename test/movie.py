# coding=utf-8
from selenium import webdriver  # 导入浏览器模块
from selenium.webdriver.support.ui import WebDriverWait  # 用于页面加载完的插件
from selenium.webdriver.support import expected_conditions as EC
# 提供了一组预定义的条件供WebDriverWait使用。
from selenium.webdriver.common.by import By  # selenium中内置的一个class
import time
import os  # os是用于操作文件的模块

# 定义了一个爬数据的方法


def spider(driver, num, path):
    # 显式等待  等待list中的元素存在
    try:
        WebDriverWait(driver, 5).until(
            lambda driver: len(driver.find_element_by_class_name('list').find_elements_by_tag_name("a")) > 0)
    except BaseException:
        driver.close()
        return

    # 获取当前所有电影
    movies = driver.find_element_by_class_name(
        'list').find_elements_by_tag_name("a")

    for i in range(len(movies)):
        # 只重最新的一页去写入电影信息
        if i >= num:
            # 拿到每一项电影
            movie = movies[i]
            # 电影的名称
            movieNameText = movie.find_element_by_tag_name("p").text
            # .replace() 删除多余的换行和空格
            movieName = movieNameText.replace(
                '\n', '').replace('\r', '').replace(' ', '')
            # 电影的评分
            movieGradeText = movie.find_element_by_tag_name('strong').text
            # .replace() 删除多余的换行和空格
            movieGrade = movieGradeText.replace(
                '\n', '').replace('\r', '').replace(' ', '')
            # 有的电影评分无法抓取到
            if(movieGrade != ''):
                # 有评分的放入单独文件中
                if(float(movieGrade) > 8.5):
                    with open(path+"doubanMovie.txt", 'a', encoding='utf-8') as f:  # 创建并打开文件 拿到文件对象
                        f.write(' '.join(
                            ['名称：'+movieName, '-------', '地址：'+movies[i].get_attribute('href')]) + '\n')
            else:
                # 抓不到评分的放入到另一个文件中
                with open(path+"nameIsToLong.txt", 'a', encoding='utf-8') as f:  # 创建并打开文件 拿到文件对象
                    # 进行写入操作
                    f.write(' '.join(['名称：'+movieName,
                                      '-------', '地址：' + movies[i].get_attribute('href')]) + '\n')
    # 返回最新的长度
    return len(movies)


# 初始化文件路径
path = os.environ['USERPROFILE']+"\\Documents\\python\\"
if os.path.exists(path) == False:
    os.makedirs(path)
if(os.path.exists(path+"doubanMovie.txt")):
    os.remove(path+"doubanMovie.txt")
if(os.path.exists(path+"nameIsToLong.txt")):
    os.remove(path+"nameIsToLong.txt")
# 需要爬的页面地址
url = 'https://movie.douban.com/explore#!type=movie&tag=%E5%8A%A8%E7%94%BB&sort=rank&page_limit=20&page_start=480'  # 定义个变量url
# 创建一个chrome浏览器
driver = webdriver.Chrome()
# 已经添加的电影数量 默认0
num = 0
# 打开浏览器 跳转指定地址
driver.get(url)
# 第一次执行爬取数据
num = spider(driver, num, path)

# 对加载更多的操作
while True:
    # 获取加载更多按钮
    load_btn = driver.find_elements_by_class_name('more')
    # 当不存在加载按钮 爬取结束
    if(len(load_btn) <= 0):
        driver.close()
        break
    # 否则 加载更多
    load_btn[0].click()
    # 等待页面加载完毕
    time.sleep(2)
    num = spider(driver, num, path)
