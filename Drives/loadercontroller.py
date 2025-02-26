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
# import tkinter as tk
# from tkinter import messagebox
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
        # 系统是否复位完成
        self.is_reset=False
        # 电机失能是否完成
        self.is_disenble=False
        # 通信串口基本配置
        self.serial = serial.Serial(port, 115200, timeout=0.01)
        self.crc8 = crcmod.predefined.mkPredefinedCrcFun("crc-8")
        time.sleep(2)
        # self.serial_pump = serial.Serial("COM5", 9600, timeout=0.5)
        # time.sleep(2)
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
                    self.get_busy_judge_x(accuracy=0.5)
                elif (local == "z"):
                    self.get_busy_judge_z(accuracy=0.5)
                elif (local == "y"):
                    self.get_busy_judge_y(accuracy=0.5)

    # 判断z是否到达预定位置
    def get_busy_judge_z(self, accuracy=0.5) -> int:
        # print("zinput={}\n".format(self.z_input))
        # print("ztarget={}\n".format(self.z_target))
        # print("local dz={}\n".format(np.abs(self.z_input - self.z_target)))
        if (np.abs(self.z_input - self.z_target) <= accuracy):
            # 若当前坐标和指定坐标的三轴误差都小于5mm，则判断就位
            self.is_busy = False

    # 判断x是否到达预定位置
    def get_busy_judge_x(self, accuracy=0.5) -> int:
        # print("xinput={}\n".format(self.x_input))
        # print("xtarget={}\n".format(self.x_target))
        # print("local dx={}\n".format(np.abs(self.x_input - self.x_target)))
        if (np.abs(self.x_input - self.x_target) <= accuracy):  # 若当前坐标和指定坐标的三轴误差都小于0.5mm，则判断就位
            self.is_busy = False

    # 判断y是否到达预定位置
    def get_busy_judge_y(self, accuracy=0.5) -> int:
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

    def set_delivery_abs_xz(self, x, z):
        self.x_target = x
        self.z_target = z
        self.send_cmd_frame(b"\xB1", struct.pack("<f", self.x_target))  # x轴
        self.send_cmd_frame(b"\xB2", struct.pack("<f", self.z_target))  # z轴
        self.wait_busy(local="x")
        self.wait_busy(local="z")

    # 复位及判断
    def reset_xyz(self):
        self.is_reset = False
        self.send_cmd_frame(b"\xB5", struct.pack("<f", self.reset_val))
        while not self.is_reset :
            time.sleep(0.005)

    # 电机失能及判断
    def scan_disenble_motor(self):
        self.is_disenble = False
        self.send_cmd_frame(b"\xB9", struct.pack("<f", self.reset_val))
        while not self.is_disenble :
            time.sleep(0.005)                

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
                    elif cmd_id == b"\xC3":  # y轴当前位置
                        self.y_input = struct.unpack("<f", rx_data[2:6])[0]
                    elif cmd_id == b"\xD1":  # 系统故障
                        self.is_warning = True
                        self.send_error.emit()
                    elif cmd_id == b"\xD2":  # 速度设置成功
                        self.is_speed = True
                    elif cmd_id == b"\xD3":  # 复位完成
                        self.is_reset = True
                    elif cmd_id == b"\xD4":  # 失能完成
                        self.is_disenble = True                        

    # 位置修正
    def Pos_correction(self, local):
        self.correct_value = -(self.x_input - self.x_target)  # 控制电机继续运行误差的值
        if (local == "x"):
            self.send_cmd_frame(b"\xB1", struct.pack("<f", self.correct_value))
        elif (local == "z"):
            self.send_cmd_frame(b"\xB2", struct.pack("<f", self.correct_value))
        elif (local == "y"):
            self.send_cmd_frame(b"\xB3", struct.pack("<f", self.correct_value))


    # RGB灯控制
    # rgb_data[1]=1 ，1号玻片仓
    # rgb_data[2]=1 ，红色...=2，绿色...=3，黄色
    def loader_rgb_ctrl(self):
        rgb_data = bytearray([0xAA, 0xB4, 0x01, 0x03, 0x00, 0x00,0x2F,0xFF])
        self.serial.flush()
        self.serial.write(rgb_data)


    #  以下为油泵控制代码*********************************************

    #  CRC16校验函数
    def crc16(self, data):
        # CRC16 计算逻辑
        crc = 0xFFFF
        for byte in data:
            crc ^= byte
            for _ in range(8):
                if crc & 0x0001:
                    crc = (crc >> 1) ^ 0xA001
                else:
                    crc >>= 1
        return crc.to_bytes(2, byteorder='little')  # 返回 2 字节的 CRC
    
    # 使能485通讯（上电后首先设置）
    # 数据帧： 0xC0 0x05 0x1004 0xFF00 0xD9EA
    def enable_rs485(self):
        tx_data = bytes([0xC0, 0x05, 0x10, 0x04, 0xFF, 0x00])
        crc_value = self.crc16(tx_data)  # 确保 crc16 返回的是字节类型
        self.serial_pump.flush()
        self.serial_pump.write(tx_data + crc_value)  # 发送完整数据
        print("485通讯已使能")        

    # 启动泵
    # 数据帧： 0xC0 0x05 0x1001 0xFF00 0xC9EB
    def pump_start(self):
        tx_data = bytes([0xC0, 0x05, 0x10, 0x01, 0xFF, 0x00])
        crc_value = self.crc16(tx_data)  # 确保 crc16 返回的是字节类型
        self.serial_pump.flush()
        self.serial_pump.write(tx_data + crc_value)  # 发送完整数据 
        print("泵已启动")        

    # 停止泵
    # 数据帧： 0xC0 0x05 0x1001 0x0000 0x881B
    def pump_stop(self):
        tx_data = bytes([0xC0, 0x05, 0x10, 0x01, 0x00, 0x00])
        crc_value = self.crc16(tx_data)  # 确保 crc16 返回的是字节类型
        self.serial_pump.flush()
        self.serial_pump.write(tx_data + crc_value)  # 发送完整数据
        print("泵已停止")        

    # 设定泵转速
    # 数据帧： 0xC0 0x10 0x3001 0x0002 0x04 0x42C80000(输入数据) 0x0B1B #速度100
    def pump_setup_speed(self, speed):
        # 将浮点数转换为 4 字节的字节串
        speed_data = struct.pack('>f', speed)  # 大端格式
        # 构建数据帧
        tx_data = bytearray([
            0xC0,   # 起始位
            0x10,   # 命令字
            0x30,   # 数据类型或功能代码
            0x01,   # 设备 ID 或其他标识
            0x00,   # 保留字段或其他参数
            0x02,   # 数据长度，这里是 4 字节
            0x04    # 其他字段
        ])
        tx_data.extend(speed_data)
        crc_value = self.crc16(tx_data)
        self.serial_pump.flush()
        self.serial_pump.write(tx_data + crc_value)  # 发送完整的数据帧
        print(f"泵转速设置为: {speed}")        


    # 设置4-20mA模拟量控制泵(力度)
    # 数据帧： 0xC0 0x05 0x1008 0xFF00 0x19E9
    def pump_set_simulation(self):
        tx_data = bytes([0xC0, 0x05, 0x10, 0x08, 0xFF, 0x00])
        crc_value = self.crc16(tx_data)  # 确保 crc16 返回的是字节类型
        self.serial_pump.flush()
        self.serial_pump.write(tx_data + crc_value)  # 发送完整数据
        print("模拟量控制泵已设置")        

    # 泵正转
    # 数据帧： 0xC0 0x05 0x1003 0x0000 0x29DB
    def pump_forward(self):
        tx_data = bytes([0xC0, 0x05, 0x10, 0x03, 0xFF, 0x00])
        crc_value = self.crc16(tx_data)  # 确保 crc16 返回的是字节类型
        self.serial_pump.flush()
        self.serial_pump.write(tx_data + crc_value)  # 发送完整数据
        print("泵正转")        

    # 泵反转
    # 数据帧： 0xC0 0x05 0x1003 0xFF00 0x682B
    def pump_reversal(self):
        tx_data = bytes([0xC0, 0x05, 0x10, 0x03, 0x00, 0x00])
        crc_value = self.crc16(tx_data)  # 确保 crc16 返回的是字节类型
        self.serial_pump.flush()
        self.serial_pump.write(tx_data + crc_value)  # 发送完整数据
        print("泵反转")        

    # 泵排空开始
    # 数据帧： 0xC0 0x05 0x1002 0x0000 0x781B
    def pump_emptyout_start(self):
        tx_data = bytes([0xC0, 0x05, 0x10, 0x02, 0xFF, 0x00])
        crc_value = self.crc16(tx_data)  # 确保 crc16 返回的是字节类型
        self.serial_pump.flush()
        self.serial_pump.write(tx_data + crc_value)  # 发送完整数据
        print("泵排空开始")        

    # 泵排空停止
    # 数据帧： 0xC0 0x05 0x1002 0xFF00 0x39EB
    def pump_emptyout_stop(self):
        tx_data = bytes([0xC0, 0x05, 0x10, 0x02, 0x00, 0x00])
        crc_value = self.crc16(tx_data)  # 确保 crc16 返回的是字节类型
        self.serial_pump.flush()
        self.serial_pump.write(tx_data + crc_value)  # 发送完整数据
        print("泵排空停止")        

    # 油泵实际测试代码
    def user_pump_test(self):
        self.pump_forward()     # 正转
        time.sleep(0.5)         # 延时500ms
        temp_data=self.serial_pump.read(8)
        print(temp_data)
        self.pump_start()       # 泵启动
        time.sleep(3)           # 泵运行2秒
        temp_data=self.serial_pump.read(8)
        print(temp_data)        
        self.pump_stop()        # 泵停止
        time.sleep(1)         # 泵停止500ms
        temp_data=self.serial_pump.read(8)
        print(temp_data)        
        self.pump_reversal()    # 泵反转
        time.sleep(0.5)         # 延时500ms
        temp_data=self.serial_pump.read(8)
        print(temp_data)        
        self.pump_start()       # 泵启动
        time.sleep(0.4)         # 泵运行1秒
        temp_data=self.serial_pump.read(8)
        print(temp_data)        
        self.pump_stop()        # 泵停止 
        temp_data=self.serial_pump.read(8)
        print(temp_data)        


    def receive_data(self):
        while True:
            print("pumpdata:{}".format())

    # 自检
    # def user_self_test(self):
    #     # 弹窗提示用户是否开始检测X轴
    #     result = messagebox.askquestion("提示", "是否开始检测x轴", icon='question')
    #     if result == 'no':  # 如果用户选择“否”，停止自检
    #         return
    #     else:  # 如果用户选择“是”
    #         result = messagebox.showinfo("提示", "x轴开始寻找起点", icon='info')
    #         self.set_delivery_abs_x(0)
    #         # self.status_label.config(text="状态：x轴已到达起点")
    #         result = messagebox.showinfo("提示", "x轴开始寻找终点", icon='info')
    #         self.set_delivery_abs_x(306)
    #         # self.status_label.config(text="状态：x轴已到达终点")
    #     result = messagebox.askquestion("提示", "x轴是否正常", icon='question')
    #     if result == 'no':  # 如果用户选择“否”，停止自检
    #         return
    #
    #     # 弹窗提示用户是否开始检测z轴
    #     result = messagebox.askquestion("提示", "是否开始检测z轴", icon='question')
    #     if result == 'no':  # 如果用户选择“否”，停止自检
    #         return
    #     else:  # 如果用户选择“是”
    #         result = messagebox.showinfo("提示", "z轴开始寻找起点", icon='info')
    #         self.set_delivery_abs_z(0)
    #         # self.status_label.config(text="状态：z轴已到达起点")
    #         result = messagebox.showinfo("提示", "z轴开始寻找终点", icon='info')
    #         self.set_delivery_abs_z(110)
    #         # self.status_label.config(text="状态：z轴已到达终点")
    #     result = messagebox.askquestion("提示", "z轴是否正常", icon='question')
    #     if result == 'no':  # 如果用户选择“否”，停止自检
    #         return

        #     # 弹窗提示用户是否开始检测y轴
        # result = messagebox.askquestion("提示", "是否开始检测y轴", icon='question')
        # if result == 'no':  # 如果用户选择“否”，停止自检
        #     return
        # else:  # 如果用户选择“是”，更新状态为“已经到达起点”
        #     result = messagebox.showinfo("提示", "y轴伸出", icon='info')
        #     self.set_delivery_abs_y(-93)
        #     # self.status_label.config(text="状态：y轴已完全伸出")
        #     result = messagebox.showinfo("提示", "y轴收回", icon='info')
        #     self.set_delivery_abs_y(-1)
        #     # self.status_label.config(text="状态：y轴已完全收回")
        # result = messagebox.askquestion("提示", "y轴是否正常", icon='question')
        # if result == 'no':  # 如果用户选择“否”，停止自检
        #     return

        #
        # ......
        #

        # 弹窗提示用户是否开始检测y轴
        # self.status_label.config(text="装载器自检已完成")

    def stop_reading(self):
        self.flag_run = False
        self.serial_thread.join()  # 等待线程结束

    # 关闭串口进程
    def ser_close(self):
        self.stop_reading()
        self.serial.close()
        # self.serial_pump.close()
