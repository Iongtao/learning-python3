from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import traceback

browser = webdriver.Chrome()
browser.maximize_window()
browser.get('https://union.jd.com/investment/groupList')

# 要去操作 iframe里面的内容 使用switch_to.frame(iframe元素的id指)
# 进入到这个iframe中去 抓取元素
iframe = browser.switch_to.frame('indexIframe')
browser.find_element_by_css_selector("input[name=loginname]").send_keys('花木兰可厉害了')
browser.find_element_by_css_selector("input[name=nloginpwd]").send_keys('花木兰可厉害了')
# 但是呢 进入了iframe里面是 抓不到上一层的元素了
# 返回上一层文档 使用 driver.switch_to.default_content()
browser.switch_to.default_content()
