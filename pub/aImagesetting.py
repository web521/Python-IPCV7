#coding=utf-8
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import time as t
from pub import PubAction
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" ) #存储中文日志是解决编码问题


class C_aImagsSetting(PubAction.C_ipcpage):
    def aImagsSettings(self):#进入图像子菜单
        self.aVideoCamera()
        self.wait()
        self.clickID(*self.aImagsSettings_loc)
        self.logtext(*self.aImagsSettings_loc)
    def lightnessh5(self):  ##图像调节菜单
        self.wait()
        try:
            self.aImagsSettings()
        except BaseException as msg:
            print msg
        
    def exposureh5(self): 
        self.wait()
        self.aImagsSettings()
        self.clickID(*self.exposureh5_loc)
        self.logtext(*self.exposureh5_loc)

    def ircutfilterh5(self):
        self.wait()
        self.aImagsSettings()
        self.wait()
        self.clickID(*self.ircutfilterh5_loc)
        self.wait()
        self.logtext(*self.ircutfilterh5_loc)

    def aVideo(self,R):#视频，R：码率
        self.MenuConfig_aVideoCamera()
        self.wait()
        self.clickID(*self.aVideo_loc)
        self.wait()
        self.find_element(*self.constantBitRate_loc)
        self.wait()
        self.find_element(*self.constantBitRate_loc).send_keys(Keys.CONTROL,'a')
        self.wait()
        self.find_element(*self.constantBitRate_loc).send_keys(R,Keys.ENTER)
        self.wait()
        self.clickID(*self.ConfigBtn_loc)
        self.wait()
if __name__ == "__main__":
    ip = '10.255.248.207'
    username = 'admin'
    password = 'admin123'
    ttt = PubAction.C_ipcpage()
    ttt.loginIPC(ip,username,password)
    print "ttt is ok"