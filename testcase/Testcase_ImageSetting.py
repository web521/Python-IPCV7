#coding=utf-8
import time as t
import datetime,sys
from pub import aImagesetting
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from pub import ReadExcelinfo
from verifylib import Verify_ImageSetting
reload(sys)
sys.setdefaultencoding( "utf-8" ) #存储中文日志是解决编码问题
now = datetime.datetime.now()
nowprint=now.strftime('%Y-%m-%d  %H:%M:%S ') ##当前时间
logwrite = open('..\log\pub_log.txt','a')
logwrite.write(nowprint+'testcase_imagesetting_PubACtiond调用时间：'+'\n')

class C_imagesetting_testcase(aImagesetting.C_aImagsSetting, Verify_ImageSetting.C_Imagesetting_ver):
    def light(self,value):
        self.wait()
        self.find_element(*self.lightness_value_loc).send_keys(Keys.CONTROL,'a')
        self.wait()
        self.find_element(*self.lightness_value_loc).send_keys(value,Keys.ENTER)
        self.wait()
        t.sleep(5)
    def lightchange_case(self):
        self.lightnessh5()   ##单独执行需要，若在unittest函数同一个test_case中需要注释，只需要有一个菜单进入
        list1 = ReadExcelinfo.light_list
        for i in list1:
            now = datetime.datetime.now()
            nowprint=now.strftime('%Y-%m-%d  %H:%M:%S ') ##当前时间
            print 'light_value:'+i
            print nowprint+"int-rust:+++++++++++++"
            i=int(i)
            x=type(i)
            print x
            self.light(value=i)
            rust=self.lightchange_ver()
            rust=int(rust)
            y=type(rust)
            print rust
            print y
            #print 'light_change_verify:'+rust
            if i == rust:
                print 'light_change_OK'
                logwrite.write(nowprint+'light_change_OK'+'\n')
            else:
                print 'Falied'
                logwrite.write(nowprint+'light_change_Falied'+'\n')
    def constrast (self,value):
        self.wait()
        self.find_element(*self.contrast_value_loc).send_keys(Keys.CONTROL,'a')
        self.wait()
        self.find_element(*self.contrast_value_loc).send_keys(value,Keys.ENTER)
        self.wait()
        t.sleep(5)
    def constrastchange_case(self):
        self.lightnessh5()
        

    def IrcutfilterType(self,value):
        self.select=Select(self.find_element(*self.IrcutfilterType_loc))
        self.select.select_by_value(value)
        self.wait()
        self.find_element(*self.IrcutfilterType_loc).send_keys(Keys.ENTER)
        self.wait()
        t.sleep(3)
        self.now = datetime.datetime.now()
        self.driver.get_screenshot_as_file(u"../log/%s.png" %self.now.strftime("%Y%m%d.%H%M%S.%f")[:-3])
        t.sleep(10)
    def ircutchange_case(self):
        self.ircut()
        #n=0
        #while (n<2):
            #n=n+1
        list = ReadExcelinfo.daynight_list
        for i in list:
            print i
            now = datetime.datetime.now()
            nowprint=now.strftime('%Y-%m-%d  %H:%M:%S ') ##当前时间
            self.IrcutfilterType(value=i)
            r=self.ircut_ver()
            print r
            if i == "day" or r == 0:
                print  '切换日夜模式“白天”OK'
                logwrite.write(nowprint+'切换日夜模式“白天”OK'+'\n')
            elif i == "night" or r == 1:
                print  '切换日夜模式“黑夜”OK'
                logwrite.write(nowprint+'切换日夜模式“黑夜”OK'+'\n')
            elif i== "auto_gain" or r ==2:
                print '切换自动增益模式OK'
                logwrite.write(nowprint+'切换自动增益模式 OK'+'\n')
            else:
                print '切换日夜模式错误!'
                logwrite.write(nowprint+'切换日夜模式错误！'+'\n')




