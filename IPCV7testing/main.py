# coding=utf-8
#_author_='wuweibin'
#_time_='2016/4/13'
import unittest
from testcase import Testcase_ImageSetting
from pub import ReadExcelinfo
import sys,datetime
from HTMLTestRunner import HTMLTestRunner
#from test.test_optparse import TestCount
from pub import PubAction
import os
from pub.PubAction import logwrite, nowlogdir, datelogdir
reload(sys)
sys.setdefaultencoding( "utf-8" ) #存储中文日志是解决编码问题

now = datetime.datetime.now()
nowprint=now.strftime('%Y-%m-%d  %H:%M:%S ') ##当前时间
logwrite.write('\n')
logwrite.write('main执行,IPCV7自动化开始测试————start_testing：'+nowprint+'\n')
sys.path.append('./pub')
ipcip = ReadExcelinfo.ip_data
username = ReadExcelinfo.user_data
password = ReadExcelinfo.password_data

class C_IPCtest(unittest.TestCase, Testcase_ImageSetting.C_imagesetting_testcase):
    '''IPCV7自动化测试'''
    def setUp(self):
        now = datetime.datetime.now()
        nowprint=now.strftime('%Y-%m-%d  %H:%M:%S ') ##当前时间
        self.loginIPC(ip=ipcip,username=username, password=password)
        logwrite.write(nowprint+'unittest_setUp执行时间：'+'\n')
    def tearDown(self):
        now = datetime.datetime.now()
        nowprint=now.strftime('%Y-%m-%d  %H:%M:%S ') ##当前时间
        self.driver.quit()
        logwrite.write('unittest_tearDown执行时间,IPCV7自动化结束测试————end_testing：'+nowprint+'\n')
    def test_01(self):
        '''<配置---摄像机---图像>---图像调节'''
        self.lightchange_case()
        self.contrastchange_case()
        self.saturationchange_case()
        self.sharpnesschange_case()
    def test_02(self):
        '''<配置---摄像机---图像>---曝光'''
        self.GainModechange_case()
        self.gainmax_value_case()
        #self.gainlevel_value_case()
        self.IrisTypechange_case()
        self.irislevel_value_case()
        #self.irissize_value_case()
        self.ShuterModechange_case()
        self.Shutermin_case()
        #self.Shutterlevel_case()
        self.AntiFlickerMode_case() 
    def test_04(self):
        '''<配置---摄像机---图像>---日夜切换'''
        self.ircutchange_case()
        #两个测试用例时每次都会执行setUP和tearDown

if __name__ == "__main__":
    #suite=unittest.TestSuite(unittest.makeSuite(C_IPCtest))   
    #unittest.TextTestRunner(verbosity=2).run(suite)
    #suite=unittest.makeSuite(C_IPCtest)    ##将类生成suite
    suite = unittest.TestSuite()
    suite.addTest(C_IPCtest('test_01'))
    suite.addTest(C_IPCtest('test_02'))
    suite.addTest(C_IPCtest('test_04'))
    now = datetime.datetime.now()
    nowprint=now.strftime('%Y%m%d%H%M%S') ##当前时间
    resultname= datelogdir+'\\'+nowprint+'result.html'
    print resultname
    fp = open(resultname, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='IPVV7自动化测试（Python+Selenium 2.0）测试报告',
                            description='IPCv7自动化测试环境： win7，浏览器：Firefox ，测试组织：苏州中试')
    runner.run(suite)
    logwrite.close()