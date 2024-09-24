# -*- encoding: utf-8 -*-
"""
@Description:
搜索设备、启动和自检设备
@File    :   Search_device.py
@Time    :   2024/07/16
@Author  :   Li QingHao
@Version :   2.0
@Time_END :  最后修改时间：
@Developers_END :  最后修改作者：
"""
import re
import time

from Drives.microcontroller_V2 import Microcontroller
from Drives.camera import Camera
from Drives.loadercontroller import LoaderController
from Drives._def_V2 import *

import control.core_V2 as core
import Drives.camera


class device:
    def __init__(self, config):
        """
        初始化设备管理器，负责加载和管理设备的配置及状态。

        :param config: 设备的配置信息，用于初始化设备。
        """
        # 初始化配置管理器，用于从XML配置文件中加载设备配置
        # 初始化配置管理器，用于管理设备的配置信息
        self.liveController = None
        self.configurationManager = core.ConfigurationManager('./channel_configurations.xml')
        # 初始化各个设备组件的引用，初始值为None，后续将根据配置加载对应设备
        self.Loader = None
        self.camera2 = None
        self.camera1 = None
        self.camera = None
        self.navigationController = None
        self.microcontroller = None
        # 存储配置信息，用于设备初始化和其他操作
        self.config = config

        # 设备状态标志，用于标记各个设备是否已初始化并可用
        self.flag_microscope = False
        self.flag_camera = False
        self.flag_camera1 = False
        self.flag_camera2 = False
        self.flag_loader = False
        self.flag = True

    def open_device(self):
        """
        初始化设备，包括显微镜、相机和加载器。

        初始化显微镜控制器、马达驱动和相机。根据配置文件中的设置，可能初始化一个或两个相机。
        如果配置了加载器，也会初始化加载器。

        返回:
            tuple: 包含显微镜、相机1、相机2和加载器的初始化状态布尔值。
        """
        """
        初始化显微镜搜索功能。

        该函数尝试初始化显微镜的控制器、马达驱动、相机和加载器等部件。
        如果初始化成功，返回True；如果遇到任何异常，则返回False。

        Returns:
            bool: 初始化状态的标志，True表示初始化成功，False表示初始化失败。
        """
        # 初始化各种设备的状态标志为False
        # 初始化状态标志为False
        self.flag_microscope = False
        self.flag_camera = False
        self.flag_camera1 = False
        self.flag_camera2 = False
        self.flag_loader = False
        self.flag = True

        # 尝试初始化显微镜控制器及相关设备
        try:
            # 初始化显微镜控制器
            self.microcontroller = Microcontroller(COM=self.config['Microscope']['sys']['串口'])
            # 重置显微镜控制器
            self.microcontroller.reset()
            # 初始化马达驱动
            # reinitialize motor drivers and DAC (in particular for V2.1 driver board where PG is not functional)
            self.microcontroller.initialize_drivers()
            # 配置执行器
            # configure the actuators
            self.microcontroller.configure_actuators()
            # 显微镜初始化成功
            self.flag_microscope = True
        except Exception as e:
            # 如果遇到异常，不处理，继续尝试初始化下一个设备
            self.flag = False

        # 尝试初始化相机
        try:
            # 根据配置决定初始化一个还是两个相机
            # 根据配置的相机数量初始化相机
            # 获取相机数量
            if self.config['Device']['cameranumber'] == 1:
                # 单相机配置
                # configuration = self.configurationManager.configurations[0]
                self.camera = Camera(rotate_image_angle=self.config['Camera']['single']['RotateImageAngleonly'])
                # 打开相机
                self.camera.open()
                # 相机1初始化成功
                self.flag_camera = True
            elif self.config['Device']['cameranumber'] == 2:
                # 双相机配置
                configuration1 = self.configurationManager.configurations[0]
                configuration2 = self.configurationManager.configurations[1]
                self.camera1 = Camera(sn=configuration1.camera_sn,
                                      rotate_image_angle=self.config['Camera']['low']['RotateImageAnglelow'])
                self.camera2 = Camera(sn=configuration2.camera_sn,
                                      rotate_image_angle=self.config['Camera']['high']['RotateImageAnglehigh'])
                # 打开相机
                self.camera1.open()
                self.camera2.open()
                # 相机1和相机2初始化成功
                self.flag_camera1 = True
                self.flag_camera2 = True
        except Exception as e:
            # 如果遇到异常，不处理，继续尝试初始化下一个设备
            self.flag = False

        # 尝试初始化加载器
        try:
            # 根据配置决定是否初始化加载器
            # 根据Loader标志决定是否创建Loader对象
            if self.config['Device']['loaderflage']:
                self.Loader = LoaderController(self.config['Loader']['串口'])
                # 加载器初始化成功
                # 设置状态标志为True，表示初始化成功
                self.flag_loader = True

        except Exception as e:
            # 如果遇到异常，不处理
            self.flag = False
        # self.liveController = core.LiveController(self.camera, self.microcontroller, self.configurationManager)
        # 返回所有设备的初始化状态
        return self.flag, self.flag_microscope, self.flag_camera, self.flag_camera1, self.flag_camera2, self.flag_loader

    def detection_device(self):
        """
        初始化检测设备，包括相机和加载器的配置与初始化。

        返回:
            bool: 设备初始化成功与否的标志。
        """
        # 初始化设备就绪标志为False
        """
        检测设备配置并初始化相机和加载器。

        该方法首先初始化导航控制器，然后配置编码器和PID控制。接着，根据配置的相机数量和类型，
        进行相机的初始化和图像区域设置。如果配置了加载器，还会初始化加载器的位置。
        最后，根据设备是否已成功初始化，更新标志位。

        返回:
            bool: 设备检测状态，True表示设备检测完成并初始化成功，False表示检测过程中出现错误。
        """
        try:
            # 初始化设备检测标志为False
            self.flag = False
            # 初始化导航控制器
            self.navigationController = core.NavigationController(self.microcontroller)
            # 将Z轴归零
            # retract the objective
            self.navigationController.home_z()
            # 等待Z轴归零完成
            # wait for the operation to finish
            t0 = time.time()
            while self.microcontroller.is_busy():
                time.sleep(0.005)
                if time.time() - t0 > 8:
                    return self.flag
            # 将X轴归零
            t0 = time.time()
            self.navigationController.home_x()
            # 等待X轴归零完成
            while self.microcontroller.is_busy():
                time.sleep(0.005)
                if time.time() - t0 > 8:
                    return self.flag
            # 将Y轴归零
            t0 = time.time()
            self.navigationController.home_y()
            # 等待Y轴归零完成
            while self.microcontroller.is_busy():
                time.sleep(0.005)
                if time.time() - t0 > 8:
                    return self.flag
            # 根据配置信息，条件性地配置编码器
            if HAS_ENCODER_X == True:
                self.navigationController.set_axis_PID_arguments(0, PID_P_X, PID_I_X, PID_D_X)
                self.navigationController.configure_encoder(0, (SCREW_PITCH_X_MM * 1000) / ENCODER_RESOLUTION_UM_X,
                                                            ENCODER_FLIP_DIR_X)
                self.navigationController.set_pid_control_enable(0, ENABLE_PID_X)
            if HAS_ENCODER_Y == True:
                self.navigationController.set_axis_PID_arguments(1, PID_P_Y, PID_I_Y, PID_D_Y)
                self.navigationController.configure_encoder(1, (SCREW_PITCH_Y_MM * 1000) / ENCODER_RESOLUTION_UM_Y,
                                                            ENCODER_FLIP_DIR_Y)
                self.navigationController.set_pid_control_enable(1, ENABLE_PID_Y)
            if HAS_ENCODER_Z == True:
                self.navigationController.set_axis_PID_arguments(2, PID_P_Z, PID_I_Z, PID_D_Z)
                self.navigationController.configure_encoder(2, (SCREW_PITCH_Z_MM * 1000) / ENCODER_RESOLUTION_UM_Z,
                                                            ENCODER_FLIP_DIR_Z)
                self.navigationController.set_pid_control_enable(2, ENABLE_PID_Z)
            time.sleep(0.5)

            # 设置软件限位
            # set software limit
            self.navigationController.set_x_limit_pos_mm(SOFTWARE_POS_LIMIT.X_POSITIVE)
            self.navigationController.set_x_limit_neg_mm(SOFTWARE_POS_LIMIT.X_NEGATIVE)
            self.navigationController.set_y_limit_pos_mm(SOFTWARE_POS_LIMIT.Y_POSITIVE)
            self.navigationController.set_y_limit_neg_mm(SOFTWARE_POS_LIMIT.Y_NEGATIVE)
            self.navigationController.set_z_limit_pos_mm(SOFTWARE_POS_LIMIT.Z_POSITIVE)

            # 移动检查
            self.navigationController.move_x_to(8)
            while self.microcontroller.is_busy():
                time.sleep(0.005)
            self.navigationController.move_y_to(8)
            while self.microcontroller.is_busy():
                time.sleep(0.005)
            self.navigationController.home_z()
            while self.microcontroller.is_busy():
                time.sleep(0.005)
            self.navigationController.home_xy()
            while self.microcontroller.is_busy():
                time.sleep(0.005)

            # 根据配置的相机数量和编号，初始化相机并设置拍摄区域、曝光时间和增益
            if self.config['Device']['cameranumber'] == 1:
                configuration = self.configurationManager.configurations[0]
                # 根据相机型号配置参数
                # 设置相机参数
                letters_only = re.sub(r'\d+', '', configuration.camera_sn)
                if letters_only == 'FCU':
                    # 自动白平衡
                    if len(self.config['Camera']['single']['wbone']) != 3:
                        self.camera.camera.BalanceWhiteAuto.set(2)
                    else:
                        self.camera.set_wb_ratios(self.config['Camera']['single']['wbone']['R'],
                                                  self.config['Camera']['single']['wbone']['G'],
                                                  self.config['Camera']['single']['wbone']['B'])
                # 设置拍摄区域
                offset_x = (732 // 8) * 8
                offset_y = (238 // 8) * 8
                self.camera.set_ROI(offset_x, offset_y, 2560, 2560)
                # 设置曝光时间和增益
                self.camera.set_exposure_time(configuration.exposure_time)
                self.camera.set_analog_gain(configuration.analog_gain)
                # 启用软件触发拍摄
                self.camera.set_software_triggered_acquisition()
                self.camera.start_streaming()

                self.set_only_led()
                self.microcontroller.turn_on_illumination()
                self.camera.send_trigger()
                # 检查相机是否成功获取图像
                img = self.camera.read_frame()
                self.microcontroller.turn_off_illumination()
                if img is None:
                    return self.flag
            elif self.config['Device']['cameranumber'] == 2:
                configuration1 = self.configurationManager.configurations[0]
                configuration2 = self.configurationManager.configurations[1]

                letters_only = re.sub(r'\d+', '', configuration1.camera_sn)
                if letters_only == 'FCU':
                    # 自动白平衡
                    if len(self.config['Camera']['low']['wblow']) != 3:
                        self.camera1.camera.BalanceWhiteAuto.set(2)
                    else:
                        self.camera1.set_wb_ratios(self.config['Camera']['low']['wblow']['R'],
                                                   self.config['Camera']['low']['wblow']['G'],
                                                   self.config['Camera']['low']['wblow']['B'])
                # 设置拍摄区域
                offset_x = (732 // 8) * 8
                offset_y = (238 // 8) * 8
                self.camera1.set_ROI(offset_x, offset_y, 2560, 2560)
                # 设置曝光时间和增益
                self.camera1.set_exposure_time(configuration1.exposure_time)
                self.camera1.set_analog_gain(configuration1.analog_gain)
                # 启用软件触发拍摄
                self.camera1.set_software_triggered_acquisition()
                self.camera1.start_streaming()

                self.set_low_led()
                # 检查相机是否成功获取图像
                self.microcontroller.turn_on_illumination()
                self.camera1.send_trigger()
                img = self.camera1.read_frame()
                self.microcontroller.turn_off_illumination()
                if img is None:
                    return self.flag

                letters_only = re.sub(r'\d+', '', configuration2.camera_sn)
                if letters_only == 'FCU':
                    if len(self.config['Camera']['high']['wbhigh']) != 3:
                        self.camera2.camera.BalanceWhiteAuto.set(2)
                    else:
                        self.camera2.set_wb_ratios(self.config['Camera']['high']['wbhigh']['R'],
                                                   self.config['Camera']['high']['wbhigh']['G'],
                                                   self.config['Camera']['high']['wbhigh']['B'])

                self.camera2.set_ROI(offset_x, offset_y, 2560, 2560)
                self.camera2.set_exposure_time(configuration2.exposure_time)
                self.camera2.set_analog_gain(configuration2.analog_gain)
                self.camera2.set_software_triggered_acquisition()
                self.camera2.start_streaming()

                self.set_high_led()
                self.microcontroller.turn_on_illumination()
                self.camera2.send_trigger()
                # 检查相机是否成功获取图像
                img = self.camera2.read_frame()
                self.microcontroller.turn_off_illumination()
                if img is None:
                    return self.flag
            # 根据配置，初始化加载器
            if self.config['Device']['loaderflage']:
                self.Loader.reset_xyz()

            # 更新设备检测标志为True，表示设备初始化成功
            self.flag = True
            return self.flag
        except Exception as e:
            return self.flag

    def Create_liveController(self, index):
        if index == 0:
            Drives.camera.global_rotate_image_angle = self.config['Camera']['single']['RotateImageAngleonly']
            self.liveController = core.LiveController(self.camera, self.microcontroller, self.configurationManager)
        elif index == 1:
            Drives.camera.global_rotate_image_angle = self.config['Camera']['low']['RotateImageAnglelow']
            self.set_low_led()
            self.liveController = core.LiveController(self.camera1, self.microcontroller, self.configurationManager)
        elif index == 2:
            Drives.camera.global_rotate_image_angle = self.config['Camera']['high']['RotateImageAnglehigh']
            self.set_high_led()
            self.liveController = core.LiveController(self.camera2, self.microcontroller, self.configurationManager)

    def set_low_led(self):
        self.microcontroller.turn_off_illumination()
        if self.configurationManager.configurations[0].illumination_source < 10:  # LED matrix
            self.microcontroller.set_illumination_led_matrix(
                self.configurationManager.configurations[0].illumination_source,
                r=(self.configurationManager.configurations[0].illumination_intensity / 100) * LED_MATRIX_R_FACTOR,
                g=(self.configurationManager.configurations[0].illumination_intensity / 100) * LED_MATRIX_G_FACTOR,
                b=(self.configurationManager.configurations[0].illumination_intensity / 100) * LED_MATRIX_B_FACTOR)
        else:
            self.microcontroller.set_illumination(self.configurationManager.configurations[0].illumination_source,
                                                  self.configurationManager.configurations[0].illumination_intensity)

    def set_high_led(self):
        self.microcontroller.turn_off_illumination()
        if self.configurationManager.configurations[1].illumination_source < 10:  # LED matrix
            self.microcontroller.set_illumination_led_matrix(
                self.configurationManager.configurations[1].illumination_source,
                r=(self.configurationManager.configurations[1].illumination_intensity / 100) * LED_MATRIX_R_FACTOR,
                g=(self.configurationManager.configurations[1].illumination_intensity / 100) * LED_MATRIX_G_FACTOR,
                b=(self.configurationManager.configurations[1].illumination_intensity / 100) * LED_MATRIX_B_FACTOR)
        else:
            self.microcontroller.set_illumination(self.configurationManager.configurations[1].illumination_source,
                                                  self.configurationManager.configurations[1].illumination_intensity)

    def set_only_led(self):

        self.microcontroller.turn_off_illumination()
        if self.configurationManager.configurations[0].illumination_source < 10:  # LED matrix
            self.microcontroller.set_illumination_led_matrix(
                self.configurationManager.configurations[0].illumination_source,
                r=(self.configurationManager.configurations[0].illumination_intensity / 100) * LED_MATRIX_R_FACTOR,
                g=(self.configurationManager.configurations[0].illumination_intensity / 100) * LED_MATRIX_G_FACTOR,
                b=(self.configurationManager.configurations[0].illumination_intensity / 100) * LED_MATRIX_B_FACTOR)
        else:
            self.microcontroller.set_illumination(self.configurationManager.configurations[0].illumination_source,
                                                  self.configurationManager.configurations[0].illumination_intensity)

    def up_led_intensity(self, index, illumination_intensity):
        self.microcontroller.turn_off_illumination()
        if index == 0:
            self.microcontroller.turn_off_illumination()
            if self.configurationManager.configurations[0].illumination_source < 10:  # LED matrix
                self.microcontroller.set_illumination_led_matrix(
                    self.configurationManager.configurations[0].illumination_source,
                    r=(illumination_intensity / 100) * LED_MATRIX_R_FACTOR,
                    g=(illumination_intensity / 100) * LED_MATRIX_G_FACTOR,
                    b=(illumination_intensity / 100) * LED_MATRIX_B_FACTOR)
            else:
                self.microcontroller.set_illumination(self.configurationManager.configurations[0].illumination_source,
                                                      illumination_intensity)
        elif index == 1:
            self.microcontroller.turn_off_illumination()
            if self.configurationManager.configurations[0].illumination_source < 10:  # LED matrix
                self.microcontroller.set_illumination_led_matrix(
                    self.configurationManager.configurations[0].illumination_source,
                    r=(illumination_intensity / 100) * LED_MATRIX_R_FACTOR,
                    g=(illumination_intensity / 100) * LED_MATRIX_G_FACTOR,
                    b=(illumination_intensity / 100) * LED_MATRIX_B_FACTOR)
            else:
                self.microcontroller.set_illumination(self.configurationManager.configurations[0].illumination_source,
                                                      illumination_intensity)
        elif index == 2:
            self.microcontroller.turn_off_illumination()
            if self.configurationManager.configurations[1].illumination_source < 10:  # LED matrix
                self.microcontroller.set_illumination_led_matrix(
                    self.configurationManager.configurations[1].illumination_source,
                    r=(illumination_intensity / 100) * LED_MATRIX_R_FACTOR,
                    g=(illumination_intensity / 100) * LED_MATRIX_G_FACTOR,
                    b=(illumination_intensity / 100) * LED_MATRIX_B_FACTOR)
            else:
                self.microcontroller.set_illumination(self.configurationManager.configurations[1].illumination_source,
                                                      illumination_intensity)

    def up_camera_exposure(self, index, exposure_time):
        if index == 0:
            self.camera.set_exposure_time(exposure_time / 1000)
        elif index == 1:
            self.camera1.set_exposure_time(exposure_time / 1000)
        elif index == 2:
            self.camera2.set_exposure_time(exposure_time / 1000)

    def close_device(self):
        """
        关闭设备。

        该方法用于安全关闭与设备相关的各种组件。如果设备中使用了显微镜、相机、载物台等组件，
        将分别关闭这些组件。这个方法的存在是为了确保在程序结束或设备需要重置时，所有组件都能
        被正确关闭，以避免资源泄漏或设备损坏。

        注意：
        - 在关闭设备前，如果显微镜已定位，将先缓存当前位置，然后返回原点。
        - 对于每个组件，只有在其标志位为真时才会调用相应的关闭方法。
        """
        # 如果显微镜标志位为真，则关闭显微镜相关设备
        if self.flag_microscope:
            # 缓存当前位置，以便日后可以快速回到这个位置
            self.navigationController.cache_current_position()
            # 将显微镜返回到原点位置
            self.navigationController.home()
            # 禁用轴的PID控制，以防止关闭过程中出现意外运动
            self.navigationController.turnoff_axis_pid_control()
            # 关闭显微镜控制器
            self.microcontroller.close()
        # 如果相机标志位为真，则关闭相机
        if self.flag_camera:
            self.camera.close()
        # 如果第二个相机标志位为真，则关闭双镜头第1个相机
        if self.flag_camera1:
            self.camera1.close()
        # 如果第三个相机标志位为真，则关闭双镜头第2个相机
        if self.flag_camera2:
            self.camera2.close()
        # 如果加载器标志位为真，则关闭加载器
        if self.flag_loader:
            self.Loader.ser_close()
