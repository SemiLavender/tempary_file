import time

import selenium
from selenium import webdriver
from pykeyboard import PyKeyboard


url = 'https://item.mi.com/product/10000118.html'
# url = 'https://item.mi.com/product/10000123.html'
driver = webdriver.Chrome('/Users/cloudin/Downloads/chromedriver')
while True:
    try:
        driver.get(url)
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="J_buyBox"]/div/div[1]/div/a[1]').click()
        driver.find_element_by_id('username').send_keys('18813155281')
        driver.find_element_by_id('pwd').send_keys('lf52013146987+.')
        driver.find_element_by_id('login-button').click()
        yzm = input("验证码：")
        driver.find_element_by_id('captcha-code').send_keys(yzm)
        driver.find_element_by_id('login-button').click()
        break
    except selenium.common.exceptions.NoSuchElementException:
        pass
while True:
    while True:
        try:
            driver.find_element_by_xpath('//*[@id="J_list"]/div[1]/ul/li[1]/a/span[1]').click()
            # driver.find_element_by_xpath('//*[@id="J_list"]/div[2]/ul/li/a').click()
            break
        except selenium.common.exceptions.WebDriverException or selenium.common.exceptions.NoSuchElementException:
            pass
    while True:
        try:
            driver.find_element_by_xpath('//*[@id="J_buyBtnBox"]/li[1]/a').click()
            if '购' in driver.find_element_by_xpath('//*[@id="J_buyBtnBox"]/li[1]/a').text:
                break
        except selenium.common.exceptions.WebDriverException:
            pass
        print('准备抢货中')
    while True:
        try:
            driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div[2]/a[2]').click()
            driver.find_element_by_xpath('//*[@id="J_goCheckout"]').click()
            break
        except selenium.common.exceptions.NoSuchElementException:
            pass
    while True:
        try:
            driver.find_element_by_xpath('//*[@id="J_addressList"]/div[1]/dl').click()
            driver.find_element_by_xpath('//*[@id="J_checkoutToPay"]').click()
            if driver.find_element_by_xpath('//*[@id="J_payForm"]/div[1]/div[1]/div[1]/h2').text == '订单提交成功！去付款咯～':
                print('购买成功')
                break
        except selenium.common.exceptions.NoSuchElementException:
            pass
    driver.quit()
    break
    #except selenium.common.exceptions.NoSuchElementException:
    #    pass
