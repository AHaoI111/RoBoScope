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
    single_send2_request_pre_scan_pic = Signal(numpy.ndarray, str, str)
    single_send2_request_scan_pic_low = Signal(numpy.ndarray, str, int)
    single_updata_points = Signal()
    create_view = Signal(str, str, str, list)
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
                    if len(Point_XY) == 3:
                        if task_info['pre_request_flag']:
                            pass
                        else:
                            cv2.imencode('.' + self.PixelFormat, bgr_image,
                                         [cv2.IMWRITE_JPEG_QUALITY, self.ImageQuailty])[
                                1].tofile(
                                os.path.join(path_save,
                                             f"{timesave}_{UUID}_{Point_XY[0]}_{Point_XY[1]}_{formatted_a}.{self.PixelFormat}"))
                            if task_info['flag_create_view']:
                                # 视野信息
                                path_sub = path_save.replace(task_info['savepath'], "")
                                self.create_view.emit(UUID, path_sub,
                                                      f"{timesave}_{UUID}_{Point_XY[0]}_{Point_XY[1]}_{formatted_a}.{self.PixelFormat}",
                                                      [Point_XY[0], Point_XY[1]])

                    elif len(Point_XY) == 4:
                        cv2.imencode('.' + self.PixelFormat, bgr_image, [cv2.IMWRITE_JPEG_QUALITY, self.ImageQuailty])[
                            1].tofile(
                            os.path.join(path_save,
                                         f"{timesave}_{UUID}_{formatted_a}.{self.PixelFormat}"))
                        if task_info['flag_create_view']:
                            # 视野信息
                            path_sub = path_save.replace(task_info['savepath'], "")
                            self.create_view.emit(UUID, path_sub,
                                                  f"{timesave}_{UUID}_{formatted_a}.{self.PixelFormat}", Point_XY)

                    # 图像拼接
                    if len(Point_XY) == 3:
                        self.stitch_part(Point_XY, image)
                    # 正常扫描
                    if len(Point_XY) == 3:
                        if task_info['scanmode']:
                            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                            self.single_send2_request_scan_pic_low.emit(gray, task_info['scan_api'], a)
                        if a == numberw * numberh:
                            image_array = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                            if task_info['pre_request_flag']:
                                # 将 PIL 图像对象转换为 NumPy 数组
                                image_array = np.array(self.image_stitch_all)
                                self.single_send2_request_pre_scan_pic.emit(image_array, task_info['task_id'],
                                                                            task_info['pre_scan_api'])
                            else:
                                self.image_stitch_all.save(path_save + '/' + UUID + '_slide' + '.jpg', quality=80)
                                self.single_updata_points.emit()
                            self.image_stitch_all = None
                    elif len(Point_XY) == 4:
                        if a == numberw:
                            pass

                # 标记任务完成
                self.queue.task_done()
            except Exception as e:
                # print(str(e))
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
