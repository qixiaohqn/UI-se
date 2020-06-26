
from selenium import webdriver
import time

path = r'/Users/qixiaohan/Downloads/chromedriver'

driver = webdriver.Chrome(executable_path=path)

url='https://mail.163.com/'#https协议怎么处理？

driver.get(url)
#1、切换框架
time.sleep(1)

login=driver.find_element_by_xpath('//*[@id="auto-id-1593157743657"]')
driver.switch_to.window(login)
driver.find_element_by_name("email").send_keys("18001036589")
time.sleep(3)
driver.switch_to.default_content()


head=driver.find_element_by_xpath('//*[@id="footer"]/div/div[1]/a[1]')
driver.switch_to.window(head)
