# coding=utf-8

from selenium import webdriver  # 导入浏览器模块
from selenium.webdriver.support.ui import WebDriverWait  # 用于页面加载完的插件
from selenium.webdriver.support import expected_conditions as EC
# 提供了一组预定义的条件供WebDriverWait使用。
from selenium.webdriver.common.by import By  # selenium中内置的一个class
import time
import os  # os是用于操作文件的模块


def spider(driver):

    try:
        WebDriverWait(driver, 5).until(
            lambda driver: len(driver.find_element_by_tag_name('tbody').find_elements_by_tag_name('tr')) > 1)
    except BaseException:
        driver.close()
        return
    datas = driver.find_element_by_tag_name(
        'tbody').find_elements_by_tag_name('tr')

    for i in range(len(datas)):
        if (i % 2) == 0:
            # 没有class的tr项
            # jadlayouts = datas[i].find_elements_by_tag_name('td')[6].text
            jadlayouts = datas[i].find_elements_by_tag_name(
                'td')[6].find_elements_by_class_name('jad-layout')
            for j in range(len(jadlayouts)):
                namekey = jadlayouts[j].find_element_by_class_name(
                    'jad-layout-sider.jad-layout-left').text
                content = jadlayouts[j].find_element_by_class_name(
                    'jad-layout-content').text
                print(namekey + ':' + content)
        else:
            # 有class的tr项
            divs = datas[i].find_elements_by_css_selector('div.jad-col > div')
            print('divs'+divs[1].text)


browser = webdriver.Chrome()

url = 'https://passport.jd.com/new/login.aspx?ReturnUrl=https://jzt.jd.com/jtk/#/activity-center'

browser.get(url)

WebDriverWait(browser, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "login-box")))

print('show')
browser.find_element_by_xpath(
    '//*[@id="content"]/div[2]/div[1]/div/div[3]').click()
browser.find_element_by_xpath('//*[@id="loginname"]').send_keys('紫紫紫紫轩')
browser.find_element_by_xpath('//*[@id="nloginpwd"]').send_keys('zx123456')


element = WebDriverWait(browser, 100).until(
    EC.presence_of_element_located((By.CLASS_NAME, "jzt-nav-menu-title-sub")))

print('登入成功')

time.sleep(3)
browser.find_element_by_xpath(
    '/html/body/div[1]/div[2]/div[3]/ul/li[2]/ul/div[2]').click()

time.sleep(3)
browser.find_element_by_xpath(
    '//*[@id="app"]/div[1]/div[2]/div/div/div[1]/div/div/div[4]').click()

time.sleep(3)
# datas = browser.find_elements_by_class_name('jad-table-expand-cell')
# print(len(datas))

spider(browser)

while True:
    next_btn = browser.find_element_by_xpath(
        '//*[@id="app"]/div[1]/div[2]/div/div/div[2]/div/div/div[3]/div/button[2]')
    if next_btn.get_attribute('disabled') == 'disabled':
        print('没有下一页了')
        browser.close()
    else:
        next_btn.click()
        spider(browser)
