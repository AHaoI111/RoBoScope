# -*- encoding: utf-8 -*-
"""
@Description:
用于控制装载器的封装类
@File    :   action_loader.py
@Time    :   2024/07/16
@Author  :   Li QingHao
@Version :   2.0
@Time_END :  最后修改时间：
@Developers_END :  最后修改作者：
"""
import os
import time

import cv2

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
from paddleocr import PaddleOCR


class Color(object):
    red = b"\x01"
    green = b"\x10"
    yellow = b"\x11"


class Key(object):
    none = b"\x00"
    pressed = b"\x01"
    released = b"\x02"


class ActionLoader(object):
    def __init__(self, loader_controller, config):
        self.key = Key()
        self.color = Color()
        self.ocr = None
        self.loader = loader_controller
        self.config = config
        # 加载参数
        self.x_start1 = float(self.config['xstart1'])
        self.z_start1 = float(self.config['zstart1'])
        self.x_start2 = float(self.config['xstart2'])
        self.z_start2 = float(self.config['zstart2'])
        self.x_start3 = float(self.config['xstart3'])
        self.z_start3 = float(self.config['zstart3'])
        self.x_start4 = float(self.config['xstart4'])
        self.z_start4 = float(self.config['zstart4'])

        self.x_gap = float(self.config['xgap'])
        self.z_gap = float(self.config['zgap'])
        self.x_end = float(self.config['xend'])
        self.z_end = float(self.config['zend'])
        self.y_push_start = float(self.config['ypushstart'])
        self.y_push_end = float(self.config['ypushend'])
        self.y_return = float(self.config['yreturn'])
        self.z_lift = float(self.config['zlift'])
        self.X_avoid = float(self.config['xavoid'])
        self.cameraexposure = int(self.config['cameraexposure'])
        self.rectangle1 = [int(item) for item in self.config['rectangle1'].split(',')]
        self.z_camera = float(self.config['zcamera'])
        # 装载器的相机
        self.camera_index = int(self.config['cameraindex'])
        self.cap = None
        self.open_ocr_model()

    def up_config(self):
        # 更新参数
        self.x_start1 = float(self.config['xstart1'])
        self.z_start1 = float(self.config['zstart1'])
        self.x_start2 = float(self.config['xstart2'])
        self.z_start2 = float(self.config['zstart2'])
        self.x_start3 = float(self.config['xstart3'])
        self.z_start3 = float(self.config['zstart3'])
        self.x_start4 = float(self.config['xstart4'])
        self.z_start4 = float(self.config['zstart4'])

        self.x_gap = float(self.config['xgap'])
        self.z_gap = float(self.config['zgap'])
        self.x_end = float(self.config['xend'])
        self.z_end = float(self.config['zend'])
        self.y_push_start = float(self.config['ypushstart'])
        self.y_push_end = float(self.config['ypushend'])
        self.y_return = float(self.config['yreturn'])
        self.z_lift = float(self.config['zlift'])
        self.X_avoid = float(self.config['xavoid'])
        self.cameraexposure = int(self.config['cameraexposure'])
        self.rectangle1 = [int(item) for item in self.config['rectangle1'].split(',')]
        self.z_camera = float(self.config['zcamera'])

    # box初始位置(准备取片)
    def get_box_points(self, numer_box, number_slide):
        """
        选择并设置第几个玻片仓box

        该方法为对象选择一个合适的加载器，并根据需要设置其交付点到指定的(x,z)坐标。

        参数:
        self: 表示对象自身
        numer_box: 第几个玻片盒，用于计算玻片盒的起始位置
        number_slide: 需要设置的玻片数量，用于计算终止位置

        返回值:
        list_points: 包含每个玻片目标交付点坐标的列表，列表中每个元素都是一个包含两个数字的列表，分别代表x和z坐标。
        """
        # 初始化交付点列表
        list_points = []
        # 遍历设定的玻片数量，计算并添加每个玻片的交付点坐标
        x_start = 0
        z_start = 0
        if numer_box == 1:
            x_start = self.x_start1
            z_start = self.z_start1
        elif numer_box == 2:
            x_start = self.x_start2
            z_start = self.z_start2
        elif numer_box == 3:
            x_start = self.x_start3
            z_start = self.z_start3
        elif numer_box == 4:
            x_start = self.x_start4
            z_start = self.z_start4
        if x_start > 0 and z_start > 0:
            for i in range(number_slide):
                list_points.append([x_start, z_start - i * self.z_gap])
        return list_points

    def move_xz_to(self, x, z):
        """
        将加载器移动到指定的(x,z)坐标。
        """
        self.loader.set_delivery_abs_point(x, z)

    def move_z(self, z):
        self.loader.set_delivery_rev_z(z)

    def move_z_to(self, z):
        """
        将加载器移动到指定的(z)坐标。
        """
        self.loader.set_delivery_abs_z(z)

    def move_x_to(self, x):
        """
        将加载器移动到指定的(z)坐标。
        """
        self.loader.set_delivery_abs_x(x)

    def move_y_to(self, y):
        """
        将加载器移动到指定的(y)坐标。
        """
        loader_flage = self.loader.set_loader_abs_y(y)

        return loader_flage

    def move_2_microscope_give(self):
        """
        将加载器移动到显微镜的指定位置。

        该函数不接受参数，并且没有返回值。
        它通过调用self.loader的set_delivery_abs_point方法，设置加载器到显微镜的绝对交付点。
        """
        self.loader.set_delivery_abs_point(self.x_end, self.z_end)  # 设置加载器到显微镜的绝对交付点为(x_end, z_end)

    def move_2_microscope_get(self):
        """
        将加载器移动到显微镜的指定位置。

        该函数不接受参数，并且没有返回值。
        它通过调用self.loader的set_delivery_abs_point方法，设置加载器到显微镜的绝对交付点。
        """
        self.loader.set_delivery_abs_point(self.x_end, self.z_end + self.z_lift)  # 设置加载器到显微镜的绝对交付点为(x_end, z_end)

    def retry_move_y_push(self, start_y, end_y):
        # 收回
        loader_flage = self.move_y_to(end_y)
        self.loader.set_loader_clear_y()
        # if loader_flage != 1:
        #     self.log_warning("尝试退回异常，请联系，返回状态" + str(loader_flage))
        # else:
        #     self.log_warning("尝试退回正常，返回状态" + str(loader_flage))

        # 尝试再次伸出
        loader_flage = self.move_y_to(start_y)
        # if loader_flage != 1:
        #     self.log_warning("尝试再次伸出异常，请联系，返回状态" + str(loader_flage))
        # else:
        #     self.log_warning("尝试再次伸出正常，返回状态" + str(loader_flage))
        return loader_flage

    def retry_move_y_return(self, start_y, end_y):
        # 伸出
        loader_flage = self.move_y_to(start_y)
        # if loader_flage != 1:
        #     self.log_warning("尝试伸出异常，请联系，返回状态" + str(loader_flage))
        # else:
        #     self.log_warning("尝试伸出正常，返回状态" + str(loader_flage))

        # 尝试再次收回
        loader_flage = self.move_y_to(end_y)
        self.loader.set_loader_clear_y()
        # if loader_flage != 1:
        #     self.log_warning("尝试再次回收异常，请联系，返回状态" + str(loader_flage))
        # else:
        #     self.log_warning("尝试再次回收正常，返回状态" + str(loader_flage))
        return loader_flage

    def get_slide_from_box(self):
        """
        从盒子中获取滑块的函数。
        此函数不接受参数，并且没有返回值。
        函数执行过程：
        1. 通过执行机构伸出，将loader设置到初始的y位置。
        2. 调整loader的高度，使其向上移动。
        3. 收回执行机构，将loader移回初始位置。
        """
        try:
            loader_flage = self.move_y_to(self.y_push_start)
            if loader_flage != 1:
                loader_flage = self.retry_move_y_push(self.y_push_start, self.y_return)
                if loader_flage != 1:
                    # self.log_warning("尝试退回异常卡住，请联系，返回状态" + str(loader_flage))
                    return loader_flage

            time.sleep(1)
            self.move_z(-self.z_gap)
            time.sleep(1)

            loader_flage = self.move_y_to(self.y_return)
            self.loader.set_loader_clear_y()
            if loader_flage != 1:
                # self.log_warning("从玻片仓收回异常" + str(loader_flage))
                loader_flage = self.retry_move_y_return(self.y_push_start, self.y_return)
                if loader_flage != 1:
                    # self.log_warning("尝试伸出异常卡住，请联系，返回状态" + str(loader_flage))
                    return loader_flage

        except Exception as e:
            # self.log_warning(f"操作过程中发生异常: {e}")
            return -1
        return loader_flage

    def give_slide_to_box(self):
        """
        将滑块送入盒子中的函数。
        此函数不接受参数，并且没有返回值。
        函数执行过程：
        1. 使执行机构伸出到指定的y位置。
        2. 调整执行机构，使其向下移动到指定的z位置。
        3. 恢复执行机构的原始位置。
        """
        try:
            loader_flage = self.move_y_to(self.y_push_start)
            if loader_flage != 1:
                loader_flage = self.retry_move_y_push(self.y_push_start, self.y_return)
                if loader_flage != 1:
                    # self.log_warning("尝试退回异常卡住，请联系，返回状态" + str(loader_flage))
                    return loader_flage

            time.sleep(1)
            self.move_z(self.z_gap)
            time.sleep(1)

            loader_flage = self.move_y_to(self.y_return)
            self.loader.set_loader_clear_y()
            if loader_flage != 1:
                # self.log_warning("从玻片仓收回异常" + str(loader_flage))
                loader_flage = self.retry_move_y_return(self.y_push_start, self.y_return)
                if loader_flage != 1:
                    # self.log_warning("尝试伸出异常卡住，请联系，返回状态" + str(loader_flage))
                    return loader_flage

        except Exception as e:
            # self.log_warning(f"操作过程中发生异常: {e}")
            return -1
        return loader_flage

    def give_slide_to_microscope(self):
        """
        将滑块送入显微镜中的函数。
        此函数不接受参数，并且没有返回值。
        函数执行过程：
        1. 使执行机构伸出到指定的y位置。
        2. 调整执行机构，使其向下移动到指定的z位置。
        3. 恢复执行机构的原始位置。
        """
        try:
            loader_flage = self.move_y_to(self.y_push_start)
            if loader_flage != 1:
                loader_flage = self.retry_move_y_push(self.y_push_start, self.y_return)
                if loader_flage != 1:
                    # self.log_warning("尝试退回异常卡住，请联系，返回状态" + str(loader_flage))
                    return loader_flage

            time.sleep(1)
            self.move_z(self.z_lift)
            time.sleep(1)

            loader_flage = self.move_y_to(self.y_return)
            self.loader.set_loader_clear_y()
            if loader_flage != 1:
                # self.log_warning("从显微镜收回异常" + str(loader_flage))
                loader_flage = self.retry_move_y_return(self.y_push_start, self.y_return)
                if loader_flage != 1:
                    # self.log_warning("尝试伸出异常卡住，请联系，返回状态" + str(loader_flage))
                    return loader_flage

        except Exception as e:
            # self.log_warning(f"操作过程中发生异常: {e}")
            return -1
        return loader_flage

    def get_slide_from_microscope(self):
        """
        从显微镜中获取滑块的函数。
        此函数不接受参数，并且没有返回值。
        函数执行过程：
        1. 使执行机构伸出到指定的y位置。
        2. 调整执行机构，使其向下移动到指定的z位置。
        3. 恢复执行机构的原始位置。
        """
        try:
            loader_flage = self.move_y_to(self.y_push_start)
            if loader_flage != 1:
                loader_flage = self.retry_move_y_push(self.y_push_start, self.y_return)
                if loader_flage != 1:
                    # self.log_warning("尝试退回异常卡住，请联系，返回状态" + str(loader_flage))
                    return loader_flage

            time.sleep(1)
            self.move_z(-self.z_lift)
            time.sleep(1)

            loader_flage = self.move_y_to(self.y_return)
            self.loader.set_loader_clear_y()
            if loader_flage != 1:
                # self.log_warning("从显微镜收回异常" + str(loader_flage))
                loader_flage = self.retry_move_y_return(self.y_push_start, self.y_return)
                if loader_flage != 1:
                    # self.log_warning("尝试伸出异常卡住，请联系，返回状态" + str(loader_flage))
                    return loader_flage

        except Exception as e:
            # self.log_warning(f"操作过程中发生异常: {e}")
            return -1
        return loader_flage

    def set_led(self, num, color):
        self.loader.led[num] = color  # 设置灯颜色
        self.loader.set_led_color(self.loader.led[0:4])

    def get_key(self):
        box_key = []
        box_list = []
        for key in self.loader.key:
            if key == self.key.none:
                box_key.append(0)
            elif key == self.key.pressed:
                box_key.append(1)
            elif key == self.key.released:
                box_key.append(2)
        for i in range(len(box_key)):
            if box_key[i] == 1:
                box_list.append(i + 1)
        return box_list

    def loader_reset(self):
        """
        重置加载器。
        """
        self.loader.reset()

    def loader_avoid(self):
        """
        避免加载器。
        """
        self.loader.set_delivery_abs_x(self.X_avoid)

    def loader_move2_camera(self):
        self.move_z_to(self.z_camera)

    def loader_last_push(self):
        loader_flage = self.move_y_to(self.y_push_start)
        if loader_flage == 1:
            pass
        else:
            # self.log_warning("伸出到玻片仓异常卡住")
            return loader_flage
        loader_flage = self.move_y_to(self.y_return)
        self.loader.set_loader_clear_y()
        if loader_flage == 1:
            pass
        else:
            return loader_flage
        return loader_flage

    def open_camera(self):
        # 打开摄像头
        self.cap = cv2.VideoCapture(self.camera_index)

        self.cap.set(cv2.CAP_PROP_EXPOSURE, self.cameraexposure)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 2592)  # 宽度为2592像素
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1944)  # 高度为1944像素
        # 检查摄像头是否成功打开
        if not self.cap.isOpened():
            # self.log_warning("拍摄玻片相机打开失败")
            return False
        else:
            return True

    def capture_image(self):
        # 检查摄像头是否已打开
        if self.cap is None or not self.cap.isOpened():
            return None

        # 捕获单张图像
        ret, frame = self.cap.read()

        # 检查图像是否成功捕获
        if not ret:
            print("Failed to capture image")
            return None

        return frame

    def crop_image(self, img):
        return img[self.rectangle1[1]:self.rectangle1[3], self.rectangle1[0]:self.rectangle1[2]]

    def release_camera(self):
        # 释放摄像头资源
        if self.cap is not None and self.cap.isOpened():
            self.cap.release()
            return True
        else:
            return False

    def open_ocr_model(self):
        self.ocr = PaddleOCR(use_angle_cls=True, lang="en",
                             det_model_dir='./src/model/ch_ppocr_server_v2.0_det_infer')

    def get_ocr_result(self, image):
        return self.ocr.ocr(image, cls=True)

    def match_ID(self, results, length):
        ID = []
        IDaLL = []
        if results is None:
            return ID, IDaLL
        else:
            for data in results:
                IDaLL.append(data[1][0])
                if len(data[1][0]) == length:
                    ID.append(data[1][0])
        return ID, IDaLL
