# coding=utf-8
#_author_='wuweibin'
#_time_='2016/4/13'
import unittest
from testcase import Testcase_ImageSetting
from pub import ReadExcelinfo
import sys
sys.path.append('./pub')
ipcip = ReadExcelinfo.ip_data
username = ReadExcelinfo.user_data
password = ReadExcelinfo.password_data

class IPCtest(unittest.TestCase, Testcase_ImageSetting.testcase_imagesetting):
    def setUp(self):
        self.loginIPC(ip=ipcip,username=username, password=password)
    def tearDown(self):
        self.driver.quit()
    def test_01(self):
        self.ircutcase()
    #def test_02(self):
    #    lists = ReadExcelinfo.light_list
    #    self.lightnessh5()
    #    for i in lists:
    #        print i
    #        self.light(value=i)
if __name__ == "__main__":
        suite=unittest.TestSuite(unittest.makeSuite(IPCtest))
        unittest.TextTestRunner(verbosity=2).run(suite)