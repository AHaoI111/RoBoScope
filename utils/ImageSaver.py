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



class Image_Saver:
    # 信号
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
        self.width = None
        self.height = None
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
                [Img_Number,image, UUID, multiple, base_flag, points_xy_position, stitch_flag, is_end, path_save] = self.queue.get(
                    timeout=0.1)
                if image is not None:
                    # 判断是否需要平场矫正
                    bgr_image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                    if self.correction_model != 0:
                        base_img = self.base_img_low if base_flag == 'low' else self.base_img_high
                        if base_img is not None:
                            bgr_image = self.flat_field_correction(bgr_image, base_img)

                    # 保存
                    multiple_str = str(multiple) + 'X'
                    name = f"{UUID}_{multiple_str}_{Img_Number}.{self.PixelFormat}"

                    # 根据不同的图片格式设置编码参数
                    if self.PixelFormat.lower() == 'jpg':
                        encode_params = [cv2.IMWRITE_JPEG_QUALITY, self.ImageQuailty]
                    elif self.PixelFormat.lower() == 'png':
                        encode_params = [cv2.IMWRITE_PNG_COMPRESSION,
                                         9 - self.ImageQuailty // 10]  # PNG uses compression level 0-9
                    elif self.PixelFormat.lower() == 'bmp':
                        encode_params = []
                    else:
                        encode_params = []

                    # 编码并保存图像
                    encoded_image = cv2.imencode('.' + self.PixelFormat, bgr_image, encode_params)[1]
                    encoded_image.tofile(os.path.join(path_save, name))

                    # 判断是否拼接
                    if stitch_flag:
                        if is_end:
                            self.stitch_part(points_xy_position, bgr_image)
                            cv_image = np.array(self.image_stitch_all)
                            # opencv_image = cv2.cvtColor(cv_image, cv2.COLOR_RGB2BGR)
                            name_stitch_img = UUID + "_slide.jpg"
                            encoded_stitch_image = cv2.imencode('.jpg', cv_image, [cv2.IMWRITE_JPEG_QUALITY, 100])[
                                1]
                            encoded_stitch_image.tofile(os.path.join(path_save, name_stitch_img))
                            self.image_stitch_flag = True
                        else:
                            self.stitch_part(points_xy_position, bgr_image)
                # 标记任务完成
                self.queue.task_done()
            except Exception as e:
                pass

    def enqueue(self, Img_Number,image, UUID, multiple, base_flag, points_xy_position, stitch_flag, is_end, path_save):
        """
        将图像保存任务添加到队列中。
        """
        try:
            self.queue.put_nowait(
                [Img_Number,image, UUID, multiple, base_flag, points_xy_position, stitch_flag, is_end, path_save])
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

    def clear_stitch_all(self):
        """
        清除全局拼接图像。
        """
        self.image_stitch_all = None
        self.image_stitch_flag = False
