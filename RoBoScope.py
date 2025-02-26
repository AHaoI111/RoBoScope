# -*- encoding: utf-8 -*-
"""
@Description:
程序主函数入口
@File    :   main.py
@Time    :   2024/07/16
@Author  :   Li QingHao
@Version :   2.0
@Time_END :  最后修改时间：
@Developers_END :  最后修改作者：
"""
# 标准库
import sys
import os
import time
import uuid
import json
import math
import shutil
import re
import struct
import logging
import platform
from datetime import datetime
from configparser import ConfigParser
import random

# 第三方库
import cv2  # OpenCV
import pandas
import numpy as np  # np
import pyqtgraph as pg
import scipy
import scipy.signal
from PySide6 import QtCore
from PySide6.QtWidgets import QMainWindow
from scipy.ndimage import label
from lxml import etree as ET
import imageio
import serial  # pySerial
from serial.tools import list_ports
from PIL import Image
import yaml
import crcmod
from crc import CrcCalculator, Crc8
import requests
import base64
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from uvicorn import Server, Config
import subprocess

# 并发库
from concurrent.futures import ThreadPoolExecutor
from queue import Queue
import threading
# from threading import Thread, Lock

# PySide6
from PySide6.QtCore import QObject, Signal, Qt

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from UI.modules import *
from UI.widgets import *

os.environ["QT_FONT_DPI"] = "100"  # FIX Problem for High DPI and Scale above 100%

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None
# Set font for QPlainTextEdit
font = QFont("Arial", 12)  # Use a font that supports Chinese characters

import Drives.camera as camera
from DataSaver.Saverdata import Saver
from utils import read_config
from apply.task_info import apply_task_info
from utils.action_loader import ActionLoader
from utils.action_microscope import ActionMicroscope
import Server.FastAPIThread as FastAPIThread
from Server import Requester
from utils import Scan


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
    cvimg: np.ndarray
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
    return QImage(
        bytes(cvimg.data), width, height, bytes_per_line,
        format_
    )


def parse_json_from_text_edit(json_text):
    # Parse the JSON text to a Python dictionary
    parsed_data = json.loads(json_text)
    return parsed_data


class MainWindow(QMainWindow):
    Updata_textEdit_log = Signal(str)
    updata_internet_info = Signal(str)
    updata_parameter = Signal()
    live_img = Signal(np.ndarray)
    finished_test = Signal()

    def __init__(self):
        # 调用父类QMainWindow的构造函数进行初始化
        QMainWindow.__init__(self)

        # 设置全局小部件变量
        # ///////////////////////////////////////////////////////////////
        # 加载用户界面文件（Ui_MainWindow）并设置给widgets
        self.Scanning = None
        self.remaining_time = 0
        self.plan_points = {}
        self.plan = []
        self.ui = Ui_MainWindow()
        # 使用widgets设置用户界面
        self.ui.setupUi(self)
        self.scale_factor = 2.0
        # 定义一个全局变量widgets指向widgets，方便其他地方引用
        global widgets
        widgets = self.ui
        widgets.plainTextEdit_micro_sys.setFont(font)
        # 配置自定义标题栏
        # ///////////////////////////////////////////////////////////////
        # 设置是否启用自定义标题栏
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # 设置应用程序名称和描述
        # ///////////////////////////////////////////////////////////////
        # 应用程序名称
        title = "KMS"
        # 应用程序描述
        description = "KMS-RoBoScope"
        # 设置窗口标题
        self.setWindowTitle(title)
        # 设置右侧标题信息
        widgets.titleRightInfo.setText(description)

        # 设置菜单切换功能
        # ///////////////////////////////////////////////////////////////
        # 当点击toggleButton时，调用toggleMenu方法切换菜单
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # 设置UI定义
        # ///////////////////////////////////////////////////////////////
        # 调用UIFunctions.uiDefinitions方法来设置UI定义
        UIFunctions.uiDefinitions(self)

        # 按钮点击事件
        # ///////////////////////////////////////////////////////////////

        # 左侧菜单按钮点击事件
        # 当点击左侧菜单按钮时，触发buttonClick方法
        widgets.btn_scan.clicked.connect(self.buttonClick)
        widgets.btn_setting.clicked.connect(self.buttonClick)
        widgets.btn_test.clicked.connect(self.buttonClick)
        widgets.btn_internet.clicked.connect(self.buttonClick)

        # 显示应用程序
        # ///////////////////////////////////////////////////////////////
        # 显示主窗口
        self.show()

        # 设置主页和选择菜单
        # ///////////////////////////////////////////////////////////////
        # 将堆叠小部件的当前页面设置为home页面
        widgets.stackedWidget.setCurrentWidget(widgets.home)
        # 为btn_home按钮应用选中样式
        widgets.btn_scan.setStyleSheet(UIFunctions.selectMenu(widgets.btn_scan.styleSheet()))

        """
                初始化窗口类，设置窗口的基本属性和操作。

                :param splash: 启动屏幕对象，用于显示程序启动过程中的信息。
        """

        self.save_pic = None
        # 显示启动信息
        self.config_info = None
        self.config = None
        self.i = 0

        # 初始化各种对象和变量
        self.logger = None
        self.thread_Task = None
        self.task = None
        self.ActionLoader = None
        self.ActionMicroscope = None
        self.RUN = None

        self.Device = None
        self.Saver = None

        self.config = read_config.ConfigReader()
        self.config_info = self.config.get_config_info()

        # 初始化保存对象
        # 保存
        self.Saver = Saver(self.config_info['ImageSaver'])

        # 初始化图形场景
        # 拼图控件
        self.scene_puzzle = QGraphicsScene()
        widgets.graphicsView.setScene(self.scene_puzzle)
        # 显示graphicsView_fcous以准备显示图像
        widgets.graphicsView.show()

        # 对焦控件
        self.scene_focus = QGraphicsScene()
        widgets.graphicsView_fcous.setScene(self.scene_focus)
        # 显示graphicsView_fcous以准备显示图像
        widgets.graphicsView_fcous.show()

        # 实时控件
        # 设置能够拖动
        widgets.graphicsView_live.setDragMode(QGraphicsView.ScrollHandDrag)
        self.scene_live = QGraphicsScene()
        widgets.graphicsView_live.setScene(self.scene_live)
        # 显示graphicsView_fcous以准备显示图像
        widgets.graphicsView_live.show()
        widgets.scrollArea.setWidgetResizable(True)

        # 初始化界面参数
        # 加载界面参数

        self.used_width = int(100)
        self.used_height = int(100)
        self.led_index = -1
        self.camera_index = -1

        # 绑定按钮点击事件
        # 扫描
        widgets.pushButton_run.clicked.connect(self.run)
        widgets.pushButton_slide_task.clicked.connect(self.show_slide_task)
        # 暂停
        widgets.pushButton_pause.clicked.connect(self.pause)
        # 复位显微镜
        widgets.pushButton_micro_reset.clicked.connect(self.micro_reset)
        # 复位loader
        widgets.pushButton_loader_reset.clicked.connect(self.loader_test)
        # 保存参数
        widgets.pushButton_save.clicked.connect(self.save_setup)
        widgets.pushButton_set_ip.clicked.connect(self.save_setup)

        # 启用按钮
        widgets.pushButton_run.setEnabled(True)
        widgets.pushButton_pause.setEnabled(True)
        widgets.pushButton_micro_reset.setEnabled(True)
        widgets.pushButton_loader_reset.setEnabled(True)
        ##
        self.Updata_textEdit_log.connect(self.updata_log)
        self.updata_internet_info.connect(self.updata_internet)
        self.create_empty_pixmap()

        self.initialize()

        # 加载参数
        self.updata_parameter.connect(self.Up_parameter)
        self.updata_parameter.emit()

        # 绑定调试按钮点击事件
        # 调试
        widgets.pushButton_test_micro_movex2.clicked.connect(self.test_micro_movex2)
        widgets.pushButton_test_micro_movey2.clicked.connect(self.test_micro_movey2)
        widgets.pushButton_test_micro_movez2.clicked.connect(self.test_micro_movez2)
        widgets.pushButton_test_loader_movex2.clicked.connect(self.test_loader_movex2)
        widgets.pushButton_test_loader_movey2.clicked.connect(self.test_loader_movey2)
        widgets.pushButton_test_loader_movez2.clicked.connect(self.test_loader_movez2)

        widgets.pushButton_open_cameraonly.clicked.connect(self.open_cameraonly)
        widgets.pushButton_close_cameraonly.clicked.connect(self.close_cameraonly)
        widgets.pushButton_open_camera_low.clicked.connect(self.open_camera_low)
        widgets.pushButton_close_camera_low.clicked.connect(self.close_camera_low)
        widgets.pushButton_open_camera_high.clicked.connect(self.open_camera_high)
        widgets.pushButton_close_camera_high.clicked.connect(self.close_camera_high)

        widgets.pushButton_open_led_only.clicked.connect(self.open_led_only)
        widgets.pushButton_close_led_only.clicked.connect(self.close_led_only)
        widgets.pushButton_open_led_low.clicked.connect(self.open_led_low)
        widgets.pushButton_close_led_low.clicked.connect(self.close_led_low)
        widgets.pushButton_open_led_high.clicked.connect(self.open_led_high)
        widgets.pushButton_close_led_high.clicked.connect(self.close_led_high)

        widgets.pushButton_refresh_plan.clicked.connect(self.refresh_plan)

        widgets.pushButton_test_get_slide.clicked.connect(self.test_get_slide)
        widgets.pushButton_test_put_slide.clicked.connect(self.test_put_slide)
        widgets.pushButton_test_move_2_singleview_center.clicked.connect(self.test_move_2_singleview_center)
        widgets.pushButton_test_move_2_lowview_center.clicked.connect(self.test_move_2_lowview_center)
        widgets.pushButton_test_move_2_highview_center.clicked.connect(self.test_move_2_highview_center)
        self.finished_test.connect(self.close_msg_box)

        # 灯控
        widgets.horizontalSlider_led_intensity.valueChanged.connect(self.sliderValueChanged_led)
        # 曝光控制
        widgets.horizontalSlider_exposure.valueChanged.connect(self.sliderValueChanged_camera)
        # 确认当前扫描参数
        widgets.pushButton_save_scan.clicked.connect(self.set_scan)
        # 确认更改当前曝光参数
        widgets.pushButton_save_exposure.clicked.connect(self.set_exposure)
        # 捕获
        widgets.pushButton_savepic.clicked.connect(self.savepic)
        # 更换保存的图片路径
        widgets.pushButton_savepath.clicked.connect(self.change_savepath)
        self.Server = None
        # 服务器
        if self.config_info['Network']['flag']:
            # 发送请求类
            self.Request = Requester.Request(self.config_info['Network']['serverip'],
                                             self.config_info['Network']['serverport'],
                                             self.config_info['Network']['localip'],
                                             self.config_info['Network']['localport'])
            #
            widgets.pushButton_get.clicked.connect(self.get_request_res)
            self.Server = FastAPIThread.HTTPServer(self.config_info['Network']['localip'],
                                                   self.config_info['Network']['localport'])
            self.Server.Com2scope.config_info = self.config_info
            if self.config_info['Microscope']['sys']['当前系统'] == 'single':
                self.Server.Com2scope.led_camera.append(self.Device.configurationManager.configurations[0].camera_sn)
            elif self.config_info['Microscope']['sys']['当前系统'] == 'double':
                self.Server.Com2scope.led_camera.append(self.Device.configurationManager.configurations[0].camera_sn)
                self.Server.Com2scope.led_camera.append(self.Device.configurationManager.configurations[1].camera_sn)
            self.Server.Com2scope.send_scan_pic.connect(self.pre_scan_pic)
            if self.task is not None:
                self.Server.Com2scope.send_scan_label.connect(self.task.send2_request_pre_pic_label)
            self.Server.start()
            if self.Saver is not None:
                self.Saver.Request = self.Request
            if self.task is not None:
                self.task.request = self.Request
            if self.ActionMicroscope is not None:
                self.ActionMicroscope.request = self.Request
            self.Saver.up_points_high.connect(self.updata_points_high)

        # 定时器倒计时
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_time)

        widgets.stackedWidget.setCurrentWidget(widgets.scan)

    def wheelEvent(self, event):
        factor = 1.2
        if event.angleDelta().y() < 0:
            factor = 1.0 / factor

        # Apply the scaling transformation
        widgets.graphicsView_live.scale(factor, factor)
        event.accept()

    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    # ///////////////////////////////////////////////////////////////
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW HOME PAGE
        if btnName == "btn_scan":
            widgets.stackedWidget.setCurrentWidget(widgets.scan)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW WIDGETS PAGE
        if btnName == "btn_setting":
            widgets.stackedWidget.setCurrentWidget(widgets.setting)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW NEW PAGE
        if btnName == "btn_test":
            widgets.stackedWidget.setCurrentWidget(widgets.test)  # SET PAGE
            UIFunctions.resetStyle(self, btnName)  # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))  # SELECT MENU
        if btnName == "btn_internet":
            widgets.stackedWidget.setCurrentWidget(widgets.internet)  # SET PAGE
            UIFunctions.resetStyle(self, btnName)  # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))  # SELECT MENU

        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')

    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPosition().toPoint()

        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')

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
        # 根据配置信息决定是否初始化设备
        if self.config_info['Device']['microscope']:
            # 初始化设备对象
            if self.config_info['Device']['firmware'] == 'V1':
                from utils.Search_device_V1 import device

                self.Updata_textEdit_log.emit('firmware:V1')
            elif self.config_info['Device']['firmware'] == 'V2':
                from utils.Search_device_V2 import device
                self.Updata_textEdit_log.emit('firmware:V2')
            else:
                self.Updata_textEdit_log.emit('选择版本不正确，设备未启动')
                return
                # 启动设备
            self.Device = device(self.config_info)
            # 设备打开
            flag, flag_microscope, flag_camera, flag_camera1, flag_camera2, flag_loader = self.Device.open_device()
            # 根据设备打开状态给出相应反馈
            if flag:
                self.Updata_textEdit_log.emit('设备启动成功')
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
                # 如果启动失败，则禁用所有设备相关的用户界面按钮
                widgets.pushButton_run.setEnabled(False)
                widgets.pushButton_pause.setEnabled(False)
                widgets.pushButton_micro_reset.setEnabled(False)
                widgets.pushButton_loader_reset.setEnabled(False)
                widgets.pushButton_open_cameraonly.setEnabled(False)
                widgets.pushButton_close_cameraonly.setEnabled(False)
                widgets.pushButton_open_camera_low.setEnabled(False)
                widgets.pushButton_open_camera_low.setEnabled(False)
                widgets.pushButton_open_camera_high.setEnabled(False)
                widgets.pushButton_close_camera_high.setEnabled(False)
                widgets.pushButton_test_micro_movex2.setEnabled(False)
                widgets.pushButton_test_micro_movey2.setEnabled(False)
                widgets.pushButton_test_micro_movez2.setEnabled(False)
                widgets.pushButton_test_loader_movex2.setEnabled(False)
                widgets.pushButton_test_loader_movey2.setEnabled(False)
                widgets.pushButton_test_loader_movez2.setEnabled(False)
                widgets.pushButton_open_led_only.setEnabled(False)
                widgets.pushButton_close_led_only.setEnabled(False)
                widgets.pushButton_open_led_low.setEnabled(False)
                widgets.pushButton_close_led_low.setEnabled(False)
                widgets.pushButton_open_led_high.setEnabled(False)
                widgets.pushButton_close_led_high.setEnabled(False)
                widgets.pushButton_save_scan.setEnabled(False)
                widgets.pushButton_save_exposure.setEnabled(False)
                widgets.pushButton_test_get_slide.setEnabled(False)
                widgets.pushButton_test_put_slide.setEnabled(False)
                widgets.pushButton_test_move_2_singleview_center.setEnabled(False)
                widgets.pushButton_test_move_2_lowview_center.setEnabled(False)
                widgets.pushButton_test_move_2_highview_center.setEnabled(False)
                return
            # 进行设备自检
            flag = self.Device.detection_device()
            # 根据自检结果给出相应反馈
            if flag:
                self.Updata_textEdit_log.emit('设备自检成功')
                # 初始化显微镜动作对象，并设置相关事件处理函数
                # 显微镜行为类
                self.ActionMicroscope = ActionMicroscope(self.Device)
                # 扫描类
                self.Scanning = Scan.Scanning(self.ActionMicroscope, self.Saver)
                # 绑定扫描槽函数
                self.Scanning.updata_puzzle.connect(self.upimage_puzzle)
                self.Scanning.updata_focus.connect(self.upimage_fcous)
                self.Scanning.updata_point_clear.connect(self.clear_points)
                self.Scanning.updata_point_draw.connect(self.update_points)
                self.Scanning.updata_textEdit_log_microscope.connect(self.updata_log)
                self.Scanning.write_log_microscope.connect(self.write_log)
                self.Device.navigationController.xyzPos.connect(self.updateLabelXYZpos)
                self.Updata_textEdit_log.emit('显微镜系统初始化成功')
                # 如果配置了装载器，并且装载器打开成功，则初始化装载器动作对象
                if self.config_info['Device']['loaderflage'] and flag_loader == True:
                    self.ActionLoader = ActionLoader(self.Device.Loader, self.config_info)
                    self.Device.Loader.send_error.connect(self.loader_error)
                    flag = self.ActionLoader.open_camera()
                    if flag:
                        self.Updata_textEdit_log.emit('装载器相机初始化成功')
                    else:
                        self.Updata_textEdit_log.emit('装载器相机初始化失败')
                    self.Updata_textEdit_log.emit('装载器系统初始化成功')
                else:
                    self.Updata_textEdit_log.emit('没有设置装载器')
            else:
                self.Updata_textEdit_log.emit('设备自检失败')
                return
            # 初始化任务对象，并设置相关事件处理函数
            try:
                from apply.taskwork import Task
                # 初始化任务
                self.task = Task(self.ActionLoader, self.ActionMicroscope,self.Scanning)
                # 绑定槽函数
                self.task.activate_pushbutton.connect(self.activate)
                self.task.updata_textEdit_log_task.connect(self.updata_log)
                self.task.write_log_task.connect(self.write_log)
                self.task.test_single_step_pause.connect(self.test_single_step_pause)
                self.task.updata_Progress.connect(self.up_progress)
                self.task.stop_task.connect(self.close_msg_box)
            except:
                self.Updata_textEdit_log.emit('apply.taskwork.py文件不存在')
            # 启用相关用户界面按钮
            widgets.pushButton_pause.setEnabled(True)
            widgets.pushButton_micro_reset.setEnabled(True)
            widgets.pushButton_loader_reset.setEnabled(True)
            widgets.pushButton_run.setEnabled(True)
            if self.config_info['Device']['cameranumber'] == 1:
                widgets.pushButton_open_camera_low.setEnabled(False)
                widgets.pushButton_open_camera_high.setEnabled(False)
                widgets.pushButton_close_camera_low.setEnabled(False)
                widgets.pushButton_close_camera_high.setEnabled(False)
                widgets.pushButton_open_led_low.setEnabled(False)
                widgets.pushButton_close_led_high.setEnabled(False)
                widgets.pushButton_open_led_low.setEnabled(False)
                widgets.pushButton_close_led_high.setEnabled(False)
                widgets.pushButton_test_move_2_lowview_center.setEnabled(False)
                widgets.pushButton_test_move_2_highview_center.setEnabled(False)
            elif self.config_info['Device']['cameranumber'] == 2:
                widgets.pushButton_open_cameraonly.setEnabled(False)
                widgets.pushButton_close_cameraonly.setEnabled(False)
                widgets.pushButton_open_led_only.setEnabled(False)
                widgets.pushButton_close_led_only.setEnabled(False)
                widgets.pushButton_test_move_2_singleview_center.setEnabled(False)
        else:
            # 如果配置中没有显微镜，则禁用所有设备相关的用户界面按钮
            widgets.pushButton_run.setEnabled(False)
            widgets.pushButton_pause.setEnabled(False)
            widgets.pushButton_micro_reset.setEnabled(False)
            widgets.pushButton_loader_reset.setEnabled(False)
            widgets.pushButton_open_cameraonly.setEnabled(False)
            widgets.pushButton_close_cameraonly.setEnabled(False)
            widgets.pushButton_open_camera_low.setEnabled(False)
            widgets.pushButton_open_camera_high.setEnabled(False)
            widgets.pushButton_close_camera_low.setEnabled(False)
            widgets.pushButton_close_camera_high.setEnabled(False)
            widgets.pushButton_test_micro_movex2.setEnabled(False)
            widgets.pushButton_test_micro_movey2.setEnabled(False)
            widgets.pushButton_test_micro_movez2.setEnabled(False)
            widgets.pushButton_test_loader_movex2.setEnabled(False)
            widgets.pushButton_test_loader_movey2.setEnabled(False)
            widgets.pushButton_test_loader_movez2.setEnabled(False)
            widgets.pushButton_open_led_only.setEnabled(False)
            widgets.pushButton_close_led_only.setEnabled(False)
            widgets.pushButton_open_led_low.setEnabled(False)
            widgets.pushButton_close_led_low.setEnabled(False)
            widgets.pushButton_open_led_high.setEnabled(False)
            widgets.pushButton_close_led_high.setEnabled(False)
            widgets.pushButton_save_scan.setEnabled(False)
            widgets.pushButton_save_exposure.setEnabled(False)
            widgets.pushButton_test_get_slide.setEnabled(False)
            widgets.pushButton_test_put_slide.setEnabled(False)
            widgets.pushButton_test_move_2_singleview_center.setEnabled(False)
            widgets.pushButton_test_move_2_lowview_center.setEnabled(False)
            widgets.pushButton_test_move_2_highview_center.setEnabled(False)

    def show_slide_task(self):
        if self.ActionLoader is None:
            pass
        else:
            self.dialog = Dialog(slide_task=self.ActionLoader.slide_task,
                                 slide_points=self.ActionLoader.slide_points)  # 创建对话框实例
            self.dialog.reset_slide.connect(self.reset_slide_task)
            self.dialog.save_slide.connect(self.save_slide_task)
            self.dialog.exec()

    @Slot()
    def reset_slide_task(self):
        if self.ActionLoader is None:
            pass
        else:
            self.ActionLoader.reset_slide_task()
            self.dialog.slide_task = self.ActionLoader.slide_task
            self.dialog.flash()

    @Slot(np.ndarray)
    def save_slide_task(self, slide_task):
        if self.ActionLoader is None:
            pass
        else:
            self.ActionLoader.slide_task = slide_task
            self.ActionLoader.save_slide_task_file()
            print(slide_task)

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
        box_1 = None
        box_2 = None
        box_3 = None
        box_4 = None

        # 检查复选框1是否被选中，如果被选中，则将1添加到列表中
        if widgets.checkBox_1.isChecked():
            box_1 = True

        else:
            box_1 = False

        # 检查复选框2是否被选中，如果被选中，则将2添加到列表中
        if widgets.checkBox_2.isChecked():
            box_2 = True

        else:
            box_2 = False

        # 检查复选框3是否被选中，如果被选中，则将3添加到列表中
        if widgets.checkBox_3.isChecked():
            box_3 = True

        else:
            box_3 = False

        # 检查复选框4是否被选中，如果被选中，则将4添加到列表中
        if widgets.checkBox_4.isChecked():
            box_4 = True

        else:
            box_4 = False

        # 返回包含所有选中复选框值的列表
        return box_1, box_2, box_3, box_4

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
        widgets.pushButton_run.setEnabled(False)
        widgets.pushButton_pause.setEnabled(True)
        widgets.pushButton_micro_reset.setEnabled(False)
        widgets.pushButton_loader_reset.setEnabled(False)
        widgets.pushButton_open_cameraonly.setEnabled(False)
        widgets.pushButton_close_cameraonly.setEnabled(False)
        widgets.pushButton_open_camera_low.setEnabled(False)
        widgets.pushButton_open_camera_low.setEnabled(False)
        widgets.pushButton_close_camera_high.setEnabled(False)
        widgets.pushButton_close_camera_high.setEnabled(False)
        widgets.pushButton_test_micro_movex2.setEnabled(False)
        widgets.pushButton_test_micro_movey2.setEnabled(False)
        widgets.pushButton_test_micro_movez2.setEnabled(False)
        widgets.pushButton_test_loader_movex2.setEnabled(False)
        widgets.pushButton_test_loader_movey2.setEnabled(False)
        widgets.pushButton_test_loader_movez2.setEnabled(False)
        widgets.pushButton_open_led_only.setEnabled(False)
        widgets.pushButton_close_led_only.setEnabled(False)
        widgets.pushButton_open_led_low.setEnabled(False)
        widgets.pushButton_close_led_low.setEnabled(False)
        widgets.pushButton_open_led_high.setEnabled(False)
        widgets.pushButton_close_led_high.setEnabled(False)
        widgets.pushButton_save_scan.setEnabled(False)
        widgets.pushButton_save_exposure.setEnabled(False)
        widgets.pushButton_test_get_slide.setEnabled(False)
        widgets.pushButton_test_put_slide.setEnabled(False)
        widgets.pushButton_test_move_2_singleview_center.setEnabled(False)
        widgets.pushButton_test_move_2_lowview_center.setEnabled(False)
        widgets.pushButton_test_move_2_highview_center.setEnabled(False)
        Taskinfo = apply_task_info(self.config_info)
        Taskinfo['pre_request_flag'] = False
        Taskinfo['task_id'] = None
        try:
            selected_text = widgets.comboBox_Task.currentText()
            # 判断方案读取方案信息
            if selected_text is not None and len(self.plan) > 0:
                for plan in self.plan:
                    if selected_text == plan['name']:
                        # 方案的id
                        Taskinfo['task_type_id'] = plan['task_type_id']
                        # 双镜头系统
                        if Taskinfo['sys'] == "double":
                            # 判断是否启用高低倍配合
                            if plan['field_view_type'] != "None" and plan['camera'] == "all":
                                # 启用
                                Taskinfo['field_view_type'] = plan['field_view_type']
                                Taskinfo['scanmode'] = True
                                Taskinfo['region_w_low'] = plan['scan_width']
                                Taskinfo['region_h_low'] = plan['scan_hight']
                                Taskinfo['FocusMode_low'] = plan['focus_mode']['id']
                                if plan['focus_mode']['Gap_flag'] == "true":
                                    Taskinfo['fcous_Gap_low'] = plan['focus_mode']['gap']
                                Taskinfo['scan_label'] = plan['scan_label']
                                Taskinfo['scan_api'] = plan['field_view_model_url']
                                Taskinfo['max_views'] = plan['max_views']
                                # 获取任务id
                                task_id = self.Request.create_task(Taskinfo['task_type_id'], Taskinfo['savepath'])
                                Taskinfo['task_id'] = task_id
                            elif plan['field_view_type'] == "None" and plan['camera'] != "all":
                                # 不启用，只用单镜头扫描
                                Taskinfo['field_view_type'] = plan['field_view_type']
                                Taskinfo['scanmode'] = False
                                Taskinfo['scanmultiple'] = plan['camera']
                                if plan['camera'] == "low":
                                    Taskinfo['region_w_low'] = plan['scan_width']
                                    Taskinfo['region_h_low'] = plan['scan_hight']
                                    Taskinfo['FocusMode_low'] = plan['focus_mode']['id']
                                    if plan['focus_mode']['Gap_flag'] == "true":
                                        Taskinfo['fcous_Gap_low'] = plan['focus_mode']['gap']
                                    Taskinfo['scan_label'] = plan['scan_label']
                                    # 获取任务id
                                    task_id = self.Request.create_task(Taskinfo['task_type_id'], Taskinfo['savepath'])
                                    Taskinfo['task_id'] = task_id
                                elif plan['camera'] == "high":
                                    Taskinfo['region_w_high'] = plan['scan_width']
                                    Taskinfo['region_h_high'] = plan['scan_hight']
                                    Taskinfo['FocusMode_high'] = plan['focus_mode']['id']
                                    if plan['focus_mode']['Gap_flag'] == "true":
                                        Taskinfo['fcous_Gap_high'] = plan['focus_mode']['gap']
                                    Taskinfo['scan_label'] = plan['scan_label']
                                    # 获取任务id
                                    task_id = self.Request.create_task(Taskinfo['task_type_id'], Taskinfo['savepath'])
                                    Taskinfo['task_id'] = task_id
                        elif Taskinfo['sys'] == "single":
                            # 单镜头扫描
                            Taskinfo['scanmode'] = False
                            Taskinfo['FocusMode'] = plan['focus_mode']['id']
                            Taskinfo['region_w'] = plan['scan_width']
                            Taskinfo['region_h'] = plan['scan_hight']
                            if plan['focus_mode']['Gap_flag'] == "true":
                                Taskinfo['fcous_Gap'] = plan['focus_mode']['gap']
                            Taskinfo['scan_label'] = plan['scan_label']
                            task_id = self.Request.create_task(Taskinfo['task_type_id'], Taskinfo['savepath'])
                            Taskinfo['task_id'] = task_id
            self.scan(Taskinfo)
        except Exception as e:
            print(f"Error processing task: {e}")

    def scan(self, Taskinfo):
        # 关闭之前开启的实时
        if self.camera_index != -1:
            if self.camera_index == 0:
                self.close_cameraonly()
            elif self.camera_index == 1:
                self.close_camera_low()
            elif self.camera_index == 2:
                self.close_camera_high()
        if self.led_index != -1:
            if self.led_index == 0:
                self.close_led_only()
            elif self.led_index == 1:
                self.close_led_low()
            elif self.led_index == 2:
                self.close_led_high()

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

        # 创建一个线程，用于执行任务
        # self.task.run(self.RUN)
        self.thread_Task = threading.Thread(target=self.task.run, args=(Taskinfo,))
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
        # 调用任务对象的pause方法，实际暂停任务执行
        self.task.pause()
        reply = QMessageBox.warning(self, "暂停！", "是否继续扫描？",
                                    QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
        if reply == QMessageBox.StandardButton.Ok:
            self.Scanning.flag = True
            self.Scanning.flage_run = True
            self.task.task_flag = True
            self.task.task_run_flag = True
            self.Updata_textEdit_log.emit('取消暂停继续扫描')
        else:
            self.Scanning.flag = True
            self.Scanning.flage_run = False
            self.task.task_flag = True
            self.task.task_run_flag = False
            self.Updata_textEdit_log.emit('停止扫描')
            # 执行移动操作
            self.show_msg_box("正在停止扫描和放回玻片，请耐心稍等")

    def save_setup(self):
        """
        保存配置信息。

        该方法从用户界面获取各种配置参数，并将它们存储在self.config_info字典中。
        配置信息包括任务设置、图像保存设置、设备设置、显微镜设置和相机设置。
        最后，调用config.save_config_info方法保存配置信息。
        """
        try:
            # 任务分配参数
            box_1, box_2, box_3, box_4 = self.get_box()
            self.config_info['Task']['box_1'] = box_1
            self.config_info['Task']['box_2'] = box_2
            self.config_info['Task']['box_3'] = box_3
            self.config_info['Task']['box_4'] = box_4
            self.config_info['Task']['slidenumber'] = widgets.spinBox_slide_number.value()
            # 保存图像保存设置
            # 图像参数
            self.config_info['ImageSaver']['maxworkers'] = int(widgets.spinBox_maxworkers.value())
            self.config_info['ImageSaver']['imagestitchsize'] = int(widgets.spinBox_imagestitchsize.value())
            self.config_info['ImageSaver']['queuenumber'] = int(widgets.spinBox_queuenumber.value())
            self.config_info['ImageSaver']['pixelformat'] = str(widgets.comboBox_pixelformat.currentText())
            self.config_info['ImageSaver']['imagequailty'] = int(widgets.spinBox_imagequailty.value())
            self.config_info['ImageSaver']['savepath'] = str(widgets.label_savepath.text())

            # 保存设备设置
            # 设备参数
            self.config_info['Device']['cameranumber'] = int(widgets.spinBox_cameranumber.value())
            self.config_info['Device']['loaderflage'] = widgets.checkBox_loaderflage.isChecked()
            self.config_info['Device']['microscope'] = widgets.checkBox_microscopeflage.isChecked()

            # 保存显微镜设置
            # 显微镜参数
            self.config_info['Microscope']['sys'] = json.loads(widgets.plainTextEdit_micro_sys.toPlainText())
            self.config_info['Microscope']['single'] = json.loads(widgets.plainTextEdit_micro_single.toPlainText())
            self.config_info['Microscope']['low'] = json.loads(widgets.plainTextEdit_micro_low.toPlainText())
            self.config_info['Microscope']['high'] = json.loads(widgets.plainTextEdit_micro_high.toPlainText())
            # 相机参数
            self.config_info['Camera']['single'] = json.loads(widgets.plainTextEdit_camera_single.toPlainText())
            self.config_info['Camera']['low'] = json.loads(widgets.plainTextEdit_camera_low.toPlainText())
            self.config_info['Camera']['high'] = json.loads(widgets.plainTextEdit_camera_high.toPlainText())
            # 装载器
            self.config_info['Loader'] = json.loads(widgets.plainTextEdit_loader.toPlainText())
            # 网络通信
            self.config_info['Network']['flag'] = widgets.checkBox_IP.isChecked()
            if widgets.lineEdit_IP.text():
                self.config_info['Network']['localip'] = str(widgets.lineEdit_IP.text())
            if widgets.lineEdit_port.text():
                self.config_info['Network']['localport'] = int(widgets.lineEdit_port.text())
            # 创建消息框
            reply = QMessageBox.warning(None, "保存当前参数", "确认保存当前参数？",
                                        QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)

            # 根据用户的选择进行处理
            if reply == QMessageBox.StandardButton.Ok:
                # 保存配置信息到文件
                self.config.save_config_info(self.config_info)
                self.Updata_textEdit_log.emit('保存设置成功')
                if self.ActionLoader is None:
                    pass
                else:
                    self.ActionLoader.config = self.config_info
                # 服务器
                if self.config_info['Network']['flag']:
                    self.Server.Com2scope.device_info = self.config_info
                    if self.config_info['Microscope']['sys']['当前系统'] == 'single':
                        self.Server.Com2scope.led_camera.append(
                            self.Device.configurationManager.configurations[0].camera_sn)
                    elif self.config_info['Microscope']['sys']['当前系统'] == 'double':
                        self.Server.Com2scope.led_camera.append(
                            self.Device.configurationManager.configurations[0].camera_sn)
                        self.Server.Com2scope.led_camera.append(
                            self.Device.configurationManager.configurations[1].camera_sn)

            elif reply == QMessageBox.StandardButton.Cancel:
                self.Updata_textEdit_log.emit('取消保存')
        except Exception as e:
            QMessageBox.warning(None, "保存参数失败", str(e), QMessageBox.Ok)

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
                self.ActionMicroscope.microscope_move_x_to(widgets.doubleSpinBox_test_micro_movex2.value())
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
                self.ActionMicroscope.microscope_move_y_to(widgets.doubleSpinBox_test_micro_movey2.value())
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
                self.ActionMicroscope.microscope_move_z_to(widgets.doubleSpinBox_test_micro_movez2.value())
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
                self.ActionLoader.move_x_to(widgets.doubleSpinBox_test_loader_movex2.value())
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
                self.ActionLoader.move_y_to(widgets.doubleSpinBox_test_loader_movey2.value())
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
                self.ActionLoader.move_z_to(widgets.doubleSpinBox_test_loader_movez2.value())
        except Exception as e:
            # 捕获并打印在移动过程中可能发生的任何异常
            print(e)

    def open_cameraonly(self):
        camera.global_signals.image_updated.connect(self.upimage_live)
        self.Device.Create_liveController(0)
        self.Device.liveController._set_trigger_fps(25)
        self.Device.liveController.start_live()
        self.camera_index = 0

    def close_cameraonly(self):
        camera.global_signals.image_updated.disconnect(self.upimage_live)
        self.Device.liveController.stop_live()
        self.Device.camera.disable_callback()
        self.camera_index = -1

    def open_camera_low(self):
        camera.global_signals.image_updated.connect(self.upimage_live)
        self.Device.Create_liveController(1)
        self.Device.liveController._set_trigger_fps(25)
        self.Device.liveController.start_live()
        self.camera_index = 1

    def close_camera_low(self):
        camera.global_signals.image_updated.disconnect(self.upimage_live)
        self.Device.liveController.stop_live()
        self.Device.camera1.disable_callback()
        self.camera_index = -1

    def open_camera_high(self):
        camera.global_signals.image_updated.connect(self.upimage_live)
        self.Device.Create_liveController(2)
        self.Device.liveController._set_trigger_fps(25)
        self.Device.liveController.start_live()
        self.camera_index = 2

    def close_camera_high(self):
        camera.global_signals.image_updated.disconnect(self.upimage_live)
        self.Device.liveController.stop_live()
        self.Device.camera2.disable_callback()
        self.camera_index = -1

    def open_led_only(self):
        self.Device.microcontroller.turn_on_illumination()
        self.led_index = 0

    def close_led_only(self):
        self.Device.microcontroller.turn_off_illumination()
        self.led_index = -1

    def open_led_low(self):
        self.Device.set_low_led()
        self.Device.microcontroller.turn_on_illumination()
        self.led_index = 1

    def close_led_low(self):
        self.Device.microcontroller.turn_off_illumination()
        self.led_index = -1

    def open_led_high(self):
        self.Device.set_high_led()
        self.Device.microcontroller.turn_on_illumination()
        self.led_index = 2

    def close_led_high(self):
        self.Device.microcontroller.turn_off_illumination()
        self.led_index = -1

    def sliderValueChanged_led(self):
        if self.led_index >= 0:
            value = widgets.horizontalSlider_led_intensity.value()
            self.Device.microcontroller.turn_off_illumination()
            self.Device.up_led_intensity(self.led_index, value)
            self.Device.microcontroller.turn_on_illumination()

    def sliderValueChanged_camera(self):
        value = widgets.horizontalSlider_exposure.value()
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
                        self.config_info['Microscope']['single']['单镜头扫描中心xy']['x'] = float(
                            widgets.label_SETX.text())
                        self.config_info['Microscope']['single']['单镜头扫描中心xy']['y'] = float(
                            widgets.label_SETY.text())
                        self.config_info['Microscope']['single'][
                            '对焦经验值单镜头'] = float(widgets.label_SETZ.text()) / 1000 - 0.04
                    elif self.camera_index == 1:
                        self.config_info['Microscope']['low']['低倍扫描中心xy']['x'] = float(widgets.label_SETX.text())
                        self.config_info['Microscope']['low']['低倍扫描中心xy']['y'] = float(widgets.label_SETY.text())
                        self.config_info['Microscope']['low']['对焦经验值低倍'] = float(
                            widgets.label_SETZ.text()) / 1000 - 0.04
                    elif self.camera_index == 2:
                        self.config_info['Microscope']['high']['高倍扫描中心xy']['x'] = float(widgets.label_SETX.text())
                        self.config_info['Microscope']['high']['高倍扫描中心xy']['y'] = float(widgets.label_SETY.text())
                        self.config_info['Microscope']['high']['对焦经验值高倍'] = float(
                            widgets.label_SETZ.text()) / 1000 - 0.04
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
                if self.camera_index == 0:
                    self.Device.configurationManager.update_configuration_without_writing(1, 'ExposureTime',
                                                                                          float(
                                                                                              widgets.horizontalSlider_exposure.value() / 1000))
                    self.Device.configurationManager.update_configuration_without_writing(1, 'IlluminationIntensity',
                                                                                          widgets.horizontalSlider_led_intensity.value())
                elif self.camera_index == 1:
                    self.Device.configurationManager.update_configuration_without_writing(1, 'ExposureTime',
                                                                                          float(
                                                                                              widgets.horizontalSlider_exposure.value() / 1000))
                    self.Device.configurationManager.update_configuration_without_writing(1, 'IlluminationIntensity',
                                                                                          widgets.horizontalSlider_led_intensity.value())
                elif self.camera_index == 2:
                    self.Device.configurationManager.update_configuration_without_writing(2, 'ExposureTime',
                                                                                          float(
                                                                                              widgets.horizontalSlider_exposure.value() / 1000))
                    self.Device.configurationManager.update_configuration_without_writing(2, 'IlluminationIntensity',
                                                                                          widgets.horizontalSlider_led_intensity.value())
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
            widgets.label_savepath.setText(folder_path)
            self.config_info['ImageSaver']['savepath'] = folder_path
        else:
            QMessageBox.warning(self, "提示", "未选择文件夹！")

    def get_request_res(self):
        status, data = self.Request.request2local_get_info('/roboscope_info')

        self.updata_internet_info.emit(str(status))
        self.updata_internet_info.emit(str(data))

    def refresh_plan(self):
        status, data = self.Request.get_plan_from_server(self.config_info['Device']['sn'])
        widgets.comboBox_Task.clear()
        self.plan = data
        for plan in data:
            widgets.comboBox_Task.addItem(plan['name'])
        self.Updata_textEdit_log.emit("刷新任务方案发送请求状态:" + str(status))
        self.Updata_textEdit_log.emit("刷新任务方案接口返回数据:" + str(data))

    def show_msg_box(self, msg):
        # 创建并显示消息框，使用 widgets 作为父窗口
        self.msg_box = QMessageBox(self)
        self.msg_box.setWindowTitle("警告！")
        self.msg_box.setText(msg)
        self.msg_box.setStandardButtons(QMessageBox.Cancel)
        self.msg_box.setModal(True)  # 设置为模态窗口
        self.msg_box.show()  # 显示消息框

    def close_msg_box(self):
        if self.msg_box:
            self.msg_box.close()

    def test_get_slide_(self):
        try:
            # 先复位
            self.ActionMicroscope.microscope_homezxy()
            self.ActionLoader.loader_reset()
            # 获取玻片位置
            slide_tasks, slide__points = self.ActionLoader.get_box_points(1)
            # 移动取片
            # 移动到盒子取玻片处
            self.ActionLoader.move_x_to(slide__points[0][0])
            self.ActionLoader.move_z_to(slide__points[0][1])
            # 取片(动作为y伸出、z上台、y回收)
            self.ActionLoader.get_slide_from_box(slide__points[0][1])
            # 显微镜移动至接片处等待
            self.ActionMicroscope.move_2_loader_get_wait(float(self.config_info['Microscope']['sys']['xend']),
                                                         float(self.config_info['Microscope']['sys']['yend']))
            # 装载器移动
            self.ActionLoader.move_2_microscope_give_location()
            # 确认完成动作
            self.ActionMicroscope.wait_busy()
            # 放片到载物台
            self.ActionLoader.give_slide_to_microscope()
            if self.ActionLoader.loader.is_warning:
                return
            # 避位
            self.ActionLoader.loader_avoid()
            # 失能
            self.ActionLoader.disenble_motor()
        finally:
            self.finished_test.emit()  # 任务完成后关闭消息框

    def test_get_slide(self):
        # 执行移动操作
        self.show_msg_box("正在从玻片仓取片放入载物台，请耐心稍等")
        # 启动线程
        thread = threading.Thread(target=self.test_get_slide_)
        thread.start()

    def test_put_slide_(self):
        try:
            self.ActionMicroscope.microscope_home_z()
            # 显微镜移动至交接处
            self.ActionMicroscope.move_2_loader_give(float(self.config_info['Microscope']['sys']['xend']),
                                                     float(self.config_info['Microscope']['sys']['yend']))
            # 移动至显微镜处下方
            self.ActionLoader.move_2_microscope_get_location()
            # 取片
            self.ActionLoader.get_slide_from_microscope()
            if self.ActionLoader.loader.is_warning:
                return
            # 显微镜复位
            self.ActionMicroscope.microscope_homezxy_wait()
            # 获取玻片位置
            slide_tasks, slide__points = self.ActionLoader.get_box_points(1)
            # 返回玻片仓位置放片
            self.ActionLoader.move_x_to(slide__points[0][0])
            self.ActionLoader.move_z_to(slide__points[0][1] - self.ActionLoader.boxzgap)
            # 放片
            self.ActionLoader.give_slide_to_box(slide__points[0][1] - self.ActionLoader.boxzgap)
            if self.ActionLoader.loader.is_warning:
                return
            self.ActionMicroscope.wait_busy()
        finally:
            self.finished_test.emit()  # 任务完成后关闭消息框

    def test_put_slide(self):
        # 执行移动操作
        self.show_msg_box("正在从载物台取片放入玻片仓，请耐心稍等")
        # 启动线程
        thread = threading.Thread(target=self.test_put_slide_)
        thread.start()

    def test_move_2_singleview_center(self):
        self.ActionMicroscope.microscope_move_y_to(
            float(self.config_info['Microscope']['single']['单镜头扫描中心xy']['y']))
        self.ActionMicroscope.microscope_move_x_to(
            float(self.config_info['Microscope']['single']['单镜头扫描中心xy']['x']))

    def test_move_2_lowview_center(self):
        # 创建并显示消息框，使用 self 作为父窗口
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("提示")
        msg_box.setText("正在执行，请稍候...")
        # msg_box.setStandardButtons(QMessageBox.NoButton)  # 不显示按钮
        msg_box.setModal(True)  # 设置为模态窗口
        msg_box.show()  # 显示消息框
        # 执行移动操作
        try:
            # 移动显微镜到指定位置
            self.ActionMicroscope.microscope_move_y_to(
                float(self.config_info['Microscope']['low']['低倍扫描中心xy']['y']))
            self.ActionMicroscope.microscope_move_x_to(
                float(self.config_info['Microscope']['low']['低倍扫描中心xy']['x']))
        finally:
            msg_box.close()  # 任务完成后关闭消息框

    def test_move_2_highview_center(self):
        self.ActionMicroscope.microscope_move_y_to(
            float(self.config_info['Microscope']['high']['高倍扫描中心xy']['y']))
        self.ActionMicroscope.microscope_move_x_to(
            float(self.config_info['Microscope']['high']['高倍扫描中心xy']['x']))

    @Slot()
    def loader_error(self):
        reply = QMessageBox.information(self, "警告！", "装载器报错，is_warning值改变为True,请检查",
                                        QMessageBox.StandardButton.Ok)

    # 更新xyz坐标
    @Slot(float, float, float)
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
        widgets.label_SETX.setNum(xpos)
        widgets.label_SETY.setNum(ypos)
        widgets.label_SETZ.setNum(zpos)

    # 更新拼图显示
    @Slot(int, list, np.ndarray)
    def upimage_puzzle(self, a, Point_XY, img):
        """
        Update the image in the graphics view of the GUI.

        This function is used to display a processed image in the graphics view, and can adjust the alignment and clear the scene
        according to the input parameters. It supports both grayscale and RGB images.

        Parameters:
        a: An integer flag, used to determine whether to reset the alignment and clear the scene.
        Point_XY: A list containing two integers, representing the coordinates where the image is to be located in the scene.
        img: A np array representing the image data.
        """
        # Show the graphics view
        # widgets.graphicsView.show()
        # Determine the image channel and set the corresponding QImage format
        channel = len(img.shape)
        format_ = QImage.Format_Grayscale8 if channel == 2 else QImage.Format_RGB888
        # Convert the OpenCV image to QImage
        q_img = create_qimage_from_cvimg(img, format_)
        # If a is 1, reset the alignment of the graphics view and clear the scene
        if a == 1:
            widgets.graphicsView.setAlignment(Qt.AlignLeft | Qt.AlignTop)
            self.scene_puzzle.clear()
        # Scale the pixmap to the specified size
        """Add a scaled pixmap to the scene at a specific position."""
        scaled_pixmap = QPixmap.fromImage(q_img).scaled(
            int(self.used_width),
            int(self.used_height)
        )
        # Create a pixmap item and set its position
        pixmap_item = QGraphicsPixmapItem(scaled_pixmap)
        pixmap_item.setPos(Point_XY[1] * int(self.used_width),
                           Point_XY[0] * int(self.used_height))
        # Center the graphics view on the pixmap
        widgets.graphicsView.centerOn(Point_XY[1] * int(self.used_width) + int(self.used_width / 2),
                                      Point_XY[0] * int(self.used_height) + int(self.used_height / 2))
        # Add the pixmap item to the scene
        self.scene_puzzle.addItem(pixmap_item)

    # 更新对焦图像
    @Slot(np.ndarray)
    def upimage_fcous(self, img):
        """
        显示图像焦点区域。

        此方法用于在graphicsView_fcous中显示传入的图像。它首先清除之前的显示内容，
        然后根据图像的通道数决定QImage的格式，将OpenCV格式的图像转换为QImage，
        并在场景中添加一个QGraphicsPixmapItem来显示图像。最后，调整视图以适应图像
        的大小并居中显示。

        :param img: 要显示的图像，一个np.ndarray对象。
        """
        if img is None:
            return
        # 清除场景中的现有物品，为新图像做准备
        self.scene_focus.clear()

        # 根据图像通道数决定QImage的格式
        channel = len(img.shape)
        format_ = QImage.Format_Grayscale8 if channel == 2 else QImage.Format_RGB888

        # 将OpenCV格式的图像转换为QImage
        q_img = create_qimage_from_cvimg(img, format_)
        # 从QImage创建QPixmap
        pixmap = QPixmap.fromImage(q_img)
        # 创建QGraphicsPixmapItem以在场景中显示图像
        pixmap_item = QGraphicsPixmapItem(pixmap)
        # 将图像项添加到场景中
        self.scene_focus.addItem(pixmap_item)
        # 调整视图以适应图像的大小，并保持宽高比
        widgets.graphicsView_fcous.fitInView(pixmap_item, Qt.KeepAspectRatio)
        # 将视图的对齐方式设置为居中
        widgets.graphicsView_fcous.setAlignment(Qt.AlignCenter)

    # 更新实时图像
    @Slot(np.ndarray)
    def upimage_live(self, img):
        """
        显示图像焦点区域。

        此方法用于在graphicsView_fcous中显示传入的图像。它首先清除之前的显示内容，
        然后根据图像的通道数决定QImage的格式，将OpenCV格式的图像转换为QImage，
        并在场景中添加一个QGraphicsPixmapItem来显示图像。最后，调整视图以适应图像
        的大小并居中显示。

        :param img: 要显示的图像，一个np.ndarray对象。
        """
        if img is None:
            return
        self.save_pic = img
        # 清除场景中的现有物品，为新图像做准备
        self.scene_live.clear()

        # 根据图像通道数决定QImage的格式
        channel = len(img.shape)
        format_ = QImage.Format_Grayscale8 if channel == 2 else QImage.Format_RGB888

        # 将OpenCV格式的图像转换为QImage
        q_img = create_qimage_from_cvimg(img, format_)
        # 从QImage创建QPixmap
        pixmap = QPixmap.fromImage(q_img)
        # 创建QGraphicsPixmapItem以在场景中显示图像
        pixmap_item = QGraphicsPixmapItem(pixmap)
        # 将图像项添加到场景中
        self.scene_live.addItem(pixmap_item)

    # 清空示意图坐标
    @Slot()
    def clear_points(self):
        """
        清空当前所有点的数据，用于重置或开始新的绘图。

        该方法通过调用create_empty_pixmap方法来实现清空操作，
        目的是为了在图形界面中清除之前的点数据，为新的绘图操作做准备。
        """
        self.create_empty_pixmap()

    # 创建空的图像
    def create_empty_pixmap(self):
        """
        创建一个空的 pixmap 对象，并将其设置为 ui 中 label_slide 的内容。
        如果 label_slide 当前已经有 pixmap，就使用现有的 pixmap；
        否则，根据 label_slide 的大小创建一个新的 pixmap。
        """
        # 根据 label_slide 是否已有 pixmap 来决定是获取现有 pixmap 还是创建新 pixmap
        pixmap = widgets.label_slide.pixmap() if widgets.label_slide.pixmap() else QPixmap(widgets.label_slide.size())
        # 设置 pixmap 的背景颜色为灰色
        color = QColor(186, 186, 186)
        pixmap.fill(color)
        # 将处理后的 pixmap 设置给 label_slide
        widgets.label_slide.setPixmap(pixmap)

    # 更新示意图点位
    @Slot(list)
    def update_points(self, point_real):
        """
        更新标注点的位置。

        根据区域宽度的不同，调整点的位置并更新显示。此函数用于在图形用户界面中，
        根据用户的选择，动态修改图像上标注点的位置。

        参数:
        point: 包含x和y坐标的列表，表示标注点的当前位置。
        region_width: int，表示当前区域的宽度，用于确定点的绘制位置。
        """
        # 获取当前标签控件中的像素映射对象，用于后续在上面绘制点
        pixmap = widgets.label_slide.pixmap()
        # 创建一个画家对象，用于在pixmap上绘制
        painter = QPainter(pixmap)
        # 开启抗锯齿渲染，以获得更平滑的绘制效果
        painter.setRenderHint(QPainter.Antialiasing)
        # 设置绘制笔的颜色和宽度
        pen = QPen(Qt.red)
        pen.setWidth(2)
        painter.setPen(pen)
        # 定义一个比例因子，用于根据区域宽度调整点的位置
        # 根据区域宽度的不同，计算并绘制点的位置
        y = int((44.8 - point_real[0]) / 0.32)
        x = int((61 - point_real[1]) / 0.32)
        painter.drawPoint(QPoint(x, y))
        # 绘制操作完成，结束画家对象
        painter.end()
        # 更新标签控件的像素映射，显示绘制后的结果
        widgets.label_slide.setPixmap(pixmap)
        # 强制标签控件更新，确保绘制的点能够显示出来
        widgets.label_slide.update()

    # 激活按钮
    @Slot()
    def activate(self):
        """
        启用相关按钮，以允许用户进行操作。

        此方法通过启用运行、微重置和加载器重置按钮，为用户提供执行不同操作的权限。
        这通常在程序进入特定状态或满足特定条件时被调用。
        """
        # 启用运行按钮，允许用户触发相关运行操作
        widgets.pushButton_run.setEnabled(True)
        # 启用微重置按钮，允许用户进行轻微的系统重置操作
        widgets.pushButton_micro_reset.setEnabled(True)
        # 启用加载器重置按钮，允许用户重置加载器至初始状态
        widgets.pushButton_loader_reset.setEnabled(True)
        widgets.pushButton_pause.setEnabled(True)

        if self.config_info['Device']['cameranumber'] == 1:
            widgets.pushButton_open_cameraonly.setEnabled(True)
            widgets.pushButton_close_cameraonly.setEnabled(True)
            widgets.pushButton_open_led_only.setEnabled(True)
            widgets.pushButton_close_led_only.setEnabled(True)
        elif self.config_info['Device']['cameranumber'] == 2:
            widgets.pushButton_open_camera_low.setEnabled(True)
            widgets.pushButton_close_camera_low.setEnabled(True)
            widgets.pushButton_close_camera_high.setEnabled(True)
            widgets.pushButton_open_camera_high.setEnabled(True)
            widgets.pushButton_open_led_low.setEnabled(True)
            widgets.pushButton_close_led_low.setEnabled(True)
            widgets.pushButton_open_led_high.setEnabled(True)
            widgets.pushButton_close_led_high.setEnabled(True)

        widgets.pushButton_test_micro_movex2.setEnabled(True)
        widgets.pushButton_test_micro_movey2.setEnabled(True)
        widgets.pushButton_test_micro_movez2.setEnabled(True)
        widgets.pushButton_test_loader_movex2.setEnabled(True)
        widgets.pushButton_test_loader_movey2.setEnabled(True)
        widgets.pushButton_test_loader_movez2.setEnabled(True)

        widgets.pushButton_save_scan.setEnabled(True)
        widgets.pushButton_save_exposure.setEnabled(True)
        widgets.pushButton_test_get_slide.setEnabled(True)
        widgets.pushButton_test_put_slide.setEnabled(True)
        widgets.pushButton_test_move_2_singleview_center.setEnabled(True)
        widgets.pushButton_test_move_2_lowview_center.setEnabled(True)
        widgets.pushButton_test_move_2_highview_center.setEnabled(True)

    @Slot()
    def test_single_step_pause(self):
        reply = QMessageBox.warning(self, "暂停！", "是否继续扫描？",
                                    QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
        if reply == QMessageBox.StandardButton.Ok:
            self.task.test_single_step_pause_flag = True
            self.task.test_single_step_run_flag = True
            self.Updata_textEdit_log.emit('取消暂停继续扫描')
        else:
            self.task.test_single_step_pause_flag = True
            self.task.test_single_step_run_flag = False
            self.Updata_textEdit_log.emit('停止扫描')

    # 更新log日志
    @Slot(str)
    def updata_log(self, log):
        """
        更新日志文本框的内容。

        通过此方法将日志文本追加到用户界面的日志文本框中，以便用户可以实时查看程序运行的日志信息。

        :param log: 需要添加到日志文本框的字符串信息
        """
        widgets.textEdit_log.appendPlainText(log)

    # 更新网络通信信息
    @Slot(str)
    def updata_internet(self, log):
        """
        更新日志文本框的内容。

        通过此方法将日志文本追加到用户界面的日志文本框中，以便用户可以实时查看程序运行的日志信息。

        :param log: 需要添加到日志文本框的字符串信息
        """
        widgets.plainTextEdit_internetinfo.appendPlainText(log)

    @Slot(int, str)
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

    # 更新参数
    @Slot()
    def Up_parameter(self):
        """
        根据配置信息更新界面参数。

        从config_info中读取各种参数设置，并更新到用户界面的相应控件中。
        这包括任务参数、图像保存参数、设备参数、显微镜参数和相机参数。
        """
        try:
            # 更新任务参数
            # 任务分配参数
            if self.config_info['Task']['box_1']:
                widgets.checkBox_1.setChecked(True)
            if self.config_info['Task']['box_2']:
                widgets.checkBox_2.setChecked(True)
            if self.config_info['Task']['box_3']:
                widgets.checkBox_3.setChecked(True)
            if self.config_info['Task']['box_4']:
                widgets.checkBox_4.setChecked(True)
            # 更新滑块数目
            widgets.spinBox_slide_number.setValue(int(self.config_info['Task']['slidenumber']))
            widgets.spinBox_cameranumber.setValue(int(self.config_info['Device']['cameranumber']))
            # 更新图像保存参数
            widgets.spinBox_maxworkers.setValue(int(self.config_info['ImageSaver']['maxworkers']))
            widgets.spinBox_imagestitchsize.setValue(int(self.config_info['ImageSaver']['imagestitchsize']))
            widgets.spinBox_queuenumber.setValue(int(self.config_info['ImageSaver']['queuenumber']))
            widgets.comboBox_pixelformat.setCurrentText(self.config_info['ImageSaver']['pixelformat'])
            widgets.spinBox_imagequailty.setValue(int(self.config_info['ImageSaver']['imagequailty']))
            widgets.label_savepath.setText(self.config_info['ImageSaver']['savepath'])
            if self.config_info['Device']['loaderflage']:
                widgets.checkBox_loaderflage.setChecked(True)
            if self.config_info['Device']['microscope']:
                widgets.checkBox_microscopeflage.setChecked(True)
            if self.config_info['Network']['flag']:
                widgets.checkBox_IP.setChecked(True)

            # 更新设备参数
            # 显微镜
            json_str = json.dumps(self.config_info['Microscope']['sys'], ensure_ascii=False, indent=4)
            widgets.plainTextEdit_micro_sys.setPlainText(json_str)
            json_str = json.dumps(self.config_info['Microscope']['single'], ensure_ascii=False, indent=4)
            widgets.plainTextEdit_micro_single.setPlainText(json_str)
            json_str = json.dumps(self.config_info['Microscope']['low'], ensure_ascii=False, indent=4)
            widgets.plainTextEdit_micro_low.setPlainText(json_str)
            json_str = json.dumps(self.config_info['Microscope']['high'], ensure_ascii=False, indent=4)
            widgets.plainTextEdit_micro_high.setPlainText(json_str)
            # 相机参数
            json_str = json.dumps(self.config_info['Camera']['single'], ensure_ascii=False, indent=4)
            widgets.plainTextEdit_camera_single.setPlainText(json_str)
            json_str = json.dumps(self.config_info['Camera']['low'], ensure_ascii=False, indent=4)
            widgets.plainTextEdit_camera_low.setPlainText(json_str)
            json_str = json.dumps(self.config_info['Camera']['high'], ensure_ascii=False, indent=4)
            widgets.plainTextEdit_camera_high.setPlainText(json_str)
            # 装载器参数
            json_str = json.dumps(self.config_info['Loader'], ensure_ascii=False, indent=4)
            widgets.plainTextEdit_loader.setPlainText(json_str)

            widgets.label_IP.setText(self.config_info['Network']['localip'])
            widgets.label_post.setText(str(self.config_info['Network']['localport']))

        except Exception as e:
            print(e)

    # 更新进度条
    @Slot(float, float, float)
    def up_progress(self, vlaue, time, count_slide):
        """
        更新进度条的值。

        通过此方法设置进度条的显示进度。使用了Qt的Slot装饰器，使得此方法可以作为信号连接，
        以便于在GUI界面中动态更新进度条的进度。

        参数:
        vlaue (float): 进度条的新值。此值将被设置为进度条的当前进度。
        """
        if time > 0:
            widgets.progressBar.setValue(vlaue)
            number = (1 - (vlaue / 100)) * count_slide
            self.remaining_time = time * number
            if self.timer.isActive():
                print("状态")
                print(self.timer.isActive())
            else:
                self.timer.start(1000)
        elif time < 0:
            self.timer.stop()

    def update_time(self):
        hours = int(self.remaining_time // 3600)
        minutes = int((self.remaining_time % 3600) // 60)
        seconds = int(self.remaining_time % 60)

        widgets.lcdNumber_hour.display(hours)
        widgets.lcdNumber_min.display(minutes)
        widgets.lcdNumber_second.display(seconds)

        # 如果需要倒计时，可以减少剩余时间
        if self.remaining_time > 0:
            self.remaining_time -= 1
        else:
            self.timer.stop()  # 停止计时器

    # 执行预扫描槽函数
    @Slot(dict)
    def pre_scan_pic(self, json_data):
        # 解析 JSON 字符串
        # 禁用运行按钮，启用暂停按钮，以准备开始任务
        widgets.pushButton_run.setEnabled(False)
        widgets.pushButton_pause.setEnabled(True)
        widgets.pushButton_micro_reset.setEnabled(False)
        widgets.pushButton_loader_reset.setEnabled(False)
        self.scan(json_data)
        self.Updata_textEdit_log.emit("接收请求，开始预扫描玻片")

    @Slot(list)
    def updata_points_high(self, points, low_for_high_Scan_Mode):
        self.Scanning.points_xy_real_high = points
        self.Scanning.low_2_high_method = low_for_high_Scan_Mode
        self.Scanning.request_flag = False

    def closeEvent(self, event):
        # 在窗口关闭事件中触发的函数
        self.close_thing()
        event.accept()

    def close_thing(self):
        if self.Server is not None:
            self.Server.stop()

        # 执行需要在应用程序退出时触发的操作
        if self.Device is None:
            pass
        else:
            self.Device.close_device()
        if self.ActionLoader is not None:
            self.ActionLoader.release_camera()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./UI/images/images/kemoshen.ico"))
    window = MainWindow()
    sys.exit(app.exec())
