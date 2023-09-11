# 运动方式
import configparser
import multiprocessing
import os
import threading
import time
from datetime import datetime

import cv2
from PyQt5 import QtCore
from qtpy.QtCore import *

from UI.Data.Graph import Graph
from control.img_func import Sharpness


def get_time_save():
    # 获取当前系统时间
    current_time = datetime.now()
    # 格式化时间显示
    formatted_time = current_time.strftime("%Y_%m_%d_%H_%M_%S")
    return formatted_time


def Data_1and2(Graph_class, ID, multiple, Focusing_method, length):
    # 录入数据库
    # 一级
    data = {'Code': ID, 'label': ID}
    root_id = Graph_class.add_node(data)

    # 录入数据库
    # 二级
    Code = multiple
    data = {}
    parent_code = Graph_class.get_node_info(root_id)['Data']['Code']
    data['Code'] = parent_code + '_' + Code
    data['label'] = Code
    data['对焦方式'] = Focusing_method
    data['视野数量'] = length
    PP_code = Graph_class.add_node(data, root_id)
    return PP_code


def Data_3(Graph_class, PP_code, ID, Z, a, XY, timesave):
    # 录入数据库
    # 三级节点(多少张图就多少个)
    data = {}
    data['Code'] = 'Img' + ID + '_' + str(a)
    data['label'] = data['Code']
    data['Date'] = str(datetime.now())
    data['Pos_XY'] = [XY[0], XY[1]]
    data['Pos_Z'] = [Z]
    data['Desc'] = '区域扫描'
    data['Image'] = 'pic\\' + timesave + '_' + ID + '_' + str(a) + '.png'
    unique_id = Graph_class.add_node(data, PP_code)


class Move(QObject):
    posz_mm = Signal()
    upData = Signal()
    posz_mm_save = Signal()
    posz_mm_1 = Signal()
    posz_mm_2 = Signal()
    posz_mm_3 = Signal()
    posz_mm_4 = Signal()
    save_data = Signal(str, int, list, list)
    uplabel1 = Signal(int, list)

    def __init__(self, camera, motion, clear_point_signal, point_signal, fcous_imagetolabel_signal,
                 image_to_label_func, add_image_to_label_func, UI_BIO, client):
        QObject.__init__(self)
        self.client = client
        self.imglist = None
        self.Graph_class = None
        self.fcous_pos_z_mm_save = None
        self.FLAGE = True
        self.w = None
        self.h = None
        self.number_y = None
        self.number_x = None
        self.y_mm = None
        self.x_mm = None
        self.ListXY = []
        self.camera = camera
        self.motion = motion
        self.Sharpness_func = Sharpness
        self.clear_point_signal = clear_point_signal
        self.point_signal = point_signal
        self.fcous_imagetolabel_signal = fcous_imagetolabel_signal
        self.image_to_label_func = image_to_label_func
        self.add_image_to_label_func = add_image_to_label_func
        self.UI_BIO = UI_BIO
        self.fcous_pos_z_mm = 0
        self.posz_mm.connect(self.updateZpos)
        self.posz_mm_1.connect(self.updateZpos1)
        self.posz_mm_2.connect(self.updateZpos2)
        self.posz_mm_3.connect(self.updateZpos3)
        self.posz_mm_4.connect(self.updateZpos4)
        self.posz_mm_save.connect(self.updateZpossave)
        self.upData.connect(self.update)
        self.save_data.connect(self.save)
        self.uplabel1.connect(self.upimage)

        self.MaxImg = None
        # 加载配置
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')
        self.center_x = self.config.getfloat('Setup', '玻片扫描中心x')
        self.center_y = (self.config.getfloat('Setup', '玻片扫描中心y'))
        self.scan_w = (self.config.getfloat('Setup', '玻片扫描区域宽度'))
        self.scan_h = (self.config.getfloat('Setup', '玻片扫描区域高度'))
        self.calibration = (self.config.getfloat('Setup', '像素标定'))
        self.Focusing_method = (self.config.get('Setup', '对焦方式'))
        self.posz = (self.config.getfloat('Setup', '对焦经验值'))
        self.multiple = (self.config.get('Setup', '对焦倍数'))
        self.ID = (self.config.get('Setup', '玻片ID'))

    @QtCore.pyqtSlot(str, int, list, list)
    def save(self, PP_code, a, Point_XY, Zlist):
        # 检查文件夹路径是否存在
        folder_path = os.path.join('pic')
        if not os.path.exists(folder_path):
            # 如果路径不存在，则创建文件夹
            os.makedirs(folder_path)
        timesave = get_time_save()
        cv2.imwrite('pic\\' + timesave + '_' + self.ID + '_' + str(a) + '.png', self.imglist[a - 1])
        Data_3(self.Graph_class, PP_code, self.ID, Zlist[a - 1], a, Point_XY, timesave)
        self.imglist[a - 1] = None

    def get_route(self):
        points = []
        while True:
            img = self.get_focus_image()
            if img is not None:
                break
        if img is not None:
            self.h, self.w, _ = img.shape
            # 起始点
            self.x_mm = self.center_x - self.scan_w / 2
            self.y_mm = self.center_y - self.scan_h / 2
            # 4点
            points.append([self.center_x - self.scan_w / 4, self.center_y - self.scan_h / 4])
            points.append([self.center_x - self.scan_w / 4, self.center_y + self.scan_h / 4])
            points.append([self.center_x + self.scan_w / 4, self.center_y + self.scan_h / 4])
            points.append([self.center_x + self.scan_w / 4, self.center_y - self.scan_h / 4])
            # number
            self.number_x = self.scan_w / (self.w * self.calibration)
            self.number_y = self.scan_h / (self.h * self.calibration)
            for i in range(int(self.number_x)):
                if i % 2 == 0:
                    for j in range(int(self.number_y)):
                        if (i + 1 - 0.5) * (self.w * self.calibration) <= self.center_x and (j + 1 - 0.5) * (
                                self.h * self.calibration) <= self.center_y:
                            self.ListXY.append([i, j, 1])
                        elif (i + 1 - 0.5) * (self.w * self.calibration) < self.center_x and (j + 1 - 0.5) * (
                                self.h * self.calibration) > self.center_y:
                            self.ListXY.append([i, j, 2])
                        elif (i + 1 - 0.5) * (self.w * self.calibration) > self.center_x and (j + 1 - 0.5) * (
                                self.h * self.calibration) > self.center_y:
                            self.ListXY.append([i, j, 3])
                        elif (i + 1 - 0.5) * (self.w * self.calibration) > self.center_x and (j + 1 - 0.5) * (
                                self.h * self.calibration) < self.center_y:
                            self.ListXY.append([i, j, 4])
                else:
                    for j in range(int(self.number_y) - 1, -1, -1):
                        if (i + 1 - 0.5) * (self.w * self.calibration) <= self.center_x and (j + 1 - 0.5) * (
                                self.h * self.calibration) <= self.center_y:
                            self.ListXY.append([i, j, 1])
                        elif (i + 1 - 0.5) * (self.w * self.calibration) < self.center_x and (j + 1 - 0.5) * (
                                self.h * self.calibration) > self.center_y:
                            self.ListXY.append([i, j, 2])
                        elif (i + 1 - 0.5) * (self.w * self.calibration) > self.center_x and (j + 1 - 0.5) * (
                                self.h * self.calibration) > self.center_y:
                            self.ListXY.append([i, j, 3])
                        elif (i + 1 - 0.5) * (self.w * self.calibration) > self.center_x and (j + 1 - 0.5) * (
                                self.h * self.calibration) < self.center_y:
                            self.ListXY.append([i, j, 4])
            self.UI_BIO.lineEdit_only_size.setText(
                '宽' + str(self.w * self.calibration) + '——' + '高' + str(self.h * self.calibration))
        return points

    def get_focus_image(self):
        if self.camera is not None:
            if self.camera.liveController.trigger_mode == 'Software Trigger':
                self.camera.camera.send_trigger()

            image = self.camera.camera.read_frame()

        return image

    def get_time(self):
        # 获取当前系统时间
        current_time = datetime.now()
        # 格式化时间显示
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
        return formatted_time

    @QtCore.pyqtSlot(int, list)
    def upimage(self, a, Point_XY):
        if a == 1:
            self.image_to_label_func(self.imglist[a - 1],
                                     Point_XY[0] * int(
                                         self.UI_BIO.label_3.width() / int(self.number_x)),
                                     (int(self.number_y) - 1 - Point_XY[1]) * int(
                                         self.UI_BIO.label_3.height() / int(self.number_y)),
                                     int(self.UI_BIO.label_3.width() / int(self.number_x)),
                                     int(self.UI_BIO.label_3.height() / int(self.number_y)))
        else:
            self.add_image_to_label_func(self.imglist[a - 1],
                                         Point_XY[0] * int(
                                             self.UI_BIO.label_3.width() / int(self.number_x)),
                                         (int(self.number_y) - 1 - Point_XY[1]) * int(
                                             self.UI_BIO.label_3.height() / int(self.number_y)),
                                         int(self.UI_BIO.label_3.width() / int(self.number_x)),
                                         int(self.UI_BIO.label_3.height() / int(self.number_y)))

    @QtCore.pyqtSlot()
    def updateZpos1(self):
        self.fcous_pos_z_mm_1 = self.motion.navigationController.z_pos_mm

    @QtCore.pyqtSlot()
    def updateZpos2(self):
        self.fcous_pos_z_mm_2 = self.motion.navigationController.z_pos_mm

    @QtCore.pyqtSlot()
    def updateZpos3(self):
        self.fcous_pos_z_mm_3 = self.motion.navigationController.z_pos_mm

    @QtCore.pyqtSlot()
    def updateZpos4(self):
        self.fcous_pos_z_mm_4 = self.motion.navigationController.z_pos_mm

    @QtCore.pyqtSlot()
    def updateZpos(self):
        self.fcous_pos_z_mm = self.motion.navigationController.z_pos_mm

    @QtCore.pyqtSlot()
    def updateZpossave(self):
        self.fcous_pos_z_mm_save = self.motion.navigationController.z_pos_mm

    @QtCore.pyqtSlot()
    def update(self):
        self.UI_BIO.lineEdit_ID.setText(self.ID)
        self.UI_BIO.lineEdit_Region.setText('宽' + str(self.scan_w) + '——' + '高' + str(self.scan_h))
        self.UI_BIO.lineEdit_fcou_method.setText(self.Focusing_method + '——' + self.multiple)

    # 首次对焦
    def first_point(self, pointflag):
        # 第一次对焦更新z
        # 初步位置
        img = self.get_focus_image()
        definition1 = self.Sharpness_func(img)
        self.posz_mm.emit()
        if pointflag == 1:
            self.posz_mm_1.emit()
        elif pointflag == 2:
            self.posz_mm_2.emit()
        elif pointflag == 3:
            self.posz_mm_2.emit()
        elif pointflag == 4:
            self.posz_mm_2.emit()
        time.sleep(0.1)
        # 往下0.01mm
        self.motion.navigationController.move_z_to(self.posz + 0.01)
        while self.motion.microcontroller.is_busy():
            time.sleep(0.005)
        img = self.get_focus_image()
        self.fcous_imagetolabel_signal.emit(img)
        definition2 = self.Sharpness_func(img)
        if definition2 > definition1:
            definition1 = definition2
            while True:
                self.motion.navigationController.move_z(0.01)
                while self.motion.microcontroller.is_busy():
                    time.sleep(0.005)
                img = self.get_focus_image()
                self.fcous_imagetolabel_signal.emit(img)
                definition2 = self.Sharpness_func(img)
                if definition2 > definition1:
                    definition1 = definition2
                else:
                    self.posz_mm.emit()
                    if pointflag == 1:
                        self.posz_mm_1.emit()
                    elif pointflag == 2:
                        self.posz_mm_2.emit()
                    elif pointflag == 3:
                        self.posz_mm_2.emit()
                    elif pointflag == 4:
                        self.posz_mm_2.emit()
                    time.sleep(0.1)
                    break
        else:
            self.motion.navigationController.move_z_to(self.posz)
            while self.motion.microcontroller.is_busy():
                time.sleep(0.005)
            while True:
                self.motion.navigationController.move_z(-0.01)
                while self.motion.microcontroller.is_busy():
                    time.sleep(0.005)
                img = self.get_focus_image()
                self.fcous_imagetolabel_signal.emit(img)
                definition2 = self.Sharpness_func(img)
                if definition2 > definition1:
                    definition1 = definition2
                else:
                    self.posz_mm.emit()
                    if pointflag == 1:
                        self.posz_mm_1.emit()
                    elif pointflag == 2:
                        self.posz_mm_2.emit()
                    elif pointflag == 3:
                        self.posz_mm_2.emit()
                    elif pointflag == 4:
                        self.posz_mm_2.emit()
                    time.sleep(0.1)
                    break
        return definition1

    def start_move(self):
        if (
                self.ListXY is None and self.Focusing_method is None and self.camera is None and self.Sharpness_func is None
                and self.clear_point_signal is None and self.point_signal is None and self.image_to_label_func is None and self.add_image_to_label_func is None
                and self.motion is None):
            formatted_time = self.get_time()
            self.UI_BIO.log.append(formatted_time + '     ' + '!设备未完全加载，不能扫描!')
        else:
            self.imglist = []
            Zlist = []
            # 注销相机回调
            self.camera.camera.disable_callback()
            self.motion.microcontroller.turn_on_illumination()
            # 计算路径
            points = self.get_route()
            try:
                self.upData.emit()
                self.Graph_class = Graph()
                # 录入数据库一级、二级标题
                PP_code = Data_1and2(self.Graph_class, self.ID, self.multiple, self.Focusing_method, len(self.ListXY))
                if self.Focusing_method == '对焦一次':
                    formatted_time = self.get_time()
                    self.UI_BIO.log.append(formatted_time + '     ' + '!开始扫描!')
                    self.clear_point_signal.emit()
                    # 初始点位
                    self.motion.navigationController.move_x_to(self.center_x)
                    self.motion.navigationController.move_y_to(self.center_y)
                    self.motion.navigationController.move_z_to(self.posz)
                    while self.motion.microcontroller.is_busy():
                        time.sleep(0.005)
                    definition = self.first_point(0)
                    a = 1
                    self.motion.navigationController.move_z_to(self.fcous_pos_z_mm)
                    while self.motion.microcontroller.is_busy():
                        time.sleep(0.005)
                    self.posz_mm_save.emit()
                    for Point_XY in self.ListXY:
                        if not self.FLAGE:
                            result = 2 / 0
                        self.motion.navigationController.move_x_to(self.x_mm + Point_XY[0] * self.w * self.calibration)
                        self.motion.navigationController.move_y_to(self.y_mm + Point_XY[1] * self.h * self.calibration)
                        while self.motion.microcontroller.is_busy():
                            time.sleep(0.005)
                        self.point_signal.emit()
                        img = self.get_focus_image()
                        # self.fcous_imagetolabel_signal.emit(img)
                        self.MaxImg = self.get_focus_image()
                        self.imglist.append(self.MaxImg)
                        Zlist.append(self.fcous_pos_z_mm_save)
                        self.uplabel1.emit(a, Point_XY)
                        self.save_data.emit(PP_code, a, Point_XY, Zlist)
                        formatted_time = self.get_time()
                        self.UI_BIO.log.append(formatted_time + '     ' + '!第' + str(a) + 'OK!')
                        a = a + 1
                    formatted_time = self.get_time()
                    self.UI_BIO.log.append(formatted_time + '     ' + '!扫描完成!')
                    self.UI_BIO.result.append(self.ID + '     ' + '已扫描')
                    self.camera.camera.enable_callback()
                elif self.Focusing_method == '每次对焦':
                    formatted_time = self.get_time()
                    self.UI_BIO.log.append(formatted_time + '     ' + '!开始扫描!')
                    self.clear_point_signal.emit()
                    # 初始点位
                    self.motion.navigationController.move_x_to(self.center_x)
                    self.motion.navigationController.move_y_to(self.center_y)
                    self.motion.navigationController.move_z_to(self.posz)
                    while self.motion.microcontroller.is_busy():
                        time.sleep(0.005)
                    definition = self.first_point(0)

                    a = 1
                    for Point_XY in self.ListXY:
                        if not self.FLAGE:
                            result = 2 / 0
                        self.motion.navigationController.move_x_to(self.x_mm + Point_XY[0] * self.w * self.calibration)
                        self.motion.navigationController.move_y_to(self.y_mm + Point_XY[1] * self.h * self.calibration)
                        self.motion.navigationController.move_z_to(self.fcous_pos_z_mm)
                        while self.motion.microcontroller.is_busy():
                            time.sleep(0.005)
                        self.point_signal.emit()

                        img = self.get_focus_image()
                        self.MaxImg = img
                        definition1 = self.Sharpness_func(img)
                        # self.fcous_imagetolabel_signal.emit(img)
                        self.motion.navigationController.move_z(0.01)
                        while self.motion.microcontroller.is_busy():
                            time.sleep(0.005)
                        img = self.get_focus_image()
                        definition2 = self.Sharpness_func(img)
                        # self.fcous_imagetolabel_signal.emit(img)
                        if definition2 > definition1:
                            self.MaxImg = img
                            self.motion.navigationController.move_z_to(self.fcous_pos_z_mm)
                            while self.motion.microcontroller.is_busy():
                                time.sleep(0.005)
                            while True:
                                self.motion.navigationController.move_z(0.01)
                                while self.motion.microcontroller.is_busy():
                                    time.sleep(0.005)
                                img = self.get_focus_image()
                                definition2 = self.Sharpness_func(img)
                                if definition2 > definition1:
                                    definition1 = definition2
                                    self.MaxImg = img
                                    self.posz_mm_save.emit()
                                    time.sleep(0.05)
                                else:
                                    break
                        else:
                            self.motion.navigationController.move_z_to(self.fcous_pos_z_mm)
                            while self.motion.microcontroller.is_busy():
                                time.sleep(0.005)
                            while True:
                                self.motion.navigationController.move_z(-0.01)
                                while self.motion.microcontroller.is_busy():
                                    time.sleep(0.005)
                                img = self.get_focus_image()
                                definition2 = self.Sharpness_func(img)
                                # self.fcous_imagetolabel_signal.emit(img)
                                if definition2 > definition1:
                                    definition1 = definition2
                                    self.MaxImg = img

                                    self.posz_mm_save.emit()
                                    time.sleep(0.05)
                                else:
                                    break
                        self.imglist.append(self.MaxImg)
                        Zlist.append(self.fcous_pos_z_mm_save)
                        self.uplabel1.emit(a, Point_XY)
                        self.save_data.emit(PP_code, a, Point_XY, Zlist)
                        self.fcous_imagetolabel_signal.emit(self.MaxImg)

                        formatted_time = self.get_time()
                        self.UI_BIO.log.append(formatted_time + '     ' + '!第' + str(a) + 'OK!')
                        a = a + 1
                    formatted_time = self.get_time()
                    self.UI_BIO.log.append(formatted_time + '     ' + '!扫描完成!')
                    self.UI_BIO.result.append(self.ID + '     ' + '已扫描')
                    self.camera.camera.enable_callback()
                elif self.Focusing_method == '智能对焦':
                    formatted_time = self.get_time()
                    self.UI_BIO.log.append(formatted_time + '     ' + '!开始扫描!')
                    self.clear_point_signal.emit()
                    # 初始点位
                    pointflag = 1
                    for point in points:
                        self.motion.navigationController.move_x_to(point[0])
                        self.motion.navigationController.move_y_to(point[1])
                        self.motion.navigationController.move_z_to(self.posz)
                        while self.motion.microcontroller.is_busy():
                            time.sleep(0.005)
                        self.first_point(pointflag)
                        pointflag = pointflag + 1
                    a = 1
                    for Point_XY in self.ListXY:
                        if not self.FLAGE:
                            result = 2 / 0
                        self.motion.navigationController.move_x_to(self.x_mm + Point_XY[0] * self.w * self.calibration)
                        self.motion.navigationController.move_y_to(self.y_mm + Point_XY[1] * self.h * self.calibration)
                        if Point_XY[2] == 1:
                            self.motion.navigationController.move_z_to(self.fcous_pos_z_mm_1)
                        elif Point_XY[2] == 2:
                            self.motion.navigationController.move_z_to(self.fcous_pos_z_mm_2)
                        elif Point_XY[2] == 3:
                            self.motion.navigationController.move_z_to(self.fcous_pos_z_mm_3)
                        elif Point_XY[2] == 4:
                            self.motion.navigationController.move_z_to(self.fcous_pos_z_mm_4)
                        while self.motion.microcontroller.is_busy():
                            time.sleep(0.005)
                        self.point_signal.emit()
                        ############
                        img = self.get_focus_image()
                        self.fcous_imagetolabel_signal.emit(img)
                        self.MaxImg = img
                        self.imglist.append(self.MaxImg)
                        Zlist.append(self.fcous_pos_z_mm_save)
                        self.uplabel1.emit(a, Point_XY)
                        self.save_data.emit(PP_code, a, Point_XY, Zlist)
                        formatted_time = self.get_time()
                        self.UI_BIO.log.append(formatted_time + '     ' + '!第' + str(a) + 'OK!')
                        a = a + 1
                    formatted_time = self.get_time()
                    self.UI_BIO.log.append(formatted_time + '     ' + '!扫描完成!')
                    self.UI_BIO.result.append(self.ID + '     ' + '已扫描')
                self.client.send_data(self.ID)
                self.motion.microcontroller.turn_off_illumination()
                self.camera.camera.enable_callback()
                self.motion.navigationController.home_z()
                while self.motion.microcontroller.is_busy():
                    time.sleep(0.005)
                self.motion.navigationController.move_y_to(60)
                while self.motion.microcontroller.is_busy():
                    time.sleep(0.005)
            except:
                Zlist = []
                time.sleep(0.5)
                self.motion.microcontroller.turn_off_illumination()
                self.camera.camera.enable_callback()
                if not self.FLAGE:
                    self.UI_BIO.log.append(formatted_time + '     ' + '!扫描停止!')
                else:
                    self.UI_BIO.log.append(formatted_time + '     ' + '!扫描失败!')
