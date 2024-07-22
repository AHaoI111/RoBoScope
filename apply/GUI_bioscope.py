# -*- encoding: utf-8 -*-
"""
@Description:
用户界面和功能
@File    :   GUI_bioscope.py
@Time    :   2024/07/16
@Author  :   Li QingHao
@Version :   2.0
@Time_END :  最后修改时间：
@Developers_END :  最后修改作者：
"""

import logging
import threading
import time
from datetime import datetime

import cv2
import numpy
from PySide6 import QtCore, QtGui
from PySide6.QtCore import Qt, Signal, QPoint
from PySide6.QtGui import QPainter, QPixmap, QColor, QPen
from PySide6.QtWidgets import QMainWindow, QGraphicsScene, QGraphicsPixmapItem, QMessageBox, QFileDialog

import Drives.camera as camera
from DataSaver.Saverdata import Saver
from apply.taskworkonlycamera import Task
from apply.ui_mainwindow import Ui_MainWindow
from utils import read_config
from utils.Search_device import device
from utils.action_loader import ActionLoader
from utils.action_microscopeonly import ActionMicroscope



def get_time():
    """
    获取当前时间并返回格式化的字符串表示。

    返回:
        str: 格式为"YYYY_MM_DD HH:MM:SS"的当前时间字符串。
    """
    # 获取当前系统时间
    current_time = datetime.now()
    # 格式化时间显示
    formatted_time = current_time.strftime("%Y_%m_%d %H:%M:%S")
    return formatted_time


def create_qimage_from_cvimg(cvimg, format_):
    """
    Convert an OpenCV image (cvimg) to a QImage object.

    Parameters:
    cvimg: numpy.ndarray
        The OpenCV image, typically in BGR format.
    format_: QtGui.QImage.Format
        The format of the QImage to be created.

    Returns:
    QtGui.QImage
        The converted QImage object.
    """
    # Get the height and width of the OpenCV image
    height, width = cvimg.shape[:2]
    # Calculate the bytes per line of the image, considering whether it is a color image (more than 2 dimensions)
    bytes_per_line = width * cvimg.shape[2] if len(cvimg.shape) > 2 else width
    # Create a QImage object using the data of the OpenCV image, specifying the width, height, bytes per line,
    # and format
    return QtGui.QImage(
        bytes(cvimg.data), width, height, bytes_per_line,
        format_
    )


class MyMainWindow(QMainWindow):
    Updata_textEdit_log = Signal(str)
    updata_parameter = Signal()
    live_img = Signal(numpy.ndarray)

    def __init__(self, splash):
        """
        初始化窗口类，设置窗口的基本属性和操作。

        :param splash: 启动屏幕对象，用于显示程序启动过程中的信息。
        """
        super().__init__()

        self.save_pic = None
        self.splash = splash
        # 显示启动信息
        self.splash.showMessage("正在启动...", Qt.AlignBottom | Qt.AlignCenter, Qt.white)
        self.config_info = None
        self.config = None
        self.i = 0

        # 初始化各种对象和变量
        self.root = None
        self.logger = None
        self.thread_Task = None
        self.task = None
        self.ActionLoader = None
        self.ActionMicroscope = None
        self.RUN = None

        self.Device = None
        # 初始化主窗口界面
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # 初始化保存对象
        # 保存
        self.Saver = Saver()

        # 初始化图形场景
        self.scene_puzzle = QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene_puzzle)
        # 显示graphicsView_fcous以准备显示图像
        self.ui.graphicsView.show()

        self.scene_focus = QGraphicsScene()
        self.ui.graphicsView_fcous.setScene(self.scene_focus)

        # 显示graphicsView_fcous以准备显示图像
        self.ui.graphicsView_fcous.show()

        # 初始化界面参数
        # 加载界面参数

        self.used_width = int(100)
        self.used_height = int(100)
        self.led_index = -1
        self.camera_index = -1

        # 绑定按钮点击事件
        # 扫描
        self.ui.pushButton_run.clicked.connect(self.run)
        # 暂停
        self.ui.pushButton_pause.clicked.connect(self.pause)
        # 复位显微镜
        self.ui.pushButton_micro_reset.clicked.connect(self.micro_reset)
        # 复位loader
        self.ui.pushButton_loader_reset.clicked.connect(self.loader_test)
        # 保存参数
        self.ui.pushButton_save.clicked.connect(self.save_setup)

        # 启用按钮
        self.ui.pushButton_run.setEnabled(True)
        self.ui.pushButton_pause.setEnabled(True)
        self.ui.pushButton_micro_reset.setEnabled(True)
        self.ui.pushButton_loader_reset.setEnabled(True)
        ##
        self.Updata_textEdit_log.connect(self.updata_log)
        self.create_empty_pixmap()

        self.initialize()
        # 加载参数
        self.updata_parameter.connect(self.Up_parameter)
        self.updata_parameter.emit()
        self.splash.showMessage("正在加载参数设置...", Qt.AlignBottom | Qt.AlignCenter, Qt.white)
        self.ui.progressBar.setValue(0)

        # 绑定调试按钮点击事件
        # 调试
        self.ui.pushButton_test_micro_movex2.clicked.connect(self.test_micro_movex2)
        self.ui.pushButton_test_micro_movey2.clicked.connect(self.test_micro_movey2)
        self.ui.pushButton_test_micro_movez2.clicked.connect(self.test_micro_movez2)
        self.ui.pushButton_test_loader_movex2.clicked.connect(self.test_loader_movex2)
        self.ui.pushButton_test_loader_movey2.clicked.connect(self.test_loader_movey2)
        self.ui.pushButton_test_loader_movez2.clicked.connect(self.test_loader_movez2)
        self.ui.pushButton_open_cameraonly.clicked.connect(self.open_cameraonly)
        self.ui.pushButton_close_cameraonly.clicked.connect(self.close_cameraonly)
        self.ui.pushButton_open_camera_1.clicked.connect(self.open_camera1)
        self.ui.pushButton_close_camera_1.clicked.connect(self.close_camera1)
        self.ui.pushButton_open_camera_2.clicked.connect(self.open_camera2)
        self.ui.pushButton_close_camera_2.clicked.connect(self.close_camera2)
        self.ui.pushButton_open_led_only.clicked.connect(self.open_led_only)
        self.ui.pushButton_close_led_only.clicked.connect(self.close_led_only)
        self.ui.pushButton_open_led_1.clicked.connect(self.open_led_1)
        self.ui.pushButton_close_led_1.clicked.connect(self.close_led_1)
        self.ui.pushButton_open_led_2.clicked.connect(self.open_led_2)
        self.ui.pushButton_close_led_2.clicked.connect(self.close_led_2)

        # 灯控
        self.ui.horizontalSlider_led_intensity.valueChanged.connect(self.sliderValueChanged_led)
        # 曝光控制
        self.ui.horizontalSlider_exposure.valueChanged.connect(self.sliderValueChanged_camera)
        # 确认当前扫描参数
        self.ui.pushButton_save_scan.clicked.connect(self.set_scan)
        # 确认更改当前曝光参数
        self.ui.pushButton_save_exposure.clicked.connect(self.set_exposure)
        # 捕获
        self.ui.pushButton_savepic.clicked.connect(self.savepic)
        # 更换保存的图片路径
        self.ui.pushButton_savepath.clicked.connect(self.change_savepath)

    # 设备初始化
    def initialize(self):
        """
        初始化函数，用于设备和相关组件的初始化。

        这里首先读取配置信息，然后根据配置信息决定是否初始化设备。如果设备需要初始化，
        则会尝试打开设备并进行设备自检。如果自检通过，会进一步初始化显微镜和装载器系统，
        并设置相关事件处理函数。如果设备自检失败，则会提示用户并停止初始化过程。

        设备初始化完成后，会启用相应的用户界面按钮，准备进行后续操作。
        """
        # 加载配置信息
        # 加载配置
        self.config = read_config.ConfigReader()
        self.config_info = self.config.get_config_info()
        # 根据配置信息决定是否初始化设备
        if self.config_info['Device']['microscope']:
            camera.global_rotate_image_angle = self.config_info['Camera']['RotateImageAngle']
            # 初始化设备对象
            # 启动设备
            self.Device = device(self.config_info)
            # 显示启动设备的消息
            self.splash.showMessage("正在启动设备...", Qt.AlignBottom | Qt.AlignCenter, Qt.white)
            # 尝试打开设备
            # 设备打开
            flag, flag_microscope, flag_camera, flag_camera1, flag_camera2, flag_loader = self.Device.open_device()
            self.splash.showMessage("正在打开设备...", Qt.AlignBottom | Qt.AlignCenter, Qt.white)
            # 根据设备打开状态给出相应反馈
            if flag:
                self.Updata_textEdit_log.emit('设备启动成功')
                self.splash.showMessage("设备打开成功...", Qt.AlignBottom | Qt.AlignCenter, Qt.white)
            else:
                # 如果特定设备打开失败，则记录日志
                if not flag_microscope:
                    self.Updata_textEdit_log.emit('显微镜启动失败')
                if not flag_camera:
                    self.Updata_textEdit_log.emit('相机启动失败')
                if not flag_camera1:
                    self.Updata_textEdit_log.emit('相机1启动失败')
                if not flag_camera2:
                    self.Updata_textEdit_log.emit('相机2启动失败')
                if not flag_loader:
                    self.Updata_textEdit_log.emit('装载器启动失败')
                self.splash.showMessage("设备打开失败...", Qt.AlignBottom | Qt.AlignCenter, Qt.white)
                # 如果启动失败，则禁用所有设备相关的用户界面按钮
                self.ui.pushButton_run.setEnabled(False)
                self.ui.pushButton_pause.setEnabled(False)
                self.ui.pushButton_micro_reset.setEnabled(False)
                self.ui.pushButton_loader_reset.setEnabled(False)
                self.ui.pushButton_open_cameraonly.setEnabled(False)
                self.ui.pushButton_close_cameraonly.setEnabled(False)
                self.ui.pushButton_open_camera_1.setEnabled(False)
                self.ui.pushButton_open_camera_2.setEnabled(False)
                self.ui.pushButton_close_camera_1.setEnabled(False)
                self.ui.pushButton_close_camera_2.setEnabled(False)
                self.ui.pushButton_test_micro_movex2.setEnabled(False)
                self.ui.pushButton_test_micro_movey2.setEnabled(False)
                self.ui.pushButton_test_micro_movez2.setEnabled(False)
                self.ui.pushButton_test_loader_movex2.setEnabled(False)
                self.ui.pushButton_test_loader_movey2.setEnabled(False)
                self.ui.pushButton_test_loader_movez2.setEnabled(False)
                self.ui.pushButton_open_led_only.setEnabled(False)
                self.ui.pushButton_close_led_only.setEnabled(False)
                self.ui.pushButton_open_led_1.setEnabled(False)
                self.ui.pushButton_close_led_1.setEnabled(False)
                self.ui.pushButton_open_led_2.setEnabled(False)
                self.ui.pushButton_close_led_2.setEnabled(False)
                self.ui.pushButton_save_scan.setEnabled(False)
                self.ui.pushButton_save_exposure.setEnabled(False)
                return
            # 进行设备自检
            self.splash.showMessage("设备正在自检...", Qt.AlignBottom | Qt.AlignCenter, Qt.white, )
            flag = self.Device.detection_device()
            # 根据自检结果给出相应反馈
            if flag:
                self.Updata_textEdit_log.emit('设备自检成功')
                self.splash.showMessage("设备自检成功...", Qt.AlignBottom | Qt.AlignCenter, Qt.white)
                # 初始化显微镜动作对象，并设置相关事件处理函数
                # 给设备赋予行为
                self.ActionMicroscope = ActionMicroscope(self.Device, self.config_info, self.Saver)
                # 绑定槽函数
                self.ActionMicroscope.updata_puzzle.connect(self.upimage_puzzle)
                self.ActionMicroscope.updata_focus.connect(self.upimage_fcous)
                self.ActionMicroscope.updata_point_clear.connect(self.clear_points)
                self.ActionMicroscope.updata_point_draw.connect(self.update_points)
                # self.ActionMicroscope.ok.connect(self.finish)
                self.ActionMicroscope.updata_textEdit_log_microscope.connect(self.updata_log)
                self.ActionMicroscope.updata_textEdit_ID.connect(self.updata_ID)
                self.ActionMicroscope.write_log_microscope.connect(self.write_log)
                self.ActionMicroscope.updata_Progress.connect(self.up_progress)
                self.Device.navigationController.xyzPos.connect(self.updateLabelXYZpos)
                self.splash.showMessage("显微镜系统初始化成功...", Qt.AlignBottom | Qt.AlignCenter, Qt.white)
                self.Updata_textEdit_log.emit('显微镜系统初始化成功')
                # 如果配置了装载器，并且装载器打开成功，则初始化装载器动作对象
                if self.config_info['Device']['loaderflage'] == 'True' and flag_loader == True:
                    self.ActionLoader = ActionLoader(self.Device.Loader.loaderController,
                                                     self.config_info['Loader'])
                    # 设置灯颜色
                    for i in range(4):
                        self.ActionLoader.set_led(i - 1, self.ActionLoader.color.green)
                    self.Updata_textEdit_log.emit('装载器系统初始化成功')
                    self.splash.showMessage("装载器系统初始化成功...", Qt.AlignBottom | Qt.AlignCenter, Qt.white)
                else:
                    self.Updata_textEdit_log.emit('没有设置装载器')
                    self.splash.showMessage("没有设置装载器...", Qt.AlignBottom | Qt.AlignCenter, Qt.white)
            else:
                self.splash.showMessage("设备自检失败...", Qt.AlignBottom | Qt.AlignCenter, Qt.white)
                self.Updata_textEdit_log.emit('设备自检失败')
                return
            # 初始化任务对象，并设置相关事件处理函数
            # 初始化任务
            self.task = Task(self.ActionLoader, self.ActionMicroscope, self.config_info)
            # 绑定槽函数
            self.task.activate_pushbutton.connect(self.activate)
            self.task.updata_textEdit_log_task.connect(self.updata_log)
            self.task.write_log_task.connect(self.write_log)
            # 启用相关用户界面按钮
            self.ui.pushButton_pause.setEnabled(True)
            self.ui.pushButton_micro_reset.setEnabled(True)
            self.ui.pushButton_loader_reset.setEnabled(True)
            self.ui.pushButton_run.setEnabled(True)
            if self.config_info['Device']['cameranumber'] == 1:
                self.ui.pushButton_open_camera_1.setEnabled(False)
                self.ui.pushButton_open_camera_2.setEnabled(False)
                self.ui.pushButton_close_camera_1.setEnabled(False)
                self.ui.pushButton_close_camera_2.setEnabled(False)
                self.ui.pushButton_open_led_1.setEnabled(False)
                self.ui.pushButton_close_led_1.setEnabled(False)
                self.ui.pushButton_open_led_2.setEnabled(False)
                self.ui.pushButton_close_led_2.setEnabled(False)
            elif self.config_info['Device']['cameranumber'] == 2:
                self.ui.pushButton_open_cameraonly.setEnabled(False)
                self.ui.pushButton_close_cameraonly.setEnabled(False)
                self.ui.pushButton_open_led_only.setEnabled(False)
                self.ui.pushButton_close_led_only.setEnabled(False)
        else:
            # 如果配置中没有显微镜，则禁用所有设备相关的用户界面按钮
            self.ui.pushButton_run.setEnabled(False)
            self.ui.pushButton_pause.setEnabled(False)
            self.ui.pushButton_micro_reset.setEnabled(False)
            self.ui.pushButton_loader_reset.setEnabled(False)
            self.ui.pushButton_open_cameraonly.setEnabled(False)
            self.ui.pushButton_close_cameraonly.setEnabled(False)
            self.ui.pushButton_open_camera_1.setEnabled(False)
            self.ui.pushButton_open_camera_2.setEnabled(False)
            self.ui.pushButton_close_camera_1.setEnabled(False)
            self.ui.pushButton_close_camera_2.setEnabled(False)
            self.ui.pushButton_test_micro_movex2.setEnabled(False)
            self.ui.pushButton_test_micro_movey2.setEnabled(False)
            self.ui.pushButton_test_micro_movez2.setEnabled(False)
            self.ui.pushButton_test_loader_movex2.setEnabled(False)
            self.ui.pushButton_test_loader_movey2.setEnabled(False)
            self.ui.pushButton_test_loader_movez2.setEnabled(False)
            self.ui.pushButton_open_led_only.setEnabled(False)
            self.ui.pushButton_close_led_only.setEnabled(False)
            self.ui.pushButton_open_led_1.setEnabled(False)
            self.ui.pushButton_close_led_1.setEnabled(False)
            self.ui.pushButton_open_led_2.setEnabled(False)
            self.ui.pushButton_close_led_2.setEnabled(False)
            self.ui.pushButton_save_scan.setEnabled(False)
            self.ui.pushButton_save_exposure.setEnabled(False)

            self.splash.showMessage("设备自检警告...", Qt.AlignBottom | Qt.AlignCenter, Qt.white)

    def micro_reset(self):
        """
        执行显微镜的复位操作。

        该函数调用显微镜设备的复位方法，将显微镜移动到预设的home位置。
        同时，它也会触发一个信号来更新日志文本框，记录复位操作的信息。

        无参数。

        无返回值。
        """
        # 调用显微镜动作控制方法，将显微镜移动到home位置
        self.ActionMicroscope.microscope_homezxy()
        # 发送信号以更新日志文本框，显示显微镜复位的操作信息
        self.Updata_textEdit_log.emit('显微镜复位')

    def loader_test(self):
        """
        测试装载器的功能。

        本函数用于验证装载器是否能正确复位。它首先调用ActionLoader的loader_reset方法来复位装载器，
        然后通过发射Updata_textEdit_log信号来记录复位操作的日志。这有助于在开发和调试过程中
        监控装载器的状态变化。
        """
        # 调用装载器的复位方法，准备进行测试
        self.ActionLoader.loader_reset()
        # 发送信号以记录复位操作的日志
        self.Updata_textEdit_log.emit('装载器复位')

    def get_box(self):
        """
        根据用户界面中复选框的状态，构建并返回一个整数列表。

        该方法检查四个复选框（checkBox_1至checkBox_4）的选中状态，并将选中的复选框对应的值（1至4）添加到列表中。
        如果没有复选框被选中，将返回一个空列表。

        返回:
            list: 包含选中复选框对应值的列表。
        """
        # 初始化一个空列表，用于存储复选框的值
        box = []

        # 检查复选框1是否被选中，如果被选中，则将1添加到列表中
        if self.ui.checkBox_1.isChecked():
            box.append(1)

        # 检查复选框2是否被选中，如果被选中，则将2添加到列表中
        if self.ui.checkBox_2.isChecked():
            box.append(2)

        # 检查复选框3是否被选中，如果被选中，则将3添加到列表中
        if self.ui.checkBox_3.isChecked():
            box.append(3)

        # 检查复选框4是否被选中，如果被选中，则将4添加到列表中
        if self.ui.checkBox_4.isChecked():
            box.append(4)

        # 返回包含所有选中复选框值的列表
        return box

    # 扫描
    def run(self):
        """
        启动任务执行的函数。

       禁用运行按钮，启用暂停按钮，禁用微调重置按钮和加载器重置按钮。
        设置当前日期时间格式，并创建一个以日期时间为名的日志文件。
        初始化日志记录器，配置日志级别为DEBUG，并将日志输出到指定的文件。
        开始一个新的线程来运行任务。
        """
        # 禁用运行按钮，启用暂停按钮，以准备开始任务
        self.ui.pushButton_run.setEnabled(False)
        self.ui.pushButton_pause.setEnabled(True)
        self.ui.pushButton_micro_reset.setEnabled(False)
        self.ui.pushButton_loader_reset.setEnabled(False)

        # 获取当前日期时间，用于日志文件命名
        # 获取当前日期时间
        current_datetime = datetime.now()
        formatted_date = current_datetime.strftime("%Y%m%d")

        # 初始化日志记录器，用于记录运行过程中的信息
        # 创建一个logger对象
        self.logger = logging.getLogger('RUN')

        # 设置日志记录级别为DEBUG，以便记录详细的信息
        # 配置日志记录器
        self.logger.setLevel(logging.DEBUG)  # 设置日志级别为DEBUG

        # 创建文件处理器，将日志输出到指定的文件
        # 创建一个文件处理器，将日志写入到文件中
        file_handler = logging.FileHandler(str(formatted_date) + '.log')

        # 配置日志格式，包括时间、级别和消息
        # 创建一个格式化器，定义日志消息的格式
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)

        # 防止日志信息被父进程的日志处理器处理
        # 移除默认的StreamHandler处理器，避免日志消息同时输出到控制台
        self.logger.propagate = False

        # 添加文件处理器到日志记录器
        # 将文件处理器添加到logger中
        self.logger.addHandler(file_handler)

        # 暂停短暂时间，以确保界面更新
        time.sleep(0.005)

        # 准备执行任务所需的参数
        # box = self.get_box()
        box = []

        # 创建一个线程，用于执行任务
        # self.task.run(self.RUN)
        self.thread_Task = threading.Thread(target=self.task.run, args=(box,))
        self.thread_Task.start()

    def pause(self):
        """
        暂停当前任务。

        该方法调用外部获取时间的函数，并暂停实例中当前正在进行的任务。
        时间获取用于记录暂停时刻，以便于任务恢复时可以准确继续。

        参数:
            无

        返回值:
            无
        """
        # 获取当前时间，用于记录任务暂停的时刻
        Time = get_time()
        # 调用任务对象的pause方法，实际暂停任务执行
        self.task.pause()
        reply = QMessageBox.warning(self, "暂停！", "是否继续扫描？",
                                    QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
        if reply == QMessageBox.StandardButton.Ok:
            self.ActionMicroscope.flag = True
            self.ActionMicroscope.flage_run = True
            self.Updata_textEdit_log.emit('取消暂停继续扫描')
        else:
            self.ActionMicroscope.flag = True
            self.ActionMicroscope.flage_run = False
            self.Updata_textEdit_log.emit('停止扫描')

    def save_setup(self):
        """
        保存配置信息。

        该方法从用户界面获取各种配置参数，并将它们存储在self.config_info字典中。
        配置信息包括任务设置、图像保存设置、设备设置、显微镜设置和相机设置。
        最后，调用config.save_config_info方法保存配置信息。
        """

        # 保存任务设置
        # 任务分配参数
        self.config_info['Task']['box'] = self.get_box()
        self.config_info['Task']['slidenumber'] = str(self.ui.spinBox_slide_number.value())

        # 保存图像保存设置
        # 图像参数
        self.config_info['ImageSaver']['maxworkers'] = int(self.ui.spinBox_maxworkers.value())
        self.config_info['ImageSaver']['imagestitchsize'] = int(self.ui.spinBox_imagestitchsize.value())
        self.config_info['ImageSaver']['newimage'] = int(self.ui.spinBox_AIimage.value())
        self.config_info['ImageSaver']['queuenumber'] = int(self.ui.spinBox_queuenumber.value())
        self.config_info['ImageSaver']['pixelformat'] = str(self.ui.comboBox_pixelformat.currentText())
        self.config_info['ImageSaver']['imagequailty'] = int(self.ui.spinBox_imagequailty.value())
        self.config_info['ImageSaver']['savepath'] = str(self.ui.label_savepath.text())

        # 保存设备设置
        # 设备参数
        self.config_info['Device']['cameranumber'] = int(self.ui.spinBox_cameranumber.value())
        self.config_info['Device']['loaderflage'] = self.ui.checkBox_loaderflage.isChecked()
        self.config_info['Device']['microscope'] = self.ui.checkBox_microscopeflage.isChecked()

        # 保存显微镜设置
        # 显微镜参数
        self.config_info['Microscope']['串口'] = str(self.ui.comboBox_MicroCom.currentText())
        self.config_info['Microscope']['玻片扫描中心xy50x'] = [self.ui.doubleSpinBox_50xcenterx.value(),
                                                               self.ui.doubleSpinBox_50xcentery.value()]
        self.config_info['Microscope']['玻片扫描中心xy20x'] = [self.ui.doubleSpinBox_20xcenterx.value(),
                                                               self.ui.doubleSpinBox_20xcentery.value()]
        self.config_info['Microscope']['单镜头扫描中心xy'] = [self.ui.doubleSpinBox_Onlycenterx.value(),
                                                              self.ui.doubleSpinBox_Onlycentery.value()]
        self.config_info['Microscope']['玻片扫描区域宽度'] = int(self.ui.spinBox_scan_w.value())
        self.config_info['Microscope']['玻片扫描区域高度'] = int(self.ui.spinBox_scan_h.value())
        self.config_info['Microscope']['对焦经验值50x'] = float(self.ui.doubleSpinBox_50xzfocus.value())
        self.config_info['Microscope']['对焦经验值20x'] = float(self.ui.doubleSpinBox_20xzfocus.value())
        self.config_info['Microscope']['对焦经验值单镜头'] = float(self.ui.doubleSpinBox_Onlyzfocus.value())
        self.config_info['Microscope']['对焦方式'] = str(self.ui.comboBox_FocusMethod.currentText())
        self.config_info['Microscope']['对焦倍数'] = [str(self.ui.comboBox_Objective.currentText()),
                                                      str(self.ui.comboBox_Objective_SYS.currentText())]
        self.config_info['Microscope']['对焦步数'] = int(self.ui.spinBox_FocusNumber.value())
        self.config_info['Microscope']['对焦分辨率'] = float(self.ui.doubleSpinBox_FocusStep.value())
        self.config_info['Microscope']['隔点对焦步长'] = int(self.ui.spinBox_FocusGap_number.value())
        self.config_info['Microscope']['xend'] = float(self.ui.doubleSpinBox_connect_loader_x.value())
        self.config_info['Microscope']['yend'] = float(self.ui.doubleSpinBox_connect_loader_y.value())

        # 保存相机设置
        # 相机参数
        self.config_info['Camera']['像素标定50x'] = float(self.ui.doubleSpinBox_50xCalibration.value())
        self.config_info['Camera']['像素标定20x'] = float(self.ui.doubleSpinBox_20xCalibration.value())
        self.config_info['Camera']['单镜头标定'] = float(self.ui.doubleSpinBox_OnlyCalibration.value())
        self.config_info['Camera']['wb50x'] = [self.ui.doubleSpinBox_50xWB_R.value(),
                                               self.ui.doubleSpinBox_50xWB_G.value(),
                                               self.ui.doubleSpinBox_50xWB_B.value()]
        self.config_info['Camera']['wb20x'] = [self.ui.doubleSpinBox_20xWB_R.value(),
                                               self.ui.doubleSpinBox_20xWB_G.value(),
                                               self.ui.doubleSpinBox_20xWB_B.value()]

        self.config_info['Camera']['wbone'] = [self.ui.doubleSpinBox_OnlyWB_R.value(),
                                               self.ui.doubleSpinBox_OnlyWB_G.value(),
                                               self.ui.doubleSpinBox_OnlyWB_B.value()]

        # 保存装载器设置
        # 装载器参数
        self.config_info['Loader']['串口'] = str(self.ui.comboBox_LoaderCom.currentText())
        self.config_info['Loader']['box1startxz'] = [self.ui.doubleSpinBox_Box1_startx.value(),
                                                     self.ui.doubleSpinBox_Box1_startz.value()]
        self.config_info['Loader']['box2startxz'] = [self.ui.doubleSpinBox_Box2_startx.value(),
                                                     self.ui.doubleSpinBox_Box2_startz.value()]
        self.config_info['Loader']['box3startxz'] = [self.ui.doubleSpinBox_Box3_startx.value(),
                                                     self.ui.doubleSpinBox_Box3_startz.value()]
        self.config_info['Loader']['box4startxz'] = [self.ui.doubleSpinBox_Box4_startx.value(),
                                                     self.ui.doubleSpinBox_Box4_startz.value()]

        self.config_info['Loader']['boxxgap'] = float(self.ui.doubleSpinBox_BoxXGap.value())
        self.config_info['Loader']['boxzgap'] = float(self.ui.doubleSpinBox_BoxZGap.value())
        self.config_info['Loader']['slidepush'] = float(self.ui.spinBox_slide_push.value())
        self.config_info['Loader']['slidereturn'] = float(self.ui.spinBox_slide_return.value())
        self.config_info['Loader']['xavoid'] = float(self.ui.doubleSpinBox_Xavoid.value())
        self.config_info['Loader']['zlift'] = float(self.ui.doubleSpinBox_Zlift.value())
        self.config_info['Loader']['xend'] = float(self.ui.doubleSpinBox_connect_micro_x.value())
        self.config_info['Loader']['zend'] = float(self.ui.doubleSpinBox_connect_micro_z.value())
        self.config_info['Loader']['cameraindex'] = int(self.ui.spinBox_cameraindex.value())
        self.config_info['Loader']['cameraexposure'] = int(self.ui.spinBox_cameraexposure.value())
        self.config_info['Loader']['zcamera'] = float(self.ui.doubleSpinBox_zcamera.value())
        self.config_info['Loader']['rectanglex1'] = int(self.ui.spinBox_rectangleX1.value())
        self.config_info['Loader']['rectangley1'] = int(self.ui.spinBox_rectangleY1.value())
        self.config_info['Loader']['rectanglex2'] = int(self.ui.spinBox_rectangleX2.value())
        self.config_info['Loader']['rectangley2'] = int(self.ui.spinBox_rectangleY2.value())

        # 创建消息框
        reply = QMessageBox.warning(None, "保存当前参数", "确认保存当前参数？",
                                    QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
        # 根据用户的选择进行处理
        if reply == QMessageBox.StandardButton.Ok:
            # 保存配置信息到文件
            self.config.save_config_info(self.config_info)
            self.Updata_textEdit_log.emit('保存设置成功')
        elif reply == QMessageBox.StandardButton.Cancel:
            self.Updata_textEdit_log.emit('取消保存')

    def test_micro_movex2(self):
        """
        测试显微镜在X轴方向上的移动功能。

        本函数尝试根据UI界面上的doubleSpinBox_test_micro_movex2控件的值，
        调用显微镜动作模块（如果已初始化）来移动显微镜到指定的X坐标。
        如果在移动过程中发生异常，异常信息将被打印出来。

        注意：本函数不返回任何值。
        """
        try:
            # 检查ActionMicroscope是否已初始化，如果已初始化，则尝试进行X轴移动
            if self.ActionMicroscope is not None:
                # 调用显微镜移动函数，传入UI控件的值作为目标X坐标
                self.ActionMicroscope.microscope_move_x_to(self.ui.doubleSpinBox_test_micro_movex2.value())
        except Exception as e:
            # 捕获并打印任何在移动过程中发生的异常
            print(e)

    def test_micro_movey2(self):
        """
        尝试控制显微镜进行Y轴微调。

        本函数尝试根据UI中双精度旋钮的值，调整显微镜的Y轴位置。
        如果ActionMicroscope对象已初始化，即不为None，则调用其方法进行移动。
        如果在移动过程中发生异常，异常信息将被打印。

        参数:
        无

        返回值:
        无
        """
        try:
            # 检查ActionMicroscope对象是否已初始化，以避免空指针异常
            if self.ActionMicroscope is not None:
                # 根据UI中doubleSpinBox_test_micro_movey2控件的值，调用显微镜移动函数
                self.ActionMicroscope.microscope_move_y_to(self.ui.doubleSpinBox_test_micro_movey2.value())
        except Exception as e:
            # 捕获并打印任何在移动过程中发生的异常
            print(e)

    def test_micro_movez2(self):
        """
        测试显微镜的Z轴微调功能。

        本函数尝试根据UI界面上的doubleSpinBox_test_micro_movez2控件的值，
        调用显微镜动作类的microscope_move_z_to方法，将显微镜的Z轴移动到指定位置。
        如果在执行过程中遇到任何异常，将会打印出异常信息。

        注意：本函数假设ActionMicroscope属性已经被正确初始化为一个显微镜动作类的实例。
        """
        try:
            # 检查ActionMicroscope是否已经初始化，如果已经初始化，则尝试执行Z轴移动操作
            if self.ActionMicroscope is not None:
                # 根据UI界面上的值调整显微镜的Z轴位置
                self.ActionMicroscope.microscope_move_z_to(self.ui.doubleSpinBox_test_micro_movez2.value())
        except Exception as e:
            # 捕获并打印任何在执行过程中发生的异常
            print(e)

    def test_loader_movex2(self):
        """
        尝试将加载器移动到指定的X坐标。

        此方法尝试根据UI中双精度旋钮的值来移动动作加载器到指定的X坐标。如果动作加载器已初始化，
        则调用其移动到X坐标的方法。如果在移动过程中发生异常，异常信息将被打印。

        注意：此方法是测试目的，用于验证加载器的X坐标移动功能。
        """
        try:
            # 检查ActionLoader是否已初始化，如果已初始化，则根据UI的值移动到指定的X坐标
            if self.ActionLoader is not None:
                self.ActionLoader.move_x_to(self.ui.doubleSpinBox_test_loader_movex2.value())
        except Exception as e:
            # 打印任何在移动过程中发生的异常
            print(e)

    def test_loader_movey2(self):
        """
        尝试移动动作加载器到Y轴上的指定位置。

        本方法尝试根据UI中双精度旋钮的值，移动动作加载器的Y坐标。如果动作加载器已初始化，
        则调用其移动方法；否则，不执行任何操作。如果在移动过程中发生异常，异常信息将被打印。

        注意：此方法是针对特定UI元素设计的，其功能可能依赖于特定的UI布局和逻辑。
        """
        try:
            # 检查ActionLoader是否已初始化，如果已初始化，则根据UI的值移动Y轴
            if self.ActionLoader is not None:
                self.ActionLoader.move_y_to(self.ui.doubleSpinBox_test_loader_movey2.value())
        except Exception as e:
            # 打印异常信息，用于调试和错误跟踪
            print(e)

    def test_loader_movez2(self):
        """
        测试加载器的Z轴移动功能。

        该方法尝试调用ActionLoader对象的move_z_to方法，将Z轴移动到由ui的doubleSpinBox_test_loader_movez2控件指定的值。
        如果ActionLoader对象为None，则不执行移动操作。如果在移动过程中发生异常，异常信息将被打印。

        注意：此方法假设ActionLoader对象已经正确初始化并可用。
        """
        try:
            # 检查ActionLoader是否已初始化，如果已初始化，则执行Z轴移动操作
            if self.ActionLoader is not None:
                # 根据ui中的doubleSpinBox_test_loader_movez2控件的值来移动Z轴
                self.ActionLoader.move_z_to(self.ui.doubleSpinBox_test_loader_movez2.value())
        except Exception as e:
            # 捕获并打印在移动过程中可能发生的任何异常
            print(e)

    def open_cameraonly(self):
        camera.global_signals.image_updated.connect(self.upimage_fcous)
        self.Device.Create_liveController(0,self.Device.camera, self.Device.microcontroller)
        self.Device.liveController._set_trigger_fps(25)
        self.Device.liveController.start_live()
        self.camera_index = 0

    def close_cameraonly(self):
        camera.global_signals.image_updated.disconnect(self.upimage_fcous)
        self.Device.liveController.stop_live()
        self.Device.camera.disable_callback()
        self.camera_index = -1

    def open_camera1(self):
        camera.global_signals.image_updated.connect(self.upimage_fcous)
        self.Device.Create_liveController(1,self.Device.camera1, self.Device.microcontroller)
        self.Device.liveController._set_trigger_fps(25)
        self.Device.liveController.start_live()
        self.camera_index = 1

    def close_camera1(self):
        camera.global_signals.image_updated.disconnect(self.upimage_fcous)
        self.Device.liveController.stop_live()
        self.Device.camera1.disable_callback()
        self.camera_index = -1

    def open_camera2(self):
        camera.global_signals.image_updated.connect(self.upimage_fcous)
        self.Device.Create_liveController(2,self.Device.camera2, self.Device.microcontroller)
        self.Device.liveController._set_trigger_fps(25)
        self.Device.liveController.start_live()
        self.camera_index = 2

    def close_camera2(self):
        camera.global_signals.image_updated.disconnect(self.upimage_fcous)
        self.Device.liveController.stop_live()
        self.Device.camera2.disable_callback()
        self.camera_index = -1

    def open_led_only(self):
        self.Device.microcontroller.turn_on_illumination()
        self.led_index = 0

    def close_led_only(self):
        self.Device.microcontroller.turn_off_illumination()
        self.led_index = -1

    def open_led_1(self):
        self.Device.set_left_led()
        self.Device.microcontroller.turn_on_illumination()
        self.led_index = 1

    def close_led_1(self):
        self.Device.microcontroller.turn_off_illumination()
        self.led_index = -1

    def open_led_2(self):
        self.Device.set_right_led()
        self.Device.microcontroller.turn_on_illumination()
        self.led_index = 2

    def close_led_2(self):
        self.Device.microcontroller.turn_off_illumination()
        self.led_index = -1

    def sliderValueChanged_led(self):
        if self.led_index >= 0:
            value = self.ui.horizontalSlider_led_intensity.value()
            self.Device.microcontroller.turn_off_illumination()
            self.Device.up_led_intensity(self.led_index, value)
            self.Device.microcontroller.turn_on_illumination()

    def sliderValueChanged_camera(self):
        value = self.ui.horizontalSlider_exposure.value()
        if self.camera_index >= 0:
            self.Device.up_camera_exposure(self.camera_index, value)

    def set_scan(self):

        # 创建消息框
        reply = QMessageBox.warning(None, "参数更改！", "确认更像成当前扫描中心参数？",
                                    QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
        # 根据用户的选择进行处理
        if reply == QMessageBox.StandardButton.Ok:
            try:
                if self.config_info is not None:
                    if self.camera_index == 0:
                        self.config_info['Microscope']['单镜头扫描中心xy'][0] = float(self.ui.label_SETX.text())
                        self.config_info['Microscope']['单镜头扫描中心xy'][1] = float(self.ui.label_SETY.text())
                        self.config_info['Microscope'][
                            '对焦经验值单镜头'] = float(self.ui.label_SETZ.text()) / 1000 - 0.09
                    elif self.camera_index == 1:
                        self.config_info['Microscope']['玻片扫描中心xy20x'][0] = float(self.ui.label_SETX.text())
                        self.config_info['Microscope']['玻片扫描中心xy20x'][1] = float(self.ui.label_SETY.text())
                        self.config_info['Microscope']['对焦经验值20x'] = float(self.ui.label_SETZ.text()) / 1000 - 0.09
                    elif self.camera_index == 2:
                        self.config_info['Microscope']['玻片扫描中心xy50x'][0] = float(self.ui.label_SETX.text())
                        self.config_info['Microscope']['玻片扫描中心xy50x'][1] = float(self.ui.label_SETY.text())
                        self.config_info['Microscope']['对焦经验值50x'] = float(self.ui.label_SETZ.text()) / 1000 - 0.09
                self.updata_parameter.emit()
                self.save_setup()
                self.Updata_textEdit_log.emit('扫描参数更新成功')
            except:
                self.Updata_textEdit_log.emit('扫描参数更新失败')
        elif reply == QMessageBox.StandardButton.Cancel:
            self.Updata_textEdit_log.emit('取消更新参数')

    def set_exposure(self):
        # 创建消息框
        reply = QMessageBox.warning(None, "参数更改！", "确认更像成当前曝光参数？",
                                    QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
        # 根据用户的选择进行处理
        if reply == QMessageBox.StandardButton.Ok:
            try:
                # 曝光
                if self.camera_index >= 0:
                    self.Device.configurationManager.update_configuration_without_writing(1, 'ExposureTime',
                                                                                          int(self.ui.horizontalSlider_exposure.value() / 1000))
                    self.Device.configurationManager.update_configuration_without_writing(1, 'IlluminationIntensity',
                                                                                          self.ui.horizontalSlider_led_intensity.value())
                elif self.camera_index == 1:
                    self.Device.configurationManager.update_configuration_without_writing(1, 'ExposureTime',
                                                                                          int(self.ui.horizontalSlider_exposure.value() / 1000))
                    self.Device.configurationManager.update_configuration_without_writing(1, 'IlluminationIntensity',
                                                                                          self.ui.horizontalSlider_led_intensity.value())
                elif self.camera_index == 2:
                    self.Device.configurationManager.update_configuration_without_writing(2, 'ExposureTime',
                                                                                          int(self.ui.horizontalSlider_exposure.value() / 1000))
                    self.Device.configurationManager.update_configuration_without_writing(2, 'IlluminationIntensity',
                                                                                          self.ui.horizontalSlider_led_intensity.value())
                self.Device.configurationManager.save_configurations()
                self.Updata_textEdit_log.emit('曝光参数更新成功')
            except:
                self.Updata_textEdit_log.emit('曝光参数更新失败')

        elif reply == QMessageBox.StandardButton.Cancel:
            self.Updata_textEdit_log.emit('取消更新参数')

    def savepic(self):
        if self.save_pic is None:
            QMessageBox.warning(self, "错误", "没有捕获到图片，无法保存图片！")
            return

        default_filename = "image.png"  # 默认文件名
        file_path, _ = QFileDialog.getSaveFileName(self, "保存图片", default_filename,
                                                   "Images (*.png *.jpg *.bmp)")

        if file_path:
            # 将图片保存到文件
            img = cv2.cvtColor(self.save_pic, cv2.COLOR_RGB2BGR)
            if cv2.imwrite(file_path, img):
                QMessageBox.information(self, "成功", f"图片已成功保存到：{file_path}")
            else:
                QMessageBox.warning(self, "保存失败", "保存图片失败！")
        else:
            QMessageBox.warning(self, "提示", "未选择保存路径！")

    def change_savepath(self):
        folder_path = QFileDialog.getExistingDirectory(self, "选择文件夹")

        if folder_path:
            QMessageBox.warning(self, "图片保存路径修改成功", "路径为：" + folder_path)
            self.ui.label_savepath.setText(folder_path)
            self.config_info['ImageSaver']['savepath'] = folder_path
        else:
            QMessageBox.warning(self, "提示", "未选择文件夹！")

    @QtCore.Slot(float, float, float)
    def updateLabelXYZpos(self, xpos, ypos, zpos):
        """
        更新UI中显示XYZ位置的标签数值。

        通过此函数，可以动态更新用户界面中表示X、Y、Z位置的三个标签的数值，
        以反映系统的当前坐标位置。使用了Qt的Slot机制，以便与界面组件的信号连接，
        当坐标位置发生变化时，自动更新标签显示。

        参数:
        xpos (float): X坐标的位置。
        ypos (float): Y坐标的位置。
        zpos (float): Z坐标的位置。
        """
        self.ui.label_SETX.setNum(xpos)
        self.ui.label_SETY.setNum(ypos)
        self.ui.label_SETZ.setNum(zpos)

    @QtCore.Slot(int, list, numpy.ndarray)
    def upimage_puzzle(self, a, Point_XY, img):
        """
        Update the image in the graphics view of the GUI.

        This function is used to display a processed image in the graphics view, and can adjust the alignment and clear the scene
        according to the input parameters. It supports both grayscale and RGB images.

        Parameters:
        a: An integer flag, used to determine whether to reset the alignment and clear the scene.
        Point_XY: A list containing two integers, representing the coordinates where the image is to be located in the scene.
        img: A numpy array representing the image data.
        """
        # Show the graphics view
        # self.ui.graphicsView.show()
        # Determine the image channel and set the corresponding QImage format
        channel = len(img.shape)
        format_ = QtGui.QImage.Format_Grayscale8 if channel == 2 else QtGui.QImage.Format_RGB888
        # Convert the OpenCV image to QImage
        q_img = create_qimage_from_cvimg(img, format_)
        # If a is 1, reset the alignment of the graphics view and clear the scene
        if a == 1:
            self.ui.graphicsView.setAlignment(Qt.AlignLeft | Qt.AlignTop)
            self.scene_puzzle.clear()
        # Scale the pixmap to the specified size
        """Add a scaled pixmap to the scene at a specific position."""
        scaled_pixmap = QtGui.QPixmap.fromImage(q_img).scaled(
            int(self.used_width),
            int(self.used_height)
        )
        # Create a pixmap item and set its position
        pixmap_item = QGraphicsPixmapItem(scaled_pixmap)
        pixmap_item.setPos(Point_XY[1] * int(self.used_width),
                           Point_XY[0] * int(self.used_height))
        # Center the graphics view on the pixmap
        self.ui.graphicsView.centerOn(Point_XY[1] * int(self.used_width) + int(self.used_width / 2),
                                      Point_XY[0] * int(self.used_height) + int(self.used_height / 2))
        # Add the pixmap item to the scene
        self.scene_puzzle.addItem(pixmap_item)

    @QtCore.Slot(numpy.ndarray)
    def upimage_fcous(self, img):
        """
        显示图像焦点区域。

        此方法用于在graphicsView_fcous中显示传入的图像。它首先清除之前的显示内容，
        然后根据图像的通道数决定QImage的格式，将OpenCV格式的图像转换为QImage，
        并在场景中添加一个QGraphicsPixmapItem来显示图像。最后，调整视图以适应图像
        的大小并居中显示。

        :param img: 要显示的图像，一个numpy.ndarray对象。
        """
        if img is None:
            return
        self.save_pic = img
        # 清除场景中的现有物品，为新图像做准备
        self.scene_focus.clear()

        # 根据图像通道数决定QImage的格式
        channel = len(img.shape)
        format_ = QtGui.QImage.Format_Grayscale8 if channel == 2 else QtGui.QImage.Format_RGB888

        # 将OpenCV格式的图像转换为QImage
        q_img = create_qimage_from_cvimg(img, format_)
        # 从QImage创建QPixmap
        pixmap = QtGui.QPixmap.fromImage(q_img)
        # 创建QGraphicsPixmapItem以在场景中显示图像
        pixmap_item = QGraphicsPixmapItem(pixmap)
        # 将图像项添加到场景中
        self.scene_focus.addItem(pixmap_item)
        # 调整视图以适应图像的大小，并保持宽高比
        self.ui.graphicsView_fcous.fitInView(pixmap_item, Qt.KeepAspectRatio)
        # 将视图的对齐方式设置为居中
        self.ui.graphicsView_fcous.setAlignment(Qt.AlignCenter)

    @QtCore.Slot()
    def clear_points(self):
        """
        清空当前所有点的数据，用于重置或开始新的绘图。

        该方法通过调用create_empty_pixmap方法来实现清空操作，
        目的是为了在图形界面中清除之前的点数据，为新的绘图操作做准备。
        """
        self.create_empty_pixmap()

    def create_empty_pixmap(self):
        """
        创建一个空的 pixmap 对象，并将其设置为 ui 中 label_slide 的内容。
        如果 label_slide 当前已经有 pixmap，就使用现有的 pixmap；
        否则，根据 label_slide 的大小创建一个新的 pixmap。
        """
        # 根据 label_slide 是否已有 pixmap 来决定是获取现有 pixmap 还是创建新 pixmap
        pixmap = self.ui.label_slide.pixmap() if self.ui.label_slide.pixmap() else QPixmap(self.ui.label_slide.size())
        # 设置 pixmap 的背景颜色为灰色
        color = QColor(186, 186, 186)
        pixmap.fill(color)
        # 将处理后的 pixmap 设置给 label_slide
        self.ui.label_slide.setPixmap(pixmap)

    @QtCore.Slot(list, int)
    def update_points(self, point, region_width):
        """
        更新标注点的位置。

        根据区域宽度的不同，调整点的位置并更新显示。此函数用于在图形用户界面中，
        根据用户的选择，动态修改图像上标注点的位置。

        参数:
        point: 包含x和y坐标的列表，表示标注点的当前位置。
        region_width: int，表示当前区域的宽度，用于确定点的绘制位置。
        """
        # 获取当前标签控件中的像素映射对象，用于后续在上面绘制点
        pixmap = self.ui.label_slide.pixmap()
        # 创建一个画家对象，用于在pixmap上绘制
        painter = QPainter(pixmap)
        # 开启抗锯齿渲染，以获得更平滑的绘制效果
        painter.setRenderHint(QPainter.Antialiasing)
        # 设置绘制笔的颜色和宽度
        pen = QPen(Qt.red)
        pen.setWidth(2)
        painter.setPen(pen)
        # 定义一个比例因子，用于根据区域宽度调整点的位置
        xishu = 2
        # 根据区域宽度的不同，计算并绘制点的位置
        if region_width == 4:
            painter.drawPoint(QPoint(point[0] + 85 - 5, point[1] + 40 - 5))
        elif region_width == 8:
            painter.drawPoint(QPoint(int(point[0] * xishu) + 85 - 10, int(point[1] * xishu) + 40 - 10))
        else:
            painter.drawPoint(QPoint(point[0] + 85 - 20, point[1] + 40 - 20))
        # 绘制操作完成，结束画家对象
        painter.end()
        # 更新标签控件的像素映射，显示绘制后的结果
        self.ui.label_slide.setPixmap(pixmap)
        # 强制标签控件更新，确保绘制的点能够显示出来
        self.ui.label_slide.update()

    @QtCore.Slot(str, numpy.ndarray, str)
    def finish(self, code, img, multiple):
        pass

    @QtCore.Slot()
    def activate(self):
        """
        启用相关按钮，以允许用户进行操作。

        此方法通过启用运行、微重置和加载器重置按钮，为用户提供执行不同操作的权限。
        这通常在程序进入特定状态或满足特定条件时被调用。
        """
        # 启用运行按钮，允许用户触发相关运行操作
        self.ui.pushButton_run.setEnabled(True)
        # 启用微重置按钮，允许用户进行轻微的系统重置操作
        self.ui.pushButton_micro_reset.setEnabled(True)
        # 启用加载器重置按钮，允许用户重置加载器至初始状态
        self.ui.pushButton_loader_reset.setEnabled(True)

    @QtCore.Slot(str)
    def updata_log(self, log):
        """
        更新日志文本框的内容。

        通过此方法将日志文本追加到用户界面的日志文本框中，以便用户可以实时查看程序运行的日志信息。

        :param log: 需要添加到日志文本框的字符串信息
        """
        self.ui.textEdit_log.append(log)

    @QtCore.Slot(str)
    def updata_ID(self, ID):
        """
        更新文本编辑框中的ID文本。

        此函数被设计为接收一个字符串类型的ID，并将其显示在用户界面的文本编辑框中。
        使用了Qt的Slot装饰器，使得这个函数可以作为信号的接收者，当接收到信号时，
        函数会被调用并更新文本编辑框的内容。

        参数:
        ID (str): 需要显示在文本编辑框中的ID字符串。
        """
        self.ui.textEdit_ID.setText(ID)

    @QtCore.Slot(int, str)
    def write_log(self, flage, info):
        """
        根据标志位写入日志信息。

        通过传入的标志位决定是记录普通信息还是警告信息。
        如果标志位为0，记录普通信息；如果标志位为1，记录警告信息。

        :param flage: 标志位，用于区分日志类型，0表示普通信息，1表示警告信息。
        :param info: 需要记录的日志信息。
        """
        try:
            # 根据标志位选择日志记录方法
            if flage == 0:
                self.logger.info(info)
            elif flage == 1:
                self.logger.warning(info)
        except Exception as e:
            # 捕获并打印日志记录过程中可能出现的异常
            print(e)

    @QtCore.Slot()
    def Up_parameter(self):
        """
        根据配置信息更新界面参数。

        从config_info中读取各种参数设置，并更新到用户界面的相应控件中。
        这包括任务参数、图像保存参数、设备参数、显微镜参数和相机参数。
        """
        try:
            # 更新任务参数
            # 任务分配参数
            boxes = self.config_info['Task']['box']
            for box in boxes:
                # 根据box值设置复选框状态
                if box == 1:
                    self.ui.checkBox_1.setChecked(True)
                elif box == 2:
                    self.ui.checkBox_2.setChecked(True)
                elif box == 3:
                    self.ui.checkBox_3.setChecked(True)
                elif box == 4:
                    self.ui.checkBox_4.setChecked(True)
            # 更新滑块数目
            self.ui.spinBox_slide_number.setValue(int(self.config_info['Task']['slidenumber']))

            # 更新图像保存参数
            # 图像参数
            self.ui.spinBox_maxworkers.setValue(int(self.config_info['ImageSaver']['maxworkers']))
            self.ui.spinBox_imagestitchsize.setValue(int(self.config_info['ImageSaver']['imagestitchsize']))
            self.ui.spinBox_AIimage.setValue(int(self.config_info['ImageSaver']['newimage']))
            self.ui.spinBox_queuenumber.setValue(int(self.config_info['ImageSaver']['queuenumber']))
            self.ui.comboBox_pixelformat.setCurrentText(self.config_info['ImageSaver']['pixelformat'])
            self.ui.spinBox_imagequailty.setValue(int(self.config_info['ImageSaver']['imagequailty']))
            self.ui.label_savepath.setText(self.config_info['ImageSaver']['savepath'])

            # 更新设备参数
            # 设备参数
            self.ui.spinBox_cameranumber.setValue(int(self.config_info['Device']['cameranumber']))
            # 根据loaderflage设置复选框状态
            if self.config_info['Device']['loaderflage']:
                self.ui.checkBox_loaderflage.setChecked(True)
            else:
                self.ui.checkBox_loaderflage.setChecked(False)
            # 根据microscope设置复选框状态
            if self.config_info['Device']['microscope']:
                self.ui.checkBox_microscopeflage.setChecked(True)
            else:
                self.ui.checkBox_microscopeflage.setChecked(False)

            # 更新显微镜参数
            # 显微镜参数
            self.ui.comboBox_MicroCom.setCurrentText(self.config_info['Microscope']['串口'])
            self.ui.doubleSpinBox_50xcenterx.setValue(float(self.config_info['Microscope']['玻片扫描中心xy50x'][0]))
            self.ui.doubleSpinBox_50xcentery.setValue(float(self.config_info['Microscope']['玻片扫描中心xy50x'][1]))
            self.ui.doubleSpinBox_20xcenterx.setValue(float(self.config_info['Microscope']['玻片扫描中心xy20x'][0]))
            self.ui.doubleSpinBox_20xcentery.setValue(float(self.config_info['Microscope']['玻片扫描中心xy20x'][1]))
            self.ui.doubleSpinBox_Onlycenterx.setValue(float(self.config_info['Microscope']['单镜头扫描中心xy'][0]))
            self.ui.doubleSpinBox_Onlycentery.setValue(float(self.config_info['Microscope']['单镜头扫描中心xy'][1]))
            self.ui.spinBox_scan_w.setValue(int(self.config_info['Microscope']['玻片扫描区域宽度']))
            self.ui.spinBox_scan_h.setValue(int(self.config_info['Microscope']['玻片扫描区域高度']))
            self.ui.doubleSpinBox_50xzfocus.setValue(float(self.config_info['Microscope']['对焦经验值50x']))
            self.ui.doubleSpinBox_20xzfocus.setValue(float(self.config_info['Microscope']['对焦经验值20x']))
            self.ui.doubleSpinBox_Onlyzfocus.setValue(float(self.config_info['Microscope']['对焦经验值单镜头']))
            self.ui.comboBox_FocusMethod.setCurrentText(str(self.config_info['Microscope']['对焦方式']))
            self.ui.comboBox_Objective.setCurrentText(str(self.config_info['Microscope']['对焦倍数'][0]))
            self.ui.comboBox_Objective_SYS.setCurrentText(str(self.config_info['Microscope']['对焦倍数'][1]))
            self.ui.spinBox_FocusNumber.setValue(int(self.config_info['Microscope']['对焦步数']))
            self.ui.doubleSpinBox_FocusStep.setValue(float(self.config_info['Microscope']['对焦分辨率']))
            self.ui.spinBox_FocusGap_number.setValue(int(self.config_info['Microscope']['隔点对焦步长']))
            self.ui.doubleSpinBox_connect_loader_x.setValue(float(self.config_info['Microscope']['xend']))
            self.ui.doubleSpinBox_connect_loader_y.setValue(float(self.config_info['Microscope']['yend']))

            # 更新相机参数
            # 相机参数
            self.ui.doubleSpinBox_50xCalibration.setValue(float(self.config_info['Camera']['像素标定50x']))
            self.ui.doubleSpinBox_20xCalibration.setValue(float(self.config_info['Camera']['像素标定20x']))
            self.ui.doubleSpinBox_OnlyCalibration.setValue(float(self.config_info['Camera']['单镜头标定']))
            self.ui.doubleSpinBox_50xWB_R.setValue(float(self.config_info['Camera']['wb50x'][0]))
            self.ui.doubleSpinBox_50xWB_G.setValue(float(self.config_info['Camera']['wb50x'][1]))
            self.ui.doubleSpinBox_50xWB_B.setValue(float(self.config_info['Camera']['wb50x'][2]))
            self.ui.doubleSpinBox_20xWB_R.setValue(float(self.config_info['Camera']['wb20x'][0]))
            self.ui.doubleSpinBox_20xWB_G.setValue(float(self.config_info['Camera']['wb20x'][1]))
            self.ui.doubleSpinBox_20xWB_B.setValue(float(self.config_info['Camera']['wb20x'][2]))
            self.ui.doubleSpinBox_OnlyWB_R.setValue(float(self.config_info['Camera']['wbone'][0]))
            self.ui.doubleSpinBox_OnlyWB_G.setValue(float(self.config_info['Camera']['wbone'][1]))
            self.ui.doubleSpinBox_OnlyWB_B.setValue(float(self.config_info['Camera']['wbone'][2]))

            # 更新装载器参数
            # 装载器参数
            self.ui.comboBox_LoaderCom.setCurrentText(self.config_info['Loader']['串口'])
            self.ui.doubleSpinBox_Box1_startx.setValue(float(self.config_info['Loader']['box1startxz'][0]))
            self.ui.doubleSpinBox_Box1_startz.setValue(float(self.config_info['Loader']['box1startxz'][1]))
            self.ui.doubleSpinBox_Box2_startx.setValue(float(self.config_info['Loader']['box2startxz'][0]))
            self.ui.doubleSpinBox_Box2_startz.setValue(float(self.config_info['Loader']['box2startxz'][1]))
            self.ui.doubleSpinBox_Box3_startx.setValue(float(self.config_info['Loader']['box3startxz'][0]))
            self.ui.doubleSpinBox_Box3_startz.setValue(float(self.config_info['Loader']['box3startxz'][1]))
            self.ui.doubleSpinBox_Box4_startx.setValue(float(self.config_info['Loader']['box4startxz'][0]))
            self.ui.doubleSpinBox_Box4_startz.setValue(float(self.config_info['Loader']['box4startxz'][1]))
            self.ui.doubleSpinBox_BoxXGap.setValue(float(self.config_info['Loader']['boxxgap']))
            self.ui.doubleSpinBox_BoxZGap.setValue(float(self.config_info['Loader']['boxzgap']))
            self.ui.spinBox_slide_push.setValue(int(self.config_info['Loader']['slidepush']))
            self.ui.spinBox_slide_return.setValue(int(self.config_info['Loader']['slidereturn']))
            self.ui.doubleSpinBox_Xavoid.setValue(float(self.config_info['Loader']['xavoid']))
            self.ui.doubleSpinBox_Zlift.setValue(float(self.config_info['Loader']['zlift']))
            self.ui.doubleSpinBox_connect_micro_x.setValue(float(self.config_info['Loader']['xend']))
            self.ui.doubleSpinBox_connect_micro_z.setValue(float(self.config_info['Loader']['zend']))
            self.ui.spinBox_cameraindex.setValue(int(self.config_info['Loader']['cameraindex']))
            self.ui.spinBox_cameraexposure.setValue(int(self.config_info['Loader']['cameraexposure']))
            self.ui.doubleSpinBox_zcamera.setValue(float(self.config_info['Loader']['zcamera']))
            self.ui.spinBox_rectangleX1.setValue(int(self.config_info['Loader']['rectanglex1']))
            self.ui.spinBox_rectangleY1.setValue(int(self.config_info['Loader']['rectangley1']))
            self.ui.spinBox_rectangleX2.setValue(int(self.config_info['Loader']['rectanglex2']))
            self.ui.spinBox_rectangleY2.setValue(int(self.config_info['Loader']['rectangley2']))
        except Exception as e:
            print(e)

    @QtCore.Slot(float)
    def up_progress(self, vlaue):
        """
        更新进度条的值。

        通过此方法设置进度条的显示进度。使用了Qt的Slot装饰器，使得此方法可以作为信号连接，
        以便于在GUI界面中动态更新进度条的进度。

        参数:
        vlaue (float): 进度条的新值。此值将被设置为进度条的当前进度。
        """
        self.ui.progressBar.setValue(vlaue)

    def closeEvent(self, event):
        # 在窗口关闭事件中触发的函数
        self.close_thing()
        event.accept()

    def close_thing(self):
        if self.Saver is not None:
            self.Saver.stop()

        # 执行需要在应用程序退出时触发的操作
        if self.Device is None:
            pass
        else:
            self.Device.close_device()
