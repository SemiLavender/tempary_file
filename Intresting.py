import time

from selenium import webdriver

url = ''

path = '/Users/cloudin/Desktop/LiuFeng/Fiction_Factory/temp/'

driver = webdriver.Chrome('/Users/cloudin/Downloads/chromedriver')

for i in range(2, 10):
    driver.get(url+str(i)+'.html')
    time.sleep(1)
    for j in range(1, 31):
        link = driver.find_element_by_xpath('/html/body/div[15]/div/ul/li['+str(j)+']/a')
        name = link.text
        driver.get(link.get_attribute('href'))
        time.sleep(1)
        content = driver.find_element_by_xpath('/html/body/div[14]/div[2]/div[3]/font').text
        f = open(path+name+'.txt', 'w+')
        f.write(content)
        f.close()

driver.quit()