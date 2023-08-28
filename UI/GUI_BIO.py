import sys
import threading
import time
from datetime import datetime

import cv2
import numpy
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QObject
from PyQt5.QtGui import QPixmap
from qtpy.QtCore import *
from qtpy.QtGui import *
from qtpy.QtWidgets import *
from ultralytics import YOLO

import control.camera_daheng as camera
import control.motion as motion
import control.move as move
from UI.BIOscope import Ui_MainWindow
from UI.GUI_setup import MyDialog
import UI.GUI_Data as GUI_Data


class MyWindow(QMainWindow, QObject):
    point = Signal()
    clear_point = Signal()
    fcous_image = Signal(numpy.ndarray)

    def __init__(self):
        super().__init__()
        QObject.__init__(self)

        # 实例化 Ui_MainWindow
        self.ui = Ui_MainWindow()
        # 将 ui 设置为当前窗口的界面
        self.ui.setupUi(self)
        ####
        self.motion = None
        self.camera = None
        self.MXAimg = None
        self.model = YOLO('UI/model/best.pt')
        self.model(cv2.imread('UI/model/test.png'), device='cuda:0', conf=0.5, nms=True)

        # 示意图
        self.Sketch_map = QPixmap('./control/Sketch.png').scaled(438, 365)
        self.ui.Sketch_map.setPixmap(self.Sketch_map)

        # 设置中心
        self.ui.Setup.clicked.connect(self.set_up)  # type: ignore

        # 设备初始化
        self.ui.Initialize_device.clicked.connect(self.device)
        # 复位
        self.ui.move_home.clicked.connect(self.motion_home)  # type: ignore
        # 停止
        self.ui.move_stop.clicked.connect(self.motion_stop)  # type: ignore
        # 单张
        self.ui.move_only.clicked.connect(self.motion_only)  # type: ignore
        # 数据
        self.ui.pushButton_Data.clicked.connect(self.Data)  # type: ignore

    def Data(self):
        GUI_Data.display()

    def set_up(self):
        # 创建 MyDialog 对象并显示
        self.dialog = MyDialog()
        self.dialog.show()

    # 将图片显示在界面
    def image_to_label(self, img, x, y, w, h):
        # 将OpenCV的图像数据转换为Qt的图像格式

        self.MXAimg = img
        height, width, channel = self.MXAimg.shape
        bytes_per_line = 3 * width  # 假设图像为RGB格式
        q_img = QtGui.QImage(self.MXAimg.data, width, height, bytes_per_line, QtGui.QImage.Format_RGB888)

        # 将Qt的图像格式转换为QPixmap并发送信号
        pixmap = QtGui.QPixmap.fromImage(q_img)
        scaled_pixmap = pixmap.scaled(w, h)  # 设置缩小后的大小为200x150

        # 在标签上绘制缩小后的图像
        image = QtGui.QImage(self.ui.label_3.size(), QtGui.QImage.Format_ARGB32)
        image.fill(QtGui.QColor(0, 0, 0))
        painter = QtGui.QPainter(image)
        painter.drawPixmap(x, y, scaled_pixmap)  # 在坐标(20, 30)处绘制缩小后的图像
        painter.end()

        # 在标签上显示绘制后的图像-
        self.ui.label_3.setPixmap(QtGui.QPixmap.fromImage(image))
        self.ui.label_3.setScaledContents(True)
        self.ui.label_3.setStyleSheet("background-color: transparent;")

    def add_image_to_label(self, img, x, y, w, h):
        self.MXAimg = img
        height, width, channel = self.MXAimg.shape
        bytes_per_line = 3 * width  # 假设图像为RGB格式
        q_img = QtGui.QImage(self.MXAimg.data, width, height, bytes_per_line, QtGui.QImage.Format_RGB888)

        # 将Qt的图像格式转换为QPixmap并设置到label上
        pixmap = QtGui.QPixmap.fromImage(q_img)
        # 获取原始的QPixmap对象
        original_pixmap = self.ui.label_3.pixmap()

        # 将缩小后的图像叠加到原始图像上
        scaled_pixmap = pixmap.scaled(w, h)  # 设置缩小后的大小为200x150
        if original_pixmap is None:
            original_pixmap = pixmap

        merged_pixmap = original_pixmap.copy()  # 复制原始图像
        merged_painter = QtGui.QPainter(merged_pixmap)
        merged_painter.drawPixmap(x, y, scaled_pixmap)  # 在坐标(0, 0)处绘制缩小后的图像
        merged_painter.end()

        # 将叠加后的图像转换为QImage对象并显示在标签上
        merged_image = QtGui.QImage(merged_pixmap.toImage())
        self.ui.label_3.setPixmap(QtGui.QPixmap.fromImage(merged_image))

    # 获取系统时间
    def get_time(self):
        # 获取当前系统时间
        current_time = datetime.now()
        # 格式化时间显示
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
        return formatted_time

    @QtCore.pyqtSlot(float, float)
    def updateLabelXYpos(self, xpos, ypos):
        self.ui.pos_x.setNum(xpos)
        self.ui.pos_y.setNum(ypos)

    @QtCore.pyqtSlot(float)
    def updateLabelZpos(self, zpos):
        self.ui.pos_z.setNum(zpos)

    @QtCore.pyqtSlot()
    def clear_points(self):
        pixmap = self.ui.Sketch_map.pixmap()
        painter = QPainter(pixmap)
        painter.setRenderHint(QPainter.Antialiasing)

        # 清空整个背景
        painter.eraseRect(pixmap.rect())
        painter.end()
        self.ui.Sketch_map.setPixmap(self.Sketch_map)  # 将绘制结果设置给QLabel的pixmap
        self.ui.Sketch_map.update()  # 强制刷新QLabel的显示

    # 绘制红点
    @QtCore.pyqtSlot()
    def updateLabelpoints(self):
        pixmap = self.ui.Sketch_map.pixmap()  # 获取QPixmap对象
        painter = QPainter(pixmap)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(QColor(255, 0, 0))
        painter.setBrush(QBrush(QColor(255, 0, 0)))
        radius = 2
        center_x, center_y = float(self.motion.navigationController.x_pos_mm), float(
            self.motion.navigationController.y_pos_mm)
        painter.drawEllipse(int(center_x * 3.5873 - radius + 110), int(-center_y * 3.5873 - radius + 280), 2 * radius,
                            2 * radius)
        painter.end()
        self.ui.Sketch_map.setPixmap(pixmap)  # 将绘制结果设置给QLabel的pixmap
        self.ui.Sketch_map.update()  # 强制刷新QLabel的显示

    @QtCore.pyqtSlot(numpy.ndarray)
    def updateLabelimg(self, numpy_image):
        self.img = numpy_image
        height, width, channel = numpy_image.shape
        bytes_per_line = 3 * width  # 假设图像为RGB格式
        q_img = QtGui.QImage(numpy_image.data, width, height, bytes_per_line, QtGui.QImage.Format_RGB888)
        pixmap = QtGui.QPixmap.fromImage(q_img)
        scaled_pixmap = pixmap.scaled(500, 320)  # 设置缩小后的大小为200x150
        # 在标签上显示绘制后的图像
        self.ui.label.setPixmap(scaled_pixmap)
        # print(numpy_image)

    def device(self):
        formatted_time = self.get_time()
        if self.motion is None:
            try:
                self.motion = motion.motion()
                if self.motion.navigationController is None:
                    self.ui.log.append(formatted_time + '     ' + '! 电机未检测到 !')
                else:
                    # 信号
                    self.motion.navigationController.xyPos.connect(self.updateLabelXYpos)
                    self.motion.navigationController.zPos.connect(self.updateLabelZpos)
                    self.point.connect(self.updateLabelpoints)
                    self.clear_point.connect(self.clear_points)
                    self.ui.log.append(formatted_time + '     ' + '! 电机连接成功 !')
            except:
                self.ui.log.append(formatted_time + '     ' + '! 电机未检测到 !')
        else:
            self.ui.log.append(formatted_time + '     ' + '! 电机已经在线 !')
        if self.camera is None:
            if self.motion.microcontroller is not None:
                try:
                    self.camera = camera.Camera(self.motion.microcontroller)
                    self.camera.imageDisplay.image_to_display.connect(self.updateLabelimg)
                    self.fcous_image.connect(self.updateLabelimg)
                    self.camera.liveController.start_live()
                    self.ui.log.append(formatted_time + '     ' + '! 相机打开成功 !')
                    self.motion_home()
                except:

                    self.ui.log.append(formatted_time + '     ' + '! 相机未检测到 !')
            else:
                self.ui.log.append(formatted_time + '     ' + '! 由于电机不在线，不开启相机 !')
        else:
            self.ui.log.append(formatted_time + '     ' + '! 相机已经在线 !')

    def motion_home(self):
        try:
            formatted_time = self.get_time()
            self.motion.navigationController.home_z()
            while self.motion.microcontroller.is_busy():
                time.sleep(0.005)
            self.motion.navigationController.home_xy()
            while self.motion.microcontroller.is_busy():
                time.sleep(0.005)
            self.ui.log.append(formatted_time + '     ' + '!复位完成!')
        except:
            self.ui.log.append(formatted_time + '     ' + '!复位失败!')

    def motion_stop(self):
        if self.move is not None:
            self.move.FLAGE = False

    def motion_only(self):
        self.move = move.Move(self.camera, self.motion, self.clear_point, self.point
                              , self.fcous_image, self.image_to_label, self.add_image_to_label
                              , self.ui, self.model)

        self.thread1 = threading.Thread(target=self.move.start_move)
        self.thread1.start()

    # 退出关闭相机光源
    def closeEvent(self, event):
        # 在窗口关闭事件中触发的函数
        self.close_thing()
        event.accept()

    def close_thing(self):
        # 执行需要在应用程序退出时触发的操作
        if self.camera is None:
            pass
        elif self.camera is not None:
            self.camera.liveController.stop_live()
            self.camera.camera.close()
            pass
        if self.motion is None:
            pass
        elif self.motion.microcontroller is not None:
            self.motion.microcontroller.turn_off_illumination()
            self.motion.microcontroller.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    dialog = MyWindow()
    dialog.showMaximized()
    dialog.show()
    sys.exit(app.exec_())
