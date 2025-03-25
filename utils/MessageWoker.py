# -*- encoding: utf-8 -*-
"""
@Description:
用于存储图片的队列
@File    :   Saverdata.py
@Time    :   2024/07/16
@Author  :   Li QingHao
@Version :   2.0
@Time_END :  最后修改时间：
@Developers_END :  最后修改作者：
"""
import os
from concurrent.futures import ThreadPoolExecutor
from queue import Queue

import cv2
import numpy as np
from PIL import Image
from PySide6.QtCore import *


class Message_Woker(QObject):
    # 信号
    up_points_high = Signal(list, str)
    """
    该类用于处理图像保存和拼接的任务。
    它包含一个队列来管理待处理的图像数据，
    并使用线程池来并发处理这些任务。
    self.correction_model:   0(不做平场校正) 1(做低倍平场校正) 2(做高倍平场校正) 3(高低倍都做平场校正)
    """

    def __init__(self, saver_info):
        """
        初始化Saver对象。
        这包括读取配置、初始化队列和线程池，
        以及设置图像处理的相关参数。
        """
        super().__init__()
        # 初始化图像变量
        self.Request = None
        self.width = 2560
        self.height = 2560
        self.base_img_low = None
        self.base_img_high = None

        # 读取配置文件
        self.maxworkers = saver_info['maxworkers']
        self.ImageStitchSize = saver_info['imagestitchsize']
        self.queuenumber = saver_info['queuenumber']
        self.PixelFormat = saver_info['pixelformat']
        self.ImageQuailty = saver_info['imagequailty']
        self.correction_model = saver_info['correction_model']

        # 初始化队列
        self.queue = Queue(self.queuenumber)

        # 初始化状态变量
        self.stopped = False  # 停止标志
        self.executor = ThreadPoolExecutor(max_workers=self.maxworkers)
        self.start_processing()

        # 初始化图像拼接和数据处理变量
        self.image_stitch_all = None
        self.image_stitch_flag = False
        if self.correction_model == 0:
            pass
        elif self.correction_model == 1:
            self.base_img_low = cv2.imread('base_low.png')
        elif self.correction_model == 2:
            self.base_img_high = cv2.imread('base_high.png')
        elif self.correction_model == 3:
            self.base_img_low = cv2.imread('base_low.png')
            self.base_img_high = cv2.imread('base_high.png')

    def flat_field_correction(self, image, flat_field):
        """
        对图像进行平场矫正。

        参数:
        image (numpy.ndarray): 输入的待矫正图像（BGR格式）。
        flat_field (numpy.ndarray): 平场图像（BGR格式）。

        返回:
        numpy.ndarray: 平场矫正后的图像（BGR格式）。
        """
        # 将图像和平场图像转换为浮点型
        image = image.astype(np.float32)
        flat_field = flat_field.astype(np.float32)

        # 避免除以零的情况，将平场图像中的零值替换为一个很小的正数
        flat_field = np.where(flat_field == 0, 1e-10, flat_field)

        # 进行平场矫正：输入图像除以平场图像
        corrected_image = image / flat_field

        # 计算平场图像的平均值，并乘以矫正后的图像以保持亮度
        scale_factor = np.mean(flat_field, axis=(0, 1))
        corrected_image = corrected_image * scale_factor

        # 将结果限制在0-255范围内，并转换为uint8类型
        corrected_image = np.clip(corrected_image, 0, 255).astype(np.uint8)

        return corrected_image

    def process_queue(self):
        """
        持续处理队列中的图像保存任务。
        3表示正常的扫描
        4表示xywh，高低倍配合扫描
        """
        while not self.stopped:
            try:
                # 从队列中获取任务数据
                [image, UUID, multiple, base_flag, Point_XY, is_end, Img_Number,
                 path_save, task_info] = self.queue.get(timeout=0.1)
                # 高低倍配合扫描
                if task_info['scanmode']:
                    # 低倍
                    if base_flag == 'low':
                        if self.Request is not None:
                            if task_info['recommend_view_source'] == 'view_pic':
                                if image is not None:
                                    # 判断是否需要平场矫正
                                    bgr_image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                                    if self.correction_model != 0:
                                        base_img = self.base_img_low if base_flag == 'low' else self.base_img_high
                                        if base_img is not None:
                                            bgr_image = self.flat_field_correction(bgr_image, base_img)
                                    px2distance = task_info['calibration_low']
                                    self.height, self.width, _ = bgr_image.shape
                                    startX = (task_info['center_x_low'] + task_info['region_w_low'] / 2
                                              - task_info['lens_gap_x'] - Point_XY[0] * (px2distance * self.width))
                                    startY = (task_info['center_y_low'] + task_info['region_h_low'] / 2
                                              - task_info['lens_gap_y'] - Point_XY[1] * (px2distance * self.height))
                                    if Img_Number == 1:
                                        flag = "start"
                                    else:
                                        flag = ""
                                    if is_end:
                                        flag = "end"
                                    status, data = self.Request.request2server_send_scan_pic_low(bgr_image, UUID,
                                                                                                 startX,
                                                                                                 startY,
                                                                                                 px2distance, flag,
                                                                                                 task_info['scan_api'],
                                                                                                 task_info['max_areas'])
                                    if flag == "end":
                                        self.up_points_high.emit(data['center_points'], data['scan_range'])
                            elif task_info['recommend_view_source'] == 'slide_pic':
                                if image is not None:
                                    print(UUID)
                                    px2distance = task_info['calibration_low'] * (self.width / self.ImageStitchSize)
                                    startX = (task_info['center_x_low'] + task_info['region_w_low'] / 2
                                              - task_info['lens_gap_x'])
                                    startY = (task_info['center_y_low'] + task_info['region_h_low'] / 2
                                              - task_info['lens_gap_y'])
                                    status, data = self.Request.request2server_send_scan_pic_low(image, UUID,
                                                                                                 startX,
                                                                                                 startY,
                                                                                                 px2distance,
                                                                                                 "once",
                                                                                                 task_info[
                                                                                                     'scan_api'],
                                                                                                 task_info['max_areas'])
                                    self.up_points_high.emit(data['center_points'], data['scan_range'])
                    elif base_flag == 'high':
                        if self.Request is not None:
                            if image is not None:
                                # 判断是否需要平场矫正
                                bgr_image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                                path_sub = "/" + path_save.replace(task_info['savepath'], "")
                                multiple_str = str(multiple) + 'X'
                                name = f"{UUID}_{multiple_str}_{Img_Number}.{self.PixelFormat}"
                                # 低倍初始点对应在高倍
                                startX = task_info['center_x_low'] + task_info['region_w_low'] / 2 - task_info[
                                    'lens_gap_x']
                                startY = task_info['center_y_low'] + task_info['region_h_low'] / 2 - task_info[
                                    'lens_gap_y']

                                # 计算像素坐标
                                pix_x = (startX - Point_XY[0]) / (
                                        task_info['calibration_low'] * (self.width / self.ImageStitchSize))
                                pix_y = (startY - Point_XY[1]) / (
                                        task_info['calibration_low'] * (self.height / self.ImageStitchSize))
                                # 宽高
                                height, width, _ = bgr_image.shape
                                w = (width * task_info['calibration_high']) / (
                                        task_info['calibration_low'] * (self.width / self.ImageStitchSize))
                                h = (height * task_info['calibration_high']) / (
                                        task_info['calibration_low'] * (self.height / self.ImageStitchSize))
                                center_point = [pix_y, pix_x, h, w]

                                status, data = self.Request.create_view(UUID, path_sub, name, center_point)
                            if is_end:
                                status, data = self.Request.finish_silde(UUID, UUID + "_slide.jpg")
                else:
                    if self.Request is not None:
                        if image is not None:
                            if task_info['pre_request_flag']:
                                if is_end:
                                    bgr_image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                                    if self.correction_model != 0:
                                        base_img = self.base_img_low if base_flag == 'low' else self.base_img_high
                                        if base_img is not None:
                                            bgr_image = self.flat_field_correction(bgr_image, base_img)
                                    status, data = self.Request.request2server_send_pre_scan_pic(bgr_image,
                                                                                                 task_info['task_id'],
                                                                                                 task_info[
                                                                                                     'pre_scan_api'])
                            else:
                                path_sub = "/" + path_save.replace(task_info['savepath'], "")
                                multiple_str = str(multiple) + 'X'
                                name = f"{UUID}_{multiple_str}_{Point_XY[0]}_{Point_XY[1]}.{self.PixelFormat}"
                                center_point = [Point_XY[0] * self.ImageStitchSize, Point_XY[1] * self.ImageStitchSize,
                                                self.ImageStitchSize, self.ImageStitchSize]
                                status, data = self.Request.create_view(UUID, path_sub, name, center_point)
                                if is_end:
                                    status, data = self.Request.finish_silde(UUID, UUID + "_slide.jpg")
                # 标记任务完成
                self.queue.task_done()
            except Exception as e:
                pass

    def enqueue(self, image, UUID, multiple, base_flag, Point_XY, is_end, Img_Number,
                 path_save, task_info):
        """
        将图像保存任务添加到队列中。
        """
        try:
            self.queue.put_nowait(
                [image, UUID, multiple, base_flag, Point_XY, is_end, Img_Number,
                 path_save, task_info])
        except:
            print('imageSaver queue is full, image discarded')

    def start_processing(self):
        """
        启动线程池执行队列中的任务。
        """
        for _ in range(self.maxworkers):
            self.executor.submit(self.process_queue)

    def stop(self):
        """
        停止处理队列中的任务。
        """
        self.stopped = True
