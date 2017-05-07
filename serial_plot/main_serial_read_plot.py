# -*- coding: utf-8 -*-
"""
Created on Sun May 07 13:38:39 2017

@author: lee
"""

'''
    开发板和PC python serial通信协议

    const.HEAD = 0xAA
    const.TAIL = 0x55
    const.LEN = 4*5         # 接收数据长度，需要修改data_code.py文件中的对应变量
'''

import serial  
import time
import numpy as np
import matplotlib.pyplot as plt

import _const as const
from str_convert  import * 
from data_code import *

# 修改编码方式显示中文
import sys 
reload(sys) 
sys.setdefaultencoding('utf-8') 


'''
  串口读操作
  //AA 08 00 00 A0 40 CD CC CC 3D 55 
'''
ser = serial.Serial('COM27',baudrate=38400,timeout=1)  # open first serial port  
print ser.portstr       # check which port was really used  



'''
 串口数据处理循环
'''

x_cnt = 0  #计数。然x轴能到了初始状态的最大值能进行改变
xlim_delt = 50
y = []

plt.ion()  #  开启matplotlib的交互模式
plt.xlim(0,xlim_delt)  #首先得设置一个x轴的区间 这个是必须的
plt.ylim(-1000,1000) # y轴区间 

while True:
    if(ser.inWaiting()): # 接收处理
        raw_data = ser.read() # c语言字符类型
        receive_buff = decode(raw_data)

        if(receive_buff):
            print time.ctime()
            print receive_buff
            
            y.append(receive_buff[0])
            x_cnt += 1
            if(x_cnt>xlim_delt):
                plt.xlim(x_cnt-xlim_delt,x_cnt) #  如果当前坐标x已经超过了50，将x的轴的范围右移。
            plt.plot(y) # 将list传入plot画图
            plt.pause(0.001)
        

plt.ioff()
ser.close()             # close port 

