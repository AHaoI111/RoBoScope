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
import configparser
import math
import os
from concurrent.futures import ThreadPoolExecutor
from queue import Queue

import cv2
import numpy
import numpy as np
from PIL import Image
from PySide6.QtCore import *
from utils import read_config


class Saver(QObject):
    # 信号
    up_points_high = Signal(list,str)
    """
    该类用于处理图像保存和拼接的任务。
    它包含一个队列来管理待处理的图像数据，
    并使用线程池来并发处理这些任务。
    """

    def __init__(self, saver_info):
        """
        初始化Saver对象。
        这包括读取配置、初始化队列和线程池，
        以及设置图像处理的相关参数。
        """
        super().__init__()
        # 初始化图像变量
        self.width = None
        self.height = None
        self.image_bacteria = None
        self.image_ec = None
        self.image_wbc = None

        # 读取配置文件
        self.maxworkers = saver_info['maxworkers']
        self.ImageStitchSize = saver_info['imagestitchsize']
        self.queuenumber = saver_info['queuenumber']
        self.PixelFormat = saver_info['pixelformat']
        self.ImageQuailty = saver_info['imagequailty']

        # 初始化队列
        self.queue = Queue(self.queuenumber)

        # 初始化状态变量
        self.stopped = False  # 停止标志
        self.executor = ThreadPoolExecutor(max_workers=self.maxworkers)
        self.start_processing()

        # 初始化图像拼接和数据处理变量
        self.image_stitch_all = None
        self.DataProcessing = None
        self.Request = None

        #

    def process_queue(self):
        """
        持续处理队列中的图像保存任务。
        3表示正常的扫描
        4表示xywh，高低倍配合扫描
        """
        while not self.stopped:
            try:
                # 从队列中获取任务数据
                [image, UUID, a, Point_XY, timesave, path_save,
                 numberw, numberh, task_info] = self.queue.get(timeout=0.1)
                if image is not None:
                    # 格式化编号
                    formatted_a = str(a).zfill(5)
                    # 转换图像格式并保存
                    bgr_image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                    # 2只为高倍的坐标
                    if len(Point_XY) == 2:
                        # 高倍视野创建
                        if task_info['flag_create_view']:
                            name = f"{timesave}_{UUID}_{formatted_a}.{self.PixelFormat}"
                            cv2.imencode('.' + self.PixelFormat, bgr_image,
                                         [cv2.IMWRITE_JPEG_QUALITY, self.ImageQuailty])[1].tofile(
                                os.path.join(path_save, name))
                            path_sub = "/" + path_save.replace(task_info['savepath'], "")
                            file_name = f"{timesave}_{UUID}_{formatted_a}.{self.PixelFormat}"
                            # 创建高倍视野
                            if self.Request is not None:
                                # 低倍初始点对应在高倍
                                startX = task_info['center_x_low'] + task_info['region_w_low'] / 2 - task_info['lens_gap_x']
                                startY = task_info['center_y_low'] + task_info['region_h_low'] / 2 - task_info['lens_gap_y']

                                # 计算像素坐标
                                pix_x = (startX - Point_XY[0])/(task_info['calibration_low']*(self.width/self.ImageStitchSize))
                                pix_y = (startY - Point_XY[1]) / (task_info['calibration_low']* (self.height / self.ImageStitchSize) )
                                # 宽高
                                height, width, _ = bgr_image.shape
                                w = (width * task_info['calibration_high']) / (task_info['calibration_low']*(self.width/self.ImageStitchSize))
                                h = (height * task_info['calibration_high']) / (task_info['calibration_low'] * (self.height / self.ImageStitchSize))
                                center_point = [pix_y, pix_x,h,w]

                                status, data = self.Request.create_view(UUID, path_sub, file_name, center_point)

                            if a == numberw and a == numberh:
                                if self.Request is not None:
                                    status, data = self.Request.finish_silde(UUID, UUID + "_slide.jpg")

                    # 3为低倍和普通坐标
                    elif len(Point_XY) == 3:
                        # 高低倍需要发送局部低倍视野(说明为高低倍扫描模式低倍)
                        if task_info['scanmode']:
                            # 拼图
                            self.stitch_part(Point_XY, image)
                            low = "low"
                            name = f"{timesave}_{UUID}_{low}_{formatted_a}.{self.PixelFormat}"
                            cv2.imencode('.' + self.PixelFormat, bgr_image,
                                         [cv2.IMWRITE_JPEG_QUALITY, self.ImageQuailty])[1].tofile(
                                os.path.join(path_save, name))
                            px2distance = task_info['calibration_low']
                            self.height, self.width, _ = bgr_image.shape
                            startX = (task_info['center_x_low'] + task_info['region_w_low'] / 2
                                      - task_info['lens_gap_x'] - Point_XY[0] * (px2distance * self.width))
                            startY = (task_info['center_y_low'] + task_info['region_h_low'] / 2
                                      - task_info['lens_gap_y'] - Point_XY[1] * (px2distance * self.height))
                            if a == 1:
                                flag = "start"
                            elif a == numberw * numberh:
                                flag = "end"
                            else:
                                flag = ""
                            # 发送低倍视野请求
                            if self.Request is not None:
                                status, data = self.Request.request2server_send_scan_pic_low(bgr_image, UUID,
                                                                                             startX,
                                                                                             startY,
                                                                                             px2distance, flag,
                                                                                             task_info['scan_api'])
                                if flag == "end":
                                    print('end')
                                    print(status)
                                    print(data)
                                    self.up_points_high.emit(data['center_points'], data['scan_range'])
                        # (说明为普通扫描模式)
                        else:
                            # 拼图
                            self.stitch_part(Point_XY, image)
                            name = f"{timesave}_{UUID}_{Point_XY[0]}_{Point_XY[1]}_{formatted_a}.{self.PixelFormat}"
                            cv2.imencode('.' + self.PixelFormat, bgr_image,
                                         [cv2.IMWRITE_JPEG_QUALITY, self.ImageQuailty])[1].tofile(
                                os.path.join(path_save, name))
                        if a == numberw * numberh:
                            if task_info['pre_request_flag']:
                                # 将 PIL 图像对象转换为 NumPy 数组
                                # 发送预扫描的请求
                                if self.Request is not None:
                                    status, data = (self.Request.request2server_send_pre_scan_pic
                                                    (bgr_image, task_info['task_id'], task_info['pre_scan_api']))
                            else:
                                # 低倍扫描和普通单倍扫描都需要保存拼图
                                # self.image_stitch_all.save(path_save + '/' + UUID + '_slide' + '.jpg', quality=80)
                                cv_image = np.array(self.image_stitch_all)

                                # 将 RGB 转换为 BGR
                                opencv_image = cv2.cvtColor(cv_image, cv2.COLOR_RGB2BGR)
                                name2 = UUID + "_slide.jpg"
                                cv2.imencode('.jpg', opencv_image,
                                             [cv2.IMWRITE_JPEG_QUALITY, self.ImageQuailty])[1].tofile(
                                    os.path.join(path_save, name2))
                                self.image_stitch_all = None
                                if task_info['scanmode']:
                                    pass
                                else:
                                    if self.Request is not None:
                                        status, data = self.Request.finish_silde(UUID, UUID + "_slide.jpg")
                # 标记任务完成
                self.queue.task_done()
            except Exception as e:
                pass

    def enqueue(self, image, UUID, a, Point_XY, timesave, path_save,
                numberw, numberh, task_info):
        """
        将图像保存任务添加到队列中。
        """
        try:
            self.queue.put_nowait(
                [image, UUID, a, Point_XY, timesave, path_save,
                 numberw, numberh, task_info])
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

    def stitch_part(self, Point_XY, image):
        """
        将小图像拼接到全局图像上。

        :param Point_XY: 小图像在全局图像中的位置。
        :param image: 待拼接的小图像。
        """
        try:
            image = cv2.resize(image, (self.ImageStitchSize, self.ImageStitchSize))
            # 将 OpenCV 图像转换为 Pillow Image 对象
            image_pil = Image.fromarray(image)
            self.image_stitch_all.paste(image_pil,
                                        (Point_XY[1] * self.ImageStitchSize, Point_XY[0] * self.ImageStitchSize))
        except Exception as e:
            pass
