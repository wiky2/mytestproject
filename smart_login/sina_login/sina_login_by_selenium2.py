#!/usr/bin/env python
# coding: utf-8
#声明必须放在前两行，# coding=<encoding name>
import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC


def login(account, passwd, url):
    # 如果driver没加入环境变量中，那么就需要明确指定其路径
    # 验证于2017年4月11日
    # 直接登陆新浪微博
    driver = webdriver.Chrome('/usr/local/bin/chromedriver')
    # driver.maximize_window()
    # locator = (By.)
    driver.get(url)
    time.sleep(15)
    print '开始登陆'
    print account
    name_field = driver.find_element_by_id('loginname')
    name_field.clear()
    for account_one in account:
        name_field.send_keys(account_one)
    password_field = driver.find_element_by_class_name('password').find_element_by_name('password')
    password_field.clear()
    for passwd_one in passwd:
        password_field.send_keys(passwd_one)
    # driver.switch_to_window(driver.window_handles[1])
    # submit = driver.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[6]/a/span')
    submit = driver.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[6]/a/span')

    ActionChains(driver).double_click(submit).perform()
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'WB_miniblog')))

    source = driver.page_source

    if is_login(source):
        print '登录成功'

    sina_cookies = driver.get_cookies()
    time.sleep(3600)
    driver.quit()
    return sina_cookies


def is_login(source):
    rs = re.search("CONFIG\['islogin'\]='(\d)'", source)
    if rs:
        return int(rs.group(1)) == 1
    else:
        return False


if __name__ == '__main__':
    url = 'https://weibo.com/'
    name_input = raw_input('请输入你的账号\n')
    print name_input
    passwd_input = raw_input('请输入你的密码\n')
    cookies = login(name_input, passwd_input, url)








