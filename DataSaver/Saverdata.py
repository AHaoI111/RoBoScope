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
from concurrent.futures import ThreadPoolExecutor
from queue import Queue

import cv2
import logbook
import numpy
from PIL import Image
from PySide6.QtCore import *

from DataSaver import data


# from src.model import model


class Saver(QObject):
    """
    该类用于处理图像保存和拼接的任务。
    它包含一个队列来管理待处理的图像数据，
    并使用线程池来并发处理这些任务。
    """

    def __init__(self):
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
        self.read_config()

        # 初始化队列
        self.queue = Queue(self.queuenumber)

        # 初始化状态变量
        self.stopped = False  # 停止标志
        self.executor = ThreadPoolExecutor(max_workers=self.maxworkers)
        self.start_processing()
        # self.model_ec = model.Model_YOLO_cell('./src/model/bioscope_cell.pt')
        # self.model_bacteria = model.Model_YOLO_bacteria('./src/model/bioscope_bacteria.pt')

        # 初始化图像拼接和数据处理变量
        self.image_stitch_all = None
        self.DataProcessing = None

    def process_queue(self):
        """
        持续处理队列中的图像保存任务。
        """
        while not self.stopped:
            try:
                # 从队列中获取任务数据
                [image, UUID, ZPoint, a, Point_XY, timesave, path_save,
                 numberw, numberh, ok, point_xy_real, multiple, code] = self.queue.get(timeout=0.1)
                if image is not None:
                    # 格式化编号
                    num_digits = len(str(numberw * numberh))
                    formatted_a = '{:0{width}d}'.format(a, width=num_digits)
                    # 转换图像格式并保存
                    bgr_image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

                    cv2.imwrite(
                        path_save + '\\' + timesave + '_' + UUID + '_' + str(formatted_a) + '.' + self.PixelFormat,
                        bgr_image,
                        [cv2.IMWRITE_JPEG_QUALITY, self.ImageQuailty])
                    # 图像拼接
                    self.stitch_part(Point_XY, image)
                    # 细胞推理
                    # results_cell = self.model_ec.pre(image)
                    # 细菌推理
                    # xylist, images = self.sub_image(image)
                    # results_bacteria = self.model_bacteria.pre(images)
                    # 保存结果
                    path = path_save + '\\' + timesave + '_' + UUID + '_' + str(formatted_a) + '.' + self.PixelFormat
                    # self.DataProcessing.Save_data_3(image, UUID, ZPoint, a, Point_XY, point_xy_real, path,
                    #                                 results_cell, results_bacteria, xylist, formatted_a)
                    # 保存拼接后的图像
                    if a == numberw * numberh:
                        try:
                            image_np = numpy.array(self.image_stitch_all)
                            ok.emit(code, image_np, multiple)
                            self.image_stitch_all.save(path_save + '\\' + UUID + '.jpg', quality=80)
                            self.image_stitch_all = None
                        except Exception as e:
                            pass

                # 标记任务完成
                self.queue.task_done()
            except:
                pass

    def enqueue(self, image, UUID, ZPoint, a, Point_XY, timesave, path_save,
                numberw, numberh, ok, point_xy_real, multiple, code):
        """
        将图像保存任务添加到队列中。
        """
        try:
            self.queue.put_nowait(
                [image, UUID, ZPoint, a, Point_XY, timesave, path_save,
                 numberw, numberh, ok, point_xy_real, multiple, code])
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

    def sub_image(self, image):
        """
        将图像分割成多个小图像。

        :param image: 输入的原始图像。
        :return: 分割后的小图像列表和对应的坐标列表。
        """
        xylist = []
        images = []
        height, width = image.shape[:2]
        num_w = math.ceil(width / self.new_width)
        num_h = math.ceil(height / self.new_height)
        for w in range(num_w):
            x = w * self.new_width
            for h in range(num_h):
                y = h * self.new_height
                cropped_image = image[y:y + self.new_height, x:x + self.new_width]
                xylist.append([x, y])
                images.append(cropped_image)
        return xylist, images

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
            with open("log.txt", "a") as log_file:
                log_file.write(str(e))

    def read_config(self):
        """
        读取配置文件并设置相关参数。
        """
        try:
            config = configparser.ConfigParser()
            config.read('config.ini')
            self.maxworkers = config.getint('ImageSaver', 'maxworkers')
            self.ImageStitchSize = config.getint('ImageSaver', 'ImageStitchSize')
            self.new_width = config.getint('ImageSaver', 'Newimage')
            self.new_height = config.getint('ImageSaver', 'Newimage')
            self.queuenumber = config.getint('ImageSaver', 'queuenumber')
            self.PixelFormat = config.get('ImageSaver', 'PixelFormat')
            self.ImageQuailty = config.getint('ImageSaver', 'ImageQuailty')
            if None in (self.maxworkers, self.ImageStitchSize, self.new_width, self.queuenumber, self.new_height):
                # 使用默认值
                self.maxworkers = 3
                self.queuenumber = 625
                self.new_width = 640
                self.new_height = 640
                self.ImageStitchSize = 640
                self.PixelFormat = 'jpg'
                self.ImageQuailty = 80
        except:
            # 使用默认值
            self.maxworkers = 3
            self.queuenumber = 625
            self.new_width = 640
            self.new_height = 640
            self.ImageStitchSize = 640
            self.PixelFormat = 'jpg'
            self.ImageQuailty = 80
