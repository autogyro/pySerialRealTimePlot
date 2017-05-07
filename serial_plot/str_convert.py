# -*- coding: utf-8 -*-
"""
Created on Sun May 07 13:41:11 2017

@author: lee
"""

'''
 各种字符转换
'''

import struct
import ctypes
import binascii


# class str_convert():

'''
    float和char之间转换
'''


class un_float_char (ctypes.Union):
    _fields_ = [
        ("fl", ctypes.c_float),
        ("ch", ctypes.c_char * 4)
    ]

# 返回的是str类型，可用str[]访问


def float_convert_char(_f):
    un_data = un_float_char()
    un_data.fl = ctypes.c_float(_f)
    return un_data.ch


def char_convert_float(_ch):
    un_data = un_float_char()
    un_data.ch = _ch
    return un_data.fl

# 接收数据str处理函数
# input:  buff = (ctypes.c_char*const.LEN)()
# output: list[float]


def chars_buff_handler(_buff):
    buff = []
    for i in range(0, _buff._length_, 4):
        # buff.append(char_convert_float(_buff.raw[i:i+4])) # 会有数据接收不对
        buff.append(cchar2float(_buff.raw[i:i + 4]))
    return buff


'''
    float和hex之间转换
'''


def cchar2hex(s):  # bytes to hex
    return binascii.b2a_hex(s)


def hex2float(h):
    return struct.unpack('f', h.decode('hex'))[0]


def cchar2float(s):  # 串口数据解码成 float
    return hex2float(cchar2hex(s))


def float2hex(f):
    return struct.pack("<f", f).encode('hex')


def hex2cchar(h):  # hex to bytes
    return binascii.a2b_hex(h)


def float2cchar(f):  # float 编码成串口发送
    return hex2cchar(float2hex(f))

#import sys
#sys.modules[__name__] = str_convert()
