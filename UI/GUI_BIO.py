import subprocess
import sys
import threading
import time
from datetime import datetime

import PySide6.QtCore as QtCore
import PySide6.QtGui as QtGui
import numpy
from PySide6.QtCore import QObject, Signal
from PySide6.QtGui import QPixmap, QPainter, QColor, QBrush, QAction
from PySide6.QtWidgets import QApplication, QMainWindow

import Client_ as Client_
import UI.GUI_Data as GUI_Data
import control.camera_daheng as camera
import control.motion as motion
import control.move as move
from UI.BIOscope import Ui_MainWindow
from UI.GUI_setup import MyDialog

# 启动推理的服务器
subprocess.Popen(['python', 'Server_.py'])


class MyWindow(QMainWindow, QObject):
    point = Signal()
    clear_point = Signal()
    fcous_image = Signal(numpy.ndarray)
    LIVE_image = Signal(numpy.ndarray)

    def __init__(self):
        super().__init__()
        # QObject.__init__(self)

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
        self.flage = True
        #
        self.ui = Ui_MainWindow()
        # 将 ui 设置为当前窗口的界面
        self.ui.setupUi(self)
        ####
        self.motion = None
        self.camera = None
        # 示意图
        self.Sketch_map = QPixmap('./control/Sketch.png').scaled(328, 273)
        self.ui.Sketch_map.setPixmap(self.Sketch_map)

        self.client = Client_.Client(host='127.0.0.1', port=8888)
        # 设置中心
        self.ui.actionshezhi.triggered.connect(self.set_up)
        # 数据浏览
        self.ui.actionshuju.triggered.connect(self.Data)
        # 控制中心
        self.ui.actionopen.triggered.connect(self.live_image_button_open)
        self.ui.actionclose.triggered.connect(self.live_image_button_close)
        self.ui.actionturn_on.triggered.connect(self.turn_on_led)
        self.ui.actionturn_off.triggered.connect(self.turn_off_led)

        # 设备初始化
        self.ui.Initialize_device.clicked.connect(self.device)
        # 复位
        self.ui.move_home.clicked.connect(self.motion_home)  # type: ignore
        # 停止
        self.ui.move_stop.clicked.connect(self.motion_stop)  # type: ignore
        # 单张
        self.ui.move_only.clicked.connect(self.motion_only)  # type: ignore
        # 弹出载物台
        self.ui.move_go.clicked.connect(self.motion_go)  # type: ignore

    def live_image(self):
        while True:
            if self.flage:
                if self.camera is not None:
                    for i in range(1):

                        if self.camera.liveController.trigger_mode == 'Software Trigger':
                            self.camera.camera.send_trigger()

                        image = self.camera.camera.read_frame()
                        self.LIVE_image.emit(image)
            else:
                height = 480
                width = 640
                channels = 3
                img = numpy.zeros((height, width, channels), dtype=numpy.uint8)
                self.fcous_image.emit(img)
                break

    def Data(self):
        # GUI_Data.display()
        self.myWindow = GUI_Data.QmyWidget()
        self.myWindow.show()

    def set_up(self):
        # 创建 MyDialog 对象并显示
        self.dialog = MyDialog()
        self.dialog.show()

    # 获取系统时间
    def get_time(self):
        # 获取当前系统时间
        current_time = datetime.now()
        # 格式化时间显示
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
        return formatted_time

    @QtCore.Slot(float, float)
    def updateLabelXYpos(self, xpos, ypos):
        self.ui.pos_x.setNum(xpos)
        self.ui.pos_y.setNum(ypos)

    @QtCore.Slot(float)
    def updateLabelZpos(self, zpos):
        self.ui.pos_z.setNum(zpos)

    @QtCore.Slot(numpy.ndarray)
    def updateLabelimg(self, numpy_image):
        self.img = numpy_image
        height, width, channel = numpy_image.shape
        bytes_per_line = 3 * width  # 假设图像为RGB格式
        q_img = QtGui.QImage(bytes(numpy_image.data), width, height, bytes_per_line, QtGui.QImage.Format_RGB888)
        pixmap = QtGui.QPixmap.fromImage(q_img)
        # scaled_pixmap = pixmap.scaled(500, 320)  # 设置缩小后的大小为200x150
        scaled_pixmap = pixmap.scaled(self.ui.label_3.size(), QtCore.Qt.AspectRatioMode.IgnoreAspectRatio)
        # 在标签上显示绘制后的图像
        self.ui.label_3.setPixmap(scaled_pixmap)

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

                    self.ui.log.append(formatted_time + '     ' + '! 电机连接成功 !')

            except:
                self.ui.log.append(formatted_time + '     ' + '! 电机未检测到 !')
        else:
            self.ui.log.append(formatted_time + '     ' + '! 电机已经在线 !')
        if self.camera is None:
            if self.motion.microcontroller is not None:
                try:
                    self.camera = camera.Camera(self.motion.microcontroller)

                    self.LIVE_image.connect(self.updateLabelimg)
                    self.ui.log.append(formatted_time + '     ' + '! 相机打开成功 !')
                    # self.motion.microcontroller.turn_on_illumination()
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
            self.motion.navigationController.move_y_to(55)
            while self.motion.microcontroller.is_busy():
                time.sleep(0.005)
            self.ui.log.append(formatted_time + '     ' + '!弹出完成!')
        except:
            self.ui.log.append(formatted_time + '     ' + '!弹出失败!')

    # 单片扫描
    def motion_only(self):
        self.flage = False
        time.sleep(0.2)
        while self.motion.microcontroller.is_busy():
            time.sleep(0.005)
        self.move = move.Move(self.camera, self.motion, self.Sketch_map, self.ui, self.client)
        self.thread1 = threading.Thread(target=self.move.start_move)
        self.thread1.start()

    def live_image_button_open(self):
        if self.flage:
            self.motion.microcontroller.turn_on_illumination()
            self.thread2 = threading.Thread(target=self.live_image)
            self.thread2.start()
            formatted_time = self.get_time()
            self.ui.log.append(formatted_time + '     ' + '!打开相机实时!')

    def live_image_button_close(self):
        # 打断实时
        self.flage = False
        self.motion.microcontroller.turn_off_illumination()
        formatted_time = self.get_time()
        self.ui.log.append(formatted_time + '     ' + '!关闭相机实时!')
        time.sleep(0.2)
        self.flage = True

    def turn_on_led(self):
        if self.motion is not None:
            self.motion.microcontroller.turn_on_illumination()

    def turn_off_led(self):
        if self.motion is not None:
            self.motion.microcontroller.turn_off_illumination()

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
