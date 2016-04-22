#coding=utf-8
import time as t
import datetime,sys,os
from pub import aImagesetting
from pub import PubAction
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from pub import ReadExcelinfo
from verifylib import Verify_ImageSetting
from pub.PubAction import logwrite, datelogdir
from pip._vendor.requests.structures import CaseInsensitiveDict
reload(sys)
sys.setdefaultencoding( "utf-8" ) #存储中文日志是解决编码问题

now = datetime.datetime.now()
nowprint=now.strftime('%Y-%m-%d  %H:%M:%S ') ##当前时间
logwrite.write('<testcase_imagesetting调用时间>：'+nowprint+'\n')
class C_imagesetting_testcase(aImagesetting.C_aImagsSetting, Verify_ImageSetting.C_Imagesetting_ver):
    def light(self,value):   ##亮度 调节功能实现
        self.lightnessh5()  
        self.wait()
        try:
            self.find_element(*self.lightness_value_loc).send_keys(Keys.CONTROL,'a')
        except BaseException as meg:
            print meg
        self.wait()
        self.find_element(*self.lightness_value_loc).send_keys(value,Keys.ENTER)
        self.wait()
        #self.now = datetime.datetime.now()  ##获取当前事件
        #self.get_screenname = datelogdir+'\\'+self.now.strftime("%Y%m%d.%H%M%S.%f")[:-3]+'.png'    ##浏览器截图名称定义
        #self.driver.get_screenshot_as_file(self.get_screenname)  ##浏览器截图
        t.sleep(5)
        #return
    def lightchange_case(self):   ##亮度 调节验证及测试用例
         ##单独执行需要，若在unittest函数同一个test_case中需要注释，只需要有一个菜单进入
        list1 = ReadExcelinfo.light_list
        case1 = "lightchange_case"
        for i in list1:
            now = datetime.datetime.now()
            nowprint=now.strftime('%Y-%m-%d  %H:%M:%S ') ##当前时间
            print 'light_value:'+i
            logwrite.write( nowprint+'当前亮度_value:'+"---"+i+'\n')
            i=int(i)
            x=type(i)
            print x
            self.light(value=i)
            rust=self.lightchange_ver()
            rust=int(rust)
            y=type(rust)
            print rust
            print y
            #self.snapshotpic(case=case1,value=i) 
            #print 'light_change_verify:'+rust
            if i == rust:
                print 'light_change_OK'
                logwrite.write(nowprint+'亮度切换_OK'+'\n')
            else:
                print 'Falied'
                logwrite.write(nowprint+'亮度切换_Falied'+'\n')
    def contrast(self,value):   ##对比度 调节功能实现
        self.lightnessh5()  
        self.wait()
        self.find_element(*self.contrast_value_loc).send_keys(Keys.CONTROL,'a')
        self.wait()
        self.find_element(*self.contrast_value_loc).send_keys(value,Keys.ENTER)
        self.wait()
        t.sleep(5)
    def contrastchange_case(self):   ##对比度 调节验证及测试用例
        #self.lightnessh5()   ##单独执行需要，若在unittest函数同一个test_case中需要注释，只需要有一个菜单进入
        list1 = ReadExcelinfo.contrast_list
        case1 = "contrastchange_case"
        for i in list1:
            now = datetime.datetime.now()
            nowprint=now.strftime('%Y-%m-%d  %H:%M:%S ') ##当前时间
            print 'contras_value:'+i
            logwrite.write( nowprint+'当前对比度_value:'+"---"+i+'\n')
            i=int(i)
            x=type(i)
            print x
            self.contrast(value=i)
            self.snapshotpic(case=case1,value=i) 
            rust=self.contrast_ver()
            rust=int(rust)
            y=type(rust)
            print rust
            print y
            #print 'light_change_verify:'+rust
            if i == rust:
                print '对比度_OK'
                logwrite.write(nowprint+'对比度_OK'+'\n')
            else:
                print '对比度_Falied'
                logwrite.write(nowprint+'对比度_Falied'+'\n')
    def saturation(self,value):   ##饱和度  调节功能实现
        self.lightnessh5()  
        self.wait()
        self.find_element(*self.saturation_value_loc).send_keys(Keys.CONTROL,'a')
        self.wait()
        self.find_element(*self.saturation_value_loc).send_keys(value,Keys.ENTER)
        self.wait()
        t.sleep(5)
    def saturationchange_case(self):   ##饱和度 调节验证及测试用例
        #self.lightnessh5()   ##单独执行需要，若在unittest函数同一个test_case中需要注释，只需要有一个菜单进入
        list1 = ReadExcelinfo.saturation_list
        case1 = "saturationchange_case"
        for i in list1:
            now = datetime.datetime.now()
            nowprint=now.strftime('%Y-%m-%d  %H:%M:%S ') ##当前时间
            print '饱和度:'+i
            logwrite.write( nowprint+'当前饱和度_value:'+"---"+i+'\n')
            i=int(i)
            x=type(i)
            print x
            self.saturation(value=i)
            self.snapshotpic(case=case1,value=i) 
            rust=self.saturation_ver()
            rust=int(rust)
            y=type(rust)
            print rust
            print y
            #print 'light_change_verify:'+rust
            if i == rust:
                print '饱和度_OK'
                logwrite.write(nowprint+'饱和度_OK'+'\n')
            else:
                print '饱和度_Falied'
                logwrite.write(nowprint+'饱和度_Falied'+'\n')       
    def sharpness(self,value):   ##锐度  调节功能实现
        self.lightnessh5()  
        self.wait()
        self.find_element(*self.sharpness_value_loc).send_keys(Keys.CONTROL,'a')
        self.wait()
        self.find_element(*self.sharpness_value_loc).send_keys(value,Keys.ENTER)
        self.wait()
        t.sleep(5)
    def sharpnesschange_case(self):   ##锐度 调节验证及测试用例
        #self.lightnessh5()   ##单独执行需要，若在unittest函数同一个test_case中需要注释，只需要有一个菜单进入
        list1 = ReadExcelinfo.sharpness_list
        case1 = "sharpnesschange_case"
        for i in list1:
            now = datetime.datetime.now()
            nowprint=now.strftime('%Y-%m-%d  %H:%M:%S ') ##当前时间
            print '锐度:'+i
            logwrite.write( nowprint+'当前锐度_value:'+"---"+i+'\n')
            i=int(i)
            x=type(i)
            print x
            self.sharpness(value=i)
            self.snapshotpic(case=case1,value=i) 
            rust=self.sharpness_ver()
            rust=int(rust)
            y=type(rust)
            print rust
            print y
            #print 'light_change_verify:'+rust
            if i == rust:
                print '锐度_OK'
                logwrite.write(nowprint+'锐度_OK'+'\n')
            else:
                print '锐度_Falied'
                logwrite.write(nowprint+'锐度_Falied'+'\n') 
    
    def GainMode(self,value):   ##曝光 ---增益模式选择
        self.exposureh5()  
        self.wait()
        self.select=Select(self.find_element(*self.GainMode_loc))
        self.select.select_by_value(value)
        self.wait()
        self.find_element(*self.GainMode_loc).send_keys(Keys.ENTER)
        self.wait()
        t.sleep(10)
    def gainmax_value(self,value):   ##曝光 ---自动时--->增益上限
        self.exposureh5()  
        self.wait()
        self.wait()
        self.find_element(*self.gainmax_value_loc).send_keys(Keys.CONTROL,'a')
        self.wait()
        self.find_element(*self.gainmax_value_loc).send_keys(value,Keys.ENTER)
        self.wait()
        t.sleep(10)
    def gainlevel_value(self,value):   ##曝光 ---手动时--->增益等级
        self.exposureh5()  
        self.wait()
        self.find_element(*self.gainlevel_value_loc).send_keys(Keys.CONTROL,'a')
        self.wait()
        self.find_element(*self.gainlevel_value_loc).send_keys(value,Keys.ENTER)
        self.wait()
        t.sleep(10)

    def GainModechange_case(self):   ##曝光 ---增益模式验证及测试用例
        #self.exposureh5()   ##单独执行需要，若在unittest函数同一个test_case中需要注释，只需要有一个菜单进入
        list1 = ReadExcelinfo.GainMode_list
        case1 = "GainModechange_case"
        for i in list1:
            now = datetime.datetime.now()
            nowprint=now.strftime('%Y-%m-%d  %H:%M:%S ') ##当前时间
            print '增益模式:'+i
            print nowprint+"++++++++++++++++++++++"
            self.GainMode(value=i)
            self.snapshotpic(case=case1,value=i) 
            rust=self.GainMode_ver()
            print "ver"+rust
    
       ##################增益模式及增益###################################
    def gainmax_value_case(self):
        #self.exposureh5()
        #self.gainmax_value(value='auto')
        list1 = ReadExcelinfo.gainmax_value_list
        case1 = "gainmax_value_case"
        for i in list1:
            now = datetime.datetime.now()
            nowprint=now.strftime('%Y-%m-%d  %H:%M:%S ') ##当前时间
            print '增益上限:'+i
            print nowprint+"++++++++++++++++++++++"
            i=int(i)
            x=type(i)
            print x
            self.gainmax_value(value=i)
            self.snapshotpic(case=case1,value=i) 
            rust=self.gainmax_value_ver()
            rust=int(rust)
            y=type(rust)
            print rust
            print y
            #print 'light_change_verify:'+rust
            if i == rust:
                print '增益上限_OK'
                logwrite.write(nowprint+'增益上限_OK'+'\n')
            else:
                print '增益上限_Falied'
                logwrite.write(nowprint+'增益上限_Falied'+'\n') 
    def gainlevel_value_case(self):   ##曝光 ---增益模式验证及测试用例
        #self.exposureh5()  ##单独执行需要，若在unittest函数同一个test_case中需要注释，只需要有一个菜单进入
        #self.GainMode(value='manual')
        list1 = ReadExcelinfo.gainlevel_value_list
        case1 = "gainlevel_value_case"
        for i in list1:
            now = datetime.datetime.now()
            nowprint=now.strftime('%Y-%m-%d  %H:%M:%S ') ##当前时间
            print '增益等级:'+i
            print nowprint+"++++++++++++++++++++++"
            i=int(i)
            x=type(i)
            print x
            self.gainlevel_value(value=i)
            self.snapshotpic(case=case1,value=i) 
            rust=self.gainlevel_value_ver()
            rust=int(rust)
            y=type(rust)
            print rust
            print y
            #print 'light_change_verify:'+rust
            if i == rust:
                print '增益等级_OK'
                logwrite.write(nowprint+'增益等级_OK'+'\n')
            else:
                print '增益等级_Falied'
                logwrite.write(nowprint+'增益等级_Falied'+'\n') 
    ####################曝光模式及曝光##########################################     
    def IrisType(self,value):   ##曝光 ---光圈模式选择
        self.exposureh5()  
        self.wait()
        self.select=Select(self.find_element(*self.IrisType_loc))
        self.select.select_by_value(value)
        self.wait()
        self.find_element(*self.IrisType_loc).send_keys(Keys.ENTER)
        self.wait()
        t.sleep(10)
    def irislevel_value(self,value):   ##曝光 ---光圈灵敏度
        self.exposureh5()  
        self.wait()
        self.find_element(*self.irislevel_value_loc).send_keys(Keys.CONTROL,'a')
        self.wait()
        self.find_element(*self.irislevel_value_loc).send_keys(value,Keys.ENTER)
        self.wait()
        t.sleep(10)
    def irissize_value(self,value):   ##曝光 ---光圈大小
        self.exposureh5()  
        self.wait()
        self.find_element(*self.irissize_value_loc).send_keys(Keys.CONTROL,'a')
        self.wait()
        self.find_element(*self.irissize_value_loc).send_keys(value,Keys.ENTER)
        self.wait()
        t.sleep(5)
    def IrisTypechange_case(self):   ##曝光 ---光圈模式验证及测试用例
        #self.exposureh5()   ##单独执行需要，若在unittest函数同一个test_case中需要注释，只需要有一个菜单进入
        list1 = ReadExcelinfo.IrisType_list
        case1 = "IrisTypechange_case"
        for i in list1:
            now = datetime.datetime.now()
            nowprint=now.strftime('%Y-%m-%d  %H:%M:%S ') ##当前时间
            print '光圈模式:'+i
            print nowprint+"++++++++++++++++++++++"
            self.IrisType(value=i)
            self.snapshotpic(case=case1,value=i) 
            rust=self.IrisType_ver()
            print "ver"+rust
    def irislevel_value_case(self):
        #self.exposureh5()
        list1 = ReadExcelinfo.irislevel_value_list
        case1 = "irislevel_value_case"
        for i in list1:
            now = datetime.datetime.now()
            nowprint=now.strftime('%Y-%m-%d  %H:%M:%S ') ##当前时间
            print '光圈灵敏度:'+i
            print nowprint+"++++++++++++++++++++++"
            i=int(i)
            x=type(i)
            print x
            self.irislevel_value(value=i)
            self.snapshotpic(case=case1,value=i) 
            rust=self.irislevel_value_ver()
            rust=int(rust)
            y=type(rust)
            print rust
            print y
            #print 'light_change_verify:'+rust
            if i == rust:
                print '光圈灵敏度_OK'
                logwrite.write(nowprint+'光圈灵敏度_OK'+'\n')
            else:
                print '光圈灵敏度_Falied'
                logwrite.write(nowprint+'光圈灵敏度_Falied'+'\n') 
    def irissize_value_case(self):
        #self.exposureh5()
        list1 = ReadExcelinfo.irissize_value_list
        case1 = "irissize_value_case"
        for i in list1:
            now = datetime.datetime.now()
            nowprint=now.strftime('%Y-%m-%d  %H:%M:%S ') ##当前时间
            print '光圈大小:'+i
            print nowprint+"++++++++++++++++++++++"
            i=int(i)
            x=type(i)
            print x
            self.irissize_value(value=i)
            self.snapshotpic(case=case1,value=i) 
            rust=self.irissize_value_ver()
            rust=int(rust)
            y=type(rust)
            print rust
            print y
            #print 'light_change_verify:'+rust
            if i == rust:
                print '光圈大小_OK'
                logwrite.write(nowprint+'光圈大小_OK'+'\n')
            else:
                print '光圈大小_Falied'
                logwrite.write(nowprint+'光圈大小_Falied'+'\n') 
    ####################快门模式及快门###########################################
    def ShuterMode(self,value):   ##快门 ---快门模式选择
        self.exposureh5()  
        self.wait()
        self.select=Select(self.find_element(*self.ShuterMode_loc))
        self.select.select_by_value(value)
        self.wait()
        self.find_element(*self.ShuterMode_loc).send_keys(Keys.ENTER)
        self.wait()
        t.sleep(10)
    def Shutermin(self,value):   ##快门 ---快门下限
        self.exposureh5()  
        self.wait()
        self.select=Select(self.find_element(*self.Shutermin_loc))
        self.select.select_by_value(value)
        self.wait()
        self.find_element(*self.Shutermin_loc).send_keys(Keys.ENTER)
        self.wait()
        t.sleep(10)
    def Shutterlevel(self,value):   ##快门 ---快门等级
        self.select=Select(self.find_element(*self.Shutterlevel_loc))
        self.select.select_by_value(value)
        self.wait()
        self.find_element(*self.Shutterlevel_loc).send_keys(Keys.ENTER)
        self.wait()
        t.sleep(10)
    def ShuterModechange_case(self):   ##曝光 ---光圈模式验证及测试用例
        #self.exposureh5()   ##单独执行需要，若在unittest函数同一个test_case中需要注释，只需要有一个菜单进入
        list1 = ReadExcelinfo.ShuterMode_list
        case1 = "ShuterModechange_case"
        for i in list1:
            now = datetime.datetime.now()
            nowprint=now.strftime('%Y-%m-%d  %H:%M:%S ') ##当前时间
            print '快门模式:'+i
            print nowprint+"++++++++++++++++++++++"
            self.ShuterMode(value=i)
            self.snapshotpic(case=case1,value=i) 
            rust=self.ShuterMode_ver()
            print "ver"+rust
    def Shutermin_case(self):
        #self.exposureh5()
        list1 = ReadExcelinfo.Shutermin_list
        case1 = "Shutermin_case"
        for i in list1:
            now = datetime.datetime.now()
            nowprint=now.strftime('%Y-%m-%d  %H:%M:%S ') ##当前时间
            print '快门下限:'+i
            print nowprint+"++++++++++++++++++++++"
            self.Shutermin(value=i)
            self.snapshotpic(case=case1,value=i) 
            '''
            rust=self.Shutermin_ver()
            print rust
            if i == rust:
                print '快门下限_OK'
                logwrite.write(nowprint+'快门下限_OK'+'\n')
            else:
                print '快门下限_Falied'
                logwrite.write(nowprint+'快门下限_Falied'+'\n') 
            '''
    def Shutterlevel_case(self):
        #self.exposureh5()
        list1 = ReadExcelinfo.Shutterlevel_list
        case1 = "Shutterlevel_case"
        for i in list1:
            now = datetime.datetime.now()
            nowprint=now.strftime('%Y-%m-%d  %H:%M:%S ') ##当前时间
            print '快门等级:'+i
            print nowprint+"++++++++++++++++++++++"
            i=int(i)
            x=type(i)
            print x
            self.Shutterlevel(value=i)
            self.snapshotpic(case=case1,value=i) 
            rust=self.Shutterlevel_ver()
            rust=int(rust)
            y=type(rust)
            print rust
            print y
            #print 'light_change_verify:'+rust
            if i == rust:
                print '快门等级_OK'
                logwrite.write(nowprint+'光圈等级_OK'+'\n')
            else:
                print '快门等级_Falied'
                logwrite.write(nowprint+'光圈等级_Falied'+'\n') 

    #########################防闪烁######################################
    def AntiFlickerMode(self,value):   ##快门 ---快门模式选择
        self.exposureh5()  
        self.wait()
        self.select=Select(self.find_element(*self.AntiFlickerMode_loc))
        self.select.select_by_value(value)
        self.wait()
        self.find_element(*self.AntiFlickerMode_loc).send_keys(Keys.ENTER)
        self.wait()
        t.sleep(10)
    def AntiFlickerMode_case(self):   ##曝光 ---光圈模式验证及测试用例
        #self.exposureh5()   ##单独执行需要，若在unittest函数同一个test_case中需要注释，只需要有一个菜单进入
        list1 = ReadExcelinfo.AntiFlickerMode_list
        case1 = "AntiFlickerMode_case"
        for i in list1:
            now = datetime.datetime.now()
            nowprint=now.strftime('%Y-%m-%d  %H:%M:%S ') ##当前时间
            print '防闪烁:'+i
            print nowprint+"++++++++++++++++++++++"
            self.AntiFlickerMode(value=i)
            self.snapshotpic(case=case1,value=i) 
            rust=self.AntiFlickerMode_ver()
            print "ver"+rust
    
    ###############################################################
    def IrcutfilterType(self,value):
        self.select=Select(self.find_element(*self.IrcutfilterType_loc))
        self.select.select_by_value(value)
        self.wait()
        self.find_element(*self.IrcutfilterType_loc).send_keys(Keys.ENTER)
        self.wait()
        t.sleep(3)
        self.now = datetime.datetime.now()  ##获取当前事件
        self.get_screenname = datelogdir+'\\'+self.now.strftime("%Y%m%d.%H%M%S.%f")[:-3]+'.png'    ##浏览器截图名称定义
        #self.driver.get_screenshot_as_file(u"../log/%s.png" %self.now.strftime("%Y%m%d.%H%M%S.%f")[:-3])
        self.driver.get_screenshot_as_file(self.get_screenname)  ##浏览器截图
        t.sleep(5)
        
    def ircutchange_case(self):
        list = ReadExcelinfo.daynight_list
        case1 = "ircutchange_case"
        for i in list:
            print i
            self.ircutfilterh5()
            now = datetime.datetime.now()
            nowprint=now.strftime('%Y-%m-%d  %H:%M:%S ') ##获取当前时间
            self.IrcutfilterType(value=i)
            self.snapshotpic(case=case1,value=i) 
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




