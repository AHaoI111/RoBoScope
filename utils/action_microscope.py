# -*- encoding: utf-8 -*-
"""
@Description:
用于控制显微镜的封装类
@File    :   action_loader.py
@Time    :   2024/07/16
@Author  :   Li QingHao
@Version :   2.0
@Time_END :  最后修改时间：
@Developers_END :  最后修改作者：
"""
import os
import time
from datetime import datetime

import cv2
import numpy
from PIL import Image
from PySide6 import QtCore
from PySide6.QtCore import Signal

from utils import Route
from utils import focus
import uuid


def get_time():
    # 获取当前系统时间
    current_time = datetime.now()
    # 格式化时间显示
    formatted_time = current_time.strftime("%Y_%m_%d_%H_%M_%S")
    return formatted_time


def get_time_2():
    # 获取当前系统时间
    current_time = datetime.now()
    # 格式化时间显示
    year = current_time.strftime("%Y")
    month = current_time.strftime("%m")
    day = current_time.strftime("%d")
    return year, month, day


class ActionMicroscope(QtCore.QObject):
    # 信号
    updata_puzzle = Signal(int, list, numpy.ndarray)  # 用于更新拼图进展的信号
    updata_focus = Signal(numpy.ndarray)  # 用于更新对焦图像的信号
    updata_point_clear = Signal()  # 用于清空点位的信号
    updata_point_draw = Signal(list)  # 用于更新绘图点位的信号

    updata_textEdit_log_microscope = Signal(str)  # 用于更新文本编辑器日志的信号

    write_log_microscope = Signal(int, str)  # 用于写入日志的信号


    slide_ok = Signal(str, str)

    def __init__(self, Device, Saver):
        super().__init__()

        self.request = None
        self.ok = None
        self.number = 20
        self.step = 0.003
        self.Stitch_pic = None
        self.Device = Device
        self.Saver = Saver
        self.flage_run = True  # 用来停止扫描
        self.flag = True  # 用来暂停扫描
        self.center_points = {}

    def microscope_homezxy(self):
        self.Device.navigationController.home_z()
        while self.Device.microcontroller.is_busy():
            time.sleep(0.005)
        self.Device.navigationController.home_x()
        # while self.Device.microcontroller.is_busy():
        #     time.sleep(0.005)
        self.Device.navigationController.home_y()
        while self.Device.microcontroller.is_busy():
            time.sleep(0.005)

    def microscope_homezxy_wait(self):
        self.Device.navigationController.home_z()
        while self.Device.microcontroller.is_busy():
            time.sleep(0.005)
        self.Device.navigationController.home_x()
        self.Device.navigationController.home_y()

    def microscope_home_z(self):
        self.Device.navigationController.home_z()
        while self.Device.microcontroller.is_busy():
            time.sleep(0.005)

    def microscope_move_x_to(self, x):
        self.Device.navigationController.move_x_to(x)
        while self.Device.microcontroller.is_busy():
            time.sleep(0.005)

    def microscope_move_y_to(self, y):
        self.Device.navigationController.move_y_to(y)
        while self.Device.microcontroller.is_busy():
            time.sleep(0.005)

    def microscope_move_z_to(self, z):
        self.Device.navigationController.move_z_to(z)
        while self.Device.microcontroller.is_busy():
            time.sleep(0.005)

    def move_2_loader_get(self, Xend, Yend):
        self.Device.navigationController.move_y_to(Yend)
        # while self.Device.microcontroller.is_busy():
        #     time.sleep(0.005)
        self.Device.navigationController.move_x_to(Xend)
        while self.Device.microcontroller.is_busy():
            time.sleep(0.005)

    def move_2_loader_give(self, Xend, Yend):
        self.Device.navigationController.move_y_to(Yend - 1)
        # while self.Device.microcontroller.is_busy():
        #     time.sleep(0.005)
        self.Device.navigationController.move_x_to(Xend)
        while self.Device.microcontroller.is_busy():
            time.sleep(0.005)

    def move_2_loader_get_wait(self, Xend, Yend):
        self.Device.navigationController.move_y_to(Yend)
        self.Device.navigationController.move_x_to(Xend)


    def wait_busy(self):
        while self.Device.microcontroller.is_busy():
            time.sleep(0.005)

    # 设置0号灯
    def set_low_light(self):
        self.Device.set_low_led()

    # 设置1号灯
    def set_high_light(self):
        self.Device.set_high_led()

    def set_only_light(self):
        self.Device.set_only_led()

    def get_image_camera_low(self):

        self.Device.camera1.send_trigger()
        image = self.Device.camera1.read_frame()
        return image

    def get_image_camera_high(self):
        self.Device.camera2.send_trigger()
        image = self.Device.camera2.read_frame()
        return image

    def get_image_camera_one(self):
        self.Device.camera.send_trigger()
        image = self.Device.camera.read_frame()
        return image

    def pause(self):
        self.flag = False

    def Focus_Single(self, zpos_start):
        """
        对显微镜进行自动对焦操作。

        :param multiple: 显微镜的放大倍数，可选值为'20x'或'50x'。
        :param zpos_start: 对焦起始位置（z轴位置）。
        :return: 返回对焦完成后的z轴位置和对应的图像。
        """
        imgmax = None  # 初始化存储最清晰图像的位置
        zpos = zpos_start  # 初始化z轴位置
        try:
            # 根据选择的倍数获取初始图像
            img = self.get_image_camera_one()
            imgmax = img
            # 更新UI显示的图像
            self.updata_focus.emit(img)
            definition1 = focus.Sharpness(img)  # 计算初始图像的清晰度
            zpos = self.Device.navigationController.z_pos_mm  # 获取当前z轴位置
            for i in range(self.number):  # 循环进行对焦尝试
                if self.flag:
                    pass
                else:
                    while not self.flag:
                        time.sleep(0.1)
                # 判断是否正在运行，若未运行则停止并对UI进行相应更新
                if self.flage_run:
                    pass
                else:
                    self.updata_textEdit_log_microscope.emit('显微镜平台对焦停止')
                    self.updata_textEdit_log_microscope.emit('显微镜平台扫描停止')
                    self.write_log_microscope.emit(1, '显微镜平台对焦停止')
                    break
                # 移动z轴到下一个位置
                self.Device.navigationController.move_z_to(zpos_start + self.step * (i + 1))
                while self.Device.microcontroller.is_busy():
                    time.sleep(0.005)
                # 获取当前位置的图像
                img = self.get_image_camera_one()
                self.updata_focus.emit(img)
                definition2 = focus.Sharpness(img)  # 计算当前图像的清晰度
                # 如果当前图像更清晰，则更新最清晰图像的位置和图像本身
                if definition2 > definition1:
                    definition1 = definition2
                    zpos = self.Device.navigationController.z_pos_mm
                    imgmax = img
                    time.sleep(0.005)
        except:
            pass  # 忽略过程中可能出现的异常
        return zpos, imgmax

    def Focus_Double_high(self, zpos_start):
        """
        对显微镜进行自动对焦操作。

        :param multiple: 显微镜的放大倍数，可选值为'20x'或'50x'。
        :param zpos_start: 对焦起始位置（z轴位置）。
        :return: 返回对焦完成后的z轴位置和对应的图像。
        """
        imgmax = None  # 初始化存储最清晰图像的位置
        zpos = zpos_start  # 初始化z轴位置
        try:
            # 根据选择的倍数获取初始图像
            img = self.get_image_camera_high()
            imgmax = img
            # 更新UI显示的图像
            self.updata_focus.emit(img)
            definition1 = focus.Sharpness(img)  # 计算初始图像的清晰度
            zpos = self.Device.navigationController.z_pos_mm  # 获取当前z轴位置
            for i in range(self.number):  # 循环进行对焦尝试
                if self.flag:
                    pass
                else:
                    while not self.flag:
                        time.sleep(0.1)
                # 判断是否正在运行，若未运行则停止并对UI进行相应更新
                if self.flage_run:
                    pass
                else:
                    self.updata_textEdit_log_microscope.emit('显微镜平台对焦停止')
                    self.updata_textEdit_log_microscope.emit('显微镜平台扫描停止')
                    self.write_log_microscope.emit(1, '显微镜平台对焦停止')
                    break
                # 移动z轴到下一个位置
                self.Device.navigationController.move_z_to(zpos_start + self.step * (i + 1))
                while self.Device.microcontroller.is_busy():
                    time.sleep(0.005)
                # 获取当前位置的图像
                img = self.get_image_camera_high()
                self.updata_focus.emit(img)
                definition2 = focus.Sharpness(img)  # 计算当前图像的清晰度
                # 如果当前图像更清晰，则更新最清晰图像的位置和图像本身
                if definition2 > definition1:
                    definition1 = definition2
                    zpos = self.Device.navigationController.z_pos_mm
                    imgmax = img
                    time.sleep(0.005)
        except:
            pass  # 忽略过程中可能出现的异常
        return zpos, imgmax

    def Focus_Double_low(self, zpos_start):
        """
        对显微镜进行自动对焦操作。

        :param multiple: 显微镜的放大倍数，可选值为'20x'或'50x'。
        :param zpos_start: 对焦起始位置（z轴位置）。
        :return: 返回对焦完成后的z轴位置和对应的图像。
        """
        imgmax = None  # 初始化存储最清晰图像的位置
        zpos = zpos_start  # 初始化z轴位置
        try:
            # 根据选择的倍数获取初始图像
            img = self.get_image_camera_low()
            imgmax = img
            # 更新UI显示的图像
            self.updata_focus.emit(img)
            definition1 = focus.Sharpness(img)  # 计算初始图像的清晰度
            zpos = self.Device.navigationController.z_pos_mm  # 获取当前z轴位置
            for i in range(self.number):  # 循环进行对焦尝试
                if self.flag:
                    pass
                else:
                    while not self.flag:
                        time.sleep(0.1)
                # 判断是否正在运行，若未运行则停止并对UI进行相应更新
                if self.flage_run:
                    pass
                else:
                    self.updata_textEdit_log_microscope.emit('显微镜平台对焦停止')
                    self.updata_textEdit_log_microscope.emit('显微镜平台扫描停止')
                    self.write_log_microscope.emit(1, '显微镜平台对焦停止')
                    break
                # 移动z轴到下一个位置
                self.Device.navigationController.move_z_to(zpos_start + self.step * (i + 1))
                while self.Device.microcontroller.is_busy():
                    time.sleep(0.005)
                # 获取当前位置的图像
                img = self.get_image_camera_low()
                self.updata_focus.emit(img)
                definition2 = focus.Sharpness(img)  # 计算当前图像的清晰度
                # 如果当前图像更清晰，则更新最清晰图像的位置和图像本身
                if definition2 > definition1:
                    definition1 = definition2
                    zpos = self.Device.navigationController.z_pos_mm
                    imgmax = img
                    time.sleep(0.005)
        except:
            pass  # 忽略过程中可能出现的异常
        return zpos, imgmax

    def Scan_Mode_one(self, zpos_start, points_xy_positions, points_xy_real,
                      get_image_camera, Focus, UUID, path_save, numberx, numbery, task_info):
        a = 1
        zpos, img = Focus(zpos_start)
        self.updata_focus.emit(img)
        self.microscope_move_z_to(zpos)
        for points_xy_position, Point_XY in zip(points_xy_positions, points_xy_real):
            if self.flag:
                pass
            else:
                while not self.flag:
                    time.sleep(0.1)
            if self.flage_run:
                pass
            else:
                self.updata_textEdit_log_microscope.emit('显微镜平台扫描停止')
                self.write_log_microscope.emit(1, '显微镜平台扫描停止')
                break
            # 由于是竖着放置玻片，所以需要将x轴和y轴交换Point_XY所以互换
            self.microscope_move_x_to(Point_XY[0])
            self.microscope_move_y_to(Point_XY[1])
            img = get_image_camera()
            self.updata_focus.emit(img)
            self.updata_puzzle.emit(a, points_xy_position, img)
            point_xy_real = Point_XY
            self.updata_point_draw.emit(point_xy_real)
            timesave = get_time()
            # 保存原图
            # self.updata_Progress.emit(float(float(a) * 100 / len(points_xy_real)))
            self.Saver.enqueue(img, UUID, a, points_xy_position, timesave,
                               path_save, numberx, numbery, task_info)
            a = a + 1

    def Scan_Mode_two(self, zpos_start, points_4, points_xy_positions, points_xy_real,
                      get_image_camera, Focus, UUID, path_save, numberx, numbery, task_info):
        zpos_4 = []
        a = 1
        for point in points_4:
            if self.flag:
                pass
            else:
                while not self.flag:
                    time.sleep(0.1)
            if self.flage_run:
                pass
            else:
                self.updata_textEdit_log_microscope.emit('显微镜平台扫描停止')
                self.write_log_microscope.emit(1, '显微镜平台扫描停止')
                break
            self.microscope_move_x_to(point[0])
            self.microscope_move_y_to(point[1])
            self.microscope_move_z_to(zpos_start)
            zpos, img = Focus(zpos_start)
            zpos_4.append(zpos)
            self.updata_focus.emit(img)
        for points_xy_position, Point_XY in zip(points_xy_positions, points_xy_real):
            if self.flag:
                pass
            else:
                while not self.flag:
                    time.sleep(0.1)
            if self.flage_run:
                pass
            else:
                self.updata_textEdit_log_microscope.emit('显微镜平台扫描停止')
                self.write_log_microscope.emit(1, '显微镜平台扫描停止')
                break
            # 由于是竖着放置玻片，所以需要将x轴和y轴交换Point_XY所以互换

            self.microscope_move_x_to(Point_XY[0])
            self.microscope_move_y_to(Point_XY[1])
            if Point_XY[2] == 1:
                self.microscope_move_z_to(zpos_4[0])
                zpos = zpos_4[0]
            elif Point_XY[2] == 2:
                self.microscope_move_z_to(zpos_4[1])
                zpos = zpos_4[1]
            elif Point_XY[2] == 3:
                self.microscope_move_z_to(zpos_4[2])
                zpos = zpos_4[2]
            elif Point_XY[2] == 4:
                self.microscope_move_z_to(zpos_4[3])
                zpos = zpos_4[3]

            img = get_image_camera()
            self.updata_focus.emit(img)
            self.updata_puzzle.emit(a, points_xy_position, img)
            point_xy_real = Point_XY
            self.updata_point_draw.emit(point_xy_real)
            timesave = get_time()
            # self.updata_Progress.emit(float(float(a) * 100 / len(points_xy_real)))
            self.Saver.enqueue(img, UUID, a, points_xy_position, timesave,
                               path_save, numberx, numbery, task_info)
            a = a + 1

    def Scan_Mode_three(self, zpos_start, points_xy_positions, points_xy_real,
                        get_image_camera, Focus, Focus_Gap, UUID, path_save, numberx, numbery, task_info):
        z_pos = zpos_start
        a = 1
        for points_xy_position, Point_XY in zip(points_xy_positions, points_xy_real):
            if self.flag:
                pass
            else:
                while not self.flag:
                    time.sleep(0.1)
            if self.flage_run:
                pass
            else:
                self.updata_textEdit_log_microscope.emit('显微镜平台扫描停止')
                self.write_log_microscope.emit(1, '显微镜平台扫描停止')
                break
            self.microscope_move_x_to(Point_XY[0])
            self.microscope_move_y_to(Point_XY[1])

            if a == 1:
                z_pos, img = Focus(zpos_start)
                self.updata_focus.emit(img)
                self.updata_puzzle.emit(a, points_xy_position, img)
                self.number = 40
                self.step = 0.0002
            elif a % Focus_Gap == 0:
                z_pos, img = Focus(z_pos - 0.004)
                self.updata_focus.emit(img)
                self.updata_puzzle.emit(a, points_xy_position, img)
            else:
                self.microscope_move_z_to(z_pos)
                img = get_image_camera()
                self.updata_focus.emit(img)
                self.updata_puzzle.emit(a, points_xy_position, img)

            point_xy_real = Point_XY
            self.updata_point_draw.emit(point_xy_real)
            timesave = get_time()
            # self.updata_Progress.emit(float(float(a) * 100 / len(points_xy_real)))
            self.Saver.enqueue(img, UUID, a, points_xy_position, timesave,
                               path_save, numberx, numbery, task_info)
            a = a + 1

    def low_for_high_Scan_Mode_three(self, zpos_start, points_xy_positions, points_xy_real,
                                     get_image_camera, Focus, Focus_Gap, UUID, path_save, numberx, numbery, task_info):
        z_pos = zpos_start
        a = 1
        for Point_XY in points_xy_real:
            if self.flag:
                pass
            else:
                while not self.flag:
                    time.sleep(0.1)
            if self.flage_run:
                pass
            else:
                self.updata_textEdit_log_microscope.emit('显微镜平台扫描停止')
                self.write_log_microscope.emit(1, '显微镜平台扫描停止')
                break
            self.microscope_move_x_to(Point_XY[0])
            self.microscope_move_y_to(Point_XY[1])

            if a == 1:
                z_pos, img = Focus(zpos_start)
                self.updata_focus.emit(img)
                self.number = 20
                self.step = 0.0002
            elif a % Focus_Gap == 0:
                z_pos, img = Focus(z_pos - 0.002)
                self.updata_focus.emit(img)
            else:
                self.microscope_move_z_to(z_pos)
                img = get_image_camera()
                self.updata_focus.emit(img)

            point_xy_real = Point_XY
            self.updata_point_draw.emit(point_xy_real)
            timesave = get_time()
            # self.updata_Progress.emit(float(float(a) * 100 / len(points_xy_real)))
            self.Saver.enqueue(img, UUID, a, points_xy_positions, timesave,
                               path_save, len(points_xy_real), len(points_xy_real), task_info)
            a = a + 1

    def start(self, Taskinfo, slide_id):
        """
                启动扫描程序，控制显微镜进行图像采集和处理。
                :param IDall: 全部标识符，用于更广泛的唯一标识扫描任务
                """
        self.flage_run = True
        self.updata_textEdit_log_microscope.emit('正在扫描请等待...')
        time_start = time.time()  # 开始计时
        try:
            if not Taskinfo:
                self.updata_textEdit_log_microscope.emit('扫描参数未正确配置，扫描结束')
                self.write_log_microscope.emit(1, '扫描参数未正确配置，扫描结束')
            else:
                self.updata_textEdit_log_microscope.emit('开始扫描')
                self.write_log_microscope.emit(0, '开始扫描')
                if Taskinfo['sys'] == 'single':
                    # 单镜头系统
                    focu_number = Taskinfo['focu_number']
                    step = Taskinfo['focu_size']
                    center_x = Taskinfo['center_x']
                    center_y = Taskinfo['center_y']
                    zpos_start = Taskinfo['zpos_start']
                    region_w = Taskinfo['region_w']
                    region_h = Taskinfo['region_h']
                    calibration = Taskinfo['calibration']
                    ImageStitchSize = Taskinfo['ImageStitchSize']
                    fcous_Gap = Taskinfo['fcous_Gap']

                    self.number = focu_number
                    self.step = step
                    # 移动到预设位置
                    self.microscope_move_y_to(center_y)
                    self.microscope_move_x_to(center_x)
                    self.microscope_move_z_to(zpos_start)
                    self.set_only_light()
                    self.Device.microcontroller.turn_on_illumination()
                    img = self.get_image_camera_one()
                    # 路径
                    points_4, points_xy, points_xy_real, number_x, number_y = Route.get_route(img,
                                                                                              center_x,
                                                                                              center_y,
                                                                                              region_w,
                                                                                              region_h,
                                                                                              calibration)
                    self.updata_textEdit_log_microscope.emit('扫描任务玻片ID为：' + str(slide_id))
                    # 清空点位
                    self.updata_point_clear.emit()
                    self.Saver.image_stitch_all = Image.new("RGB",
                                                            (number_x * ImageStitchSize,
                                                             number_y * ImageStitchSize))
                    year, month, day = get_time_2()
                    # 检查文件夹路径是否存在
                    path_save = Taskinfo[
                                    'savepath'] + '/' + year + '/' + month + '/' + day + '/' + Taskinfo[
                                    'task_id'] + '/' + str(
                        slide_id)
                    folder_path = os.path.join(path_save)
                    if not os.path.exists(folder_path):
                        # 如果路径不存在，则创建文件夹
                        os.makedirs(folder_path)

                    if Taskinfo['FocusMode'] == 1:
                        # 快速模式1
                        self.Scan_Mode_one(zpos_start, points_xy, points_xy_real,
                                           self.get_image_camera_one, self.Focus_Single, slide_id, path_save,
                                           number_x,
                                           number_y, Taskinfo)
                    elif Taskinfo['FocusMode'] == 2:
                        # 快速模式2
                        self.Scan_Mode_two(zpos_start, points_4, points_xy, points_xy_real,
                                           self.get_image_camera_one, self.Focus_Single, slide_id, path_save,
                                           number_x,
                                           number_y, Taskinfo)
                    elif Taskinfo['FocusMode'] == 3:
                        # 快速模式3
                        self.Scan_Mode_three(zpos_start, points_xy, points_xy_real,
                                             self.get_image_camera_one, self.Focus_Single, fcous_Gap, slide_id,
                                             path_save,
                                             number_x, number_y, Taskinfo)
                elif Taskinfo['sys'] == 'double':
                    # 双镜头系统
                    if Taskinfo['scanmode']:
                        # 启用低倍预扫，高倍精准扫描
                        focu_number_low = Taskinfo['focu_number_low']
                        step_low = Taskinfo['focu_size_low']
                        focu_number_high = Taskinfo['focu_number_high']
                        step_high = Taskinfo['focu_size_high']
                        center_x_low = Taskinfo['center_x_low']
                        center_y_low = Taskinfo['center_y_low']
                        center_x_high = Taskinfo['center_x_high']
                        center_y_high = Taskinfo['center_y_high']
                        zpos_start_high = Taskinfo['zpos_start_high']
                        zpos_start_low = Taskinfo['zpos_start_low']
                        region_w_low = Taskinfo['region_w_low']
                        region_h_low = Taskinfo['region_h_low']
                        region_w_high = Taskinfo['region_w_high']
                        region_h_high = Taskinfo['region_h_high']
                        calibration_high = Taskinfo['calibration_high']
                        calibration_low = Taskinfo['calibration_low']
                        ImageStitchSize = Taskinfo['ImageStitchSize']
                        fcous_Gap_low = Taskinfo['fcous_Gap_low']
                        fcous_Gap_high = Taskinfo['fcous_Gap_high']
                        lens_gap_x = Taskinfo['lens_gap_x']
                        lens_gap_y = Taskinfo['lens_gap_y']
                        self.number = focu_number_low
                        self.step = step_low
                        # 移动到预设位置
                        self.microscope_move_y_to(center_y_low)
                        self.microscope_move_x_to(center_x_low)
                        self.microscope_move_z_to(zpos_start_low)
                        #
                        self.set_low_light()
                        self.Device.microcontroller.turn_on_illumination()
                        img = self.get_image_camera_low()
                        if len(img.shape) == 2:
                            h, w = img.shape
                        else:
                            h, w, _ = img.shape
                        # 路径
                        points_4, points_xy, points_xy_real, number_x, number_y = Route.get_route(img,
                                                                                                  center_x_low,
                                                                                                  center_y_low,
                                                                                                  region_w_low,
                                                                                                  region_h_low,
                                                                                                  calibration_low)
                        self.updata_textEdit_log_microscope.emit(
                            '扫描任务玻片ID为：' + str(slide_id))
                        # 清空点位
                        self.updata_point_clear.emit()
                        self.Saver.image_stitch_all = Image.new("RGB",
                                                                (number_x * ImageStitchSize,
                                                                 number_y * ImageStitchSize))
                        # 检查文件夹路径是否存在
                        year, month, day = get_time_2()
                        path_save = Taskinfo[
                                        'savepath'] + '/' + year + '/' + month + '/' + day + '/' + Taskinfo[
                                        'task_id'] + '/' + slide_id
                        folder_path = os.path.join(path_save)
                        Taskinfo['flag_create_view'] = False
                        if not os.path.exists(folder_path):
                            # 如果路径不存在，则创建文件夹
                            os.makedirs(folder_path)
                        if Taskinfo['FocusMode_low'] == 1:
                            # 快速模式1
                            self.Scan_Mode_one(zpos_start_low, points_xy, points_xy_real,
                                               self.get_image_camera_low, self.Focus_Double_low, slide_id,
                                               path_save, number_x, number_y, Taskinfo)
                        elif Taskinfo['FocusMode_low'] == 2:
                            # 快速模式2
                            self.Scan_Mode_two(zpos_start_low, points_4, points_xy, points_xy_real,
                                               self.get_image_camera_low, self.Focus_Double_low,
                                               slide_id, path_save, number_x, number_y, Taskinfo)
                        elif Taskinfo['FocusMode_low'] == 3:
                            # 快速模式3
                            self.Scan_Mode_three(zpos_start_low, points_xy, points_xy_real,
                                                 self.get_image_camera_low, self.Focus_Double_low,
                                                 fcous_Gap_low, slide_id, path_save, number_x, number_y, Taskinfo)
                        self.Device.microcontroller.turn_off_illumination()
                        # 低倍扫描完毕
                        # 给出高倍需要扫描的points_xy
                        # 高倍扫描
                        points_xy_real_high = []
                        points_xy_location = []
                        t0 = time.time()
                        while True:
                            if len(self.center_points) != 0:
                                for key, value in self.center_points.items():
                                    start_x = points_xy_real[int(key) - 1][0] + (w / 2) * calibration_low
                                    start_y = points_xy_real[int(key) - 1][1] + (h / 2) * calibration_low
                                    scaled_points = [[start_x - y * calibration_low, start_y - x * calibration_low]
                                                     for
                                                     x, y in value]
                                    points_xy_real_high.extend(scaled_points)
                                    points_xy_location.append(
                                        [value[0], value[1], ImageStitchSize, ImageStitchSize])
                                break
                            time.sleep(0.005)
                            if time.time() - t0 > 10:
                                self.updata_textEdit_log_microscope.emit('等待高倍推荐视野超时')
                                points_xy_real_high = []
                                break
                        Taskinfo['flag_create_view'] = True
                        points_xy_real_high = [[x + lens_gap_x, y + lens_gap_y] for x, y in points_xy_real_high]
                        if len(points_xy_real_high) >= Taskinfo['max_views']:
                            points_xy_real_high = points_xy_real_high[0:Taskinfo['max_views']]
                        self.number = focu_number_high
                        self.step = step_high
                        if len(points_xy_real) > 0:
                            self.updata_textEdit_log_microscope.emit('开始扫描高倍推荐视野')
                            self.set_high_light()
                            self.Device.microcontroller.turn_on_illumination()
                            # 低倍到高倍坐标转换
                            # 低倍起始点
                            # 得到高倍下的视野
                            self.low_for_high_Scan_Mode_three(zpos_start_high, points_xy_location,
                                                              points_xy_real_high,
                                                              self.get_image_camera_high, self.Focus_Double_high,
                                                              1, slide_id, path_save, number_x, number_y, Taskinfo)
                        else:
                            self.updata_textEdit_log_microscope.emit('高倍扫描无推荐视野')
                    else:
                        if Taskinfo['scanmultiple'] == 'high':
                            focu_number = Taskinfo['focu_number_high']
                            step = Taskinfo['focu_size_high']
                            center_x_high = Taskinfo['center_x_high']
                            center_y_high = Taskinfo['center_y_high']
                            zpos_start_high = Taskinfo['zpos_start_high']
                            region_w = Taskinfo['region_w_high']
                            region_h = Taskinfo['region_h_high']
                            calibration_high = Taskinfo['calibration_high']
                            ImageStitchSize = Taskinfo['ImageStitchSize']
                            fcous_Gap = Taskinfo['fcous_Gap_high']

                            self.number = focu_number
                            self.step = step
                            # 移动到预设位置
                            self.microscope_move_y_to(center_y_high)
                            self.microscope_move_x_to(center_x_high)
                            self.microscope_move_z_to(zpos_start_high)
                            #
                            self.set_high_light()
                            self.Device.microcontroller.turn_on_illumination()
                            img = self.get_image_camera_high()
                            # 路径
                            points_4, points_xy, points_xy_real, number_x, number_y = Route.get_route(
                                img,
                                center_x_high,
                                center_y_high,
                                region_w,
                                region_h,
                                calibration_high)
                            self.updata_textEdit_log_microscope.emit(
                                '扫描任务玻片ID为：' + str(slide_id))
                            # 清空点位
                            self.updata_point_clear.emit()
                            self.Saver.image_stitch_all = Image.new("RGB",
                                                                    (number_x * ImageStitchSize,
                                                                     number_y * ImageStitchSize))
                            # 检查文件夹路径是否存在
                            year, month, day = get_time_2()
                            path_save = Taskinfo[
                                            'savepath'] + '/' + year + '/' + month + '/' + day + '/' + Taskinfo[
                                            'task_id'] + '/' + slide_id
                            folder_path = os.path.join(path_save)
                            if not os.path.exists(folder_path):
                                # 如果路径不存在，则创建文件夹
                                os.makedirs(folder_path)
                            if Taskinfo['FocusMode_high'] == 1:
                                # 快速模式1
                                self.Scan_Mode_one(zpos_start_high, points_xy, points_xy_real,
                                                   self.get_image_camera_high, self.Focus_Double_high, slide_id,
                                                   path_save,
                                                   number_x, number_y, Taskinfo)
                            elif Taskinfo['FocusMode_high'] == 2:
                                # 快速模式2
                                self.Scan_Mode_two(zpos_start_high, points_4, points_xy, points_xy_real,
                                                   self.get_image_camera_high, self.Focus_Double_high, slide_id,
                                                   path_save,
                                                   number_x, number_y, Taskinfo)
                            elif Taskinfo['FocusMode_high'] == 3:
                                # 快速模式3
                                self.Scan_Mode_three(zpos_start_high, points_xy, points_xy_real,
                                                     self.get_image_camera_high, self.Focus_Double_high, fcous_Gap,
                                                     slide_id, path_save, number_x, number_y, Taskinfo)
                        elif Taskinfo['scanmultiple'] == 'low':
                            focu_number = Taskinfo['focu_number_low']
                            step = Taskinfo['focu_size_low']
                            center_x_low = Taskinfo['center_x_low']
                            center_y_low = Taskinfo['center_y_low']
                            zpos_start_low = Taskinfo['zpos_start_low']
                            region_w = Taskinfo['region_w_low']
                            region_h = Taskinfo['region_h_low']
                            calibration_low = Taskinfo['calibration_low']
                            ImageStitchSize = Taskinfo['ImageStitchSize']
                            fcous_Gap = Taskinfo['fcous_Gap_low']
                            self.number = focu_number
                            self.step = step
                            # 移动到预设位置
                            self.microscope_move_y_to(center_y_low)
                            self.microscope_move_x_to(center_x_low)
                            self.microscope_move_z_to(zpos_start_low)
                            #
                            self.set_low_light()
                            self.Device.microcontroller.turn_on_illumination()
                            img = self.get_image_camera_low()
                            # 路径
                            points_4, points_xy, points_xy_real, number_x, number_y = Route.get_route(
                                img,
                                center_x_low,
                                center_y_low,
                                region_w,
                                region_h,
                                calibration_low)
                            self.updata_textEdit_log_microscope.emit(
                                '扫描任务玻片ID为：' + str(slide_id))
                            # 清空点位
                            self.updata_point_clear.emit()
                            self.Saver.image_stitch_all = Image.new("RGB",
                                                                    (number_x * ImageStitchSize,
                                                                     number_y * ImageStitchSize))
                            # 检查文件夹路径是否存在
                            year, month, day = get_time_2()
                            path_save = Taskinfo[
                                            'savepath'] + '/' + year + '/' + month + '/' + day + '/' + Taskinfo[
                                            'task_id'] + '/' + slide_id
                            folder_path = os.path.join(path_save)
                            if not os.path.exists(folder_path):
                                # 如果路径不存在，则创建文件夹
                                os.makedirs(folder_path)

                            if Taskinfo['FocusMode_low'] == 1:
                                # 快速模式1
                                self.Scan_Mode_one(zpos_start_low, points_xy, points_xy_real,
                                                   self.get_image_camera_low, self.Focus_Double_low, slide_id,
                                                   path_save,
                                                   number_x, number_y, Taskinfo)
                            elif Taskinfo['FocusMode_low'] == 2:
                                # 快速模式2
                                self.Scan_Mode_two(zpos_start_low, points_4, points_xy, points_xy_real,
                                                   self.get_image_camera_low, self.Focus_Double_low, slide_id,
                                                   path_save,
                                                   number_x, number_y, Taskinfo)
                            elif Taskinfo['FocusMode_low'] == 3:
                                # 快速模式3
                                self.Scan_Mode_three(zpos_start_low, points_xy, points_xy_real,
                                                     self.get_image_camera_low, self.Focus_Double_low, fcous_Gap,
                                                     slide_id,
                                                     path_save, number_x, number_y, Taskinfo)
                self.updata_Progress.emit(float(100))
                self.Device.microcontroller.turn_off_illumination()
                time_end = time.time()  # 结束计时
                time_c = time_end - time_start  # 运行所花时间
                if self.flage_run:
                    self.updata_textEdit_log_microscope.emit('显微镜平台扫描完成')
                    self.updata_textEdit_log_microscope.emit('显微镜平台扫描费时' + str(time_c))
                    self.write_log_microscope.emit(0, '显微镜平台扫描费时' + str(time_c))
                    if self.request is not None:
                        self.slide_ok.emit(slide_id, slide_id + "_slide.jpg")
                self.microscope_home_z()
        except Exception as e:
            self.updata_textEdit_log_microscope.emit('显微镜平台扫描失败')
            self.write_log_microscope.emit(1, '显微镜平台扫描停止:' + str(e))
