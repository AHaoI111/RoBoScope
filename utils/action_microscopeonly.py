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

import numpy
from PIL import Image
from PySide6 import QtCore
from PySide6.QtCore import Signal

from DataSaver import data
from utils import Route
from utils import focus


def get_time():
    # 获取当前系统时间
    current_time = datetime.now()
    # 格式化时间显示
    formatted_time = current_time.strftime("%Y_%m_%d_%H_%M_%S")
    return formatted_time


class ActionMicroscope(QtCore.QObject):
    # 信号
    updata_puzzle = Signal(int, list, numpy.ndarray)  # 用于更新拼图进展的信号
    updata_focus = Signal(numpy.ndarray)  # 用于更新对焦图像的信号
    updata_point_clear = Signal()  # 用于清空点位的信号
    updata_point_draw = Signal(list, float)  # 用于更新绘图点位的信号
    # ok = Signal(str, numpy.ndarray, str)

    updata_textEdit_log_microscope = Signal(str)  # 用于更新文本编辑器日志的信号
    updata_textEdit_ID = Signal(str)

    write_log_microscope = Signal(int, str)  # 用于写入日志的信号
    updata_Progress = Signal(float)  # 用于更新进度条的信号

    def __init__(self, Device, config, Saver):
        super().__init__()

        self.ok = None
        self.number = 60
        self.step = 0.003
        self.thread1 = None
        self.Graph_class = None
        self.Stitch_pic = None
        self.Device = Device
        self.Saver = Saver
        self.flage_run = True
        self.config_info = config
        self.flag = True

    def read_config(self):
        center_x_50x = float(self.config_info['Microscope']['玻片扫描中心xy50x'][0])
        center_y_50x = float(self.config_info['Microscope']['玻片扫描中心xy50x'][1])
        center_x_20x = float(self.config_info['Microscope']['玻片扫描中心xy20x'][0])
        center_y_20x = float(self.config_info['Microscope']['玻片扫描中心xy20x'][1])
        center_x_only = float(self.config_info['Microscope']['单镜头扫描中心xy'][0])
        center_y_only = float(self.config_info['Microscope']['单镜头扫描中心xy'][1])

        region_w = int(self.config_info['Microscope']['玻片扫描区域宽度'])
        region_h = int(self.config_info['Microscope']['玻片扫描区域高度'])
        focusing_method = self.config_info['Microscope']['对焦方式']
        zpos_start50x = float(self.config_info['Microscope']['对焦经验值50x'])
        zpos_start20x = float(self.config_info['Microscope']['对焦经验值20x'])
        zpos_startonly = float(self.config_info['Microscope']['对焦经验值单镜头'])
        focu_number = int(self.config_info['Microscope']['对焦步数'])
        focu_size = float(self.config_info['Microscope']['对焦分辨率'])
        multiple = self.config_info['Microscope']['对焦倍数'][0]
        multiple_sys = self.config_info['Microscope']['对焦倍数'][1]

        calibration_50 = float(self.config_info['Camera']['像素标定50x'])
        calibration_20 = float(self.config_info['Camera']['像素标定20x'])
        calibration_only = float(self.config_info['Camera']['单镜头标定'])

        self.ImageStitchSize = int(self.config_info['ImageSaver']['imagestitchsize'])
        self.fcous_number = int(self.config_info['Microscope']['隔点对焦步长'])
        # 加载配置
        self.Xend = float(self.config_info['Microscope']['xend'])
        self.Yend = float(self.config_info['Microscope']['yend'])

        if multiple_sys == '单镜头':
            return center_x_only, center_y_only, region_w, region_h, calibration_only, focusing_method, zpos_startonly, multiple, focu_number, focu_size, multiple_sys
        elif multiple_sys == '双镜头':
            if multiple == '20X':
                return center_x_20x, center_y_20x, region_w, region_h, calibration_20, focusing_method, zpos_start20x, multiple, focu_number, focu_size, multiple_sys
            elif multiple == '50X':
                return center_x_50x, center_y_50x, region_w, region_h, calibration_50, focusing_method, zpos_start50x, multiple, focu_number, focu_size, multiple_sys

    def microscope_homezxy(self):
        self.Device.navigationController.home_z()
        while self.Device.microcontroller.is_busy():
            time.sleep(0.005)
        self.Device.navigationController.home_x()
        while self.Device.microcontroller.is_busy():
            time.sleep(0.005)
        self.Device.navigationController.home_y()
        while self.Device.microcontroller.is_busy():
            time.sleep(0.005)

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

    def move_2_loader_get(self):
        self.Device.navigationController.move_y_to(self.Yend)
        while self.Device.microcontroller.is_busy():
            time.sleep(0.005)
        self.Device.navigationController.move_x_to(self.Xend)
        while self.Device.microcontroller.is_busy():
            time.sleep(0.005)

    def move_2_loader_give(self):
        self.Device.navigationController.move_y_to(self.Yend - 1)
        while self.Device.microcontroller.is_busy():
            time.sleep(0.005)
        self.Device.navigationController.move_x_to(self.Xend)
        while self.Device.microcontroller.is_busy():
            time.sleep(0.005)

    # 设置0号灯
    def set_left_light(self):
        self.Device.set_left_led()

    # 设置1号灯
    def set_right_light(self):
        self.Device.set_right_led()

    def set_only_light(self):
        self.Device.set_only_led()

    def get_image_camera20x(self):

        self.Device.microcontroller.turn_on_illumination()
        time.sleep(0.0005)
        self.Device.camera1.send_trigger()
        image = self.Device.camera1.read_frame()
        self.Device.microcontroller.turn_off_illumination()
        return image

    def get_image_camera50x(self):
        self.Device.microcontroller.turn_on_illumination()
        time.sleep(0.0005)
        self.Device.camera2.send_trigger()
        image = self.Device.camera2.read_frame()
        # image = cv2.rotate(image, cv2.ROTATE_180)
        self.Device.microcontroller.turn_off_illumination()
        return image

    def get_image_camera_one(self):
        # self.Device.microcontroller.turn_on_illumination()
        # time.sleep(0.0005)
        self.Device.camera.send_trigger()
        image = self.Device.camera.read_frame()
        # self.Device.microcontroller.turn_off_illumination()
        return image

    def pause(self):
        self.flag = False

    def Focus_on(self, multiple_sys, multiple, zpos_start):
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
            img = None
            if multiple_sys == '单镜头':
                img = self.get_image_camera_one()
            elif multiple_sys == '双镜头':
                if multiple == '50X':
                    img = self.get_image_camera50x()
                elif multiple == '20X':
                    img = self.get_image_camera20x()
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
                if multiple_sys == '单镜头':
                    img = self.get_image_camera_one()
                elif multiple_sys == '双镜头':
                    if multiple == '50X':
                        img = self.get_image_camera50x()
                    elif multiple == '20X':
                        img = self.get_image_camera20x()
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

    def start(self, ID, IDall):
        """
                启动扫描程序，控制显微镜进行图像采集和处理。

                :param ID: 标识符，用于区分不同的扫描任务
                :param IDall: 全部标识符，用于更广泛的唯一标识扫描任务
                :param slide_img: 玻片图像，用于初始化扫描过程
                """
        self.flage_run = True
        self.updata_textEdit_log_microscope.emit('正在扫描请等待...')
        time_start = time.time()  # 开始计时
        center_x, center_y, region_w, region_h, calibration, focusing_method, zpos_start, multiple, focus_numnber, focus_size, multiple_sys = self.read_config()
        print(calibration)
        self.number = focus_numnber
        self.step = focus_size
        # 移动到预设位置
        self.microscope_move_y_to(center_y)
        self.microscope_move_x_to(center_x)
        self.microscope_move_z_to(zpos_start)
        if multiple_sys == '单镜头':
            self.set_only_light()
            self.Device.microcontroller.turn_on_illumination()
            img = self.get_image_camera_one()
        elif multiple_sys == '双镜头':
            if multiple == '50X':
                self.set_right_light()
                img = self.get_image_camera50x()
            elif multiple == '20X':
                self.set_left_light()
                img = self.get_image_camera20x()
        points_4, points_xy, x_Start, y_Start, number_x, number_y, h, w = Route.get_route(img, center_x, center_y,
                                                                                          region_w,
                                                                                          region_h, calibration)
        # 清空点位
        self.updata_point_clear.emit()
        self.Saver.image_stitch_all = Image.new("RGB",
                                                (number_x * self.ImageStitchSize,
                                                 number_y * self.ImageStitchSize))
        # 判断code是否正确
        if len(ID) > 0:
            code = ID[0]
            self.Saver.DataProcessing = data.data_processing(code, number_x, number_y)
            UUID = self.Saver.DataProcessing.Save_data_1(code, IDall)
            self.updata_textEdit_ID.emit(code)
            # 检查文件夹路径是否存在
            path_save = self.config_info['ImageSaver']['savepath'] + '\\' + str(UUID) + '\\' + multiple
            folder_path = os.path.join(path_save)
            if not os.path.exists(folder_path):
                # 如果路径不存在，则创建文件夹
                os.makedirs(folder_path)
            # 保存玻片的图片
            path_slide = os.path.join(path_save, "slide.png")
            self.Saver.DataProcessing.Save_data_2(UUID, multiple, path_save + '\\' + str(ID[0]) + '.jpg', path_slide)
        else:
            code = "Not successfully"
            self.Saver.DataProcessing = data.data_processing(code, number_x, number_y)
            UUID = self.Saver.DataProcessing.Save_data_1(code, IDall)
            self.updata_textEdit_ID.emit(code + str(IDall))
            # 检查文件夹路径是否存在
            path_save = self.config_info['ImageSaver']['savepath'] + '\\' + str(UUID) + '\\' + multiple
            folder_path = os.path.join(path_save)
            if not os.path.exists(folder_path):
                # 如果路径不存在，则创建文件夹
                os.makedirs(folder_path)
            # 保存玻片的图片
            path_slide = os.path.join(path_save, "slide.png")
            self.Saver.DataProcessing.Save_data_2(UUID, multiple, path_save + '\\' + str(UUID) + '.jpg', path_slide)

        try:
            # 扫描方式
            if focusing_method == '快速扫描二':
                self.number = focus_numnber
                self.step = focus_size
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
                    zpos, image = self.Focus_on(multiple_sys, multiple, zpos_start)
                    zpos_4.append(zpos)
                    self.updata_focus.emit(img)
                for Point_XY in points_xy:
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
                    self.microscope_move_x_to(x_Start - (Point_XY[0] + 0.5) * w * calibration)
                    self.microscope_move_y_to(y_Start - (Point_XY[1] + 0.5) * h * calibration)
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
                    self.updata_point_draw.emit(Point_XY, region_w)
                    if multiple_sys == '单镜头':
                        img = self.get_image_camera_one()
                    elif multiple_sys == '双镜头':
                        if multiple == '50X':
                            img = self.get_image_camera50x()
                        elif multiple == '20X':
                            img = self.get_image_camera20x()
                    self.updata_focus.emit(img)
                    self.updata_puzzle.emit(a, Point_XY, img)
                    point_xy_real = [x_Start - (Point_XY[0] + 0.5) * w * calibration,
                                     y_Start - (Point_XY[1] + 0.5) * h * calibration]
                    timesave = get_time()
                    # 保存原图
                    self.Saver.enqueue(img, UUID, zpos, a, Point_XY, timesave,
                                       path_save, number_x, number_y, self.ok, point_xy_real,
                                       multiple, code)
                    self.updata_Progress.emit(float(float(a) * 100 / len(points_xy)))
                    a = a + 1
            elif focusing_method == '快速扫描一':
                self.number = focus_numnber
                self.step = focus_size
                a = 1
                self.microscope_move_x_to(center_x)
                self.microscope_move_y_to(center_y)
                zpos, image = self.Focus_on(multiple_sys, multiple, zpos_start)
                self.updata_focus.emit(img)
                self.microscope_move_z_to(zpos)
                for Point_XY in points_xy:
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
                    self.microscope_move_x_to(x_Start - (Point_XY[0] + 0.5) * w * calibration)
                    self.microscope_move_y_to(y_Start - (Point_XY[1] + 0.5) * h * calibration)
                    if multiple_sys == '单镜头':
                        img = self.get_image_camera_one()
                    elif multiple_sys == '双镜头':
                        if multiple == '50X':
                            img = self.get_image_camera50x()
                        elif multiple == '20X':
                            img = self.get_image_camera20x()
                    self.updata_point_draw.emit(Point_XY, region_w)
                    self.updata_focus.emit(img)
                    self.updata_puzzle.emit(a, Point_XY, img)
                    point_xy_real = [x_Start - (Point_XY[0] + 0.5) * w * calibration,
                                     y_Start - (Point_XY[1] + 0.5) * h * calibration]

                    timesave = get_time()
                    # 保存原图
                    self.Saver.enqueue(img, UUID, zpos, a, Point_XY, timesave,
                                       path_save, number_x, number_y, self.ok, point_xy_real,
                                       multiple, code)
                    self.updata_Progress.emit(float(float(a) * 100 / len(points_xy)))
                    a = a + 1
            elif focusing_method == '快速扫描三':
                z_pos = zpos_start
                a = 1
                for Point_XY in points_xy:
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
                    self.microscope_move_x_to(x_Start - (Point_XY[0] + 0.5) * w * calibration)
                    self.microscope_move_y_to(y_Start - (Point_XY[1] + 0.5) * h * calibration)

                    if a == 1:
                        z_pos, img = self.Focus_on(multiple_sys, multiple, zpos_start)
                        self.updata_focus.emit(img)
                        self.updata_puzzle.emit(a, Point_XY, img)
                        self.updata_point_draw.emit(Point_XY, region_w)
                        self.number = 20
                        self.step = 0.002
                    elif a % self.fcous_number == 0:
                        z_pos, img = self.Focus_on(multiple_sys, multiple, z_pos - 0.02)
                        self.updata_focus.emit(img)
                        self.updata_puzzle.emit(a, Point_XY, img)
                        self.updata_point_draw.emit(Point_XY, region_w)
                    else:
                        self.microscope_move_z_to(z_pos)
                        if multiple_sys == '单镜头':
                            img = self.get_image_camera_one()
                        elif multiple_sys == '双镜头':
                            if multiple == '50X':
                                img = self.get_image_camera50x()
                            elif multiple == '20X':
                                img = self.get_image_camera20x()
                        self.updata_point_draw.emit(Point_XY, region_w)
                        self.updata_focus.emit(img)
                        self.updata_puzzle.emit(a, Point_XY, img)

                    point_xy_real = [x_Start - (Point_XY[0] + 0.5) * w * calibration,
                                     y_Start - (Point_XY[1] + 0.5) * h * calibration]
                    timesave = get_time()
                    # 保存原图
                    self.Saver.enqueue(img, UUID, z_pos, a, Point_XY, timesave,
                                       path_save, number_x, number_y, self.ok, point_xy_real,
                                       multiple, code)
                    self.updata_Progress.emit(float(float(a) * 100 / len(points_xy)))
                    a = a + 1
            self.updata_Progress.emit(float(100))
            self.Device.microcontroller.turn_off_illumination()
            time_end = time.time()  # 结束计时
            time_c = time_end - time_start  # 运行所花时间
            if self.flage_run:
                self.updata_textEdit_log_microscope.emit('显微镜平台扫描完成')
                self.updata_textEdit_log_microscope.emit('显微镜平台扫描费时' + str(time_c))
                self.updata_textEdit_log_microscope.emit('显微镜平台还未处理完成')
                self.updata_textEdit_log_microscope.emit('请等待...')
                self.write_log_microscope.emit(0, '显微镜平台扫描费时' + str(time_c))
            self.microscope_home_z()
            self.microscope_move_y_to(center_y)
            self.microscope_move_x_to(center_x)
        except Exception as e:
            self.flage_50x = False
            self.flage_20x = False
            self.updata_textEdit_log_microscope.emit('显微镜平台扫描失败')
            self.write_log_microscope.emit(1, '显微镜平台扫描停止')
