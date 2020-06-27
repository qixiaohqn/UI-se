'''

封装setup类和teardown类
导入对应的包
1、实在setup类

2、实现setup方法

3、teardown方法

4、teardown类
'''

import unittest,time
from common.driver_baidu import start_up

class Mytest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
       cls.driver=start_up()

    def setUp(self) -> None:
        self.driver.maximize_window()
        time.sleep(10)


    def tearDown(self) -> None:
        self.driver.close()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()



