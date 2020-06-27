
from selenium import webdriver


path = r'/Users/qixiaohan/Downloads/chromedriver'

driver = webdriver.Chrome(executable_path=path)

url= 'http://baidu.com'

driver.get(url)
