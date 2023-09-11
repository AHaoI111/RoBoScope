import sys
import threading
import time
from datetime import datetime

import numpy
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QObject
from PyQt5.QtGui import QPixmap
from qtpy.QtCore import *
from qtpy.QtGui import *
from qtpy.QtWidgets import *

import Client_ as Client_
import UI.GUI_Data as GUI_Data
import control.camera_daheng as camera
import control.motion as motion
import control.move as move
from UI.BIOscope import Ui_MainWindow
from UI.GUI_setup import MyDialog
import subprocess

# 启动推理的服务器
subprocess.Popen(['python', 'Server_.py'])


class MyWindow(QMainWindow, QObject):
    point = Signal()
    clear_point = Signal()
    fcous_image = Signal(numpy.ndarray)

    def __init__(self):
        super().__init__()
        QObject.__init__(self)

        # 实例化 Ui_MainWindow
        # 更新UI的变量
        self.merged_image = None
        self.merged_painter = None
        self.merged_pixmap = None
        self.original_pixmap = None
        self.painter = None
        self.image = None
        self.scaled_pixmap = None
        self.pixmap = None
        self.q_img = None
        #
        self.ui = Ui_MainWindow()
        # 将 ui 设置为当前窗口的界面
        self.ui.setupUi(self)
        ####
        self.motion = None
        self.camera = None
        # 示意图
        self.Sketch_map = QPixmap('./control/Sketch.png').scaled(438, 365)
        self.ui.Sketch_map.setPixmap(self.Sketch_map)

        self.client = Client_.Client(host='127.0.0.1', port=8888)
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
        # 弹出载物台
        self.ui.move_go.clicked.connect(self.motion_go)  # type: ignore

    def Data(self):
        GUI_Data.display()

    def set_up(self):
        # 创建 MyDialog 对象并显示
        self.dialog = MyDialog()
        self.dialog.show()

    # 将图片显示在界面
    def image_to_label(self, img, x, y, w, h):
        # 将OpenCV的图像数据转换为Qt的图像格式
        height, width, channel = img.shape
        bytes_per_line = 3 * width  # 假设图像为RGB格式
        self.q_img = QtGui.QImage(img.data, width, height, bytes_per_line, QtGui.QImage.Format_RGB888)

        # 将Qt的图像格式转换为QPixmap并发送信号
        self.pixmap = QtGui.QPixmap.fromImage(self.q_img)
        self.scaled_pixmap = self.pixmap.scaled(w, h)  # 设置缩小后的大小为200x150

        # 在标签上绘制缩小后的图像
        self.image = QtGui.QImage(self.ui.label_3.size(), QtGui.QImage.Format_ARGB32)
        self.image.fill(QtGui.QColor(0, 0, 0))
        self.painter = QtGui.QPainter(self.image)
        self.painter.drawPixmap(x, y, self.scaled_pixmap)  # 在坐标(20, 30)处绘制缩小后的图像
        self.painter.end()

        # 在标签上显示绘制后的图像-
        self.ui.label_3.setPixmap(QtGui.QPixmap.fromImage(self.image))
        self.ui.label_3.setScaledContents(True)
        self.ui.label_3.setStyleSheet("background-color: transparent;")

    def add_image_to_label(self, img, x, y, w, h):
        height, width, channel = img.shape
        bytes_per_line = 3 * width  # 假设图像为RGB格式
        self.q_img = QtGui.QImage(img.data, width, height, bytes_per_line, QtGui.QImage.Format_RGB888)

        # 将Qt的图像格式转换为QPixmap并设置到label上
        self.pixmap = QtGui.QPixmap.fromImage(self.q_img)
        # 获取原始的QPixmap对象
        self.original_pixmap = self.ui.label_3.pixmap()

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
        self.ui.label_3.setPixmap(QtGui.QPixmap.fromImage(self.merged_image))

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
        q_img = QtGui.QImage(bytes(numpy_image.data), width, height, bytes_per_line, QtGui.QImage.Format_RGB888)
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
                    self.ui.log.append(formatted_time + '     ' + '! 相机打开成功 !')
                    self.motion.navigationController.home_z()
                    while self.motion.microcontroller.is_busy():
                        time.sleep(0.005)
                    self.motion.navigationController.home_xy()
                    while self.motion.microcontroller.is_busy():
                        time.sleep(0.005)
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

    def motion_go(self):
        try:
            formatted_time = self.get_time()
            self.motion.navigationController.home_z()
            while self.motion.microcontroller.is_busy():
                time.sleep(0.005)
            self.motion.navigationController.move_y_to(60)
            while self.motion.microcontroller.is_busy():
                time.sleep(0.005)
            self.ui.log.append(formatted_time + '     ' + '!弹出完成!')
        except:
            self.ui.log.append(formatted_time + '     ' + '!弹出失败!')

    def motion_only(self):
        while self.motion.microcontroller.is_busy():
            time.sleep(0.005)
        self.move = move.Move(self.camera, self.motion, self.clear_point, self.point
                              , self.fcous_image, self.image_to_label, self.add_image_to_label
                              , self.ui, self.client)

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
            # self.camera.liveController.stop_live()
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
