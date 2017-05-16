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

import data_code
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

    def IsSerialOpened(self):
        return self.ser.isOpen()

    ############# gui event callback #############
    def ClearGUI(self):
        self.SerialPort.SetValue('')
        self.Yaw.SetValue('')
        self.Pitch.SetValue('')
        self.Roll.SetValue('')

    def OnOpenSerial(self, event):
        self.OpenSerial()
        # check which port was really used
        self.SerialPort.SetValue(self.ser.portstr)

    def OnCloseSerial(self, event):
        self.CloseSerial()             # close port
        self.ClearGUI()

    def OnAboutSoftware(self, event):
        dlg = wx.MessageDialog(self, 'A Serial Real Time Plot Debug Application Programmed by Python',
                               'About pySerial RT Plot', wx.OK)
        dlg.ShowModal()
        dlg.Destroy()

    def OnDebugProtocol(self, event):
        dlg = wx.MessageDialog(
            self, u'const.HEAD = 0xAAconst.TAIL = 0x55const.LEN = 3*5', wx.OK)
        dlg.ShowModal()
        dlg.Destroy()

        ############# gui update thread #############
    def SerialDataDecodeThread(self):
        len_receive = self.ser.inWaiting()
        if(len_receive):  # 接收处理
            raw_data = self.ser.read(len_receive)  # c语言字符类型
            receive_buff = data_code.decode(raw_data)

            if(receive_buff):
                print time.ctime()
                print receive_buff

                self.p[0] = receive_buff[0]
                self.r[0] = receive_buff[1]
                self.y[0] = receive_buff[2]

    def AttitudeShowThread(self, buff):
        self.Pitch.SetValue(str(buff[0]))
        self.Roll.SetValue(str(buff[1]))
        self.Yaw.SetValue(str(buff[2]))


global pitch
global roll
global yaw
pitch = [0]
roll = [0]
yaw = [0]


####################################################
# thread ref
# control the run time for real time in case missing data
####################################################


def serial_thread():
    while True:
        if(serGUI.IsSerialOpened()):
            serGUI.SerialDataDecodeThread()

        # serial_thread run time 0.0004s
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
        serGUI.AttitudeShowThread(buff)
        time.sleep(0.05)


####################################################
# main loop
####################################################

threads = []
threads.append(threading.Thread(target=serial_thread, args=()))
threads.append(threading.Thread(target=attitude_show_thread, args=()))


if(__name__ == '__main__'):
    global pitch
    global roll
    global yaw
    global serGUI

    ############# gui loop set #############
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
