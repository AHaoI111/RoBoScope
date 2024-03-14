import configparser
import os
import threading
import time
from datetime import datetime

import cv2
import numpy
from PySide6 import QtCore, QtGui
from PySide6.QtCore import Qt, QRect
from PySide6.QtGui import QPainter, QPixmap, QColor, QBrush, QPen, QImage

from src import Route
from src import data
from src import focus
from src.Data.Graph import Graph_slide


def get_time():
    # 获取当前系统时间
    current_time = datetime.now()
    # 格式化时间显示
    formatted_time = current_time.strftime("%Y_%m_%d_%H_%M_%S")
    return formatted_time


class Run(QtCore.QObject):
    updata_label_fcous_img = QtCore.Signal(numpy.ndarray)
    updata_label_img = QtCore.Signal(int, list, numpy.ndarray, int, int)
    updata_point_clear = QtCore.Signal()
    updata_point_draw = QtCore.Signal(float, float, list, float, float, float, float)
    updata_informations = QtCore.Signal(str, float, float, float, float, str, str)
    ok = QtCore.Signal(str, list, list, int, int, float, float, float, float, float, float, numpy.ndarray)

    def __init__(self, Device, ui, model, ImageSaver, up_G):
        super().__init__()
        self.number = 60
        self.step = 0.003
        self.number_reset = 0
        self.thread1 = None
        self.Graph_class = None
        self.Stitch_pic = None
        self.Device = Device
        self.ui = ui
        self.up_G = up_G
        self.model = model
        self.flage_run = True
        self.ImageSaver = ImageSaver

        self.updata_label_fcous_img.connect(self.updateLabelimg)
        self.updata_label_img.connect(self.upimage)
        self.updata_point_clear.connect(self.clear_points)
        self.updata_point_draw.connect(self.updateLabelpoints)
        self.updata_informations.connect(self.updata)
        self.ok.connect(self.finish)
        self.slide_map = QPixmap("./src/480.png")

    def run_start(self):
        self.thread1 = threading.Thread(target=self.start)
        self.thread1.start()

    def read_config(self):
        # 加载配置
        config = configparser.ConfigParser()
        config.read('config.ini')
        center_x_50x = config.getfloat('Setup', '玻片扫描中心x50x')
        center_y_50x = (config.getfloat('Setup', '玻片扫描中心y50x'))
        center_x_20x = config.getfloat('Setup', '玻片扫描中心x20x')
        center_y_20x = (config.getfloat('Setup', '玻片扫描中心y20x'))
        region_w = (config.getfloat('Setup', '玻片扫描区域宽度'))
        region_h = (config.getfloat('Setup', '玻片扫描区域高度'))
        calibration_50 = (config.getfloat('Setup', '像素标定50x'))
        calibration_20 = (config.getfloat('Setup', '像素标定20x'))
        focusing_method = (config.get('Setup', '对焦方式'))
        zpos_start50x = (config.getfloat('Setup', '对焦经验值50x'))
        zpos_start20x = (config.getfloat('Setup', '对焦经验值20x'))
        focu_number = config.getint('Setup', '对焦步数')
        focu_size = config.getfloat('Setup', '对焦分辨率')
        multiple = (config.get('Setup', '对焦倍数'))
        self.ID = self.ui.lineEdit_ID.text()
        self.number_mean_ec = config.getint('合格性', '上皮细胞平均数小于')
        self.number_median_ec = config.getint('合格性', '上皮细胞中位数小于')
        self.number_mean_wbc = config.getint('合格性', '白细胞平均数大于')
        self.number_median_wbc = config.getint('合格性', '白细胞中位数大于')
        if multiple == '50x':
            return center_x_50x, center_y_50x, region_w, region_h, calibration_50, focusing_method, zpos_start50x, multiple, self.ID, focu_number, focu_size
        else:
            return center_x_20x, center_y_20x, region_w, region_h, calibration_20, focusing_method, zpos_start20x, multiple, self.ID, focu_number, focu_size

    @QtCore.Slot(str, list, list, int, int, float, float, float, float, float, float, numpy.ndarray)
    def finish(self, ID, list_window, list_window_bacteria, numberw, numberh, mean_wbc, median_wbc, mean_ec, median_ec,
               mean_bacteria, median_bacteria, img):
        msg = datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '玻片' + ID + '已扫描' + '\n'
        with open("log.txt", "a") as log_file:
            log_file.write(msg)
        # 获取拼接图
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        height, width, channel = img.shape
        qImg = QImage(img.data, width, height, 3 * width, QImage.Format_RGB888)
        # 将QImage转换为QPixmap
        pixmap = QPixmap.fromImage(qImg)
        # pixmap = QPixmap(path)  # 替换为你的图像文件路径
        self.pixmap_scale1 = pixmap.scaled(self.ui.label_camera.size(), QtCore.Qt.IgnoreAspectRatio,
                                           QtCore.Qt.SmoothTransformation)
        self.pixmap_scale2 = pixmap.scaled(self.ui.label_camera.size(), QtCore.Qt.IgnoreAspectRatio,
                                           QtCore.Qt.SmoothTransformation)
        # 推荐视野图
        painter = QPainter(self.pixmap_scale2)
        pen_cell = QPen(Qt.green)
        pen_cell.setWidth(2)
        pen_bacteria = QPen(Qt.red)
        pen_bacteria.setWidth(1)
        painter.setPen(pen_cell)
        view_number = [numberw, numberh]
        for point in list_window:
            x1, y1 = (point[0] % view_number[0] - 1, point[0] // view_number[1])
            painter.drawRect(QRect(int(x1 * self.pixmap_scale2.width() / view_number[0]),
                                   int(y1 * self.pixmap_scale2.height() / view_number[1]),
                                   int(2 * self.pixmap_scale2.width() / view_number[0]),
                                   int(2 * self.pixmap_scale2.height() / view_number[1])))
        painter.setPen(pen_bacteria)
        for point in list_window_bacteria:
            x1, y1 = (point[0] % view_number[0] - 1, point[0] // view_number[1])
            painter.drawRect(QRect(int(x1 * self.pixmap_scale2.width() / view_number[0]),
                                   int(y1 * self.pixmap_scale2.height() / view_number[1]),
                                   int(2 * self.pixmap_scale2.width() / view_number[0]),
                                   int(2 * self.pixmap_scale2.height() / view_number[1])))
        painter.end()
        self.ui.label_camera.setPixmap(self.pixmap_scale2)
        self.ui.textEdit_log.append('显微镜平台处理完成')

        self.ui.textEdit_infor_only.append('玻片ID：' + self.ID + '\n' +
                                           '白细胞平均数：' + str(mean_wbc) + '     ' + '白细胞中位数：' + str(
            median_wbc) + '\n' + '\n' +
                                           '上皮细胞平均数：' + str(mean_ec) + '     ' + '上皮细胞中位数：' + str(
            median_ec) + '\n' + '\n' +
                                           '细菌平均数：' + str(mean_bacteria) + '     ' + '细菌中位数：' + str(
            median_bacteria))
        if mean_ec <= self.number_mean_ec and mean_wbc >= self.number_mean_wbc:
            self.ui.textEdit_infor_only.append(self.ID + '该玻片合格')
        else:
            if median_ec <= self.number_median_ec and median_wbc >= self.number_median_wbc:
                self.ui.textEdit_infor_only.append(self.ID + '该玻片合格')
            else:
                self.ui.textEdit_infor_only.append(self.ID + '该玻片不合格')

        self.ui.pushButton_50Xlive.setEnabled(True)
        self.ui.pushButton_20Xlive.setEnabled(True)
        self.ui.pushButton_live_close.setEnabled(True)
        self.ui.pushButton_move2view.setEnabled(True)
        self.ui.pushButton_run.setEnabled(True)
        self.up_G()
        # self.ui.pushButton_run.click()

    @QtCore.Slot(numpy.ndarray)
    def updateLabelimg(self, numpy_image):
        channel = len(numpy_image.shape)
        if channel == 2:
            height, width = numpy_image.shape  # 获取图像的高度和宽度
            bytes_per_line = width  # 假设图像为灰度图
            q_img = QtGui.QImage(bytes(numpy_image.data), width, height, bytes_per_line,
                                 QtGui.QImage.Format_Grayscale8)  # 修改为灰度图格式
        else:
            height, width, _ = numpy_image.shape  # 获取图像的高度和宽度
            bytes_per_line = 3 * width  # 假设图像为彩色图
            q_img = QtGui.QImage(bytes(numpy_image.data), width, height, bytes_per_line,
                                 QtGui.QImage.Format_RGB888)  # 修改为灰度图格式)
        pixmap = QtGui.QPixmap.fromImage(q_img)
        scaled_pixmap = pixmap.scaled(480, 480)  # 设置缩小后的大小为200x150
        # 在标签上显示绘制后的图像
        self.ui.label_fcous_img.setPixmap(scaled_pixmap)

    def image_to_label(self, a, img, x, y, w, h):
        if a == 1:
            # 创建一个新的黑色图像
            image = QtGui.QImage(self.ui.label_camera.size(), QtGui.QImage.Format_RGB888)
            image.fill(QtGui.QColor(0, 0, 0))

            # 在标签上显示黑色图像
            self.ui.label_camera.setPixmap(QtGui.QPixmap.fromImage(image))
            self.ui.label_camera.setScaledContents(True)
            self.ui.label_camera.setStyleSheet("background-color: transparent;")
        # 获取现有图像
        current_pixmap = self.ui.label_camera.pixmap()

        # 创建一个新的绘图对象，并将现有的图像绘制到其中
        image = QtGui.QImage(self.ui.label_camera.size(), QtGui.QImage.Format_RGB888)
        image.fill(QtGui.QColor(0, 0, 0))
        painter = QtGui.QPainter(image)
        painter.drawPixmap(0, 0, current_pixmap)

        # 将OpenCV的图像数据转换为Qt的图像格式
        channel = len(img.shape)
        if channel == 2:
            height, width = img.shape  # 获取图像的高度和宽度
            bytes_per_line = width  # 假设图像为灰度图
            q_img = QtGui.QImage(bytes(img.data), width, height, bytes_per_line,
                                 QtGui.QImage.Format_Grayscale8)  # 修改为灰度图格式
        else:
            height, width, _ = img.shape  # 获取图像的高度和宽度
            bytes_per_line = 3 * width  # 假设图像为彩色图
            q_img = QtGui.QImage(bytes(img.data), width, height, bytes_per_line,
                                 QtGui.QImage.Format_RGB888)  # 修改为灰度图格式

        # 将Qt的图像格式转换为QPixmap并绘制到现有图像上
        pixmap = QtGui.QPixmap.fromImage(q_img)
        scaled_pixmap = pixmap.scaled(w, h)
        painter.drawPixmap(x, y, scaled_pixmap)
        painter.end()

        # 在标签上显示绘制后的图像
        self.ui.label_camera.setPixmap(QtGui.QPixmap.fromImage(image))
        self.ui.label_camera.setScaledContents(True)
        self.ui.label_camera.setStyleSheet("background-color: transparent;")

    @QtCore.Slot(int, list, numpy.ndarray, int, int)
    def upimage(self, a, Point_XY, img, number_x, number_y):
        self.image_to_label(a, img,
                            Point_XY[1] * int(
                                self.ui.label_camera.width() / int(number_y)),
                            (Point_XY[0]) * int(
                                self.ui.label_camera.height() / int(number_x)),
                            int(self.ui.label_camera.width() / int(number_y)),
                            int(self.ui.label_camera.height() / int(number_x)))

    @QtCore.Slot()
    def clear_points(self):
        pixmap = self.ui.label_slide.pixmap()
        painter = QPainter(pixmap)
        painter.setRenderHint(QPainter.Antialiasing)

        # 清空整个背景
        painter.eraseRect(pixmap.rect())
        painter.end()
        self.ui.label_slide.setPixmap(self.slide_map)  # 将绘制结果设置给QLabel的pixmap
        self.ui.label_slide.update()  # 强制刷新QLabel的显示

    # 绘制红点
    @QtCore.Slot(float, float, list, float, float, float, float)
    def updateLabelpoints(self, center_x, center_y, point, wcalibration, hcalibration, region_width, region_height):
        pixmap = self.ui.label_slide.pixmap()  # 获取QPixmap对象
        painter = QPainter(pixmap)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(QColor(255, 0, 0))
        painter.setBrush(QBrush(QColor(255, 0, 0)))
        radius = 2
        if region_width < 8:
            painter.drawEllipse(
                int(110 + (point[1]) * 4),
                int(50 + (point[0]) * 4),
                radius,
                radius)
        elif region_width < 15:
            painter.drawEllipse(
                int(94 + (point[1]) * 4),
                int(25 + (point[0]) * 4),
                radius,
                radius)
        else:
            painter.drawEllipse(
                int(94 + (point[1]) * 3),
                int(10 + (point[0]) * 3),
                radius,
                radius)

        painter.end()
        self.ui.label_slide.setPixmap(pixmap)  # 将绘制结果设置给QLabel的pixmap
        self.ui.label_slide.update()  # 强制刷新QLabel的显示

    @QtCore.Slot(str, float, float, float, float, str, str)
    def updata(self, ID, region_w, region_h, img_w, img_h, focusing_method,
               multiple):
        self.ui.lineEdit_slide.setText(
            '玻片ID：' + ID + '     ' + '扫描区域大小：' + str(region_w) + 'x' + str(region_h)
            + '     ' + '宽:' + str(img_w) + '     ' + '高:' + str(img_h)
            + '     ' + focusing_method + ':' + multiple)

    def get_image_camera20x(self):

        self.Device.Microscope.microcontroller.turn_on_illumination()
        time.sleep(0.0005)
        self.Device.CameraAll.camera1.send_trigger()
        image = self.Device.CameraAll.camera1.read_frame()
        self.Device.Microscope.microcontroller.turn_off_illumination()
        return image

    def get_image_camera50x(self):
        self.Device.Microscope.microcontroller.turn_on_illumination()
        time.sleep(0.0005)
        self.Device.CameraAll.camera2.send_trigger()
        image = self.Device.CameraAll.camera2.read_frame()
        image = cv2.rotate(image, cv2.ROTATE_180)
        self.Device.Microscope.microcontroller.turn_off_illumination()
        return image

    def Focus_on(self, multiple, zpos_start):
        imgmax = None
        zpos = zpos_start
        try:
            if self.flage_run:
                pass
            else:
                result = 2 / 0
            # 初步位置
            img = None
            if multiple == '20x':
                img = self.get_image_camera20x()
            elif multiple == '50x':
                img = self.get_image_camera50x()
            imgmax = img
            self.updata_label_fcous_img.emit(img)
            definition1 = focus.Sharpness(img)
            zpos = self.Device.Microscope.navigationController.z_pos_mm
            for i in range(self.number):
                # 往下
                self.Device.Microscope.navigationController.move_z_to(zpos_start + self.step * (i + 1))
                while self.Device.Microscope.microcontroller.is_busy():
                    time.sleep(0.005)
                if multiple == '20x':
                    img = self.get_image_camera20x()
                elif multiple == '50x':
                    img = self.get_image_camera50x()
                self.updata_label_fcous_img.emit(img)
                definition2 = focus.Sharpness(img)
                if definition2 > definition1:
                    definition1 = definition2
                    zpos = self.Device.Microscope.navigationController.z_pos_mm
                    imgmax = img
                    time.sleep(0.005)
        except:
            pass

        return zpos, imgmax

    def start(self):
        self.flage_run = True
        self.ui.textEdit_log.append('显微镜平台开始扫描')
        self.ui.textEdit_log.append('请等待...')
        time_start = time.time()  # 开始计时
        center_x, center_y, region_w, region_h, calibration, focusing_method, zpos_start, multiple, ID, focus_numnber, focus_size = self.read_config()
        # 检查文件夹路径是否存在
        path_save = 'pic\\' + ID + '\\' + multiple
        folder_path = os.path.join(path_save)
        if not os.path.exists(folder_path):
            # 如果路径不存在，则创建文件夹
            os.makedirs(folder_path)
        # 移动到预设位置
        self.Device.Microscope.navigationController.move_x_to(
            center_x)
        self.Device.Microscope.navigationController.move_y_to(
            center_y)
        while self.Device.Microscope.microcontroller.is_busy():
            time.sleep(0.005)
        self.Device.Microscope.navigationController.move_z_to(zpos_start)
        while self.Device.Microscope.microcontroller.is_busy():
            time.sleep(0.005)
        # 判断倍数确认光源设置
        if multiple == '50x':
            self.Device.Microscope.microcontroller.set_illumination(
                self.Device.configuration_Lightpathright.illumination_source,
                self.Device.configuration_Lightpathright.illumination_intensity)
            img = self.get_image_camera50x()
        elif multiple == '20x':
            self.Device.Microscope.microcontroller.set_illumination(
                self.Device.configuration_Lightpathleft.illumination_source,
                self.Device.configuration_Lightpathleft.illumination_intensity)
            img = self.get_image_camera20x()

        points_4, points_xy, x_Start, y_Start, number_x, number_y, h, w = Route.get_route(img, center_x, center_y,
                                                                                          region_w,
                                                                                          region_h, calibration)
        self.updata_informations.emit(ID, region_w, region_h, calibration * w, calibration * h, focusing_method,
                                      multiple)
        # 清空点位
        self.updata_point_clear.emit()
        self.Graph_class = Graph_slide(ID)
        try:
            # 录入数据库一级、二级标题
            root_id = data.Save_data_1(self.Graph_class, ID)

            PP_code = data.Save_data_2(self.Graph_class, root_id, ID, multiple, focusing_method,
                                       number_x, number_y)
            # 扫描方式
            if focusing_method == '快速扫描二':
                self.number = focus_numnber
                self.step = focus_size
                zpos_4 = []
                a = 1
                for point in points_4:
                    self.Device.Microscope.navigationController.move_x_to(point[0])
                    self.Device.Microscope.navigationController.move_y_to(point[1])
                    while self.Device.Microscope.microcontroller.is_busy():
                        time.sleep(0.005)
                    self.Device.Microscope.navigationController.move_z_to(zpos_start)
                    while self.Device.Microscope.microcontroller.is_busy():
                        time.sleep(0.005)
                    zpos, _ = self.Focus_on(multiple, zpos_start)
                    zpos_4.append(zpos)
                for Point_XY in points_xy:
                    if self.flage_run:
                        pass
                    else:
                        result = 2 / 0
                    self.Device.Microscope.navigationController.move_x_to(
                        x_Start - (Point_XY[0] + 0.5) * w * calibration)
                    self.Device.Microscope.navigationController.move_y_to(
                        y_Start - (Point_XY[1] + 0.5) * h * calibration)
                    if Point_XY[2] == 1:
                        self.Device.Microscope.navigationController.move_z_to(zpos_4[0])
                        zpos = zpos_4[0]
                    elif Point_XY[2] == 2:
                        self.Device.Microscope.navigationController.move_z_to(zpos_4[1])
                        zpos = zpos_4[1]
                    elif Point_XY[2] == 3:
                        self.Device.Microscope.navigationController.move_z_to(zpos_4[2])
                        zpos = zpos_4[2]
                    elif Point_XY[2] == 4:
                        self.Device.Microscope.navigationController.move_z_to(zpos_4[3])
                        zpos = zpos_4[3]
                    while self.Device.Microscope.microcontroller.is_busy():
                        time.sleep(0.005)
                    self.updata_point_draw.emit(center_x, center_y, Point_XY, w * calibration, h * calibration,
                                                region_w, region_h)
                    if multiple == '20x':
                        img = self.get_image_camera20x()
                    elif multiple == '50x':
                        img = self.get_image_camera50x()

                    self.updata_label_fcous_img.emit(img)
                    self.updata_label_img.emit(a, Point_XY, img, number_x, number_y)
                    point_xy_real = [x_Start - (Point_XY[0] + 0.5) * w * calibration,
                                     y_Start - (Point_XY[1] + 0.5) * h * calibration]

                    # 粘贴拼图
                    # img_np = cv2.resize(img, (320, 320))
                    # img_pil = Image.fromarray(img_np)
                    # self.Stitch_pic.paste(img_pil, box=(Point_XY[1] * 320, Point_XY[0] * 320))
                    timesave = get_time()
                    # 保存原图
                    bgr_image = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
                    self.ImageSaver.enqueue(bgr_image, self.Graph_class, PP_code, ID, zpos, a, Point_XY, timesave,
                                            path_save, number_x, number_y, self.ok, point_xy_real,
                                            multiple)
                    a = a + 1
            elif focusing_method == '快速扫描一':
                self.number = focus_numnber
                self.step = focus_size
                a = 1
                self.Device.Microscope.navigationController.move_x_to(
                    center_x)
                self.Device.Microscope.navigationController.move_y_to(
                    center_y)
                while self.Device.Microscope.microcontroller.is_busy():
                    time.sleep(0.005)
                zpos, _ = self.Focus_on(multiple, zpos_start)
                for Point_XY in points_xy:
                    if self.flage_run:
                        pass
                    else:
                        result = 2 / 0
                    self.Device.Microscope.navigationController.move_x_to(
                        x_Start - (Point_XY[0] + 0.5) * w * calibration)
                    self.Device.Microscope.navigationController.move_y_to(
                        y_Start - (Point_XY[1] + 0.5) * h * calibration)
                    while self.Device.Microscope.microcontroller.is_busy():
                        time.sleep(0.005)
                    self.Device.Microscope.navigationController.move_z_to(zpos)
                    while self.Device.Microscope.microcontroller.is_busy():
                        time.sleep(0.005)
                    self.updata_point_draw.emit(center_x, center_y, Point_XY, w * calibration, h * calibration,
                                                region_w, region_h)
                    if multiple == '20x':
                        img = self.get_image_camera20x()
                    elif multiple == '50x':
                        img = self.get_image_camera50x()
                    self.updata_label_fcous_img.emit(img)
                    self.updata_label_img.emit(a, Point_XY, img, number_x, number_y)
                    point_xy_real = [x_Start - (Point_XY[0] + 0.5) * w * calibration,
                                     y_Start - (Point_XY[1] + 0.5) * h * calibration]

                    timesave = get_time()
                    # 保存原图
                    bgr_image = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
                    self.ImageSaver.enqueue(bgr_image, self.Graph_class, PP_code, ID, zpos, a, Point_XY, timesave,
                                            path_save, number_x, number_y, self.ok, point_xy_real,
                                            multiple)
                    a = a + 1
            elif focusing_method == '精准扫描':
                self.number = focus_numnber
                self.step = focus_size
                self.Device.Microscope.navigationController.move_x_to(
                    center_x)
                self.Device.Microscope.navigationController.move_y_to(
                    center_y)
                while self.Device.Microscope.microcontroller.is_busy():
                    time.sleep(0.005)
                zpos, _ = self.Focus_on(multiple, zpos_start)
                zpos_start = zpos
                if multiple == '50x':
                    self.number = 20
                    self.step = 0.001
                elif multiple == '20x':
                    self.number = 10
                    self.step = 0.002

                a = 1
                for Point_XY in points_xy:
                    if self.flage_run:
                        pass
                    else:
                        result = 2 / 0
                    self.Device.Microscope.navigationController.move_x_to(
                        x_Start - (Point_XY[0] + 0.5) * w * calibration)
                    self.Device.Microscope.navigationController.move_y_to(
                        y_Start - (Point_XY[1] + 0.5) * h * calibration)
                    while self.Device.Microscope.microcontroller.is_busy():
                        time.sleep(0.005)
                    zpos, img = self.Focus_on(multiple, zpos_start - 0.01)

                    self.updata_point_draw.emit(center_x, center_y, Point_XY, w * calibration, h * calibration,
                                                region_w, region_h)

                    self.updata_label_fcous_img.emit(img)
                    self.updata_label_img.emit(a, Point_XY, img, number_x, number_y)
                    point_xy_real = [x_Start - (Point_XY[0] + 0.5) * w * calibration,
                                     y_Start - (Point_XY[1] + 0.5) * h * calibration]
                    timesave = get_time()
                    # 保存原图
                    bgr_image = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
                    self.ImageSaver.enqueue(bgr_image, self.Graph_class, PP_code, ID, zpos, a, Point_XY, timesave,
                                            path_save, number_x, number_y, self.ok, point_xy_real,
                                            multiple)
                    a = a + 1
            time_end = time.time()  # 结束计时
            time_c = time_end - time_start  # 运行所花时间
            self.ui.textEdit_log.append('显微镜平台扫描完成')
            self.ui.textEdit_log.append('显微镜平台扫描费时' + str(time_c))

            self.ui.textEdit_log.append('显微镜平台还未处理完成')
            self.ui.textEdit_log.append('请等待...')
            self.Device.Microscope.navigationController.home_z()
            while self.Device.Microscope.microcontroller.is_busy():
                time.sleep(0.005)
            self.Device.Microscope.navigationController.move_y_to(55)
            while self.Device.Microscope.microcontroller.is_busy():
                time.sleep(0.005)
            self.ui.pushButton_run.setEnabled(True)
            self.ui.pushButton_reset.setEnabled(True)
            self.ui.pushButton_eject.setEnabled(True)
            self.ui.pushButton_50Xlive.setEnabled(True)
            self.ui.pushButton_20Xlive.setEnabled(True)
            self.ui.pushButton_live_close.setEnabled(True)
            self.ui.pushButton_move2view.setEnabled(True)
        except Exception as e:
            while self.Device.Microscope.microcontroller.is_busy():
                time.sleep(0.005)
            error_msg = datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\n'
            with open("log.txt", "a") as log_file:
                log_file.write(error_msg + str(e))
            self.flage_50x = False
            self.flage_20x = False
            self.ui.pushButton_run.setEnabled(True)
            self.ui.pushButton_reset.setEnabled(True)
            self.ui.pushButton_eject.setEnabled(True)
            self.ui.pushButton_50Xlive.setEnabled(True)
            self.ui.pushButton_20Xlive.setEnabled(True)
            self.ui.pushButton_live_close.setEnabled(True)
            self.ui.pushButton_move2view.setEnabled(True)
            self.ui.textEdit_log.append('显微镜平台扫描失败')
