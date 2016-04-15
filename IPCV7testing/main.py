# coding=utf-8
#_author_='wuweibin'
#_time_='2016/4/13'
import unittest
from testcase import Testcase_ImageSetting
from pub import ReadExcelinfo
import sys,datetime
from HTMLTestRunner import HTMLTestRunner
reload(sys)
sys.setdefaultencoding( "utf-8" ) #存储中文日志是解决编码问题
now = datetime.datetime.now()
nowprint=now.strftime('%Y-%m-%d  %H:%M:%S ') ##当前时间
logwrite = open('..\log\pub_log.txt','a')
logwrite.write('\n')
logwrite.write(nowprint+'main执行启动时间：'+'\n')
sys.path.append('./pub')
ipcip = ReadExcelinfo.ip_data
username = ReadExcelinfo.user_data
password = ReadExcelinfo.password_data

class C_IPCtest(unittest.TestCase, Testcase_ImageSetting.C_imagesetting_testcase):
    def setUp(self):
        now = datetime.datetime.now()
        nowprint=now.strftime('%Y-%m-%d  %H:%M:%S ') ##当前时间
        self.loginIPC(ip=ipcip,username=username, password=password)
        logwrite.write(nowprint+'unittest_setUp执行时间：'+'\n')
    def tearDown(self):
        now = datetime.datetime.now()
        nowprint=now.strftime('%Y-%m-%d  %H:%M:%S ') ##当前时间
        self.driver.quit()
        logwrite.write(nowprint+'unittest_tearDown执行时间：'+'\n')
    def test_01(self):
        #self.ircutchange_case()
        self.lightchange_case()
    #def test_02(self):
        #self.lightchange_case()
        #两个测试用例时每次都会执行setUP和tearDown
if __name__ == "__main__":
    fp = open('..\log\ result.html','wb')
    runner = HTMLTestRunner(stream=fp,
                            title='日夜切换测试报告',
                            description='用例执行情况： ')
    suite=unittest.TestSuite(unittest.makeSuite(C_IPCtest))
    unittest.TextTestRunner(verbosity=2).run(suite)
    fp.close()