import time

from selenium import webdriver
import selenium

from config import CONF

driver = webdriver.Chrome('/Users/cloudin/Downloads/chromedriver')
url = 'http://jira.zhongchangcloud.com:8096/secure/admin/user/UserBrowser.jspa'

username = 'admin'
password = ''

driver.get(url)
driver.find_element_by_id("login-form-username").send_keys(username)
driver.find_element_by_id("login-form-password").send_keys(password)
driver.find_element_by_id("login-form-submit").click()
driver.find_element_by_id('login-form-authenticatePassword').send_keys(password)
driver.find_element_by_id("login-form-submit").click()

info_list = CONF

for a in info_list:
    driver.find_element_by_id('user_browser').click()
    driver.find_element_by_id("create_user").click()
    time.sleep(1)
    driver.find_element_by_id('user-create-username').send_keys(a['username'])
    driver.find_element_by_id('user-create-password').send_keys(a['username'])
    driver.find_element_by_id('user-create-confirm').send_keys(a['username'])
    driver.find_element_by_id('user-create-fullname').send_keys(a['fullname'])
    driver.find_element_by_id('user-create-email').send_keys(a['username']+'@zhongchangcloud.com')
    driver.find_element_by_id('user-create-sendEmail').click()
    driver.find_element_by_id('user-create-submit').click()
    time.sleep(1)
    try:
        driver.find_element_by_id('user-create-username-error').click()
        driver.find_element_by_id('user-create-cancel').click()
    except selenium.common.exceptions.NoSuchElementException:
        pass
    time.sleep(1)

driver.quit()




