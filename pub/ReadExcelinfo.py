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
def getdata(value): 
    table = opensheet.sheet_by_name("testcases")
    test=table.row_values(1)
    data = test[3:-1]    
    print data
if __name__ =='__main__':
    getdata(1)