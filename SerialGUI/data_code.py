# -*- coding: utf-8 -*-
"""
Created on Sun May 07 13:40:08 2017

@author: lee
"""

import ctypes
import binascii
import _const as const
from str_convert import *


# 接收报头报尾
const.HEAD = 0xAA
const.TAIL = 0x55
const.LEN = 4 * 3         # 接收数据长度，需要修改

# 接收状态机
const.RX_FREE = 0
const.RX_START = 1
const.RX_DATA = 2

'''
  接收数据解码
  input: ser.read()
  output: list[float]
'''


def static_vars(**kwargs):
    def decorate(func):
        for k in kwargs:
            setattr(func, k, kwargs[k])
        return func
    return decorate


# control the run time for real time in case missing data
@static_vars(pit=0, rx_state=const.RX_FREE, buff=(ctypes.c_char * const.LEN)())
def decode(receive_data_buff):
    for raw_data in receive_data_buff:
        data = binascii.b2a_hex(raw_data)  # 转换为16进制字符
        hex_data = int(data, 16)           # 转换为int型

        if(decode.rx_state == const.RX_FREE):  # 报头
            decode.pit = 0                    # 位置清零
            if(hex_data == const.HEAD):
                decode.rx_state = const.RX_START

        elif(decode.rx_state == const.RX_START):  # 接收数据长度并校核
            if(hex_data == const.LEN):
                decode.rx_state = const.RX_DATA
            else:
                decode.rx_state = const.RX_FREE  # 数据长度错误

        elif(decode.rx_state == const.RX_DATA):  # 接收数据
            if(decode.pit < const.LEN):
                decode.buff[decode.pit] = raw_data
                decode.pit += 1
            else:
                decode.rx_state = const.RX_FREE     # 先复位在返回
                if(hex_data == const.TAIL):           # 接收数据有效
                    return chars_buff_handler(decode.buff)  # 得到float数据


'''
  发送数据编码
  input : list[float]
  output: buff = (ctypes.c_char*(data_len*4+3))()
'''


def encode(float_data):
    data_len = len(float_data)
    pit = 2
    buff = (ctypes.c_char * (data_len * 4 + 3))()

    buff[0] = hex2cchar(str(const.HEAD).encode('ascii'))
    #buff[1] = hex2cchar()
    buff[data_len - 1] = str(const.TAIL)

    for f in float_data:
        #bf = (ctypes.c_char*4)()
        bf = float2cchar(f)
        for i in range(0, len(bf)):
            buff[pit] = bf[i]
            pit += 1
    return buff
