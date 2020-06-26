
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.by import By

path = r'/Users/qixiaohan/Downloads/chromedriver'
driver = webdriver.Chrome(executable_path=path)

url= 'http://baidu.com'

driver.get(url)

time.sleep(3)

driver.find_element_by_css_selector('div a span[class="hot-refresh-text"]').click()


#4、鼠标悬停
link=driver.find_element_by_xpath('//*[@id="s-usersetting-top"]')
ActionChains(driver).move_to_element(link).perform()
driver.find_element_by_link_text(u'搜索设置').click()



#driver.find_element_by_xpath('//*[@id="hotsearch-refresh-btn"]/span').click()
'''driver.find_element(By.ID,'kw').send_keys("地图")
driver.find_element(By.ID,'su').click()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="2"]/div[1]/div/span[2]/a[1]').click()'''




