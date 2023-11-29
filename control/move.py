# 运动方式
import configparser
import os
import time
from datetime import datetime
from queue import Queue
from threading import Thread, Lock

import cv2
import numpy
from PIL import Image
from PySide6 import QtCore
from PySide6 import QtGui
from PySide6.QtCore import *
from PySide6.QtGui import QPainter, QColor, QBrush

from UI.Data.Graph import Graph
from control.img_func import Sharpness


def get_time_save():
    # 获取当前系统时间
    current_time = datetime.now()
    # 格式化时间显示
    formatted_time = current_time.strftime("%Y_%m_%d_%H_%M_%S")
    return formatted_time


def Data_1and2(Graph_class, ID, multiple, Focusing_method, ListXY):
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
    data['视野数量'] = len(ListXY)
    # 获取第一个位置的最大值
    w = max(ListXY, key=lambda x: x[0])[0]

    # 获取第二个位置的最大值
    h = max(ListXY, key=lambda x: x[1])[1]
    data['视野长宽'] = [w, h]
    data['拼接图'] = 'pic\\' + ID + '\\' + ID + '.png'
    PP_code = Graph_class.add_node(data, root_id)
    return PP_code


def Data_3(Graph_class, PP_code, ID, Z, a, XY, timesave, results):
    # 录入数据库
    # 三级节点(多少张图就多少个)
    data = {}
    data['Code'] = 'Img' + ID + '_' + str(a)
    data['label'] = data['Code']
    data['Date'] = str(datetime.now())
    data['Pos_XY'] = [XY[0], XY[1]]
    data['Pos_Z'] = [Z]
    data['Desc'] = '区域扫描'
    data['Image'] = 'pic\\' + ID + '\\' + timesave + '_' + ID + '_' + str(a) + '.png'
    data['bbox'] = results[0].boxes.xywhn.tolist()
    data['Annotation'] = [int(x) for x in results[0].boxes.cls.tolist()]
    data['Confidence'] = results[0].boxes.conf.tolist()
    unique_id = Graph_class.add_node(data, PP_code)


# 保存图片
class ImageSaver(QObject):
    def __init__(self, model):
        QObject.__init__(self)

        self.queue = Queue(600)
        self.image_lock = Lock()
        self.model = model
        self.thread = Thread(target=self.process_queue)
        self.thread.start()

    def process_queue(self):
        while True:
            try:
                [image, Graph_class, PP_code, ID, ZPoint, a, Point_XY, timesave, path_save,
                 Stitch_pic, number, numberw, numberh] = self.queue.get(
                    timeout=0.1)
                self.image_lock.acquire(True)
                if image is not None:
                    if a == 1:
                        image_wbc = numpy.zeros((numberw, numberh), dtype=numpy.uint8)
                        image_ec = numpy.zeros((numberw, numberh), dtype=numpy.uint8)
                    # 存图
                    cv2.imwrite(path_save + '\\' + timesave + '_' + ID + '_' + str(a) + '.png', image)
                    # 推理
                    results = self.model(image, device='cuda:0', conf=0.7, nms=True)
                    # 保存结果
                    Data_3(Graph_class, PP_code, ID, ZPoint, a, Point_XY, timesave, results)
                    image_ec[numberw - 1 - Point_XY[1], Point_XY[0]] = [int(x) for x in
                                                                        results[0].boxes.cls.tolist()].count(1)
                    image_wbc[numberw - 1 - Point_XY[1], Point_XY[0]] = [int(x) for x in
                                                                         results[0].boxes.cls.tolist()].count(0)
                    if a == numberw*numberh:
                        Stitch_pic = numpy.array(Stitch_pic)
                        Stitch_pic = cv2.cvtColor(Stitch_pic, cv2.COLOR_RGB2BGR)

                        list_window = []
                        list_window_wbc = []
                        list_window_ec = []
                        # 窗口大小
                        window_size = (2, 2)
                        # 滑动窗口并计算每个窗口的灰度值综合
                        for row in range(0, image_wbc.shape[0] - window_size[0] + 1, 2):
                            for col in range(0, image_wbc.shape[1] - window_size[1] + 1, 2):
                                # 获取当前窗口
                                window_wbc = image_wbc[row:row + window_size[0], col:col + window_size[1]]
                                window_ec = image_ec[row:row + window_size[0], col:col + window_size[1]]
                                # 计算窗口的细胞数综合
                                sum_wbc = window_wbc.sum()
                                sum_ec = window_ec.sum()
                                if len(list_window) < 40:
                                    list_window.append([col, row, col + window_size[1], row + window_size[0]])
                                    list_window_wbc.append(sum_wbc)
                                    list_window_ec.append(sum_ec)
                                else:
                                    if sum_wbc > min(list_window_wbc):
                                        index = list_window_wbc.index(min(list_window_wbc))
                                        list_window[index] = [col, row, col + window_size[1], row + window_size[0]]
                                        list_window_wbc[index] = sum_wbc
                                        list_window_ec[index] = sum_ec

                        for point in list_window:
                            cv2.rectangle(Stitch_pic, (point[0] * 320, point[1] * 320),
                                          (point[2] * 320, point[3] * 320), (0, 255, 0),
                                          5)

                        sort_list_window_wbc = sorted(list_window_wbc)
                        name = 'WBC'
                        list_window_wbc2 = list_window_wbc
                        list_window2 = list_window
                        for i in range(3):
                            index = list_window_wbc2.index(sort_list_window_wbc[i + 37])
                            point = list_window2[index]
                            cv2.rectangle(Stitch_pic, (point[0] * 320, point[1] * 320),
                                          (point[2] * 320, point[3] * 320), (0, 0, 255),
                                          5)
                            cv2.putText(Stitch_pic,
                                        f'{name}:{list_window_wbc2[index]}', (point[0] * 320, point[1] * 320 - 10),
                                        cv2.FONT_HERSHEY_SIMPLEX,
                                        0.75, [0, 0, 255],
                                        thickness=1)
                            list_window_wbc2.pop(index)
                            list_window2.pop(index)
                        index = list_window_wbc.index(sort_list_window_wbc[39])
                        number_wbc = list_window_wbc[index]
                        number_ec = list_window_ec[index]
                        if number_wbc >= 25:
                            if number_ec <= 10:
                                res = True
                                cv2.putText(Stitch_pic,
                                            ID + '__Qualified', (0, 40),
                                            cv2.FONT_HERSHEY_SIMPLEX,
                                            1.5, [0, 255, 0], thickness=1)
                            else:
                                res = False
                                cv2.putText(Stitch_pic,
                                            ID + '__Unqualified', (0, 40),
                                            cv2.FONT_HERSHEY_SIMPLEX,
                                            1.5, [0, 0, 255], thickness=1)
                        else:
                            res = False
                            cv2.putText(Stitch_pic,
                                        ID + '__Unqualified', (0, 40),
                                        cv2.FONT_HERSHEY_SIMPLEX,
                                        1.5, [0, 0, 255], thickness=1)
                        cv2.imwrite('pic\\' + ID + '\\' + ID + '.png', Stitch_pic)
                        return
                self.queue.task_done()
                self.image_lock.release()
            except:
                pass

    def enqueue(self, image, Graph_class, PP_code, ID, ZPoint, a, Point_XY, timesave, path_save, Stitch_pic,
                number, numberw, numberh):
        try:
            self.queue.put_nowait(
                [image, Graph_class, PP_code, ID, ZPoint, a, Point_XY, timesave, path_save, Stitch_pic, number,
                 numberw, numberh])
        except:
            print('imageSaver queue is full, image discarded')


class Move(QObject):
    posz_mm = Signal()
    upData = Signal()
    posz_mm_save = Signal()
    posz_mm_point = Signal(int)
    save_data = Signal(str, int, list, list)
    uplabel1 = Signal(int, list)
    clear_point = Signal()
    point = Signal()
    fcous_image = Signal(numpy.ndarray)

    def __init__(self, camera, motion, Sketch_map, UI_BIO, model):
        QObject.__init__(self)
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
        self.Sketch_map = Sketch_map

        self.UI_BIO = UI_BIO
        self.fcous_pos_z_mm = 0
        self.posz_mm.connect(self.updateZpos)
        self.posz_mm_point.connect(self.updateZpos_point)

        self.posz_mm_save.connect(self.updateZpossave)
        self.upData.connect(self.update)
        self.save_data.connect(self.save)
        self.uplabel1.connect(self.upimage)
        self.point.connect(self.updateLabelpoints)
        self.clear_point.connect(self.clear_points)
        self.fcous_image.connect(self.updateLabelimg)
        self.MaxImg = None

        # 保存
        self.model = model
        self.ImageSaver = ImageSaver(self.model)

    def read_config(self):
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

    @QtCore.Slot()
    def clear_points(self):
        pixmap = self.UI_BIO.Sketch_map.pixmap()
        painter = QPainter(pixmap)
        painter.setRenderHint(QPainter.Antialiasing)

        # 清空整个背景
        painter.eraseRect(pixmap.rect())
        painter.end()
        self.UI_BIO.Sketch_map.setPixmap(self.Sketch_map)  # 将绘制结果设置给QLabel的pixmap
        self.UI_BIO.Sketch_map.update()  # 强制刷新QLabel的显示

    # 绘制红点
    @QtCore.Slot()
    def updateLabelpoints(self):
        pixmap = self.UI_BIO.Sketch_map.pixmap()  # 获取QPixmap对象
        painter = QPainter(pixmap)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(QColor(255, 0, 0))
        painter.setBrush(QBrush(QColor(255, 0, 0)))
        radius = 2
        distance = (self.w * self.calibration) / 0.0547

        center_x, center_y = float(self.motion.navigationController.x_pos_mm), float(
            self.motion.navigationController.y_pos_mm)
        painter.drawEllipse(int(center_x * 5.469 + 0), int(-center_y * 5.469 + 255), 2 * radius,
                            2 * radius)

        painter.end()
        self.UI_BIO.Sketch_map.setPixmap(pixmap)  # 将绘制结果设置给QLabel的pixmap
        self.UI_BIO.Sketch_map.update()  # 强制刷新QLabel的显示

    @QtCore.Slot(numpy.ndarray)
    def updateLabelimg(self, numpy_image):
        height, width, channel = numpy_image.shape
        bytes_per_line = 3 * width  # 假设图像为RGB格式
        q_img = QtGui.QImage(bytes(numpy_image.data), width, height, bytes_per_line, QtGui.QImage.Format_RGB888)
        pixmap = QtGui.QPixmap.fromImage(q_img)
        scaled_pixmap = pixmap.scaled(500, 320)  # 设置缩小后的大小为200x150
        # 在标签上显示绘制后的图像
        self.UI_BIO.label.setPixmap(scaled_pixmap)

    @QtCore.Slot(str, int, list, list)
    def save(self, PP_code, a, Point_XY, Zlist):
        # 检查文件夹路径是否存在
        path_save = 'pic\\' + self.ID
        folder_path = os.path.join(path_save)
        if not os.path.exists(folder_path):
            # 如果路径不存在，则创建文件夹
            os.makedirs(folder_path)
        timesave = get_time_save()
        # 粘贴拼图
        img_np = cv2.resize(self.imglist[a - 1], (320, 320))
        img_pil = Image.fromarray(img_np)
        self.Stitch_pic.paste(img_pil, box=(Point_XY[0] * 320, (self.numberh - Point_XY[1]-1) * 320))
        # 保存原图
        bgr_image = cv2.cvtColor(self.imglist[a - 1], cv2.COLOR_RGB2BGR)
        self.ImageSaver.enqueue(bgr_image, self.Graph_class, PP_code, self.ID, Zlist[a - 1], a, Point_XY, timesave,
                                path_save, self.Stitch_pic, len(self.ListXY), self.numberw, self.numberh)
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
            self.number_x = self.scan_w / (self.w * self.calibration)+1
            self.number_y = self.scan_h / (self.h * self.calibration)+1
            for i in range(int(self.number_x)):
                if i % 2 == 0:
                    for j in range(int(self.number_y)):
                        if (i + 1 - 0.5) * (
                                self.w * self.calibration) + self.center_x - self.scan_w / 2 <= self.center_x and (
                                j + 1 - 0.5) * (
                                self.h * self.calibration) + self.center_y - self.scan_h / 2 <= self.center_y:
                            self.ListXY.append([i, j, 1])
                        elif (i + 1 - 0.5) * (
                                self.w * self.calibration) + self.center_x - self.scan_w / 2 < self.center_x and (
                                j + 1 - 0.5) * (
                                self.h * self.calibration) + self.center_y - self.scan_h / 2 > self.center_y:
                            self.ListXY.append([i, j, 2])
                        elif (i + 1 - 0.5) * (
                                self.w * self.calibration) + self.center_x - self.scan_w / 2 > self.center_x and (
                                j + 1 - 0.5) * (
                                self.h * self.calibration) + self.center_y - self.scan_h / 2 > self.center_y:
                            self.ListXY.append([i, j, 3])
                        elif (i + 1 - 0.5) * (
                                self.w * self.calibration) + self.center_x - self.scan_w / 2 > self.center_x and (
                                j + 1 - 0.5) * (
                                self.h * self.calibration) + self.center_y - self.scan_h / 2 < self.center_y:
                            self.ListXY.append([i, j, 4])
                else:
                    for j in range(int(self.number_y) - 1, -1, -1):
                        if (i + 1 - 0.5) * (
                                self.w * self.calibration) + self.center_x - self.scan_w / 2 <= self.center_x and (
                                j + 1 - 0.5) * (
                                self.h * self.calibration) + self.center_y - self.scan_h / 2 <= self.center_y:
                            self.ListXY.append([i, j, 1])
                        elif (i + 1 - 0.5) * (
                                self.w * self.calibration) + self.center_x - self.scan_w / 2 < self.center_x and (
                                j + 1 - 0.5) * (
                                self.h * self.calibration) + self.center_y - self.scan_h / 2 > self.center_y:
                            self.ListXY.append([i, j, 2])
                        elif (i + 1 - 0.5) * (
                                self.w * self.calibration) + self.center_x - self.scan_w / 2 > self.center_x and (
                                j + 1 - 0.5) * (
                                self.h * self.calibration) + self.center_y - self.scan_h / 2 > self.center_y:
                            self.ListXY.append([i, j, 3])
                        elif (i + 1 - 0.5) * (
                                self.w * self.calibration) + self.center_x - self.scan_w / 2 > self.center_x and (
                                j + 1 - 0.5) * (
                                self.h * self.calibration) + self.center_y - self.scan_h / 2 < self.center_y:
                            self.ListXY.append([i, j, 4])
        return points

    def get_focus_image(self):
        self.motion.microcontroller.turn_on_illumination()
        time.sleep(0.003)

        self.camera.camera.send_trigger()

        image = self.camera.camera.read_frame()
        self.motion.microcontroller.turn_off_illumination()

        return image

    def get_time(self):
        # 获取当前系统时间
        current_time = datetime.now()
        # 格式化时间显示
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
        return formatted_time

    def image_to_label(self, img, x, y, w, h):
        # 将OpenCV的图像数据转换为Qt的图像格式
        height, width, channel = img.shape
        bytes_per_line = 3 * width  # 假设图像为RGB格式
        self.q_img = QtGui.QImage(img.data, width, height, bytes_per_line, QtGui.QImage.Format_RGB888)

        # 将Qt的图像格式转换为QPixmap并发送信号
        self.pixmap = QtGui.QPixmap.fromImage(self.q_img)
        self.scaled_pixmap = self.pixmap.scaled(w, h)  # 设置缩小后的大小为200x150

        # 在标签上绘制缩小后的图像
        self.image = QtGui.QImage(self.UI_BIO.label_3.size(), QtGui.QImage.Format_ARGB32)
        self.image.fill(QtGui.QColor(0, 0, 0))
        self.painter = QtGui.QPainter(self.image)
        self.painter.drawPixmap(x, y, self.scaled_pixmap)  # 在坐标(20, 30)处绘制缩小后的图像
        self.painter.end()

        # 在标签上显示绘制后的图像-
        self.UI_BIO.label_3.setPixmap(QtGui.QPixmap.fromImage(self.image))
        self.UI_BIO.label_3.setScaledContents(True)
        self.UI_BIO.label_3.setStyleSheet("background-color: transparent;")

    def add_image_to_label(self, img, x, y, w, h):
        height, width, channel = img.shape
        bytes_per_line = 3 * width  # 假设图像为RGB格式
        self.q_img = QtGui.QImage(img.data, width, height, bytes_per_line, QtGui.QImage.Format_RGB888)

        # 将Qt的图像格式转换为QPixmap并设置到label上
        self.pixmap = QtGui.QPixmap.fromImage(self.q_img)
        # 获取原始的QPixmap对象
        self.original_pixmap = self.UI_BIO.label_3.pixmap()

        # 将缩小后的图像叠加到原始图像上
        self.scaled_pixmap = self.pixmap.scaled(w, h)  # 设置缩小后的大小为200x150
        if self.original_pixmap is None:
            self.original_pixmap = self.pixmap

        self.merged_pixmap = self.original_pixmap.copy()  # 复制原始图像
        self.merged_painter = QtGui.QPainter(self.merged_pixmap)
        self.merged_painter.drawPixmap(x, y, self.scaled_pixmap)  # 在坐标(0, 0)处绘制缩小后的图像
        self.merged_painter.end()

        # 将叠加后的图像转换为QImage对象并显示在标签上
        self.merged_image = QtGui.QImage(self.merged_pixmap.toImage())
        self.UI_BIO.label_3.setPixmap(QtGui.QPixmap.fromImage(self.merged_image))

    @QtCore.Slot(int, list)
    def upimage(self, a, Point_XY):
        if a == 1:
            self.image_to_label(self.imglist[a - 1],
                                Point_XY[0] * int(
                                    self.UI_BIO.label_3.width() / int(self.number_x)),
                                (int(self.number_y) - 1 - Point_XY[1]) * int(
                                    self.UI_BIO.label_3.height() / int(self.number_y)),
                                int(self.UI_BIO.label_3.width() / int(self.number_x)),
                                int(self.UI_BIO.label_3.height() / int(self.number_y)))
        else:
            self.add_image_to_label(self.imglist[a - 1],
                                    Point_XY[0] * int(
                                        self.UI_BIO.label_3.width() / int(self.number_x)),
                                    (int(self.number_y) - 1 - Point_XY[1]) * int(
                                        self.UI_BIO.label_3.height() / int(self.number_y)),
                                    int(self.UI_BIO.label_3.width() / int(self.number_x)),
                                    int(self.UI_BIO.label_3.height() / int(self.number_y)))

    @QtCore.Slot(int)
    def updateZpos_point(self, pointflag):
        if pointflag == 1:
            self.fcous_pos_z_mm_1 = self.motion.navigationController.z_pos_mm
        elif pointflag == 2:
            self.fcous_pos_z_mm_2 = self.motion.navigationController.z_pos_mm
        elif pointflag == 3:
            self.fcous_pos_z_mm_3 = self.motion.navigationController.z_pos_mm
        elif pointflag == 4:
            self.fcous_pos_z_mm_4 = self.motion.navigationController.z_pos_mm

    @QtCore.Slot()
    def updateZpos(self):
        self.fcous_pos_z_mm = self.motion.navigationController.z_pos_mm

    @QtCore.Slot()
    def updateZpossave(self):
        self.fcous_pos_z_mm_save = self.motion.navigationController.z_pos_mm

    @QtCore.Slot()
    def update(self):
        self.UI_BIO.lineEdit_information.setText(
            '玻片ID：' + self.ID + '     ' + '扫描区域大小：' + str(self.scan_w) + 'x' + str(self.scan_h)
            + '     ' + '宽:' + str(self.w * self.calibration) + '     ' + '高:' + str(
                self.h * self.calibration)
            + '     ' + self.Focusing_method + ':' + self.multiple)

    def first_point(self, pointflag):
        # 第一次对焦更新z
        # 初步位置
        img = self.get_focus_image()
        definition1 = self.Sharpness_func(img)
        self.posz_mm.emit()
        if pointflag != 0:
            self.posz_mm_point.emit(pointflag)
        time.sleep(0.1)

        for i in range(20):
            # 往下0.01mm
            self.motion.navigationController.move_z_to(self.posz + 0.002 * (i + 1))
            while self.motion.microcontroller.is_busy():
                time.sleep(0.005)
            img = self.get_focus_image()
            self.fcous_image.emit(img)
            definition2 = self.Sharpness_func(img)
            if definition2 > definition1:
                definition1 = definition2
                self.posz_mm.emit()
                if pointflag != 0:
                    self.posz_mm_point.emit(pointflag)
                time.sleep(0.1)

        return definition1

    def start_move(self):
        if (
                self.ListXY is None and self.Focusing_method is None and self.camera is None and self.Sharpness_func is None
                and self.motion is None):
            formatted_time = self.get_time()
            self.UI_BIO.log.append(formatted_time + '     ' + '!设备未完全加载，不能扫描!')
        else:
            self.read_config()
            self.imglist = []
            Zlist = []
            time_start = time.time()  # 开始计时
            # 计算路径
            points = self.get_route()
            # 创建新的拼接图
            self.numberw = max(self.ListXY, key=lambda x: x[0])[0]+1
            self.numberh = max(self.ListXY, key=lambda x: x[1])[1]+1
            if self.numberw*self.numberh==len(self.ListXY):
                self.Stitch_pic = Image.new("RGB", size=(self.numberw * 320, self.numberh * 320))
                try:
                    self.upData.emit()
                    self.Graph_class = Graph()
                    # 录入数据库一级、二级标题
                    PP_code = Data_1and2(self.Graph_class, self.ID, self.multiple, self.Focusing_method, self.ListXY)
                    if self.Focusing_method == '快速扫描一':
                        formatted_time = self.get_time()
                        self.UI_BIO.log.append(formatted_time + '     ' + '!开始扫描!')
                        self.clear_point.emit()
                        # 初始点位
                        self.motion.navigationController.move_x_to(self.center_x)
                        self.motion.navigationController.move_y_to(self.center_y)
                        self.motion.navigationController.move_z_to(self.posz)
                        while self.motion.microcontroller.is_busy():
                            time.sleep(0.005)
                        definition = self.first_point(0)

                        # 校正精度
                        self.motion.navigationController.move_z_to(self.posz)
                        while self.motion.microcontroller.is_busy():
                            time.sleep(0.005)
                        B = 1
                        while True:
                            # 往下0.01mm
                            self.motion.navigationController.move_z_to(self.posz + 0.001 * B)
                            while self.motion.microcontroller.is_busy():
                                time.sleep(0.005)
                            img = self.get_focus_image()
                            self.fcous_image.emit(img)
                            definition2 = self.Sharpness_func(img)
                            if abs(definition - definition2) / definition < 0.05:
                                img = self.get_focus_image()
                                self.posz_mm.emit()
                                time.sleep(0.1)
                                break
                            B = B + 1
                        a = 1
                        self.posz_mm_save.emit()
                        for Point_XY in self.ListXY:
                            if not self.FLAGE:
                                result = 2 / 0
                            self.motion.navigationController.move_x_to(
                                self.x_mm + Point_XY[0] * self.w * self.calibration)
                            self.motion.navigationController.move_y_to(
                                self.y_mm + Point_XY[1] * self.h * self.calibration)
                            while self.motion.microcontroller.is_busy():
                                time.sleep(0.005)
                            self.point.emit()
                            img = self.get_focus_image()
                            self.fcous_image.emit(img)
                            self.imglist.append(img)
                            Zlist.append(self.fcous_pos_z_mm_save)
                            self.uplabel1.emit(a, Point_XY)
                            self.save_data.emit(PP_code, a, Point_XY, Zlist)
                            a = a + 1
                        formatted_time = self.get_time()
                        self.UI_BIO.log.append(formatted_time + '     ' + '!扫描完成!')
                        self.UI_BIO.result.append(self.ID + '     ' + '已扫描')
                    elif self.Focusing_method == '快速扫描二':
                        formatted_time = self.get_time()
                        self.UI_BIO.log.append(formatted_time + '     ' + '!开始扫描!')
                        self.clear_point.emit()
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
                            self.motion.navigationController.move_x_to(
                                self.x_mm + Point_XY[0] * self.w * self.calibration)
                            self.motion.navigationController.move_y_to(
                                self.y_mm + Point_XY[1] * self.h * self.calibration)
                            if Point_XY[2] == 1:
                                self.motion.navigationController.move_z_to(self.fcous_pos_z_mm_1)
                                self.fcous_pos_z_mm_save = self.fcous_pos_z_mm_1
                            elif Point_XY[2] == 2:
                                self.motion.navigationController.move_z_to(self.fcous_pos_z_mm_2)
                                self.fcous_pos_z_mm_save = self.fcous_pos_z_mm_2
                            elif Point_XY[2] == 3:
                                self.motion.navigationController.move_z_to(self.fcous_pos_z_mm_3)
                                self.fcous_pos_z_mm_save = self.fcous_pos_z_mm_3
                            elif Point_XY[2] == 4:
                                self.motion.navigationController.move_z_to(self.fcous_pos_z_mm_4)
                                self.fcous_pos_z_mm_save = self.fcous_pos_z_mm_4
                            while self.motion.microcontroller.is_busy():
                                time.sleep(0.005)
                            self.point.emit()
                            ############
                            img = self.get_focus_image()
                            self.fcous_image.emit(img)
                            self.imglist.append(img)
                            Zlist.append(self.fcous_pos_z_mm_save)
                            self.uplabel1.emit(a, Point_XY)
                            self.save_data.emit(PP_code, a, Point_XY, Zlist)
                            a = a + 1
                        formatted_time = self.get_time()
                        self.UI_BIO.log.append(formatted_time + '     ' + '!扫描完成!')

                        self.UI_BIO.result.append(self.ID + '     ' + '已扫描')
                    elif self.Focusing_method == '精准扫描':
                        # 初始点位
                        self.motion.navigationController.move_x_to(self.center_x)
                        self.motion.navigationController.move_y_to(self.center_y)
                        self.motion.navigationController.move_z_to(self.posz)
                        while self.motion.microcontroller.is_busy():
                            time.sleep(0.005)
                        definition = self.first_point(0)
                        # 校正精度
                        self.motion.navigationController.move_z_to(self.posz)
                        while self.motion.microcontroller.is_busy():
                            time.sleep(0.005)
                        print(self.posz)
                        B = 1
                        while True:
                            # 往下0.01mm
                            self.motion.navigationController.move_z_to(self.posz + 0.001 * B)
                            while self.motion.microcontroller.is_busy():
                                time.sleep(0.005)
                            img = self.get_focus_image()
                            self.fcous_image.emit(img)
                            definition2 = self.Sharpness_func(img)
                            if abs(definition - definition2) / definition < 0.05:
                                self.posz_mm.emit()
                                time.sleep(0.1)
                                break
                            B = B + 1
                        a = 1
                        formatted_time = self.get_time()
                        self.UI_BIO.log.append(formatted_time + '     ' + '!开始扫描!')
                        self.clear_point.emit()
                        for Point_XY in self.ListXY:
                            qingxidu_max = 0
                            if not self.FLAGE:
                                result = 2 / 0
                            self.motion.navigationController.move_x_to(
                                self.x_mm + Point_XY[0] * self.w * self.calibration)
                            self.motion.navigationController.move_y_to(
                                self.y_mm + Point_XY[1] * self.h * self.calibration)
                            while self.motion.microcontroller.is_busy():
                                time.sleep(0.005)
                            if a % 2 == 0:
                                for i in range(5):
                                    self.motion.navigationController.move_z_to(
                                        (self.fcous_pos_z_mm - 0.005) + 0.002 * (i + 1))
                                    while self.motion.microcontroller.is_busy():
                                        time.sleep(0.005)
                                    img = self.get_focus_image()
                                    self.fcous_image.emit(img)
                                    definition1 = self.Sharpness_func(img)
                                    if i == 0:
                                        qingxidu_max = definition1
                                        self.MaxImg = img
                                        self.fcous_pos_z_mm_save = self.fcous_pos_z_mm - 0.010 + 0.001 * (i + 1)
                                    else:
                                        if definition1 > qingxidu_max:
                                            qingxidu_max = definition1
                                            self.MaxImg = img
                                            self.fcous_pos_z_mm_save = self.fcous_pos_z_mm - 0.010 + 0.001 * (i + 1)
                            else:
                                for i in range(5):
                                    self.motion.navigationController.move_z_to(
                                        (self.fcous_pos_z_mm + 0.005) - 0.002 * (i + 1))
                                    while self.motion.microcontroller.is_busy():
                                        time.sleep(0.005)
                                    img = self.get_focus_image()
                                    self.fcous_image.emit(img)
                                    definition1 = self.Sharpness_func(img)
                                    if i == 0:
                                        qingxidu_max = definition1
                                        self.MaxImg = img
                                        self.fcous_pos_z_mm_save = self.fcous_pos_z_mm + 0.010 - 0.001 * (i + 1)
                                    else:
                                        if definition1 > qingxidu_max:
                                            qingxidu_max = definition1
                                            self.MaxImg = img
                                            self.fcous_pos_z_mm_save = self.fcous_pos_z_mm + 0.010 - 0.001 * (i + 1)

                            self.point.emit()
                            self.fcous_image.emit(self.MaxImg)
                            self.imglist.append(self.MaxImg)
                            Zlist.append(self.fcous_pos_z_mm_save)
                            self.uplabel1.emit(a, Point_XY)

                            self.save_data.emit(PP_code, a, Point_XY, Zlist)

                            a = a + 1
                        formatted_time = self.get_time()
                        self.UI_BIO.log.append(formatted_time + '     ' + '!扫描完成!')
                        self.UI_BIO.result.append(self.ID + '     ' + '已扫描')
                    self.motion.microcontroller.turn_off_illumination()
                    self.motion.navigationController.home_z()
                    time.sleep(0.005)
                    while self.motion.microcontroller.is_busy():
                        time.sleep(0.005)
                    self.motion.navigationController.move_y_to(62.5)
                    time_end = time.time()  # 结束计时
                    time_c = time_end - time_start  # 运行所花时间
                    formatted_time = self.get_time()
                    self.UI_BIO.log.append(formatted_time + '     ' + '!扫描玻片花费时间：' + str(time_c))
                    while self.motion.microcontroller.is_busy():
                        time.sleep(0.005)
                    self.FLAGE = True
                except:
                    Zlist = []
                    self.motion.microcontroller.turn_off_illumination()
                    if not self.FLAGE:
                        self.UI_BIO.log.append(formatted_time + '     ' + '!扫描停止!')
                        self.FLAGE = True
                    else:
                        self.UI_BIO.log.append(formatted_time + '     ' + '!扫描失败!')


