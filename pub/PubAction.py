#!/usr/bin/env python
#coding:utf-8
from selenium import webdriver
import sys
import linecache
import datetime
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time as t
import os
import shutil
from __builtin__ import str

reload(sys)
sys.setdefaultencoding( "utf-8" ) #存储中文日志是解决编码问题
now = datetime.datetime.now()
nowprint=now.strftime('%Y-%m-%d  %H:%M:%S ') ##当前时间
logwrite = open('..\log\pub_log.txt','a')
logwrite.write(nowprint+'PubACtiond调用时间：'+'\n')
print nowprint

class C_ipcaction(object):
    def wait(self):
        t.sleep(1.5)
    #def __init__ (self,driver):
    #   self.driver = driver
    def open_firefox(self):
        self.profileDir="C:/Users/Administrator/AppData/Roaming/Mozilla/Firefox/Profiles/ivjlfm23.default"
        #self.profileDir="C:/Users/admin/AppData/Roaming/Mozilla/Firefox/Profiles/d68dofkn.default"
        self.profile=webdriver.FirefoxProfile(self.profileDir)
        self.driver=webdriver.Firefox(self.profile)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
    def open_url(self,ip):
        base_url = 'http://'+ip
        self.open_firefox()
        self.driver.get(base_url)
        self.wait()
    def find_element(self,*loc):
        return self.driver.find_element(*loc)
    def clickID(self,*loc):
        return self.driver.find_element(*loc).click()    
    def logtext(self,*loc):
        now = datetime.datetime.now()
        nowprint=now.strftime('%Y-%m-%d  %H:%M:%S ') ##当前时间
        self.label = self.driver.find_element(*loc).text
        logwrite.write(nowprint+":"+self.label+'\n')

    
class C_ipcpage(C_ipcaction):#页面基本操作，元素定位等
    "IPCV7所有对象ID"
    #定位器
    username_loc=(By.ID,"username")
    password_loc=(By.ID,"password")
    login_loc=(By.ID,"b_Login")
    ##"主页面"定位器
    MenuViewer_loc=(By.ID,"MenuViewer") ##实时浏览
    MenuPlayback_loc=(By.ID ,"MenuPlayback") ##录像回放
    MenuPic_loc=(By.ID,"MenuPic")  ##图片管理
    MenuConfig_loc=(By.ID,"MenuConfig") ##配置
    ##一级菜单“配置”页面定位器
    aMLocalConfig_loc=(By.ID,"aMLocalConfig") ##本地配置
    Mfastset_loc=(By.ID,"Mfastset") ##快速配置
    aNetwork_loc=(By.ID,"aNetwork") ##网络
    aVideoCamera_loc=(By.ID,"aVideoCamera") ##摄像机
    aEvent_loc=(By.ID,"aEvent") ##事件
    aStorage_loc=(By.ID,"aStorage") ##存储
    aBaseConfig_loc=(By.ID,"aBaseConfig") ##系统
    ##二级菜单“摄像机”菜单下定位器
    aImagsSettings_loc=(By.ID,"aImagsSettings") ##图像
    aOSD_loc=(By.ID,"aOSD") ##OSD
    aVideo_loc=(By.ID,"aVideo") ##视频
    aAudio_loc=(By.ID,"aAudio") ##音频
    ##“图像—图像效果”菜单下对象
    lightnessh5_loc=(By.ID,"lightnessh5") ##图像t调节
    lightness_value_loc=(By.ID,"lightness_value") ##图像亮度
    contrast_value_loc=(By.ID,"contrast_value")   ##图像对比度
    saturation_value_loc=(By.ID,"saturation_value")  ##图像饱和度
    sharpness_value_loc=(By.ID,"sharpness_value")   ##图像锐度
    exposureh5_loc=(By.ID,"exposureh5") ##曝光
    GainMode_loc=(By.ID,"GainMode") ##增益 auto，manual
    gainmax_value_loc=(By.ID,"gainmax_value") ##增益上限0~100
    gainlevel_value_loc=(By.ID,"gainlevel_value")
    IrisType_loc=(By.ID,"IrisType") ##光圈模式dc_irisauto DC-IRIS自动，dc_irismanual DC-IRIS手动，p_irismanual P-IRIS手动
    irislevel_value_loc=(By.ID,"irislevel_value") ##光圈灵敏值 1~100
    irissize_value_loc=(By.ID,"irissize_value")
    ShuterMode_loc=(By.ID,"ShuterMode") ##快门模式：快门值auto 自动，manual 手动
    Shutermin_loc=(By.ID,"Shutermin") ##快门下限：1/1，1/2,1/7.5，1/10,1/15,1/25,1/50,1/100,1/150,1/200,1/240,1/480,1/960,1/1024,1/2000,1/4000,1/8000,1/16000,1/30000
    Shutterlevel_loc=(By.ID,"Shutterlevel")
    AntiFlickerMode_loc=(By.ID,"AntiFlickerMode") ##防闪烁 50hz，60hz，auto 自然光
    whiteblanceh5_loc=(By.ID,"whiteblanceh5") ##白平衡按钮
    WhiteBalance_loc=(By.ID,"whiteblanceh5") ##白平衡选择框  manual 手动白平衡，auto1 自动白平衡1，auto2 自动白平衡2，lock 锁定白平衡，fluorescentlight 日光灯，filamentlight 白炽灯，warmlight 暖光灯，natural 自然光
    ircutfilterh5_loc=(By.ID,'ircutfilterh5')  ##日夜转换
    IrcutfilterType_loc=(By.ID,'IrcutfilterType') ##日夜转换下拉框
    daytonightlevel_value_loc=(By.ID,'daytonightlevel_value') ##灵敏度
    daytonight_value_loc=(By.ID,'daytonight_value') ##日夜转换等待时间5~120
    threshold_value_loc=(By.ID,'threshold_value')
    
    ImageEnhancementh5_loc=(By.ID,'ImageEnhancementh5')  ##图像增强
    Antishake5_loc=(By.ID,'Antishake5')  ##防抖
    otherh5_loc=(By.ID,'otherh5')  ##翻转与回显
    
    ##二级菜单"系统"下对象
    aDeviceInformation_loc=(By.ID,"aDeviceInformation") ##设备信息
    aSecurity_loc=(By.ID,"aSecurity") ##用户安全
    aDateTime_loc=(By.ID,"aDateTime") ##时间设置
    aSerialPost_loc=(By.ID,"aSerialPost") ##串口
    aLog_loc=(By.ID,"aLog") ##日志管理
    aSystemMaintenance_loc=(By.ID,"aSystemMaintenance") ##系统维护
    ##二级菜单“系统维护”下对象定位器

    ##二级菜单“本地配置”下对象定位器
    MLocalConfig_loc=(By.ID,"MLocalConfig") ##本地配置
    tePreviewPicPath_loc=(By.ID,"tePreviewPicPath") ##抓拍---浏览抓拍保存路径



    constantBitRate_loc=(By.ID,"constantBitRate")
    ConfigBtn_loc=(By.ID,"ConfigBtn")
    changePlay_loc=(By.ID,"changePlay")
    ptz_right_loc=(By.ID,'ptz_right')

    ##实时浏览页面对象定位
    capture_loc=(By.ID,'capture')



    def typeUsername_password(self,username,password):
        self.wait()
        self.find_element(*self.username_loc).send_keys(username)
        self.wait()
        self.find_element(*self.password_loc).send_keys(password)
    def clickLogin(self):
        self.wait()
        self.clickID(*self.login_loc)
    def loginIPC(self,ip,username,password):##登录IPC函数
        self.open_url(ip)
        self.typeUsername_password(username,password)
        self.clickLogin()
        self.driver.switch_to_alert()
        self.now_url=self.driver.current_url
        logwrite.write(self.now_url+'\n')
    """############     页面菜单               ####################################"""
    def MenuViewer(self):##进入实时浏览页面
        self.driver.switch_to_frame('contentframe')
        self.clickID(*self.MenuViewer_loc)
        self.wait()
        self.logtext(*self.MenuViewer_loc)
    def MenuPlayback(self):##进入录像回放页面
        self.clickID(*self.MenuPlayback_loc)
        self.wait()
        self.logtext(*self.MenuPlayback_loc)
    def MenuPic(self):##进入图片管理页面
        self.clickID(*self.MenuPic_loc)
        self.wait()
        self.logtext(*self.MenuPic_loc)
    def MenuConfig(self):##进入配置页面
        self.clickID(*self.MenuConfig_loc)
        self.wait()
        self.logtext(*self.MenuConfig_loc)
        self.driver.switch_to_frame('contentframe') ##检查这个元素是否在一个frame中，放在对象操作之前
        self.wait()
    """############     一级菜单               ####################################"""
    def aVideoCamera(self):#进入摄像机主菜单
        self.MenuConfig()
        self.wait()
        self.clickID(*self.aVideoCamera_loc)
        self.wait()
        self.logtext(*self.aVideoCamera_loc)
    def aBaseConfig(self): ##进入系统主菜单
        self.MenuConfig()
        self.wait()
        self.clickID(*self.aBaseConfig_loc)
        self.wait()
        self.logtext(*self.aBaseConfig_loc)
    """#############  抓拍  ############################"""
    def picpath(self):  ##获取图片默认路径win7
        self.picpathfile = linecache.getline(r'C:\Users\Public\Documents\IPCWeb\ipcweb.ini',13)
        #print self.picpathfile
        self.filedir = self.picpathfile
        self.localpicpath = self.filedir[13:-1]
        return self.localpicpath
    def movetodir(self,):  ##获取图片移动到路径
        #self.nowdir=os.path.split(os.getcwd())[0] 
        self.nowdir = os.path.abspath('..\log')  ##获取绝度路径
        return self.nowdir
    def movefile(self,value):
        now = datetime.datetime.now()
        nowprint=now.strftime('%Y%m%d%H%M%S') ##当前时间
        srcpath = self.picpath()
        dstpath = self.movetodir()       
        os.chdir(srcpath)
        files = os.listdir(".")
        for filename in files:
            li = os.path.splitext(filename)
            print li
            if li[1] == ".jpg":
                newname = str(nowprint)+"test"+value+li[1] 
                print newname
                os.rename(filename,newname)
                srcfilename = self.picpath()+'\\'+newname
                os.chdir(dstpath)
                print self.movetodir()
                shutil.move(srcfilename,self.movetodir())
    def snapshotpic(self,value):  ##抓拍图片操作
        self.value=value
        self.wait()
        self.MenuViewer()
        self.wait()
        self.driver.switch_to_frame('contentframe')   ##无法识别和点击按钮时添加contentframe
        self.driver.find_element_by_id('capture').click()
        self.wait()
        self.movefile(value)




    def aSecurity(self):#用户安全
        self.aBaseConfig()
        self.wait()
        self.driver.find_element_by_id('aSecurity').click()
        self.wait()
    def openssh(self):  ##打开ssh连接
        self.aSecurity()
        self.driver.find_element_by_id('MSafetyService').click()
        self.wait()
        self.driver.find_element_by_id('IsEnableSSH').click()
        self.wait()
        self.driver.find_element_by_id("SaveSafetyService").click()
        self.wait()
if __name__ == '__main__':
    ip = '10.255.248.207'
    username = 'admin'
    password = 'admin123'
    value="day"
    ipc=C_ipcpage()
    #ipc.loginIPC(ip, username, password)
    #ipc.snapshotpic()
    ipc.movefile(value)