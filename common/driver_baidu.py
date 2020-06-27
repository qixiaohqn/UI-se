from selenium import  webdriver
import time
def start_up():
    path = r'/Users/qixiaohan/Downloads/chromedriver'

    driver=webdriver.Chrome(executable_path=path)

    url='http://baidu.com'

    driver.get(url)

    time.sleep(20)

    return driver

start_up()