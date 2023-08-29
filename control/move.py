# 运动方式
from control.img_func import Sharpness
import time
from datetime import datetime

from PyQt5 import QtCore
from qtpy.QtCore import *
import configparser
import cv2
import os
from UI.Data.Graph import Graph


def Data_1and2(Graph_class, ID, multiple, Focusing_method):
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
    PP_code = Graph_class.add_node(data, root_id)
    return PP_code


def Data_3(Graph_class, PP_code, ID, a, XY, Z, results):
    # 录入数据库
    # 三级节点(多少张图就多少个)
    data = {}
    data['Code'] = 'Img' + ID + '_' + str(a)
    data['label'] = data['Code']
    data['Date'] = str(datetime.now())
    data['Pos_XY'] = [XY[0], XY[1]]
    data['Pos_Z'] = [Z]
    data['Desc'] = '区域扫描'
    data['Image'] = 'pic\\' + ID + '_' + str(a) + '.png'
    # bbox: x,y,w,h
    data['bbox'] = results[0].boxes.xywhn.tolist()
    data['Annotation'] = [int(x) for x in results[0].boxes.cls.tolist()]
    data['Confidence'] = results[0].boxes.conf.tolist()
    unique_id = Graph_class.add_node(data, PP_code)


class Move(QObject):
    posz_mm = Signal()
    upData = Signal()

    def __init__(self, camera, motion, clear_point_signal, point_signal, fcous_imagetolabel_signal,
                 image_to_label_func, add_image_to_label_func, UI_BIO, model):
        QObject.__init__(self)

        self.model = model
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
        self.upData.connect(self.update)
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

    def get_route(self):
        img = self.get_focus_image()
        if img is not None:
            self.h, self.w, _ = img.shape
            # 起始点
            self.x_mm = self.center_x - self.scan_w / 2
            self.y_mm = self.center_y - self.scan_h / 2
            # number
            self.number_x = self.scan_w / (self.w * self.calibration)
            self.number_y = self.scan_h / (self.h * self.calibration)
            for i in range(int(self.number_x)):
                if i % 2 == 0:
                    for j in range(int(self.number_y)):
                        if abs(i - self.number_x / 2) >= 5 or abs(j - self.number_y / 2) >= 5:
                            self.ListXY.append([i, j, 5])
                        else:
                            self.ListXY.append(
                                [i, j, int(max([abs(i - self.number_x / 2), abs(j - self.number_y / 2)]))])
                else:
                    for j in range(int(self.number_y) - 1, -1, -1):
                        if abs(i - self.number_x / 2) >= 5 or abs(j - self.number_y / 2) >= 5:
                            self.ListXY.append([i, j, 5])
                        else:
                            self.ListXY.append(
                                [i, j, int(max([abs(i - self.number_x / 2), abs(j - self.number_y / 2)]))])
            self.UI_BIO.lineEdit_only_size.setText(
                '宽' + str(self.w * self.calibration) + '——' + '高' + str(self.h * self.calibration))

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

    @QtCore.pyqtSlot()
    def updateZpos(self):
        self.fcous_pos_z_mm = self.motion.navigationController.z_pos_mm

    @QtCore.pyqtSlot()
    def update(self):
        self.UI_BIO.lineEdit_ID.setText(self.ID)
        self.UI_BIO.lineEdit_Region.setText('宽' + str(self.scan_w) + '——' + '高' + str(self.scan_h))
        self.UI_BIO.lineEdit_fcou_method.setText(self.Focusing_method + '——' + self.multiple)

    def start_move(self):
        if (
                self.ListXY is None and self.Focusing_method is None and self.camera is None and self.Sharpness_func is None
                and self.clear_point_signal is None and self.point_signal is None and self.image_to_label_func is None and self.add_image_to_label_func is None
                and self.motion is None):
            formatted_time = self.get_time()
            self.UI_BIO.log.append(formatted_time + '     ' + '!设备未完全加载，不能扫描!')
        else:
            # 注销相机回调
            self.camera.camera.disable_callback()
            time.sleep(0.5)
            # 计算路径
            self.get_route()
            try:
                self.upData.emit()
                Graph_class = Graph()
                # 录入数据库一级、二级标题
                PP_code = Data_1and2(Graph_class, self.ID, self.multiple, self.Focusing_method)
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
                    # 第一次对焦更新z
                    # 初步位置
                    for j in range(15):
                        img = self.get_focus_image()
                    img = self.get_focus_image()
                    definition1 = self.Sharpness_func(img)
                    # 往下0.01mm
                    self.motion.navigationController.move_z_to(self.posz + 0.01)
                    while self.motion.microcontroller.is_busy():
                        time.sleep(0.005)
                    for j in range(15):
                        img = self.get_focus_image()
                    img = self.get_focus_image()
                    self.fcous_imagetolabel_signal.emit(img)
                    definition2 = self.Sharpness_func(img)
                    if definition2 > definition1:
                        definition1 = definition2
                        while True:
                            self.motion.navigationController.move_z(0.01)
                            while self.motion.microcontroller.is_busy():
                                time.sleep(0.005)
                            for j in range(15):
                                img = self.get_focus_image()
                            img = self.get_focus_image()
                            self.fcous_imagetolabel_signal.emit(img)
                            definition2 = self.Sharpness_func(img)
                            if definition2 > definition1:
                                definition1 = definition2
                            else:
                                self.posz_mm.emit()
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
                            for j in range(15):
                                img = self.get_focus_image()
                            img = self.get_focus_image()
                            self.fcous_imagetolabel_signal.emit(img)
                            definition2 = self.Sharpness_func(img)
                            if definition2 > definition1:
                                definition1 = definition2
                            else:
                                self.posz_mm.emit()
                                time.sleep(0.1)
                                break
                    a = 1
                    self.motion.navigationController.move_z_to(self.fcous_pos_z_mm)
                    while self.motion.microcontroller.is_busy():
                        time.sleep(0.005)
                    for Point_XY in self.ListXY:
                        if not self.FLAGE:
                            result = 2 / 0
                        self.motion.navigationController.move_x_to(self.x_mm + Point_XY[0] * self.w * self.calibration)
                        self.motion.navigationController.move_y_to(self.y_mm + Point_XY[1] * self.h * self.calibration)
                        while self.motion.microcontroller.is_busy():
                            time.sleep(0.005)
                        self.point_signal.emit()
                        for k in range(15):
                            img = self.get_focus_image()

                        self.fcous_imagetolabel_signal.emit(img)
                        self.MaxImg = self.get_focus_image()
                        ######### 模型推理
                        results = self.model(self.MaxImg, device='cuda:0', conf=0.5, nms=True)
                        num_list = results[0].boxes.cls.tolist()
                        num_ec = num_list.count(0)
                        num_wc = num_list.count(1) + num_list.count(2)
                        annotated_frame = results[0].plot(line_width=1)
                        # 在图片的左上角写入文本
                        text_ec = 'EC:' + str(num_ec)
                        text_wc = 'WBC:' + str(num_wc)
                        font = cv2.FONT_HERSHEY_SIMPLEX
                        font_scale = 4
                        color = (0, 255, 0)  # 文本的颜色，以BGR格式表示
                        thickness = 4  # 文本的线条粗细
                        cv2.putText(annotated_frame, text_ec, (0, 100), font, font_scale, color, thickness)
                        cv2.putText(annotated_frame, text_wc, (0, 300), font, font_scale, color, thickness)
                        ############
                        # 检查文件夹路径是否存在
                        folder_path = os.path.join('pic')
                        if not os.path.exists(folder_path):
                            # 如果路径不存在，则创建文件夹
                            os.makedirs(folder_path)
                        # cv2.imwrite('pic\\' + ID + '_' + str(lena) + '.png', self.Max_img)
                        cv2.imwrite('pic\\' + self.ID + '_' + str(a) + '.png', self.MaxImg)
                        Data_3(Graph_class, PP_code, self.ID, a, Point_XY, self.fcous_pos_z_mm, results)
                        if a == 1:
                            self.image_to_label_func(annotated_frame,
                                                     Point_XY[0] * int(
                                                         self.UI_BIO.label_3.width() / int(self.number_x)),
                                                     (int(self.number_y) - 1 - Point_XY[1]) * int(
                                                         self.UI_BIO.label_3.height() / int(self.number_y)),
                                                     int(self.UI_BIO.label_3.width() / int(self.number_x)),
                                                     int(self.UI_BIO.label_3.height() / int(self.number_y)))
                        else:
                            self.add_image_to_label_func(annotated_frame,
                                                         Point_XY[0] * int(
                                                             self.UI_BIO.label_3.width() / int(self.number_x)),
                                                         (int(self.number_y) - 1 - Point_XY[1]) * int(
                                                             self.UI_BIO.label_3.height() / int(self.number_y)),
                                                         int(self.UI_BIO.label_3.width() / int(self.number_x)),
                                                         int(self.UI_BIO.label_3.height() / int(self.number_y)))
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
                    # 注销相机回调
                    self.camera.camera.disable_callback()
                    time.sleep(0.5)
                    # 第一次对焦更新z
                    # 初步位置
                    for j in range(15):
                        img = self.get_focus_image()
                    img = self.get_focus_image()
                    definition1 = self.Sharpness_func(img)
                    # 往下0.01mm
                    self.motion.navigationController.move_z_to(self.posz + 0.01)
                    while self.motion.microcontroller.is_busy():
                        time.sleep(0.005)
                    for j in range(15):
                        img = self.get_focus_image()
                    img = self.get_focus_image()
                    self.fcous_imagetolabel_signal.emit(img)
                    definition2 = self.Sharpness_func(img)
                    if definition2 > definition1:
                        definition1 = definition2
                        while True:
                            self.motion.navigationController.move_z(0.01)
                            while self.motion.microcontroller.is_busy():
                                time.sleep(0.005)
                            for j in range(15):
                                img = self.get_focus_image()
                            img = self.get_focus_image()
                            self.fcous_imagetolabel_signal.emit(img)
                            definition2 = self.Sharpness_func(img)
                            if definition2 > definition1:
                                definition1 = definition2
                            else:
                                self.posz_mm.emit()
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
                            for j in range(15):
                                img = self.get_focus_image()
                            img = self.get_focus_image()
                            self.fcous_imagetolabel_signal.emit(img)
                            definition2 = self.Sharpness_func(img)
                            if definition2 > definition1:
                                definition1 = definition2
                            else:
                                self.posz_mm.emit()
                                time.sleep(0.1)
                                break
                    a = 1
                    for Point_XY in self.ListXY:
                        if not self.FLAGE:
                            result = 2 / 0
                        self.motion.navigationController.move_x_to(self.x_mm + Point_XY[0] * self.w * self.calibration)
                        self.motion.navigationController.move_y_to(self.y_mm + Point_XY[1] * self.h * self.calibration)
                        self.motion.navigationController.move_z_to(self.fcous_pos_z_mm - 3 * 0.01)
                        while self.motion.microcontroller.is_busy():
                            time.sleep(0.005)
                        self.point_signal.emit()
                        for l in range(6):
                            self.motion.navigationController.move_z_to(self.fcous_pos_z_mm - 3 * 0.01 + (l + 1) * 0.01)
                            while self.motion.microcontroller.is_busy():
                                time.sleep(0.005)
                            for k in range(15):
                                img = self.get_focus_image()
                                # self.fcous_imagetolabel_signal.emit(img)
                            self.fcous_imagetolabel_signal.emit(img)
                            if l == 0:
                                img = self.get_focus_image()
                                definition1 = self.Sharpness_func(img)
                                self.fcous_imagetolabel_signal.emit(img)
                                self.MaxImg = img
                                self.posz_mm.emit()
                                time.sleep(0.1)
                            else:
                                img = self.get_focus_image()
                                definition2 = self.Sharpness_func(img)
                                self.fcous_imagetolabel_signal.emit(img)
                                if definition2 > definition1:
                                    definition1 = definition2
                                    self.MaxImg = img
                                    self.posz_mm.emit()
                                    time.sleep(0.1)
                        ######### 模型推理
                        results = self.model(self.MaxImg, device='cuda:0', conf=0.5, nms=True)
                        num_list = results[0].boxes.cls.tolist()
                        num_ec = num_list.count(0)
                        num_wc = num_list.count(1) + num_list.count(2)
                        annotated_frame = results[0].plot(line_width=1)
                        # 在图片的左上角写入文本
                        text_ec = 'EC:' + str(num_ec)
                        text_wc = 'WBC:' + str(num_wc)
                        font = cv2.FONT_HERSHEY_SIMPLEX
                        font_scale = 4
                        color = (0, 255, 0)  # 文本的颜色，以BGR格式表示
                        thickness = 4  # 文本的线条粗细
                        cv2.putText(annotated_frame, text_ec, (0, 100), font, font_scale, color, thickness)
                        cv2.putText(annotated_frame, text_wc, (0, 300), font, font_scale, color, thickness)
                        ############
                        # 检查文件夹路径是否存在
                        folder_path = os.path.join('pic')
                        if not os.path.exists(folder_path):
                            # 如果路径不存在，则创建文件夹
                            os.makedirs(folder_path)
                        # cv2.imwrite('pic\\' + ID + '_' + str(lena) + '.png', self.Max_img)
                        cv2.imwrite('pic\\' + self.ID + '_' + str(a) + '.png', self.MaxImg)
                        Data_3(Graph_class, PP_code, self.ID, a, Point_XY, self.fcous_pos_z_mm, results)
                        if a == 1:
                            self.image_to_label_func(annotated_frame,
                                                     Point_XY[0] * int(
                                                         self.UI_BIO.label_3.width() / int(self.number_x)),
                                                     (int(self.number_y) - 1 - Point_XY[1]) * int(
                                                         self.UI_BIO.label_3.height() / int(self.number_y)),
                                                     int(self.UI_BIO.label_3.width() / int(self.number_x)),
                                                     int(self.UI_BIO.label_3.height() / int(self.number_y)))
                        else:
                            self.add_image_to_label_func(annotated_frame,
                                                         Point_XY[0] * int(
                                                             self.UI_BIO.label_3.width() / int(self.number_x)),
                                                         (int(self.number_y) - 1 - Point_XY[1]) * int(
                                                             self.UI_BIO.label_3.height() / int(self.number_y)),
                                                         int(self.UI_BIO.label_3.width() / int(self.number_x)),
                                                         int(self.UI_BIO.label_3.height() / int(self.number_y)))
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
                    self.motion.navigationController.move_x_to(self.center_x)
                    self.motion.navigationController.move_y_to(self.center_y)
                    self.motion.navigationController.move_z_to(self.posz)
                    while self.motion.microcontroller.is_busy():
                        time.sleep(0.005)
                    # 注销相机回调
                    self.camera.camera.disable_callback()
                    time.sleep(0.5)
                    # 第一次对焦更新z
                    # 初步位置
                    for j in range(15):
                        img = self.get_focus_image()
                    img = self.get_focus_image()
                    definition1 = self.Sharpness_func(img)
                    # 往下0.01mm
                    self.motion.navigationController.move_z_to(self.posz + 0.01)
                    while self.motion.microcontroller.is_busy():
                        time.sleep(0.005)
                    for j in range(15):
                        img = self.get_focus_image()
                    img = self.get_focus_image()
                    self.fcous_imagetolabel_signal.emit(img)
                    definition2 = self.Sharpness_func(img)
                    if definition2 > definition1:
                        definition1 = definition2
                        while True:
                            self.motion.navigationController.move_z(0.01)
                            while self.motion.microcontroller.is_busy():
                                time.sleep(0.005)
                            for j in range(15):
                                img = self.get_focus_image()
                            img = self.get_focus_image()
                            self.fcous_imagetolabel_signal.emit(img)
                            definition2 = self.Sharpness_func(img)
                            if definition2 > definition1:
                                definition1 = definition2
                            else:
                                self.posz_mm.emit()
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
                            for j in range(15):
                                img = self.get_focus_image()
                            img = self.get_focus_image()
                            self.fcous_imagetolabel_signal.emit(img)
                            definition2 = self.Sharpness_func(img)
                            if definition2 > definition1:
                                definition1 = definition2
                            else:
                                self.posz_mm.emit()
                                time.sleep(0.1)
                                break
                    a = 1
                    for Point_XY in self.ListXY:
                        if not self.FLAGE:
                            result = 2 / 0
                        self.motion.navigationController.move_x_to(self.x_mm + Point_XY[0] * self.w * self.calibration)
                        self.motion.navigationController.move_y_to(self.y_mm + Point_XY[1] * self.h * self.calibration)
                        self.motion.navigationController.move_z_to(self.fcous_pos_z_mm - Point_XY[2] * 0.01)
                        while self.motion.microcontroller.is_busy():
                            time.sleep(0.005)
                        self.point_signal.emit()
                        if Point_XY[2] == 0:
                            for l in range(1):
                                self.motion.navigationController.move_z_to(
                                    self.fcous_pos_z_mm - Point_XY[2] * 0.01)
                                while self.motion.microcontroller.is_busy():
                                    time.sleep(0.005)
                                for k in range(15):
                                    img = self.get_focus_image()

                                # self.fcous_imagetolabel_signal.emit(img)
                                if l == 0:
                                    img = self.get_focus_image()
                                    definition1 = self.Sharpness_func(img)
                                    self.fcous_imagetolabel_signal.emit(img)
                                    self.MaxImg = img
                                    self.posz_mm.emit()
                                    time.sleep(0.1)
                                else:
                                    img = self.get_focus_image()
                                    definition2 = self.Sharpness_func(img)
                                    self.fcous_imagetolabel_signal.emit(img)
                                    if definition2 > definition1:
                                        definition1 = definition2
                                        self.MaxImg = img
                                        self.posz_mm.emit()
                                        time.sleep(0.1)
                        else:
                            for l in range(Point_XY[2] * 2):
                                self.motion.navigationController.move_z_to(
                                    self.fcous_pos_z_mm - Point_XY[2] * 0.01 + (l + 1) * 0.01)
                                while self.motion.microcontroller.is_busy():
                                    time.sleep(0.005)
                                for k in range(15):
                                    img = self.get_focus_image()
                                    # self.fcous_imagetolabel_signal.emit(img)

                                if l == 0:
                                    img = self.get_focus_image()
                                    definition1 = self.Sharpness_func(img)
                                    self.fcous_imagetolabel_signal.emit(img)
                                    self.MaxImg = img
                                else:
                                    img = self.get_focus_image()
                                    definition2 = self.Sharpness_func(img)
                                    self.fcous_imagetolabel_signal.emit(img)
                                    if definition2 > definition1:
                                        definition1 = definition2
                                        self.MaxImg = img
                        ######### 模型推理
                        results = self.model(self.MaxImg, device='cuda:0', conf=0.5, nms=True)
                        num_list = results[0].boxes.cls.tolist()
                        num_ec = num_list.count(0)
                        num_wc = num_list.count(1) + num_list.count(2)
                        annotated_frame = results[0].plot(line_width=1)
                        # 在图片的左上角写入文本
                        text_ec = 'EC:' + str(num_ec)
                        text_wc = 'WBC:' + str(num_wc)
                        font = cv2.FONT_HERSHEY_SIMPLEX
                        font_scale = 4
                        color = (0, 255, 0)  # 文本的颜色，以BGR格式表示
                        thickness = 4  # 文本的线条粗细
                        cv2.putText(annotated_frame, text_ec, (0, 100), font, font_scale, color, thickness)
                        cv2.putText(annotated_frame, text_wc, (0, 300), font, font_scale, color, thickness)
                        ############
                        # 检查文件夹路径是否存在
                        folder_path = os.path.join('pic')
                        if not os.path.exists(folder_path):
                            # 如果路径不存在，则创建文件夹
                            os.makedirs(folder_path)
                        # cv2.imwrite('pic\\' + ID + '_' + str(lena) + '.png', self.Max_img)
                        cv2.imwrite('pic\\' + self.ID + '_' + str(a) + '.png', self.MaxImg)
                        Data_3(Graph_class, PP_code, self.ID, a, Point_XY,self.fcous_pos_z_mm,  results)
                        if a == 1:
                            self.image_to_label_func(annotated_frame,
                                                     Point_XY[0] * int(
                                                         self.UI_BIO.label_3.width() / int(self.number_x)),
                                                     (int(self.number_y) - 1 - Point_XY[1]) * int(
                                                         self.UI_BIO.label_3.height() / int(self.number_y)),
                                                     int(self.UI_BIO.label_3.width() / int(self.number_x)),
                                                     int(self.UI_BIO.label_3.height() / int(self.number_y)))
                        else:
                            self.add_image_to_label_func(annotated_frame,
                                                         Point_XY[0] * int(
                                                             self.UI_BIO.label_3.width() / int(self.number_x)),
                                                         (int(self.number_y) - 1 - Point_XY[1]) * int(
                                                             self.UI_BIO.label_3.height() / int(self.number_y)),
                                                         int(self.UI_BIO.label_3.width() / int(self.number_x)),
                                                         int(self.UI_BIO.label_3.height() / int(self.number_y)))
                        formatted_time = self.get_time()
                        self.UI_BIO.log.append(formatted_time + '     ' + '!第' + str(a) + 'OK!')
                        a = a + 1
                    formatted_time = self.get_time()
                    self.UI_BIO.log.append(formatted_time + '     ' + '!扫描完成!')
                    self.UI_BIO.result.append(self.ID + '     ' + '已扫描')
                    self.camera.camera.enable_callback()
            except:
                if not self.FLAGE:
                    self.UI_BIO.log.append(formatted_time + '     ' + '!扫描停止!')
                else:
                    self.UI_BIO.log.append(formatted_time + '     ' + '!扫描失败!')
