from selenium import  webdriver
from common.driver_baidu import start_up
from selenium.webdriver.common.action_chains import ActionChains

class HomePage(object):

    def __init__(self,driver):
        self.driver=driver

    def Suspended_case(self):
        link = self.driver.find_element_by_xpath('//*[@id="s-usersetting-top"]')
        ActionChains(self.driver).move_to_element(link).perform()
        self.driver.find_element_by_link_text(u'搜索设置').click()
