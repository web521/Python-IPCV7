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
    def ircut_ver(self):
        cmd = ["cat /usr/config/ipccfg.conf|awk -F DayNightMode '{print $5}'|awk -F , '{print $1"" }'|awk -F : '{print $2}'"]
        val=self.verifyipc(cmd)
        val = str(val)
        return val
        print val
    def lightchange_ver(self):  ##读取配置文件亮度
        cmd = ["cat /usr/config/ipccfg.conf|awk -F Brightness '{print $4}'|awk -F , '{print $1}'|awk -F : '{print $2}'"]
        val=self.verifyipc(cmd)
        val=str(val)
        #y=type(val)
        #print "lightchange_ver+y:"
        #print y
        return val
    def contrast_ver(self):  ##读取配置文件对比度
        cmd = [ "cat /usr/config/ipccfg.conf|awk -F Contrast '{print $3}'|awk -F , '{print $1}'|awk -F : '{print $2}'"]
        val=self.verifyipc(cmd)
        val=str(val)
        #y=type(val)
        #print "lightchange_ver+y:"
        #print y
        return val
    def saturation_ver(self):  ##读取配置文件饱和度
        cmd = ["cat /usr/config/ipccfg.conf|awk -F Saturation '{print $3}'|awk -F , '{print $1}'|awk -F : '{print $2}'"]
        val=self.verifyipc(cmd)
        val=str(val)
        #y=type(val)
        #print "lightchange_ver+y:"
        #print y
        return val
    def sharpness_ver(self):  ##读取配置文件锐度
        cmd = ["cat /usr/config/ipccfg.conf|awk -F Sharpness '{print $3}'|awk -F , '{print $1}'|awk -F : '{print $2}'"]
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




