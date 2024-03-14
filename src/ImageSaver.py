import configparser
import math
import os
import statistics
from concurrent.futures import ThreadPoolExecutor
from queue import Queue

import cv2
import torch
from PySide6.QtCore import *

from src import data


class ImageSaver(QObject):
    def __init__(self, model, model_bacteria):
        QObject.__init__(self)

        self.image_bacteria = None
        self.image_ec = None
        self.image_wbc = None

        self.read_config()

        self.queue = Queue(self.queuenumber)
        self.model = model
        self.model_bacteria = model_bacteria
        self.stopped = False  # 停止标志
        self.executor = ThreadPoolExecutor(max_workers=self.maxworkers)
        self.start_processing()

        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.image_stitch_part = []
        self.image_stitch_all = []

    def process_queue(self):
        while not self.stopped:
            try:
                [image, Graph_class, PP_code, ID, ZPoint, a, Point_XY, timesave, path_save,
                 numberw, numberh, ok, point_xy_real, multiple] = self.queue.get(
                    timeout=0.1)
                if a == 1:
                    self.image_stitch_part = []
                    self.image_stitch_all = []
                    self.image_wbc = torch.zeros((numberw, numberh), dtype=torch.uint8, device=self.device)
                    self.image_ec = torch.zeros((numberw, numberh), dtype=torch.uint8, device=self.device)
                    self.image_bacteria = torch.zeros((numberw, numberh), dtype=torch.uint8, device=self.device)

                if image is not None:
                    # 存图
                    cv2.imwrite(path_save + '\\' + timesave + '_' + ID + '_' + str(a) + '.' + self.PixelFormat, image,
                                [cv2.IMWRITE_JPEG_QUALITY, self.ImageQuailty])
                    # 拼接
                    self.stitch_part(a, numberw, numberh, image)
                    # 细胞推理
                    results = self.model(image, device='cuda:0', conf=0.25, iou=0.75, classes=[0, 1])
                    # 细菌推理
                    result_boxes_bacteria = []
                    result_cls_bacteria = []
                    xylist, images = self.sub_image(image)

                    results_bacteria = self.model_bacteria(images, device='cuda:0', imgsz=640,
                                                           show_labels=False,
                                                           line_width=1,
                                                           conf=0.353, verbose=False,
                                                           agnostic_nms=True)
                    for results_bacteria_part, xy in zip(results_bacteria, xylist):
                        result_cls_bacteria.extend([int(x) for x in results_bacteria_part.boxes.cls.tolist()])
                        for box in results_bacteria_part.boxes:
                            box_list = box.xyxy[0].tolist()
                            box_list[0] = box_list[0] + xy[0]
                            box_list[1] = box_list[1] + xy[1]
                            box_list[2] = box_list[2] + xy[0]
                            box_list[3] = box_list[3] + xy[1]
                            result_boxes_bacteria.append(box_list)

                    # 保存结果
                    data.Save_data_3(Graph_class, PP_code, ID, ZPoint, a, Point_XY, timesave, results, point_xy_real,
                                     result_boxes_bacteria, result_cls_bacteria, multiple, self.PixelFormat)
                    # 推荐结果
                    with torch.no_grad():
                        self.image_ec = self.update_tensor(self.image_ec, Point_XY,
                                                           sum(1 for x in results[0].boxes.cls.tolist() if x == 1))
                        self.image_wbc = self.update_tensor(self.image_wbc, Point_XY,
                                                            sum(1 for x in results[0].boxes.cls.tolist() if x == 0))
                        self.image_bacteria = self.update_tensor(self.image_bacteria, Point_XY,
                                                                 sum(1 for x in result_cls_bacteria if x == 0))
                    if a == numberw * numberh:
                        self.image_ec = self.image_ec.cpu().numpy()
                        self.image_wbc = self.image_wbc.cpu().numpy()
                        self.image_bacteria = self.image_bacteria.cpu().numpy()
                        # 检查文件夹路径是否存在
                        data_path_save = 'data\\' + ID
                        folder_path = os.path.join(data_path_save)
                        if not os.path.exists(folder_path):
                            # 如果路径不存在，则创建文件夹
                            os.makedirs(folder_path)
                        list_window = []
                        list_window_bacteria = []
                        list_window_wbc = []
                        list_window_ec = []
                        number_list_window_bacteria = []
                        # 窗口大小
                        window_size = (2, 2)
                        # 滑动窗口并计算每个窗口的灰度值综合
                        for row in range(0, self.image_wbc.shape[0] - window_size[0] + 1, 2):
                            for col in range(0, self.image_wbc.shape[1] - window_size[1] + 1, 2):
                                # 获取当前窗口
                                window_wbc = self.image_wbc[row:row + window_size[0], col:col + window_size[1]]
                                window_ec = self.image_ec[row:row + window_size[0], col:col + window_size[1]]
                                window_bacteria = self.image_bacteria[row:row + window_size[0],
                                                  col:col + window_size[1]]
                                # 计算窗口的细胞数综合
                                sum_wbc = window_wbc.sum()
                                sum_ec = window_ec.sum()
                                sum_bacteria = window_bacteria.sum()
                                if len(list_window) < 20:
                                    list_window.append([row * numberw + col + 1, row * numberw + col + 2,
                                                        (row + 1) * numberw + col + 1, (row + 1) * numberw + col + 2])
                                    list_window_bacteria.append([row * numberw + col + 1, row * numberw + col + 2,
                                                                 (row + 1) * numberw + col + 1,
                                                                 (row + 1) * numberw + col + 2])
                                    list_window_wbc.append(sum_wbc)
                                    list_window_ec.append(sum_ec)
                                    number_list_window_bacteria.append(sum_bacteria)
                                else:
                                    if sum_wbc > min(list_window_wbc):
                                        index = list_window_wbc.index(min(list_window_wbc))
                                        list_window[index] = [row * numberw + col + 1, row * numberw + col + 2,
                                                              (row + 1) * numberw + col + 1,
                                                              (row + 1) * numberw + col + 2]
                                        list_window_wbc[index] = sum_wbc
                                        list_window_ec[index] = sum_ec
                                    if sum_bacteria > min(number_list_window_bacteria):
                                        index = number_list_window_bacteria.index(min(number_list_window_bacteria))
                                        list_window_bacteria[index] = [row * numberw + col + 1, row * numberw + col + 2,
                                                                       (row + 1) * numberw + col + 1,
                                                                       (row + 1) * numberw + col + 2]
                                        number_list_window_bacteria[index] = sum_bacteria

                        # wbc
                        mean_wbc = sum(list_window_wbc) / len(list_window_wbc)
                        median_wbc = statistics.median(list_window_wbc)
                        # ec
                        mean_ec = sum(list_window_ec) / len(list_window_ec)
                        median_ec = statistics.median(list_window_ec)
                        # 细菌
                        mean_bacteria = sum(number_list_window_bacteria) / len(number_list_window_bacteria)
                        median_bacteria = statistics.median(number_list_window_bacteria)
                        data_ = {'细胞推荐视野': list_window, '细菌推荐视野': list_window_bacteria,
                                 '白细胞平均数': mean_wbc, '白细胞中位数': median_wbc, '上皮细胞平均数': mean_ec,
                                 '上皮细胞中位数': median_ec, '细菌平均数': mean_bacteria,
                                 '细菌中位数': median_bacteria}
                        Graph_class.set_attr_node(PP_code, data_)
                        Graph_class.save('./data/' + ID + '/' + ID + '.dat')
                        img = cv2.vconcat(self.image_stitch_all)

                        ok.emit(ID, list_window, list_window_bacteria, numberw, numberh, mean_wbc, median_wbc, mean_ec,
                                median_ec, mean_bacteria, median_bacteria, img)
                        cv2.imwrite(path_save + '\\' + ID + '.jpg', img,
                                    [cv2.IMWRITE_JPEG_QUALITY, 80])
                        self.image_stitch_all = []
                self.queue.task_done()

            except:
                pass

    def enqueue(self, image, Graph_class, PP_code, ID, ZPoint, a, Point_XY, timesave, path_save,
                numberw, numberh, ok, point_xy_real, multiple):
        try:
            self.queue.put_nowait(
                [image, Graph_class, PP_code, ID, ZPoint, a, Point_XY, timesave, path_save,
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

    def update_tensor(self, tensor, point_xy, value):
        with torch.no_grad():
            new_tensor = tensor.clone()  # 克隆原始张量
            new_tensor[point_xy[0], point_xy[1]] = value  # 更新指定位置的值
            return new_tensor

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
