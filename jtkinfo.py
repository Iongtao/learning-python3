
from selenium import webdriver
import os



browser=webdriver.Chrome()
browser.maximize_window()
browser.get('https://passport.jd.com/new/login.aspx?ReturnUrl')
browser.find_element_by_xpath('//*[@id="content"]/div[2]/div[1]/div/div[3]/a').click()
browser.find_element_by_xpath('//*[@id="loginname"]').send_keys('紫紫紫紫轩')
browser.find_element_by_xpath('//*[@id="nloginpwd"]').send_keys('zx123456')
browser.find_element_by_xpath('//*[@id="loginsubmit"]').click()