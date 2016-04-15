#coding:utf-8
import xlrd
import os
import sys
dirpwd = os.path.abspath('..')
filename = r'%s\IPCV7testing\IPC_v7_message.xlsx' %dirpwd
opensheet = xlrd.open_workbook(filename)
ip_list = []
user_list = []
password_list = []
sshport_list = []
telnetport_list = []
daynight_list = []
light_list = []
contrast_list = []
saturation_list = []
sharpnes_list = []
exposureh5_list = []
GainMode_list = []
gainmax_list = []
IrisType_list = []
irislevel_list = []
ShuterMode_list = []
Shutermin_list = []
AntiFlickerMode_list = []
#处理
try:
    sheet = opensheet.sheet_by_name("message")
except:
    print ("no sheet in %s named message") %filename
nrows = sheet.nrows  #获取行数
ncols = sheet.ncols  #获取列数
for i in range(2,nrows): #行 循环
    ip_data = sheet.cell_value(i,2)
    ip_list.append(ip_data)
    #print (ip_data)
    #user_data = sheet.cell_value(i,3).value.encode('utf-8')
    user_data = sheet.cell_value(i,3)
    user_list.append(user_data)
    #print (user_data)
    password_data = sheet.cell_value(i,4)
    password_list.append(password_data)
    #print (password_data)
    sshport_data = sheet.cell_value(i,5)
    sshport_list.append(sshport_data)
    #print (sshport_list)
    telnetport_data = sheet.cell_value(i,6)
    telnetport_list.append(telnetport_data)
    #print (telnetport_list)
'''
try:
    table = opensheet.sheet_by_name("testcases")
except:
    print ("no sheet in %s named testcases") %filename
nrow2 = table.nrows  #获取行数
ncol2 = table.ncols  #获取列数
#print nrow2,ncol2
for n in range(2,ncol2):
    daynight_data = table.cell(1,n).value
    daynight_list.append(daynight_data)
    #print daynight_data
for n in range(3,ncol2):
    light_data=table.cell(2,n).value
    light_list.append(light_data)
'''
def getdata(value): 
    table = opensheet.sheet_by_name("testcases")
    test=table.row_values(value)
    data = test[3:-1]
    while ''  in data:
        data1=data.remove('' ) 
    return data
    #print data
    
daynight_list = getdata(1)
light_list = getdata(2)
contrast_list = getdata(3)
saturation_list = getdata(4)
sharpnes_list = getdata(5)
GainMode_list = getdata(6)
gainmax_list = getdata(7)
IrisType_list = getdata(8)
irislevel_list = getdata(9)
ShuterMode_list = getdata(10)
Shutermin_list = getdata(11)
AntiFlickerMode_list = getdata(12)
if __name__ =='__main__':
    print daynight_list
    print light_list
    print contrast_list
    print saturation_list
    print AntiFlickerMode_list
    print Shutermin_list 