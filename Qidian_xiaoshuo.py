from time import sleep

import bs4
import selenium
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import keyword

from selenium.webdriver.common.keys import Keys

url = 'https://www.qidian.com/finish?chanId=4&action=hidden&orderId=&style=2&pageSize=50&siteid=1&pubflag=0&hiddenField=2&page='

r = requests.get(url+'1')
soup = BeautifulSoup(r.content)
# 都市小说的总页数及页面大小
pages = int(soup.select('#page-container > div > ul > li:nth-of-type(8) > a')[0].string)
pageSize = 50
Fiction_list = []
# 读取每页的小说名字及链接
for i in range(1, int(pages)+1):
    if i > 20:
        break
    r = requests.get(url+str(i))
    bs1 = BeautifulSoup(r.content)
    css_selectot = 'body > div.wrap > div.all-pro-wrap.box-center.cf > div.main-content-wrap.fl > div.all-book-list > div > table > tbody'
    Fiction = bs1.select(css_selectot)[0]
    for it in Fiction.children:
        if type(it) == bs4.element.Tag:
            name = ""
            author = ""
            link = ""
            for e in it.children:
                if type(e) == bs4.element.Tag:
                    eNext = e.next_element
                    if type(eNext) == bs4.element.Tag:
                        eClass = eNext['class'][0]
                        if eClass == 'name':
                            name = eNext.string
                            link = eNext['href']
                        if eClass == 'author':
                            author = eNext.string
            Fiction_list.append({'name': name, 'link': link, 'author': author})
# print("序号\t name\t link\t\t author")
# k = 1
# for d in Fiction_list:
#     print("%d\t %s\t %s\t\t %s" % (k, d['name'], d['link'], d['author']))
#     k += 1
# print(Fiction_list)

# driver = webdriver.Chrome('/Users/cloudin/Downloads/chromedriver')
# driver.get('http://www.baidu.com')
# driver.get('http://www.baidu.com')

option = webdriver.ChromeOptions()
prefs = {'profile.default_content_settings.popups': 0, "download.default_directory": '/Users/cloudin/Desktop/LiuFeng/Fiction_Factory'}
option.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome('/Users/cloudin/Downloads/chromedriver', chrome_options=option)

for d in Fiction_list:
    driver.get('https:'+d['link'])
    try:
        icon = driver.find_element_by_xpath('//*[@id="download"]/em')
        icon.click()
        download = driver.find_element_by_xpath('//*[@id="popup-btn"]/a')
        d['link'] = download.get_attribute('href')
        # driver.get(d['link'])
    except selenium.common.exceptions.NoSuchElementException:
        pass
    continue
driver.close()

with open('/Users/cloudin/Desktop/LiuFeng/Fiction_Factory/readme.txt', 'w+') as f:
    for d in Fiction_list:
        f.write('%-10s \t%-20s\t %-s\n' % (d['author'], d['name'], d['link']))
print('over')



