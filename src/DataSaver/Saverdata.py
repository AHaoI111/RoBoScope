import configparser
import math
from concurrent.futures import ThreadPoolExecutor
from queue import Queue

import cv2
from PySide6.QtCore import *

from DataProcessing import data
from src.model import model


class Saver(QObject):
    def __init__(self):
        QObject.__init__(self)
        self.image_bacteria = None
        self.image_ec = None
        self.image_wbc = None

        self.read_config()
        self.model_ec = model.Model_YOLO_cell('./src/model/bioscope_cell.pt')
        self.model_bacteria = model.Model_YOLO_bacteria('./src/model/bioscope_bacteria.pt')

        self.queue = Queue(self.queuenumber)

        self.stopped = False  # 停止标志
        self.executor = ThreadPoolExecutor(max_workers=self.maxworkers)
        self.start_processing()

        self.image_stitch_part = []
        self.image_stitch_all = []
        self.DataProcessing = None

    def process_queue(self):
        while not self.stopped:
            try:
                [image, ID, ZPoint, a, Point_XY, timesave, path_save,
                 numberw, numberh, ok, point_xy_real, multiple] = self.queue.get(
                    timeout=0.1)
                if image is not None:
                    if a == 1:
                        path = path_save + '\\' + ID + '.jpg'
                        self.DataProcessing = data.data_processing(ID, numberw, numberh, path, multiple)
                    # 存图
                    bgr_image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                    cv2.imwrite(path_save + '\\' + timesave + '_' + ID + '_' + str(a) + '.' + self.PixelFormat, bgr_image,
                                [cv2.IMWRITE_JPEG_QUALITY, self.ImageQuailty])
                    # 拼接
                    self.stitch_part(a, numberw, numberh, bgr_image)
                    # 细胞推理
                    results_cell = self.model_ec.pre(image)
                    # 细菌推理
                    xylist, images = self.sub_image(image)
                    results_bacteria = self.model_bacteria.pre(images)
                    # 保存结果
                    path = path_save + '\\' + timesave + '_' + ID + '_' + str(a) + '.' + self.PixelFormat
                    self.DataProcessing.Save_data_3(ID, ZPoint, a, Point_XY, point_xy_real, path,
                                                    results_cell, results_bacteria, xylist)

                    if a == numberw * numberh:
                        img = cv2.vconcat(self.image_stitch_all)
                        ok.emit(ID, img,multiple)
                        cv2.imwrite(path_save + '\\' + ID + '.jpg', img,
                                    [cv2.IMWRITE_JPEG_QUALITY, 80])
                        self.image_stitch_all = []

                self.queue.task_done()

            except:
                pass

    def enqueue(self, image, ID, ZPoint, a, Point_XY, timesave, path_save,
                numberw, numberh, ok, point_xy_real, multiple):
        try:
            self.queue.put_nowait(
                [image, ID, ZPoint, a, Point_XY, timesave, path_save,
                 numberw, numberh, ok, point_xy_real, multiple])
        except:
            print('imageSaver queue is full, image discarded')

    def start_processing(self):
        for _ in range(self.maxworkers):
            self.executor.submit(self.process_queue)

    def stop(self):
        self.stopped = True  # 设置停止标志

    def sub_image(self, image):
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

    def stitch_part(self, a, numberw, numberh, image):
        image = cv2.resize(image, (self.ImageStitchSize, self.ImageStitchSize))
        if ((a - 1) // numberw) % 2 == 0:
            # 奇数排
            self.image_stitch_part.append(image)
            if a % numberw == 0:
                self.image_stitch_all.append(cv2.hconcat(self.image_stitch_part))
                self.image_stitch_part = []

        else:
            # 偶数排
            self.image_stitch_part.insert(0, image)
            if a % numberw == 0:
                self.image_stitch_all.append(cv2.hconcat(self.image_stitch_part))
                self.image_stitch_part = []

    def read_config(self):
        try:
            # 加载配置
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
                self.maxworkers = 3
                self.queuenumber = 625
                self.new_width = 640
                self.new_height = 640
                self.ImageStitchSize = 640
                self.PixelFormat = 'jpg'
                self.ImageQuailty = 80
        except:
            # 默认
            self.maxworkers = 3
            self.queuenumber = 625
            self.new_width = 640
            self.new_height = 640
            self.ImageStitchSize = 640
            self.PixelFormat = 'jpg'
            self.ImageQuailty = 80
