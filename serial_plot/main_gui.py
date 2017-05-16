# -*- coding: utf-8 -*-
"""
Created on Sun May 07 13:38:39 2017

@author: lee
"""

'''
    开发板和PC python serial通信协议

    const.HEAD = 0xAA
    const.TAIL = 0x55
    const.LEN = 3*5         # 接收数据长度，需要修改data_code.py文件中的对应变量
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

# import the newly created GUI file
import DebugGUI



class SerialGUI(DebugGUI.MainWindow):
    def __init__(self, parent, port, baudrate, p, r, y):
        DebugGUI.MainWindow.__init__(self, parent)

        # global var
        self.p = p
        self.r = r
        self.y = y

        # serial para
        self.ser = serial.Serial(timeout=1)  # open first serial port
        self.port = port
        self.baudrate = baudrate

    ############# serial ref #############
    def OpenSerial(self):
        self.ser.port = self.port
        self.ser.baudrate = self.baudrate
        self.ser.open()

    def CloseSerial(self):
        if(self.ser.isOpen()):
            self.ser.close()

    def DataDecode(self, p, r, y):
        len_receive = self.ser.inWaiting()
        if(len_receive):  # 接收处理
            raw_data = self.ser.read(len_receive)  # c语言字符类型
            receive_buff = decode(raw_data)

            if(receive_buff):
                print time.ctime()
                print receive_buff

                p[0] = receive_buff[0]
                r[0] = receive_buff[1]
                y[0] = receive_buff[2]

                # self.AttitudeShow(receive_buff)

    ############# gui event callback #############
    def OnOpenSerial(self, event):
        self.OpenSerial()
        self.SerialPort.SetValue(self.ser.portstr)# check which port was really used

    def OnCloseSerial(self, event):
        self.CloseSerial()             # close port

    def OnAboutSoftware(self, event):
        self.MenuAbout.ShowModal()
        self.MenuAbout.Destroy()

    def SerialDataDecodeThread(self):
        self.DataDecode(self.p, self.r, self.y)

    def IsSerialOpened(self):
        return self.ser.isOpen()

    def AttitudeShow(self, buff):
        self.Pitch.SetValue(str(buff[0]))
        self.Roll.SetValue(str(buff[1]))
        self.Yaw.SetValue(str(buff[2]))


global pitch
global roll
global yaw
pitch = [0]
roll = [0]
yaw = [0]



'''
    thread ref
    serial_thread run time 0.0004s
    control the run time for real time in case missing data
'''


def serial_thread():
    while True:
        if(serGUI.IsSerialOpened()):
            serGUI.SerialDataDecodeThread()
        time.sleep(0.001)

def attitude_show_thread():
    while True:
        global pitch
        global roll
        global yaw

        buff = []
        buff.append(pitch[0])
        buff.append(roll[0])
        buff.append(yaw[0])
        serGUI.AttitudeShow(buff)
        time.sleep(0.05)

####################################################
# mian loop
####################################################
threads = []
threads.append(threading.Thread(target=serial_thread, args=()))
threads.append(threading.Thread(target=attitude_show_thread, args=()))


if(__name__ == '__main__'):
    global pitch
    global roll
    global yaw
    global serGUI


    ############# gui #############
    app = wx.PySimpleApp()

    serGUI = SerialGUI(parent=None, port='/dev/ttyUSB0', baudrate=38400,
                       p=pitch, r=roll, y=yaw)
    serGUI.Show(True)

    PlotFigure('acc x', pitch).start()
    PlotFigure('acc y', roll).start()

    for th in threads:
        th.setDaemon(True)
        th.start()
    app.MainLoop()
    # th.join()
