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

import sys  # 修改编码方式显示中文
reload(sys)
sys.setdefaultencoding('utf-8')

global flag_update
global receive_buff
global line

flag_update = False
receive_buff = []  # receive float data


'''
 plot figure
'''
fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
ax.grid()
xdata, ydata = [], []
plt.show(block=False)


def init():
    global line

    ax.set_ylim(-100, 100)
    ax.set_xlim(0, 100)
    del xdata[:]
    del ydata[:]
    line.set_data([], [])
    return line,


def update(i, buff, l):  # i frame must be the first arg
    xdata.append(i)
    ydata.append(buff[0])

    xmin, xmax = ax.get_xlim()  # update xlim and ylim
    if x_cnt >= xmax:
        ax.set_xlim(xmin + 50, xmax + 50)
        ax.figure.canvas.draw()
    l.set_data(xdata, ydata)
    print 'update'
    return l,


'''
    thread ref
    serial_thread run time 0.0004s
    control the run time for real time in case missing data
'''


def serial_thread():
    global receive_buff
    global flag_update

    ser = serial.Serial('/dev/ttyUSB0', baudrate=38400,
                        timeout=1)  # open first serial port
    print ser.portstr       # check which port was really used

    while True:
        len_receive = ser.inWaiting()
        if(len_receive):  # 接收处理
            raw_data = ser.read(len_receive)  # c语言字符类型
            receive_buff = decode(raw_data)

            if(receive_buff):
                flag_update = True
                print time.ctime()
                print receive_buff
        time.sleep(0.001)
    ser.close()             # close port


def data_plot_thread():
    global flag_update
    global receive_buff
    global line

    while True:
        if(flag_update):
            flag_update = False
            animation.FuncAnimation(fig, update, fargs=(receive_buff, line),
                                    init_func=init, blit=False, interval=5,
                                    repeat=False)
            print 'animation'
        time.sleep(0.01)


'''
  mian loop
'''
threads = []
threads.append(threading.Thread(target=serial_thread, args=()))
# threads.append(threading.Thread(target=data_plot_thread, args=()))

if(__name__ == '__main__'):
    for t in threads:
        t.setDaemon(True)
        t.start()
    t.join()
