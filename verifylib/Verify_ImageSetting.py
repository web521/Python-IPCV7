# coding=utf-8
#_author_='wuweibin'
#_time_='2016/4/13'
import paramiko
import time
import datetime
from pub import ReadExcelinfo
from __builtin__ import str
username = ReadExcelinfo.user_data
passwd = ReadExcelinfo.password_data
ip = ReadExcelinfo.ip_data

class C_Imagesetting_ver():
    def verifyipc(self,cmd):
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(ip,22,username,passwd,timeout=5)
        for m in cmd:
            stdin, stdout, stderr = self.ssh.exec_command(m)
            out = stdout.readlines()
            x=type(out)
            #print 'sshout:'
            #print x
            for o in out:
                ver = o
        return ver
        self.ssh.close()
    def ircut_ver(self):   ##读取配置文件--->日夜模式值
        cmd = ["cat /usr/config/ipccfg.conf|awk -F DayNightMode '{print $5}'|awk -F , '{print $1"" }'|awk -F : '{print $2}'"]
        val=self.verifyipc(cmd)
        val = str(val)
        return val
        print val
    def lightchange_ver(self):  ##读取配置文件--->亮度
        cmd = ["cat /usr/config/ipccfg.conf|awk -F Brightness '{print $4}'|awk -F , '{print $1}'|awk -F : '{print $2}'"]
        val=self.verifyipc(cmd)
        val=str(val)
        return val
    def contrast_ver(self):  ##读取配置文件--->对比度
        cmd = [ "cat /usr/config/ipccfg.conf|awk -F Contrast '{print $3}'|awk -F , '{print $1}'|awk -F : '{print $2}'"]
        val=self.verifyipc(cmd)
        val=str(val)
        return val
    def saturation_ver(self):  ##读取配置文件--->饱和度
        cmd = ["cat /usr/config/ipccfg.conf|awk -F Saturation '{print $3}'|awk -F , '{print $1}'|awk -F : '{print $2}'"]
        val=self.verifyipc(cmd)
        val=str(val)
        return val
    def sharpness_ver(self):  ##读取配置文件--->锐度
        cmd = ["cat /usr/config/ipccfg.conf|awk -F Sharpness '{print $3}'|awk -F , '{print $1}'|awk -F : '{print $2}'"]
        val=self.verifyipc(cmd)
        val=str(val)
        return val
    def GainMode_ver(self): ##读取配置文件--->曝光---增益模式  auto 1，manual 0
        cmd = ["cat /usr/config/ipccfg.conf|awk -F GainMode '{print $3}'|awk -F , '{print $1}'|awk -F : '{print $2}'"]
        val=self.verifyipc(cmd)
        val=str(val)
        return val
    def gainmax_value_ver(self): ##读取配置文件--->曝光---增益上限（自动 ）
        cmd = ["cat /usr/config/ipccfg.conf|awk -F GainMax '{print $3}'|awk -F , '{print $1}'|awk -F : '{print $2}'"]
        val=self.verifyipc(cmd)
        val=str(val)
        return val    
    def gainlevel_value_ver(self): ##读取配置文件--->曝光---增益等级（手动）
        cmd = ["cat /usr/config/ipccfg.conf|awk -F GainLevel '{print $3}'|awk -F , '{print $1}'|awk -F : '{print $2}'"]
        val=self.verifyipc(cmd)
        val=str(val)
        return val
    def IrisType_ver(self): ##读取配置文件--->曝光--光圈模式 （DC-IRIS自动dc_irisauto  1；DC-IRIS手动dc_irismanual 0；P-IRIS手动p_irismanual  2）   
        cmd = ["cat /usr/config/ipccfg.conf|awk -F IrisMode '{print $3}'|awk -F , '{print $1}'|awk -F : '{print $2}'"]
        val=self.verifyipc(cmd)
        val=str(val)
        return val
    def irislevel_value_ver(self): ##读取配置文件--->曝光--光圈灵敏度 （DC-IRIS自动模式）   
        cmd = ["cat /usr/config/ipccfg.conf|awk -F IrisSensitivety '{print $3}'|awk -F , '{print $1}'|awk -F : '{print $2}'"]
        val=self.verifyipc(cmd)
        val=str(val)
        return val    
    def irissize_value_ver(self): ##读取配置文件--->曝光--光圈大小 （DC-IRIS手动模式）   
        cmd = ["cat /usr/config/ipccfg.conf|awk -F IrisLevel '{print $3}'|awk -F , '{print $1}'|awk -F : '{print $2}'"]
        val=self.verifyipc(cmd)
        val=str(val)
        return val  
    def ShuterMode_ver(self): ##读取配置文件--->曝光---快门模式（auto 1；manual 0）
        cmd = ["cat /usr/config/ipccfg.conf|awk -F ShutterMode '{print $3}'|awk -F , '{print $1}'|awk -F : '{print $2}'"]
        val=self.verifyipc(cmd)
        val=str(val)
        return val
    #def Shutermin_ver(self): ##读取配置文件--->曝光---快门下限（快门自动模式）
        cmd = ["cat /usr/config/ipccfg.conf|awk -F ShutterMin '{print $3}'|awk -F , '{print $1}'|awk -F : '{print $2}'"]
        val=self.verifyipc(cmd)
        val=str(val)
        #y=type(val)
        #print "lightchange_ver+y:"
        #print y
        return val
    #def Shutterlevel_ver(self): ##读取配置文件--->曝光---快门模式（快门手动模式）
        cmd = ["cat /usr/config/ipccfg.conf|awk -F ShutterTime '{print $3}'|awk -F , '{print $1}'|awk -F : '{print $2}'"]
        val=self.verifyipc(cmd)
        val=str(val)
        #y=type(val)
        #print "lightchange_ver+y:"
        #print y
        return val
    def AntiFlickerMode_ver(self): ##读取配置文件--->曝光---防闪烁（50Hz 0；60Hz 1，自然光 2）
        cmd = ["cat /usr/config/ipccfg.conf|awk -F FrequencyMode '{print $3}'|awk -F , '{print $1}'|awk -F : '{print $2}'"]
        val=self.verifyipc(cmd)
        val=str(val)
        #y=type(val)
        #print "lightchange_ver+y:"
        #print y
        return val
    
if __name__=='__main__':
    test=C_Imagesetting_ver()
    xxx=test.lightchange_ver()
    yyy = test.ircut_ver()
    print 'xxx:'
    print xxx
    print yyy




