from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import traceback


def getContent(fileName, p: bool):
    n = 54
    l = 54
    WebDriverWait(browser, 20).until(lambda browser: len(
        browser.find_element_by_tag_name('tbody').find_elements_by_tag_name('tr')) > 1)
    while n <= l:
        try:
            # 当最后一页的时候 等待数据加载完 再去执行后续操作
            # 因为无法抓取最后一页的数据是否完全加载完了 导致tr的数量在50个
            # 但最后一页的tr的数量少于50个
            # 当for循环到42个的时候 没有内容 所以报错了
            if n == l:
                time.sleep(3)
            tr = browser.find_elements_by_class_name('el-table__row')
            print('当前页面的长度', len(tr))
            browser.find_elements_by_class_name(
                "accountingCenterRouterNewUser")
            print('现在进行到第 %s 页' % n)
            for i in range(len(tr)):
                name = tr[i].find_element_by_class_name(
                    'el-table_2_column_9').find_element_by_class_name('name').text
                print(name)
                category = tr[i].find_element_by_class_name(
                    'el-table_2_column_9').find_element_by_class_name('categories').text
                # print(category)
                ratio = tr[i].find_element_by_class_name(
                    'el-table_2_column_10').find_element_by_class_name('cell').text
                # print(ratio)
                orderquantity = tr[i].find_element_by_class_name(
                    'el-table_2_column_12').find_element_by_class_name('cell').text
                # print(orderquantity)
                commission = tr[i].find_element_by_class_name(
                    'el-table_2_column_13').find_element_by_class_name('cell').text
                # print(commission)
                msg = '|'.join(
                    [name, category, ratio, orderquantity, commission])
                print(msg)
                with open("D:\data\jd" + fileName + ".csv", 'a', encoding='utf-8') as f:
                    f.write(msg + '\n')
                print('result')
            print(n)
            n += 1
            if n <= l:
                nextpage = browser.find_element_by_xpath(
                    '//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div[2]/div/button[2]')
                nextpage.click()
        except Exception as e:
            print("异常信息:", e)
            traceback.print_exc()
            print('当前第 %s 页，排序方式是 %s 店铺类型 %s' % (n, fileName, p))
            key = input("登录失败了，请人工登录后并调整好参数后按任意键继续")


def setDesc(p: bool):
    # 佣金比例 降序
    browser.find_element_by_xpath(
        '//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/table/thead/tr/th[2]/div/span/i[2]').click()
    getContent('佣金比例', p)
    # 引入单量 降序
    browser.find_element_by_xpath(
        '//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/table/thead/tr/th[4]/div/span/i[2]').click()
    getContent('引入单量', p)
    # 引入金额 降序
    browser.find_element_by_xpath(
        '//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/table/thead/tr/th[5]/div/span/i[2]').click()
    getContent('引入金额', p)


browser = webdriver.Chrome()
browser.maximize_window()
browser.get('https://union.jd.com/investment/groupList')
WebDriverWait(browser, 200).until(
    EC.presence_of_element_located((By.CLASS_NAME, "point")))
print('登入成功')

time.sleep(1)
browser.find_element_by_xpath(
    '//*[@id="app"]/div/div[1]/div[1]/div/ul/div[2]/li/div').click()
time.sleep(1)
browser.find_element_by_xpath(
    '//*[@id="app"]/div/div[1]/div[1]/div/ul/div[2]/li/ul/a[2]/li').click()
time.sleep(1)
page = browser.find_element_by_xpath(
    '//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div[2]/div/span[2]/div/div/span/span/i').click()
time.sleep(1)
page50 = browser.find_element_by_xpath(
    '/html/body/div[2]/div[1]/div[1]/ul/li[4]').click()
time.sleep(3)

# 点击选择框
browser.find_element_by_xpath(
    '//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div/div/div/div/input').click()
time.sleep(1)
# 点击自营并查询
browser.find_element_by_xpath(
    '/html/body/div[3]/div[1]/div[1]/ul/li[2]').click()
time.sleep(3)
browser.find_element_by_xpath(
    '//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/button').click()
time.sleep(3)
setDesc(True)

# 点击选择框
browser.find_element_by_xpath(
    '//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div/div/div/div/input').click()
time.sleep(1)
# 点击非自营并查询
browser.find_element_by_xpath(
    '/html/body/div[3]/div[1]/div[1]/ul/li[3]').click()
time.sleep(3)
browser.find_element_by_xpath(
    '//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/button').click()
time.sleep(3)
setDesc(False)
