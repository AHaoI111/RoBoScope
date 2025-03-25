# -*- encoding: utf-8 -*-
"""
@Description:
用于控制显微镜的封装类
@File    :   action_loader.py
@Time    :   2025/03/06
@Author  :   Li QingHao
@Version :   2.0
@Time_END :  最后修改时间：
@Developers_END :  最后修改作者：
"""
import time


class ActionMicroscope:

    def __init__(self, Device):
        super().__init__()

        self.Device = Device

    def microscope_homezxy(self):
        self.Device.navigationController.home_z()
        while self.Device.microcontroller.is_busy():
            time.sleep(0.005)
        self.Device.navigationController.home_x()
        while self.Device.microcontroller.is_busy():
            time.sleep(0.005)
        self.Device.navigationController.home_y()
        while self.Device.microcontroller.is_busy():
            time.sleep(0.005)

    def microscope_homezxy_wait(self):
        self.Device.navigationController.home_z()
        while self.Device.microcontroller.is_busy():
            time.sleep(0.005)
        self.Device.navigationController.home_x()
        self.Device.navigationController.home_y()

    def microscope_home_z(self):
        self.Device.navigationController.home_z()
        while self.Device.microcontroller.is_busy():
            time.sleep(0.005)

    def microscope_move_x_to(self, x):
        self.Device.navigationController.move_x_to(x)
        while self.Device.microcontroller.is_busy():
            time.sleep(0.005)

    def microscope_move_y_to(self, y):
        self.Device.navigationController.move_y_to(y)
        while self.Device.microcontroller.is_busy():
            time.sleep(0.005)

    def microscope_move_z_to(self, z):
        self.Device.navigationController.move_z_to(z)
        while self.Device.microcontroller.is_busy():
            time.sleep(0.005)

    def move_2_loader_get(self, Xend, Yend):
        self.Device.navigationController.move_y_to(Yend)
        # while self.Device.microcontroller.is_busy():
        #     time.sleep(0.005)
        self.Device.navigationController.move_x_to(Xend)
        while self.Device.microcontroller.is_busy():
            time.sleep(0.005)

    def move_2_loader_give(self, Xend, Yend):
        self.Device.navigationController.move_y_to(Yend - 1)
        # while self.Device.microcontroller.is_busy():
        #     time.sleep(0.005)
        self.Device.navigationController.move_x_to(Xend)
        while self.Device.microcontroller.is_busy():
            time.sleep(0.005)

    def move_2_loader_get_wait(self, Xend, Yend):
        self.Device.navigationController.move_y_to(Yend)
        self.Device.navigationController.move_x_to(Xend)

    def wait_busy(self):
        while self.Device.microcontroller.is_busy():
            time.sleep(0.005)

    # 设置0号灯
    def set_low_light(self):
        self.Device.set_low_led()

    # 设置1号灯
    def set_high_light(self):
        self.Device.set_high_led()

    # 打开灯
    def turn_on_light(self):
        self.Device.microcontroller.turn_on_illumination()

    # 关闭灯
    def turn_off_light(self):
        self.Device.microcontroller.turn_off_illumination()

    def set_only_light(self):
        self.Device.set_only_led()

    def get_image_camera_low(self):
        self.Device.camera1.send_trigger()
        image = self.Device.camera1.read_frame()
        return image

    def get_image_camera_high(self):
        self.Device.camera2.send_trigger()
        image = self.Device.camera2.read_frame()
        return image

    def get_image_camera_one(self):
        self.Device.camera.send_trigger()
        image = self.Device.camera.read_frame()
        return image
