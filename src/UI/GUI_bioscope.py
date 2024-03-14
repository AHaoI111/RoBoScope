import configparser
import re
import threading
import time
from datetime import datetime

import cv2
import numpy
from PIL import Image, ImageDraw
from PySide6 import QtCore, QtGui
from PySide6.QtCore import Signal, Qt
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtWidgets import QMainWindow
from ultralytics import YOLO

from src import ImageSaver
from src import Device
from src import Run
from src.Data import Graph
from src.UI.GUI_img import MyQMainWindow
from src.UI.ui import Ui_MainWindow


def get_time():
    # 获取当前系统时间
    current_time = datetime.now()
    # 格式化时间显示
    formatted_time = current_time.strftime("%Y_%m_%d %H:%M:%S")
    return formatted_time


class MyMainWindow(QMainWindow):
    LIVE_image = Signal(numpy.ndarray)
    LIVE_image_view = Signal(numpy.ndarray)
    display_image_all = Signal(str)
    view_pos = Signal(list, list)

    def __init__(self):
        super().__init__()

        self.posz = None
        self.posxy = None
        self.flage_50x = True
        self.flag = True
        self.flage_run = True
        self.Device = None
        self.G = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.model = YOLO('./model/bioscope_cell.pt')
        self.model(cv2.imread('./model/test.png'), device='cuda:0', conf=0.7, nms=True)
        self.model_bacteria = YOLO('./model/bioscope_bacteria.pt')
        self.model_bacteria(cv2.imread('./model/test.png'), device='cuda:0', imgsz=640, show_labels=False, line_width=1,
                            conf=0.353, verbose=False,
                            agnostic_nms=True)
        self.ImageSaver = ImageSaver.ImageSaver(self.model, self.model_bacteria)
        # 加载界面参数
        # 加载配置
        config = configparser.ConfigParser()
        config.read('config.ini')
        center_x = config.getfloat('Setup', '玻片扫描区域宽度')
        center_y = config.getfloat('Setup', '玻片扫描区域高度')
        focusing_method = config.get('Setup', '对焦方式')
        multiple = config.get('Setup', '对焦倍数')
        self.ui.comboBox_multiple.setCurrentText(multiple)
        self.ui.comboBox_mode.setCurrentText(focusing_method)
        self.ui.comboBox_region.setCurrentText(str(int(center_x)) + 'mmx' + str(int(center_y)) + 'mm')
        #
        self.view_pos.connect(self.view_posxyz)
        # 初始化设备
        self.ui.pushButton_initialize.clicked.connect(self.initialize)
        # 复位
        self.ui.pushButton_reset.clicked.connect(self.reset)
        # 弹出
        self.ui.pushButton_eject.clicked.connect(self.eject)
        # 20x实时and50x实时
        self.ui.pushButton_20Xlive.clicked.connect(self.live_20x)
        self.ui.pushButton_50Xlive.clicked.connect(self.live_50x)
        self.LIVE_image.connect(self.updateLabelimg)
        self.LIVE_image_view.connect(self.updateLabelimg_view)
        self.ui.pushButton_live_close.clicked.connect(self.live_img_close)
        # 扫描
        self.ui.pushButton_run.clicked.connect(self.run)
        # 停止
        self.ui.pushButton_stop.clicked.connect(self.stop)
        # 确认参数
        self.ui.pushButton_save_setup.clicked.connect(self.save_setup)
        # 移动视野
        self.ui.pushButton_move2view.clicked.connect(self.move_to_view)
        # 加载界面参数
        self.ui.pushButton_initialize.setEnabled(True)
        self.ui.pushButton_run.setEnabled(False)
        self.ui.pushButton_stop.setEnabled(False)
        self.ui.pushButton_reset.setEnabled(False)
        self.ui.pushButton_eject.setEnabled(False)
        self.ui.pushButton_50Xlive.setEnabled(False)
        self.ui.pushButton_20Xlive.setEnabled(False)
        self.ui.pushButton_live_close.setEnabled(False)
        self.ui.pushButton_move2view.setEnabled(False)

    @QtCore.Slot(list, list)
    def view_posxyz(self, posxy, posz):
        self.posxy = posxy
        self.posz = posz

    # 双击功能

    def mouseDoubleClickEvent(self, event):
        if event.button() == Qt.LeftButton:
            pos = self.ui.label_camera.mapFromGlobal(event.globalPosition())  # 将全局坐标转换为相对于QLabel的位置像素坐标
            list_pic = []
            ID = self.ui.lineEdit_ID.text()
            Graph_ = self.G
            if ID != '':
                w, h = 5120, 5120
                self.pic2 = Image.new("RGB", size=(w, h))
                code = Graph_.get_IDfromCode(ID + '_' + self.ui.comboBox_multiple.currentText())
                node_info = Graph_.get_node_info(code)
                list_hw = node_info['Data']['视野长宽']
                size = (self.ui.label_camera.pixmap().width(), self.ui.label_camera.pixmap().height())
                if size[0] > 0 and size[1] > 0:
                    w_size = 2 * size[0] / list_hw[1]
                    h_size = 2 * size[1] / list_hw[0]
                    numberx = int(pos.x() / w_size) * 2 + 1
                    numbery = int((pos.y()) / h_size) * 2 + 1
                    # 边缘待优化
                    # 左上角
                    list_pic.append([(numbery - 1) * list_hw[0] + numberx, 0, 0])
                    # 左下角
                    list_pic.append([(numbery + 1) * list_hw[0] - numberx + 1, 0, 1])
                    # 右上角
                    list_pic.append([(numbery - 1) * list_hw[0] + numberx + 1, 1, 0])
                    # 右下角
                    list_pic.append([(numbery + 1) * list_hw[0] - numberx, 1, 1])
                    number_ec = 0
                    number_wbc = 0
                    number_bacteria = 0
                    for i in list_pic:
                        UUID = Graph_.get_IDfromCode('Img' + ID + '_' + str(i[0]))
                        node_info = Graph_.get_node_info(UUID)
                        image = Image.open(node_info['Data']['Image'])
                        image2 = image.resize((int(w / 2), int(h / 2)))
                        bbox_cell = node_info['Data']['bbox_cell']
                        cls_cell = node_info['Data']['Annotation_cell']
                        bbox_bacteria = node_info['Data']['bbox_bacteria']
                        cls_bacteria = node_info['Data']['Annotation_bacteria']
                        draw = ImageDraw.Draw(image2)
                        for point, class_ in zip(bbox_cell, cls_cell):
                            if class_ == 1:
                                color = "blue"
                                number_ec = number_ec + 1
                            else:
                                color = "green"
                                number_wbc = number_wbc + 1
                            draw.rectangle((int(point[0]),
                                            int(point[1]),
                                            int(point[2]),
                                            int(point[3])), outline=color, width=10)
                        color = "red"
                        for point, class_ in zip(bbox_bacteria, cls_bacteria):
                            number_bacteria = number_bacteria + 1
                            draw.rectangle((int(point[0]),
                                            int(point[1]),
                                            int(point[2]),
                                            int(point[3])), outline=color, width=2)

                        self.pic2.paste(image2, box=(i[1] * int(w / 2), i[2] * int(h / 2)))
                        # 左上角view——pos
                        if i == list_pic[0]:
                            posxy = node_info['Data']['Pos_XY_real']
                            posz = node_info['Data']['Pos_Z']
                            self.view_pos.emit(posxy, posz)
                    qimage = QImage(self.pic2.tobytes(), self.pic2.size[0], self.pic2.size[1], QImage.Format_RGB888)
                    # 将 QImage 对象转换为 QPixmap 对象
                    qpixmap = QPixmap.fromImage(qimage)
                    # 创建 MyDialog 对象并显示
                    self.MyQMainWindow = MyQMainWindow(qpixmap, number_ec, number_wbc)
                    self.MyQMainWindow.show()

    # 设备初始化
    def initialize(self):
        # 加载界面参数
        self.ui.pushButton_initialize.setEnabled(False)
        Time = get_time()
        try:
            self.Device = Device.device()
            self.RUN = Run.Run(self.Device, self.ui, self.model, self.ImageSaver, self.up_G)
            #
            self.Device.Microscope_home()
            self.Device.Microscope.navigationController.xyzPos.connect(self.updateLabelXYZpos)

            if self.Device.CameraAll.camera1 is None or self.Device.CameraAll.camera2 is None:
                self.ui.textEdit_log.append('显微镜平台初始化失败' + '           ' + Time)
                self.ui.pushButton_initialize.setEnabled(True)
                self.ui.pushButton_run.setEnabled(False)
                self.ui.pushButton_stop.setEnabled(False)
                self.ui.pushButton_reset.setEnabled(False)
                self.ui.pushButton_eject.setEnabled(False)
                self.ui.pushButton_50Xlive.setEnabled(False)
                self.ui.pushButton_20Xlive.setEnabled(False)
                self.ui.pushButton_live_close.setEnabled(False)
                self.ui.pushButton_move2view.setEnabled(False)
            else:
                self.ui.textEdit_log.append('显微镜平台初始化成功' + '           ' + Time)
                self.ui.pushButton_initialize.setEnabled(False)
                self.ui.pushButton_run.setEnabled(True)
                self.ui.pushButton_stop.setEnabled(True)
                self.ui.pushButton_reset.setEnabled(True)
                self.ui.pushButton_eject.setEnabled(True)
                self.ui.pushButton_50Xlive.setEnabled(True)
                self.ui.pushButton_20Xlive.setEnabled(True)
                self.ui.pushButton_live_close.setEnabled(True)
                self.ui.pushButton_move2view.setEnabled(True)
        except:
            self.ui.pushButton_initialize.setEnabled(True)
            self.ui.pushButton_run.setEnabled(False)
            self.ui.pushButton_stop.setEnabled(False)
            self.ui.pushButton_reset.setEnabled(False)
            self.ui.pushButton_eject.setEnabled(False)
            self.ui.pushButton_50Xlive.setEnabled(False)
            self.ui.pushButton_20Xlive.setEnabled(False)
            self.ui.pushButton_live_close.setEnabled(False)
            self.ui.pushButton_move2view.setEnabled(False)
            self.ui.textEdit_log.append('显微镜平台初始化失败' + '           ' + Time)

    # 设备复位

    def reset(self):
        Time = get_time()
        try:
            self.Device.Microscope_home()
            self.ui.textEdit_log.append('显微镜平台复位成功' + '              ' + Time)
        except:
            self.ui.textEdit_log.append('显微镜平台复位失败' + '              ' + Time)

    # 弹出玻片
    def eject(self):
        Time = get_time()
        try:
            self.Device.Microscope_eject()
            self.ui.textEdit_log.append('显微镜平台弹出成功' + '              ' + Time)
        except:
            self.ui.textEdit_log.append('显微镜平台弹出失败' + '              ' + Time)

    # 扫描
    def run(self):
        self.ui.pushButton_run.setEnabled(False)
        self.ui.pushButton_stop.setEnabled(True)
        self.ui.pushButton_reset.setEnabled(False)
        self.ui.pushButton_eject.setEnabled(False)
        self.ui.pushButton_50Xlive.setEnabled(False)
        self.ui.pushButton_20Xlive.setEnabled(False)
        self.ui.pushButton_live_close.setEnabled(False)
        self.ui.pushButton_move2view.setEnabled(False)
        self.ui.textEdit_infor_only.clear()
        #
        self.Device.Microscope_home()
        # 关闭20x、50x实时
        self.flage_50x = False
        self.flage_20x = False
        time.sleep(0.005)
        while self.Device.Microscope.microcontroller.is_busy():
            time.sleep(0.005)
        self.RUN.number_reset = 0
        self.RUN.run_start()

    # 停止
    def stop(self):
        # self.ui.pushButton_run.setEnabled(True)
        # self.ui.pushButton_reset.setEnabled(True)
        # self.ui.pushButton_eject.setEnabled(True)
        # self.ui.pushButton_50Xlive.setEnabled(True)
        # self.ui.pushButton_20Xlive.setEnabled(True)
        # self.ui.pushButton_live_close.setEnabled(True)
        # self.ui.pushButton_move2view.setEnabled(True)
        Time = get_time()
        # 关闭20x、50x实时
        self.RUN.flage_run = False
        self.ui.textEdit_log.append('显微镜平台停止成功' + '              ' + Time)

    # 保存参数
    def save_setup(self):
        Time = get_time()
        try:
            multiple_ = self.ui.comboBox_multiple.currentText()
            model_ = self.ui.comboBox_mode.currentText()
            region_ = self.ui.comboBox_region.currentText()
            numbers = re.findall(r'\d+', region_)
            # 加载配置
            config = configparser.ConfigParser()
            config.read('config.ini')
            config.set('Setup', '玻片扫描区域宽度', str(numbers[0]))
            config.set('Setup', '玻片扫描区域高度', str(numbers[1]))
            config.set('Setup', '对焦方式', model_)
            config.set('Setup', '对焦倍数', multiple_)
            with open('config.ini', 'w') as configfile:
                config.write(configfile)
            self.ui.textEdit_log.append('显微镜平台确认参数成功' + '        ' + Time)
        except:
            self.ui.textEdit_log.append('显微镜平台确认参数失败' + '        ' + Time)

    @QtCore.Slot(float, float)
    def updateLabelXYZpos(self, xpos, ypos, zpos):
        self.ui.label_x.setNum(xpos)
        self.ui.label_y.setNum(ypos)
        self.ui.label_z.setNum(zpos)

    # 启动20x实时
    def live_20x(self):
        self.ui.pushButton_20Xlive.setEnabled(False)
        self.ui.pushButton_50Xlive.setEnabled(True)
        self.ui.pushButton_move2view.setEnabled(False)
        Time = get_time()
        self.Device.Microscope.navigationController.move_x_to(48.9)
        self.Device.Microscope.navigationController.move_y_to(34.927)
        while self.Device.Microscope.microcontroller.is_busy():
            time.sleep(0.005)
        self.Device.Microscope.navigationController.move_z_to(5.250)
        while self.Device.Microscope.microcontroller.is_busy():
            time.sleep(0.005)
        self.flage_50x = False
        self.flage_20x = True
        self.Device.Microscope.microcontroller.turn_off_illumination()
        self.Device.Microscope.microcontroller.set_illumination(
            self.Device.configuration_Lightpathleft.illumination_source,
            self.Device.configuration_Lightpathleft.illumination_intensity)
        self.Device.Microscope.microcontroller.turn_on_illumination()
        self.thread2 = threading.Thread(target=self.live_img_20x)
        self.thread2.start()
        self.ui.textEdit_log.append('显微镜平台20x物镜' + '              ' + Time)

    # 启动50x实时
    def live_50x(self):
        self.ui.pushButton_20Xlive.setEnabled(True)
        self.ui.pushButton_50Xlive.setEnabled(False)
        self.ui.pushButton_move2view.setEnabled(False)
        Time = get_time()
        self.Device.Microscope.navigationController.home_z()
        while self.Device.Microscope.microcontroller.is_busy():
            time.sleep(0.005)
        self.Device.Microscope.navigationController.move_x_to(13)
        self.Device.Microscope.navigationController.move_y_to(35)
        while self.Device.Microscope.microcontroller.is_busy():
            time.sleep(0.005)
        self.Device.Microscope.navigationController.move_z_to(5.120)
        while self.Device.Microscope.microcontroller.is_busy():
            time.sleep(0.005)
        self.flage_50x = True
        self.flage_20x = False
        self.Device.Microscope.microcontroller.turn_off_illumination()
        self.Device.Microscope.microcontroller.set_illumination(
            self.Device.configuration_Lightpathright.illumination_source,
            self.Device.configuration_Lightpathright.illumination_intensity)
        self.Device.Microscope.microcontroller.turn_on_illumination()
        self.thread2 = threading.Thread(target=self.live_img_50x)
        self.thread2.start()
        self.ui.textEdit_log.append('显微镜平台50x物镜' + '              ' + Time)

    # 复查视野
    def move_to_view(self):
        if self.posz is not None or self.posxy is not None:
            self.Device.Microscope.navigationController.move_x_to(self.posxy[0] + 35.7)
            self.Device.Microscope.navigationController.move_y_to(self.posxy[1] - 0.273)
            while self.Device.Microscope.microcontroller.is_busy():
                time.sleep(0.005)
            self.Device.Microscope.navigationController.move_z_to(self.posz[0])
            while self.Device.Microscope.microcontroller.is_busy():
                time.sleep(0.005)
            self.flage_50x = False
            self.flage_20x = True
            self.Device.Microscope.microcontroller.turn_off_illumination()
            self.Device.Microscope.microcontroller.set_illumination(
                self.Device.configuration_Lightpathleft.illumination_source,
                self.Device.configuration_Lightpathleft.illumination_intensity)
            self.Device.Microscope.microcontroller.turn_on_illumination()
            self.thread2 = threading.Thread(target=self.live_img_20x_view)
            self.thread2.start()
            self.ui.pushButton_50Xlive.setEnabled(False)
            self.ui.pushButton_20Xlive.setEnabled(False)
            self.ui.pushButton_move2view.setEnabled(False)

    def live_img_20x_view(self):
        while True:
            if self.flage_20x:
                if self.Device is not None:
                    self.Device.CameraAll.camera1.send_trigger()
                    image = self.Device.CameraAll.camera1.read_frame()
                    self.LIVE_image_view.emit(image)
            else:
                break

    def live_img_20x(self):
        while True:
            if self.flage_20x:
                if self.Device is not None:
                    self.Device.CameraAll.camera1.send_trigger()
                    image = self.Device.CameraAll.camera1.read_frame()
                    self.LIVE_image.emit(image)
            else:
                break

    def live_img_50x(self):
        while True:
            if self.flage_50x:
                if self.Device is not None:
                    self.Device.CameraAll.camera2.send_trigger()
                    image = self.Device.CameraAll.camera2.read_frame()
                    image = cv2.rotate(image, cv2.ROTATE_180)
                    self.LIVE_image.emit(image)
            else:
                break

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
                                 QtGui.QImage.Format_RGB888)  # 修改为灰度图格式

        pixmap = QtGui.QPixmap.fromImage(q_img)
        scaled_pixmap = pixmap.scaled(self.ui.label_camera.size(), QtCore.Qt.AspectRatioMode.IgnoreAspectRatio)
        # 在标签上显示绘制后的图像
        self.ui.label_camera.setPixmap(scaled_pixmap)

    @QtCore.Slot(numpy.ndarray)
    def updateLabelimg_view(self, numpy_image):
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
                                 QtGui.QImage.Format_RGB888)  # 修改为灰度图格式

        pixmap = QtGui.QPixmap.fromImage(q_img)
        scaled_pixmap = pixmap.scaled(self.ui.label_fcous_img.size(), QtCore.Qt.AspectRatioMode.IgnoreAspectRatio)
        # 在标签上显示绘制后的图像
        self.ui.label_fcous_img.setPixmap(scaled_pixmap)

    # 关闭实时
    def live_img_close(self):
        self.ui.pushButton_20Xlive.setEnabled(True)
        self.ui.pushButton_50Xlive.setEnabled(True)
        self.ui.pushButton_move2view.setEnabled(True)
        self.flage_50x = False
        self.flage_20x = False
        self.Device.Microscope.microcontroller.turn_off_illumination()

    def closeEvent(self, event):
        # 在窗口关闭事件中触发的函数
        self.close_thing()
        event.accept()

    def close_thing(self):
        self.ImageSaver.stop()
        # 执行需要在应用程序退出时触发的操作
        if self.Device is None:
            pass
        else:
            if self.Device.CameraAll.camera1 is None or self.Device.CameraAll.camera2 is None:
                pass
            else:
                self.Device.CameraAll.camera1.close()
                self.Device.CameraAll.camera2.close()
                self.Device.Microscope.microcontroller.close()
                self.ImageSaver.stop()

    def up_G(self):
        self.G = self.RUN.Graph_class
