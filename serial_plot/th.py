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

import threading
import time

import serial
import wx
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

import _const as const
from str_convert import *
from data_code import *
from data_plot import PlotFigure


global pitch
global roll
pitch = [0]
roll = [0]



'''
    thread ref
    serial_thread run time 0.0004s
    control the run time for real time in case missing data
'''


def serial_thread():
    global pitch
    global roll

    ser = serial.Serial('/dev/ttyUSB0', baudrate=38400,
                        timeout=1)  # open first serial port
    print ser.portstr       # check which port was really used

    while True:
        len_receive = ser.inWaiting()
        if(len_receive):  # 接收处理
            raw_data = ser.read(len_receive)  # c语言字符类型
            receive_buff = decode(raw_data)

            if(receive_buff):
                print time.ctime()
                print receive_buff

                pitch[0] = receive_buff[0]
                roll[0] = receive_buff[1]

        time.sleep(0.001)
    ser.close()             # close port


'''
  mian loop
'''
threads = []
threads.append(threading.Thread(target=serial_thread, args=()))

if(__name__ == '__main__'):
    for th in threads:
        th.setDaemon(True)
        th.start()

    app = wx.PySimpleApp()

    # class example
    global pitch
    global roll

    frame = PlotFigure('acc x', pitch)
    frame.start()

    frame_ = PlotFigure('acc y', roll)
    frame_.start()

    app.MainLoop()

    th.join()
