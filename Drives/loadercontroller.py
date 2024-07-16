# -*- encoding: utf-8 -*-
'''
@Description:
1.上位机对应的处理程序
@File    :   loadercontroller.py
@Time    :   2024/05/21 20:12:46
@Author  :   Ma Yuqi
@Version :   1.0
'''

import crcmod
import time
import serial
import struct
import queue
import numpy as np
from threading import Thread


class Color(object):
    red = b"\x01"
    green = b"\x10"
    yellow = b"\x11"


class Key(object):
    none = b"\x00"
    pressed = b"\x01"
    released = b"\x02"


class LoaderController(object):
    def __init__(self, port):
        self.x_input = 0.0
        self.z_input = 0.0
        self.y_input = 0.0
        self.sw_input = 0.0

        self.x_target = 0.0
        self.z_target = 0.0
        self.y_target = 0.0

        self.is_busy = True
        self.delivery_reach = False
        self.loader_reach = False

        self.serial = serial.Serial(port, 115200, timeout=0.01)
        self.crc8 = crcmod.predefined.mkPredefinedCrcFun("crc-8")
        time.sleep(2)
        self.serial_thread = Thread(target=self.read_msg)
        self.serial_thread.start()

        self.queue = queue.PriorityQueue()
        self.key = [Key.none, Key.none, Key.none, Key.none]
        self.led = [Color.red, Color.red, Color.red, Color.red]
        self.flag = True
        # self.set_led_color(self.led)

    # (b"\xB3", struct.pack("<f", y))
    def send_cmd_frame(self, cmd_id, data):
        # AA B3 data CRC FF
        tx_data = b"\xAA" + cmd_id + data
        self.serial.flush()
        self.serial.write(tx_data + self.crc8(tx_data).to_bytes(1, 'big') + b"\xFF")

    def wait_busy(self, local="x"):
        self.is_busy = True
        temp_busy_time = 0
        temp_judge = 0
        t0 = time.time()
        while self.is_busy:
            time.sleep(0.1)
            temp_busy_time += 1
            if (temp_busy_time % 10 == 0):
                # print("waiting has been {} s".format(np.round(temp_busy_time / 10, 1)))
                # 以精度5 mm进行判断是否已经到达指定位置，若是则退出循环
                # x轴和z轴使用该busy函数，用于是否已经到达位置，避免错过busy单脉冲信号
                if (local == "x"):
                    self.get_busy_judge_x(accuracy=0.5)
                elif (local == "z"):
                    self.get_busy_judge_z(accuracy=0.5)
                else:
                    print("error check local x or z")
            if (temp_busy_time >= 100):
                temp_busy_time = 0
            if time.time() - t0 > 10:
                temp_judge = -1
                return temp_judge
        self.is_busy = True
        return temp_judge

    def wait_busy_y(self):
        self.is_busy = True
        temp_busy_time = 0
        temp_judge = 0
        while (self.is_busy) or (temp_judge == 0):
            time.sleep(0.1)
            temp_busy_time += 1
            if (temp_busy_time % 10 == 0):
                # print("waiting has been {} s".format(np.round(temp_busy_time/10,1)))
                # print("Local y is {}\n And local sw is {}".format(self.y_input,self.sw_input))
                temp_judge = self.get_busy_judge_y(accuracy=10.0)
                # 0 移动中
                if (temp_judge == 0):
                    pass
                # 1 移动完成，到达目标位置（自动清除busy位）
                elif (temp_judge == 1):
                    pass
                # -1 中途堵塞，提前返回-1
                elif (temp_judge == -1):
                    return -1
            if (temp_busy_time >= 1000):
                temp_busy_time = 0
        self.is_busy = True
        return temp_judge

    # 判断x是否到达预定位置
    def get_busy_judge_z(self, accuracy=0.5) -> int:
        # print("local dz={}\n".format(np.abs(self.z_input - self.z_target)))
        if (np.abs(self.z_input - self.z_target) <= accuracy):
            # 若当前坐标和指定坐标的三轴误差都小于5mm，则判断就位
            self.is_busy = False

    # 判断z是否到达预定位置
    def get_busy_judge_x(self, accuracy=0.5) -> int:
        # print("local dx={}\n".format(np.abs(self.x_input - self.x_target)))
        if (np.abs(self.x_input - self.x_target) <= accuracy):
            # 若当前坐标和指定坐标的三轴误差都小于5mm，则判断就位
            self.is_busy = False

    # 判断y是否到达预定位置
    # 0 移动中
    # -1 移动完毕，堵塞在中途
    # 1 移动完毕，成功到达目标位置
    def get_busy_judge_y(self, accuracy=10.0) -> int:
        # 是否转动了指定圈数
        # print("local dy={}\n".format(np.abs(self.y_input - self.y_target)))
        if (np.abs(self.y_input - self.y_target) <= accuracy):
            # 若转动了指定圈数，且触发了限位开关，则成功到达目标位置，并自动退出busy状态
            if (self.sw_input == 1):
                self.is_busy = False
                # print("清空标志位")
                return 1
            elif (self.sw_input == 0):
                # 若转动了指定圈数，并没有触发限位开关，则在中途堵塞
                # 打印堵塞提示
                print("blocking, please check out error!")
                return -1
        else:
            return 0

    def update_delivery_x(self):
        self.send_cmd_frame(b"\xB1", struct.pack("<f", self.x_target))
        temp = self.wait_busy(local="x")
        # print("x reached at {}\n".format(self.x_input))
        return temp

    def update_delivery_z(self):
        self.send_cmd_frame(b"\xB2", struct.pack("<f", self.z_target))
        temp = self.wait_busy(local="z")
        # print("z reached at {}\n".format(self.z_input))
        return temp

    def set_delivery_abs_x(self, x):
        self.x_target = x
        temp = self.update_delivery_x()
        return temp

    def set_delivery_abs_z(self, z):
        self.z_target = z
        temp = self.update_delivery_z()
        return temp

    def set_delivery_rev_x(self, x):
        self.x_target += x
        self.update_delivery_x()

    def set_delivery_rev_z(self, z):
        self.z_target += z
        self.update_delivery_z()

    def set_delivery_abs_point(self, x, z):
        self.set_delivery_abs_x(x)
        self.set_delivery_abs_z(z)

    def set_delivery_rev_point(self, x, z):
        self.set_delivery_rev_x(x)
        self.set_delivery_rev_z(z)

    def set_loader_abs_y(self, y):
        # 赋予目标值为y
        self.y_target = y
        self.send_cmd_frame(b"\xB3", struct.pack("<f", y))
        # busy_time 判断阈值时间，s
        temp = self.wait_busy_y()
        # print("y reached and state is temp_judge = {}\n".format(temp))
        # 返回的temp有三个状态
        # 0     移动中（不会收到这个值） 
        # -1    中途阻塞 
        # 1     到达预定位置
        return temp

    def set_loader_clear_y(self):
        self.y_target = 0
        self.send_cmd_frame(b"\xED", struct.pack("<f", 0))

    def set_led_color(self, led):
        # print(led)
        self.send_cmd_frame(b"\xB4", led[0] + led[1] + led[2] + led[3])

    def set_delivery_unit_convert_x(self, x):
        self.send_cmd_frame(b"\xD1", struct.pack("<f", x))

    def set_delivery_unit_convert_z(self, z):
        self.send_cmd_frame(b"\xD2", struct.pack("<f", z))

    def set_loader_unit_convert_y(self, y):
        self.send_cmd_frame(b"\xD3", struct.pack("<f", y))

    def read_msg(self):
        # byte 0 start 0xAA
        # byte 1 cmd id(delivery/loader/key)
        #
        # is busy: 0xC1
        # byte 2 is busy
        #
        # key: 0xC4
        # byte 2 key0
        # byte 3 key1
        # byte 4 key2
        # byte 5 key3
        while self.flag:
            if self.serial.read() == b"\xAA":
                rx_data = b"\xAA" + self.serial.read(7)
                # 校验通过
                if rx_data[6] == self.crc8(rx_data[0:6]) and rx_data[7].to_bytes(1, byteorder='big') == b"\xFF":
                    cmd_id = rx_data[1].to_bytes(1, byteorder='big')
                    if cmd_id == b"\xC0":
                        print(rx_data[2])
                        # 执行递出指令后，等待直到接收到非忙碌判断
                        # is_busy
                        # AA C0 00 XX XX XX CRC FF
                        # if rx_data[2].to_bytes(1, byteorder='big') == b"\x00":
                        #     self.is_busy = False
                    # 获得当前的x,y,z位置
                    elif cmd_id == b"\xC1":
                        self.x_input = struct.unpack("<f", rx_data[2:6])[0]
                    elif cmd_id == b"\xC2":
                        self.z_input = struct.unpack("<f", rx_data[2:6])[0]
                    elif cmd_id == b"\xC3":
                        self.y_input = struct.unpack("<f", rx_data[2:6])[0]
                    elif cmd_id == b"\xC4":
                        self.key = struct.unpack("<cccc", rx_data[2:6])
                        # print(self.key)
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
                        # if(motor.get_sw_Pos()==0){tx_data[1] = 0xC5;}
                    # else{tx_data[1] = 0xC6;}
                    # 同时获取sw和y的值，尽可能避免错位
                    elif cmd_id == b"\xC5":
                        self.sw_input = 0
                        self.y_input = struct.unpack("<f", rx_data[2:6])[0]
                    elif cmd_id == b"\xC6":
                        self.sw_input = 1
                        self.y_input = struct.unpack("<f", rx_data[2:6])[0]

            # print(self.serial.read().decode("utf-8"))

    def take_slide(self, y_push, z_lift):
        self.set_loader_abs_y(y_push)  # 执行机构伸出
        self.set_delivery_rev_z(-z_lift)  # 向上
        self.set_loader_abs_y(-1.0)  # 执行机构收回

    def give_slide(self, y_push, z_lift):
        self.set_loader_abs_y(y_push)  # 执行机构伸出
        self.set_delivery_rev_z(z_lift)  # 向下
        self.set_loader_abs_y(-1.0)  # 执行机构收回

    def reset(self):
        tempflage = self.set_loader_abs_y(-1)
        self.set_loader_clear_y()
        self.set_delivery_abs_point(200.0, 0.0)
        self.is_busy = False

    def close(self):
        self.flag = False
        self.serial_thread.join()
        self.serial.close()


class MainController(object):
    def __init__(self, loader_controller):
        self.loader = loader_controller

        # 310.3
        self.x_start = 160.3  # 载玻片仓X原点
        self.z_start = 120.5  # 载玻片仓Z原点

        self.x_gap = 50.0  # 载玻片仓X间隔
        self.z_gap = 4.0  # 载玻片仓Z间隔

        self.x_end = 31.0  # 载物台X位置
        self.z_end = 113.0  # 载物台Z位置

        self.y_push_start = 500.0  # 载玻片仓推杆行程
        self.y_push_end = 500.0  # 显微镜推杆行程
        self.z_lift = 4.0  # 抬升行程

    def start_loader(self, num):
        self.loader.led[num] = Color.yellow  # 开始装载，亮黄灯
        self.loader.set_led_color(self.loader.led[0:4])
        self.loader.set_delivery_abs_point(self.x_start + self.x_gap * num,
                                           self.z_start)  # 移到最底层
        for i in range(25):
            self.loader.take_slide(self.y_push_start, self.z_lift)  # 从装载仓取出
            self.loader.set_delivery_abs_point(self.x_end, self.z_end)  # 运送到载物台
            self.loader.give_slide(self.y_push_end, self.z_lift)  # 放入载物台
            # 等待扫描
            time.sleep(1)
            self.loader.take_slide(self.y_push_end, self.z_lift)  # 从载物台取出
            self.loader.set_delivery_abs_point(self.x_start + self.x_gap * num,
                                               self.z_start - self.z_lift - self.z_gap * i)  # 移到下层
            self.loader.give_slide(self.y_push_start, self.z_lift)  # 放入装载仓
            self.loader.set_delivery_abs_point(self.x_start + self.x_gap * num,
                                               self.z_start - self.z_gap * (i + 1))  # 移到上层
        self.loader.set_loader_abs_y(400.0)  # 将最后一片推出
        self.loader.set_loader_abs_y(-1.0)
        self.loader.led[num] = Color.green  # 完成装载，亮绿灯
        self.loader.set_led_color(self.loader.led[0:4])

    def select_loader(self):
        self.loader.set_delivery_abs_x(x=160.3)
        # self.loader.set_loader_abs_y(-500.0)
        # self.loader.set_delivery_abs_x(self.x_end)
        # self.loader.set_delivery_abs_z(self.z_end)
        # self.loader.set_delivery_abs_z(120.5-100.0-0.2)
        # self.loader.set_delivery_abs_z(120.5-100.0-0.2)
        # self.loader.set_delivery_abs_z(0)
        # self.loader.reset()
        # while True:
        #     self.start_loader(3)
        #     self.start_loader(1)
        #     self.start_loader(2)
        #     self.start_loader(3)
        #     time.sleep(1)
        # while True:
        #     if not self.loader.queue.empty():
        #         self.start_loader(self.loader.queue.get()[1])
