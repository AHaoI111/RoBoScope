# -*- encoding: utf-8 -*-
'''
@Description:
1.上位机对应的处理程序
@File    :   loadercontroller.py
@Time    :   2024/09/05 10:38:46
@Author  :   He qing xin
@Version :   2.0
'''
import threading

from PySide6 import QtCore, QtGui, QtWidgets
import crcmod
import time
import serial
import struct
import queue
import numpy as np
from threading import Thread

from PySide6 import QtCore
from PySide6.QtCore import Signal


# 指示灯颜色类
class Color(object):
    red = b"\x01"
    green = b"\x10"
    yellow = b"\x11"


# 按键状态类
class Key(object):
    none = b"\x00"
    pressed = b"\x01"
    released = b"\x02"


# 显微镜基本控制类
class LoaderController(QtCore.QObject):
    send_error = Signal()

    def __init__(self, port):
        super().__init__()
        # xyz轴当前实际所处位置和y轴限位开关的状态
        self.x_input = 0.0
        self.z_input = 0.0
        self.y_input = 0.0
        # 用户从上位机输入的XYZ轴即将运动到的位置
        self.x_target = 0.0
        self.z_target = 0.0
        self.y_target = 0.0
        self.reset_val = 0.0
        # xyz轴速度
        self.x_speed = 0.0
        self.z_speed = 0.0
        self.y_speed = 0.0
        self.is_speed = False
        # 修正的位置误差值
        self.correct_value = 0.0
        # 机械轴是否正在工作
        self.is_busy = True
        # 系统是否有警告
        self.is_warning = False
        # 通信串口基本配置
        self.serial = serial.Serial(port, 115200, timeout=0.01)
        self.crc8 = crcmod.predefined.mkPredefinedCrcFun("crc-8")
        time.sleep(2)
        self.serial_thread = Thread(target=self.read_msg)
        self.serial_thread.start()
        self.flag_run = True


        self.queue = queue.PriorityQueue()
        self.key = [Key.none, Key.none, Key.none, Key.none]
        self.led = [Color.red, Color.red, Color.red, Color.red]

    # 上位机串口发送数据帧功能函数(b"\xB3", struct.pack("<f", y))
    def send_cmd_frame(self, cmd_id, data):
        # AA B3 data CRC FF
        tx_data = b"\xAA" + cmd_id + data
        self.serial.flush()
        self.serial.write(tx_data + self.crc8(tx_data).to_bytes(1, 'big') + b"\xFF")

    # 机械轴正在工作函数处理
    def wait_busy(self, local):
        self.is_busy = True
        temp_busy_time = 0
        while self.is_busy:
            time.sleep(0.1)  # 延时100ms
            temp_busy_time += 1
            if (temp_busy_time % 5 == 0):  # 每500ms进行一次位置判定
                # 以精度0.5mm进行判断是否已经到达指定位置，若是则退出循环
                # x轴和z轴使用该busy函数，用于是否已经到达位置，避免错过busy单脉冲信号
                if (local == "x"):
                    self.get_busy_judge_x(accuracy=0.1)
                elif (local == "z"):
                    self.get_busy_judge_z(accuracy=0.1)
                elif (local == "y"):
                    self.get_busy_judge_y(accuracy=0.1)

    # 判断z是否到达预定位置
    def get_busy_judge_z(self, accuracy=0.1) -> int:
        # print("zinput={}\n".format(self.z_input))
        # print("ztarget={}\n".format(self.z_target))
        # print("local dz={}\n".format(np.abs(self.z_input - self.z_target)))
        if (np.abs(self.z_input - self.z_target) <= accuracy):
            # 若当前坐标和指定坐标的三轴误差都小于5mm，则判断就位
            self.is_busy = False

    # 判断x是否到达预定位置
    def get_busy_judge_x(self, accuracy=0.1) -> int:
        # print("xinput={}\n".format(self.x_input))
        # print("xtarget={}\n".format(self.x_target))
        # print("local dx={}\n".format(np.abs(self.x_input - self.x_target)))
        if (np.abs(self.x_input - self.x_target) <= accuracy):  # 若当前坐标和指定坐标的三轴误差都小于0.5mm，则判断就位
            self.is_busy = False

    # 判断y是否到达预定位置
    def get_busy_judge_y(self, accuracy=0.1) -> int:
        # print("yinput={}\n".format(self.y_input))
        # print("ytarget={}\n".format(self.y_target))
        # print("local dy={}\n".format(np.abs(self.y_input - self.y_target)))
        if (np.abs(self.y_input - self.y_target) <= accuracy):
            self.is_busy = False

    # 控制x轴运动距离
    def update_delivery_x(self):
        self.send_cmd_frame(b"\xB1", struct.pack("<f", self.x_target))
        self.wait_busy(local="x")

    # 控制z轴运动距离
    def update_delivery_z(self):
        self.send_cmd_frame(b"\xB2", struct.pack("<f", self.z_target))
        self.wait_busy(local="z")

    # 控制y轴运动距离
    def update_delivery_y(self):
        self.send_cmd_frame(b"\xB3", struct.pack("<f", self.y_target))
        self.wait_busy(local="y")

    # 控制x轴移动绝对距离
    def set_delivery_abs_x(self, x):
        self.x_target = x
        self.update_delivery_x()

    # 控制z轴移动绝对距离
    def set_delivery_abs_z(self, z):
        self.z_target = z
        self.update_delivery_z()

    # 控制y轴移动绝对距离
    def set_delivery_abs_y(self, y):
        self.y_target = y
        self.update_delivery_y()

    # 设置x轴速度    
    def setup_speed_x(self, xs):
        self.x_speed = xs
        self.is_speed = False
        self.send_cmd_frame(b"\xB6", struct.pack("<f", self.x_speed))

    # 设置z轴速度    
    def setup_speed_z(self, zs):
        self.x_speed = zs
        self.is_speed = False
        self.send_cmd_frame(b"\xB7", struct.pack("<f", self.z_speed))

    # 设置y轴速度    
    def setup_speed_y(self, ys):
        self.x_speed = ys
        self.is_speed = False
        self.send_cmd_frame(b"\xB8", struct.pack("<f", self.y_speed))

        # 控制xz轴同时运动绝对距离

    def set_delivery_abs_point(self, x, z):
        self.x_target = x
        self.z_target = z
        self.send_cmd_frame(b"\xB1", struct.pack("<f", self.x_target))  # x轴
        self.send_cmd_frame(b"\xB2", struct.pack("<f", self.z_target))  # z轴
        self.wait_busy(local="x")
        self.wait_busy(local="z")

    # 复位
    def reset_xyz(self):
        self.send_cmd_frame(b"\xB5", struct.pack("<f", self.reset_val))

    # 控制指示灯的颜色
    def set_led_color(self, led):
        self.send_cmd_frame(b"\xB4", led[0] + led[1] + led[2] + led[3])

    # 读取并处理下位机串口通信发送过来的数据
    def read_msg(self):
        self.flag_run = True
        while self.flag_run:
            if self.serial.read() == b"\xAA":
                rx_data = b"\xAA" + self.serial.read(7)
                # 校验通过
                if rx_data[6] == self.crc8(rx_data[0:6]) and rx_data[7].to_bytes(1, byteorder='big') == b"\xFF":
                    cmd_id = rx_data[1].to_bytes(1, byteorder='big')
                    if cmd_id == b"\xC0":
                        print(rx_data[2])
                    elif cmd_id == b"\xC1":  # x轴当前位置
                        self.x_input = struct.unpack("<f", rx_data[2:6])[0]
                    elif cmd_id == b"\xC2":  # z轴当前位置
                        self.z_input = struct.unpack("<f", rx_data[2:6])[0]
                    elif cmd_id == b"\xC4":  # 按键状态
                        self.key = struct.unpack("<cccc", rx_data[2:6])
                        for i in range(0, 4):
                            if self.key[i] == Key.pressed:
                                if i == 0:
                                    self.queue.put((1, 0))
                                else:
                                    self.queue.put((2, i))
                                self.led[i] = Color.red
                            elif self.key[i] == Key.released:
                                self.led[i] = Color.red
                        self.set_led_color(self.led[0:4])
                    elif cmd_id == b"\xC5":  # y轴当前位置
                        self.y_input = struct.unpack("<f", rx_data[2:6])[0]
                    elif cmd_id == b"\xD1":  # 系统故障
                        self.is_warning = True
                        self.send_error.emit()
                    elif cmd_id == b"\xD2":  # 速度设置成功
                        self.is_speed = True

                        # 位置误差修正

    def Pos_correction(self, local):
        self.correct_value = -(self.x_input - self.x_target)  # 控制电机继续运行误差的值
        if (local == "x"):
            self.send_cmd_frame(b"\xB1", struct.pack("<f", self.correct_value))
        elif (local == "z"):
            self.send_cmd_frame(b"\xB2", struct.pack("<f", self.correct_value))
        elif (local == "y"):
            self.send_cmd_frame(b"\xB3", struct.pack("<f", self.correct_value))

    def stop_reading(self):
        self.flag_run = False
        self.serial_thread.join()  # 等待线程结束

    # 关闭串口进程
    def ser_close(self):
        self.stop_reading()
        self.serial.close()
