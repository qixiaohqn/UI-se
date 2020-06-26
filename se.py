
from selenium import webdriver

path = r'/Users/qixiaohan/Downloads/chromedriver'
driver = webdriver.Chrome(executable_path=path)

url1 = 'http://baidu.com'

driver.get(url=url1)
