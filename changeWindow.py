
from selenium import webdriver
import time

path = r'/Users/qixiaohan/Downloads/chromedriver'

driver = webdriver.Chrome(executable_path=path)

url= 'http://baidu.com'

driver.get(url)
