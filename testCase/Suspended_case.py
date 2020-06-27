from common.driver_baidu import start_up
from common.My_test import Mytest
import unittest
from PO.HomePage import HomePage




class Suspended_case(Mytest):
    @unittest.skip
    def test_Suspended_case(self):
        hp=HomePage(self.driver)
        hp.Suspended_case()