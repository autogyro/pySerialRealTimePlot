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
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

import _const as const
from str_convert import *
from data_code import *

import wx
from matplotlib.figure import Figure
import matplotlib.font_manager as font_manager
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
# wxWidgets object ID for the timer
TIMER_ID = wx.NewId()
# number of data points
POINTS = 300
global data
y_lim = 1000


class PlotFigure(wx.Frame):
    """Matplotlib wxFrame with animation effect"""
    global data

    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY,
                          title="Serial Data Plot", size=(600, 400))
        # Matplotlib Figure
        self.fig = Figure((6, 4), 100)
        # bind the Figure to the backend specific canvas
        self.canvas = FigureCanvas(self, wx.ID_ANY, self.fig)
        # add a subplot
        self.ax = self.fig.add_subplot(111)
        # limit the X and Y axes dimensions
        self.ax.set_ylim([0, 100])
        self.ax.set_xlim([0, POINTS])

        self.ax.set_autoscale_on(False)
        self.ax.set_xticks([])
        # we want a tick every 10 point on Y (101 is to have 10
        self.ax.set_yticks(range(0, 101, 10))
        # disable autoscale, since we don't want the Axes to ad
        # draw a grid (it will be only for Y)
        self.ax.grid(True)
        # generates first "empty" plots
        self.user = [None] * POINTS
        self.l_user, = self.ax.plot(range(POINTS), self.user, label='Acc_X')

        # add the legend
        self.ax.legend(loc='upper center',
                           ncol=4,
                           prop=font_manager.FontProperties(size=10))
        # force a draw on the canvas()
        # trick to show the grid and the legend
        self.canvas.draw()
        # save the clean background - everything but the line
        # is drawn and saved in the pixel buffer background
        self.bg = self.canvas.copy_from_bbox(self.ax.bbox)
        # bind events coming from timer with id = TIMER_ID
        # to the onTimer callback function
        wx.EVT_TIMER(self, TIMER_ID, self.onTimer)

    def onTimer(self, evt):
        """callback function for timer events"""
        # restore the clean background, saved at the beginning
        self.canvas.restore_region(self.bg)
        # update the data
        # temp = np.random.randint(10, 80)
        temp = data
        self.user = self.user[1:] + [temp]
        # update the plot
        self.l_user.set_ydata(self.user)
        # just draw the "animated" objects
        # It is used to efficiently update Axes data (axis ticks, labels, etc
        # are not updated)
        self.ax.draw_artist(self.l_user)
        self.canvas.blit(self.ax.bbox)


    # def __del__(self):
    #     t.Stop()


'''
    thread ref
    serial_thread run time 0.0004s
    control the run time for real time in case missing data
'''


def serial_thread():
    global data

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

                data = receive_buff[0]
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
    frame = PlotFigure()
    t = wx.Timer(frame, TIMER_ID)
    t.Start(50)
    frame.Show()
    app.MainLoop()

    th.join()
