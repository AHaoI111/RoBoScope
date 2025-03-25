# -*- encoding: utf-8 -*-
"""
@Description:
显微镜扫描
@File    :   Scan.py
@Time    :   2025/03/06
@Author  :   Li QingHao
@Version :   2.0
@Time_END :  最后修改时间：
@Developers_END :  最后修改作者：
"""

import os
import time
from datetime import datetime
import cv2
import numpy
from PIL import Image
from PySide6 import QtCore
from PySide6.QtCore import Signal

from utils import Route
from utils import focus
import math

from concurrent.futures import ThreadPoolExecutor
from queue import Queue


def get_time_2():
    # 获取当前系统时间
    current_time = datetime.now()
    # 格式化时间显示
    year = current_time.strftime("%Y")
    month = current_time.strftime("%m")
    day = current_time.strftime("%d")
    return year, month, day


class Scanning(QtCore.QObject):
    # 信号
    updata_puzzle = Signal(int, list, numpy.ndarray)  # 用于更新拼图进展的信号
    updata_focus = Signal(numpy.ndarray)  # 用于更新对焦图像的信号

    updata_rectangle_clear = Signal()  # 用于清空的信号
    updata_point_rectangle = Signal(list)  # 用于更新绘图的信号
    draw_grid = Signal(list)
    draw_point = Signal(list)

    updata_textEdit_log_microscope = Signal(str)  # 用于更新文本编辑器日志的信号
    write_log_microscope = Signal(int, str)  # 用于写入日志的信号

    def __init__(self, action_microscope, Image_Saver, Message_Woker):
        super().__init__()

        self.number = 20
        self.step = 0.003
        self.action_microscope = action_microscope
        self.Image_Saver = Image_Saver
        self.Message_Woker = Message_Woker
        self.flage_run = True  # 用来停止扫描
        self.flag = True  # 用来暂停扫描
        self.request = None
        self.points_xy_real_high = []
        self.low_2_high_method = None
        self.request_flag = True
        self.threshold_fcous = 0.85

    def pause(self):
        self.flag = False

    def AutofocusWorker(self, start, get_img, is_first):
        self.focus_score = [0] * self.number
        self.focus_img = [0] * self.number
        self.pos_z_all = [start] * self.number
        self.max_focus_img = None
        # 初始化队列
        self.queue = Queue(self.number)
        # 初始化状态变量
        self.stopped = False  # 停止标志
        self.Autofocus_flag = True
        self.max_pos = start
        self.executor = ThreadPoolExecutor(max_workers=3)
        self.start_processing()
        for i in range(self.number):
            self.action_microscope.microscope_move_z_to(start + self.step * i)
            img = get_img()
            self.updata_focus.emit(img)
            self.enqueue(is_first, i, img, (self.number - 1), start + self.step * i)
            if self.Autofocus_flag:
                pass
            else:
                break
        time_start = time.time()  # 开始计时
        while self.Autofocus_flag:
            time_end = time.time()  # 结束计时
            time_c = time_end - time_start  # 等待所花时间
            if time_c > 5:
                self.Autofocus_flag = False
            time.sleep(0.005)
        self.focus_img = None
        return self.max_pos, self.max_focus_score_img

    def process_queue(self):
        """
        持续处理队列中的图像任务。
        """
        while not self.stopped:
            try:
                # 从队列中获取任务数据
                [is_first, i, image, count, posz] = self.queue.get(timeout=0.1)
                if image is not None:
                    if is_first:
                        definition = focus.Sharpness_sobel(image)
                    else:
                        definition = focus.Sharpness_chromosome(image)
                    self.focus_img[i] = image
                    self.focus_score[i] = definition
                    self.pos_z_all[i] = posz
                    if definition < max(self.focus_score) * self.threshold_fcous:
                        index = self.focus_score.index(max(self.focus_score))
                        if i > index:
                            self.stopped = True
                            self.max_pos = self.pos_z_all[self.focus_score.index(max(self.focus_score))]
                            self.Autofocus_flag = False
                            self.max_focus_score_img = self.focus_img[self.focus_score.index(max(self.focus_score))]
                    if i == count:
                        self.stopped = True
                        self.max_pos = self.pos_z_all[self.focus_score.index(max(self.focus_score))]
                        self.Autofocus_flag = False
                        self.max_focus_score_img = self.focus_img[self.focus_score.index(max(self.focus_score))]
                self.queue.task_done()
            except Exception as e:
                pass

    def enqueue(self, is_first, i, image, count, posz):
        """
        将图像保存任务添加到队列中。
        """
        try:
            self.queue.put_nowait(
                [is_first, i, image, count, posz])
        except:
            print('imageSaver queue is full, image discarded')

    def start_processing(self):
        """
        启动线程池执行队列中的任务。
        """
        for _ in range(3):
            self.executor.submit(self.process_queue)

    # 第一种扫描模式（中心点对焦）
    def Scan_Mode_one(self, zpos_start, points_xy_positions, points_xy_real,
                      get_image_camera, UUID, path_save, save_flag, multiple, stitch_flag, base_flag, task_info):
        self.updata_textEdit_log_microscope.emit('中心点对焦扫描启动')
        self.write_log_microscope.emit(0, '中心点对焦扫描启动')
        Img_Number = 1
        zpos, img = self.AutofocusWorker(zpos_start, get_image_camera, True)
        if img is None:
            return 0
        self.updata_focus.emit(img)
        self.action_microscope.microscope_move_z_to(zpos)
        for points_xy_position, Point_XY in zip(points_xy_positions, points_xy_real):
            if self.flag:
                pass
            else:
                while not self.flag:
                    time.sleep(0.1)
            if self.flage_run:
                pass
            else:
                self.updata_textEdit_log_microscope.emit('显微镜平台扫描停止')
                self.write_log_microscope.emit(1, '显微镜平台扫描停止')
                break
            # 由于是竖着放置玻片，所以需要将x轴和y轴交换Point_XY所以互换
            self.action_microscope.microscope_move_x_to(Point_XY[0])
            self.action_microscope.microscope_move_y_to(Point_XY[1])
            img = get_image_camera()
            self.updata_focus.emit(img)
            self.updata_puzzle.emit(Img_Number, points_xy_position, img)
            if Img_Number == len(points_xy_real):
                is_end = True
            else:
                is_end = False
            if save_flag:
                self.Image_Saver.enqueue(Img_Number, img, UUID, multiple, base_flag, points_xy_position, stitch_flag,
                                         is_end,
                                         path_save)
            if task_info['Network'] and task_info['recommend_view_source'] != 'slide_pic':
                self.Message_Woker.enqueue(img, UUID, multiple, base_flag, points_xy_position, is_end, Img_Number,
                                           path_save,
                                           task_info)
            elif task_info['Network'] and base_flag == 'high':
                self.Message_Woker.enqueue(img, UUID, multiple, base_flag, points_xy_position, is_end, Img_Number,
                                           path_save,
                                           task_info)
            self.draw_point.emit(points_xy_position)
            Img_Number = Img_Number + 1
        return 1

    # 第二种扫描模式（4点对焦）
    def Scan_Mode_two(self, zpos_start, points_4, points_xy_positions, points_xy_real,
                      get_image_camera, UUID, path_save, save_flag, multiple, stitch_flag, base_flag, task_info):
        self.updata_textEdit_log_microscope.emit('4点对焦扫描启动')
        self.write_log_microscope.emit(0, '4点对焦扫描启动')
        zpos_4 = []
        Img_Number = 1
        for point in points_4:
            if self.flag:
                pass
            else:
                while not self.flag:
                    time.sleep(0.1)
            if self.flage_run:
                pass
            else:
                self.updata_textEdit_log_microscope.emit('显微镜平台扫描停止')
                self.write_log_microscope.emit(1, '显微镜平台扫描停止')
                break
            self.action_microscope.microscope_move_x_to(point[0])
            self.action_microscope.microscope_move_y_to(point[1])
            self.action_microscope.microscope_move_z_to(zpos_start)
            zpos, img = self.AutofocusWorker(zpos_start, get_image_camera, True)
            if img is None:
                return 0
            self.updata_focus.emit(img)
            zpos_4.append(zpos)
        for points_xy_position, Point_XY in zip(points_xy_positions, points_xy_real):
            if self.flag:
                pass
            else:
                while not self.flag:
                    time.sleep(0.1)
            if self.flage_run:
                pass
            else:
                self.updata_textEdit_log_microscope.emit('显微镜平台扫描停止')
                self.write_log_microscope.emit(1, '显微镜平台扫描停止')
                break
            # 由于是竖着放置玻片，所以需要将x轴和y轴交换Point_XY所以互换

            self.action_microscope.microscope_move_x_to(Point_XY[0])
            self.action_microscope.microscope_move_y_to(Point_XY[1])
            if Point_XY[2] == 1:
                self.action_microscope.microscope_move_z_to(zpos_4[0])
                zpos = zpos_4[0]
            elif Point_XY[2] == 2:
                self.action_microscope.microscope_move_z_to(zpos_4[1])
                zpos = zpos_4[1]
            elif Point_XY[2] == 3:
                self.action_microscope.microscope_move_z_to(zpos_4[2])
                zpos = zpos_4[2]
            elif Point_XY[2] == 4:
                self.action_microscope.microscope_move_z_to(zpos_4[3])
                zpos = zpos_4[3]
            img = get_image_camera()
            self.updata_focus.emit(img)
            self.updata_puzzle.emit(Img_Number, points_xy_position, img)
            if Img_Number == len(points_xy_real):
                is_end = True
            else:
                is_end = False
            if save_flag:
                self.Image_Saver.enqueue(Img_Number, img, UUID, multiple, base_flag, points_xy_position, stitch_flag,
                                         is_end,
                                         path_save)
            if task_info['Network'] and task_info['recommend_view_source'] != 'slide_pic':
                self.Message_Woker.enqueue(img, UUID, multiple, base_flag, points_xy_position, is_end, Img_Number,
                                           path_save,
                                           task_info)
            elif task_info['Network'] and base_flag == 'high':
                self.Message_Woker.enqueue(img, UUID, multiple, base_flag, points_xy_position, is_end, Img_Number,
                                           path_save,
                                           task_info)
            self.draw_point.emit(points_xy_position)
            Img_Number = Img_Number + 1
        return 1

    # 第三种扫描模式（隔点对焦）
    def Scan_Mode_three(self, zpos_start, points_xy_positions, points_xy_real,
                        get_image_camera, Focus_Gap, UUID, path_save, save_flag, multiple, stitch_flag, base_flag,
                        task_info):
        self.updata_textEdit_log_microscope.emit('隔点对焦扫描启动')
        self.write_log_microscope.emit(0, '隔点对焦扫描启动')
        zpos = zpos_start
        Img_Number = 1
        for points_xy_position, Point_XY in zip(points_xy_positions, points_xy_real):
            if self.flag:
                pass
            else:
                while not self.flag:
                    time.sleep(0.1)
            if self.flage_run:
                pass
            else:
                self.updata_textEdit_log_microscope.emit('显微镜平台扫描停止')
                self.write_log_microscope.emit(1, '显微镜平台扫描停止')
                break
            if Img_Number == 1:
                if base_flag == 'low':
                    self.action_microscope.microscope_move_x_to(task_info['center_x_low'])
                    self.action_microscope.microscope_move_y_to(task_info['center_y_low'])
                    self.action_microscope.microscope_move_z_to(zpos_start)
                    zpos, img = self.AutofocusWorker(zpos_start, get_image_camera, True)
                    self.number = 20
                    self.step = 0.004
                elif base_flag == 'high':
                    self.action_microscope.microscope_move_x_to(task_info['center_x_high'])
                    self.action_microscope.microscope_move_y_to(task_info['center_y_high'])
                    self.action_microscope.microscope_move_z_to(zpos_start)
                    zpos, img = self.AutofocusWorker(zpos_start, get_image_camera, True)
                    self.number = 30
                    self.step = 0.0005
                elif base_flag == 'only':
                    self.action_microscope.microscope_move_x_to(task_info['center_x'])
                    self.action_microscope.microscope_move_y_to(task_info['center_y'])
                    self.action_microscope.microscope_move_z_to(zpos_start)
                    zpos, img = self.AutofocusWorker(zpos_start, get_image_camera, True)

            self.action_microscope.microscope_move_x_to(Point_XY[0])
            self.action_microscope.microscope_move_y_to(Point_XY[1])

            if Img_Number == 1:
                if base_flag == 'high':
                    zpos, img = self.AutofocusWorker(zpos - 0.0075, get_image_camera, False)
                elif base_flag == 'low':
                    zpos, img = self.AutofocusWorker(zpos - 0.04, get_image_camera, False)
                if img is None:
                    return 0
                self.updata_focus.emit(img)
                self.updata_puzzle.emit(Img_Number, points_xy_position, img)
            elif Img_Number % Focus_Gap == 0:
                if base_flag == 'high':
                    zpos, img = self.AutofocusWorker(zpos - 0.0075, get_image_camera, False)
                elif base_flag == 'low':
                    zpos, img = self.AutofocusWorker(zpos - 0.04, get_image_camera, False)
                if img is None:
                    return 0
                self.updata_focus.emit(img)
                self.updata_puzzle.emit(Img_Number, points_xy_position, img)
            else:
                self.action_microscope.microscope_move_z_to(zpos)
                img = get_image_camera()
                self.updata_focus.emit(img)
                self.updata_puzzle.emit(Img_Number, points_xy_position, img)

            if Img_Number == len(points_xy_real):
                is_end = True
            else:
                is_end = False
            if save_flag:
                self.Image_Saver.enqueue(Img_Number, img, UUID, multiple, base_flag, points_xy_position, stitch_flag,
                                         is_end,
                                         path_save)
            if task_info['Network'] and task_info['recommend_view_source'] != 'slide_pic':
                self.Message_Woker.enqueue(img, UUID, multiple, base_flag, points_xy_position, is_end, Img_Number,
                                           path_save,
                                           task_info)
            elif task_info['Network'] and base_flag == 'high':
                self.Message_Woker.enqueue(img, UUID, multiple, base_flag, points_xy_position, is_end, Img_Number,
                                           path_save,
                                           task_info)
            self.draw_point.emit(points_xy_position)
            Img_Number = Img_Number + 1
        return 1

    # 染色体扫描方式
    def low_for_high_Scan_Mode_three_box(self, zpos_start, points_xy_real,
                                         get_image_camera, Focus_Gap, UUID, path_save, save_flag, multiple, stitch_flag,
                                         base_flag, task_info):
        self.updata_textEdit_log_microscope.emit('染色体扫描方式启动')
        self.write_log_microscope.emit(0, '染色体扫描方式启动')
        zpos = zpos_start
        Img_Number = 1
        for Point_XY in points_xy_real:
            if Point_XY[0] < 60 and Point_XY[1] < 60:
                if self.flag:
                    pass
                else:
                    while not self.flag:
                        time.sleep(0.1)
                if self.flage_run:
                    pass
                else:
                    self.updata_textEdit_log_microscope.emit('显微镜平台扫描停止')
                    self.write_log_microscope.emit(1, '显微镜平台扫描停止')
                    break
                self.action_microscope.microscope_move_x_to(Point_XY[0])
                self.action_microscope.microscope_move_y_to(Point_XY[1])
                if Img_Number == 1:
                    zpos, img = self.AutofocusWorker(zpos_start, get_image_camera, True)
                    if img is None:
                        return 0
                    self.updata_focus.emit(img)
                    self.number = 20
                    self.step = 0.0005
                    zpos, img = self.AutofocusWorker(zpos - 0.005, get_image_camera, False)
                    self.updata_focus.emit(img)
                elif Img_Number % Focus_Gap == 0:
                    zpos, img = self.AutofocusWorker(zpos - 0.005, get_image_camera, False)
                    self.updata_focus.emit(img)
                else:
                    self.action_microscope.microscope_move_z_to(zpos)
                    img = get_image_camera()
                    self.updata_focus.emit(img)

                if Img_Number == len(points_xy_real):
                    is_end = True
                else:
                    is_end = False
                if save_flag:
                    self.Image_Saver.enqueue(Img_Number, img, UUID, multiple, base_flag, [0, Img_Number], stitch_flag,
                                             is_end,
                                             path_save)
                if task_info['Network']:
                    self.Message_Woker.enqueue(img, UUID, multiple, base_flag, [0, Img_Number], is_end, Img_Number,
                                               path_save,
                                               task_info)
                Img_Number = Img_Number + 1
            else:
                self.write_log_microscope.emit(0, '坐标超出设定范围')
                if Img_Number == len(points_xy_real) * len(points_xy_real_center):
                    is_end = True
                    self.Message_Woker.enqueue(None, UUID, multiple, base_flag, [0, Img_Number], is_end,
                                               Img_Number,
                                               path_save,
                                               task_info)
                Img_Number = Img_Number + 1
        return 1

    # 微生物扫描方式
    def low_for_high_Scan_Mode_three_view_filed(self, zpos_start, points_xy_real_center,
                                                get_image_camera, Focus_Gap, UUID, path_save, save_flag, multiple,
                                                stitch_flag,
                                                base_flag, task_info):
        self.updata_textEdit_log_microscope.emit('微生物扫描方式启动')
        self.write_log_microscope.emit(0, '微生物扫描方式启动')
        Img_Number = 1
        for i in range(len(points_xy_real_center)):
            z_pos = zpos_start
            # 到初始点
            # self.action_microscope.microscope_move_z_to(z_pos)
            img = self.action_microscope.get_image_camera_high()
            if len(img.shape) == 2:
                h, w = img.shape
            else:
                h, w, _ = img.shape
            # 根据中心点重新路径

            points_4, points_xy, points_xy_real, number_x, number_y = Route.get_route(img,
                                                                                      points_xy_real_center[i][0],
                                                                                      points_xy_real_center[i][1],
                                                                                      math.ceil(math.sqrt(
                                                                                          task_info['max_views'])) * w *
                                                                                      task_info['calibration_high'],
                                                                                      math.ceil(math.sqrt(
                                                                                          task_info['max_views'])) * h *
                                                                                      task_info['calibration_high'],
                                                                                      task_info['calibration_high'])
            for Point_XY in points_xy_real:
                if Point_XY[0] < 60 and Point_XY[1] < 60:
                    if self.flag:
                        pass
                    else:
                        while not self.flag:
                            time.sleep(0.1)
                    if self.flage_run:
                        pass
                    else:
                        self.updata_textEdit_log_microscope.emit('显微镜平台扫描停止')
                        self.write_log_microscope.emit(1, '显微镜平台扫描停止')
                        break
                    self.action_microscope.microscope_move_x_to(Point_XY[0])
                    self.action_microscope.microscope_move_y_to(Point_XY[1])
                    if Img_Number == 1 or (Img_Number - 1) % len(points_xy_real) == 0:
                        self.number = task_info['focu_number_high']
                        self.step = task_info['focu_size_high']
                        zpos, img = self.AutofocusWorker(zpos_start, get_image_camera, True)
                        if img is None:
                            return 0
                        self.updata_focus.emit(img)
                        self.number = 20
                        self.step = 0.0005
                    elif Img_Number % Focus_Gap == 0:
                        zpos, img = self.AutofocusWorker(zpos - 0.005, get_image_camera, False)
                        self.updata_focus.emit(img)
                    else:
                        self.action_microscope.microscope_move_z_to(z_pos)
                        img = get_image_camera()
                        self.updata_focus.emit(img)
                    if Img_Number == len(points_xy_real) * len(points_xy_real_center):
                        is_end = True
                    else:
                        is_end = False
                    if save_flag:
                        self.Image_Saver.enqueue(Img_Number, img, UUID, multiple, base_flag, [Point_XY[0], Point_XY[1]],
                                                 stitch_flag, is_end,
                                                 path_save)
                    if task_info['Network']:
                        self.Message_Woker.enqueue(img, UUID, multiple, base_flag, [Point_XY[0], Point_XY[1]], is_end,
                                                   Img_Number,
                                                   path_save,
                                                   task_info)
                    Img_Number = Img_Number + 1
                else:
                    self.write_log_microscope.emit(0, '坐标超出设定范围')
                    if Img_Number == len(points_xy_real) * len(points_xy_real_center):
                        is_end = True
                        self.Message_Woker.enqueue(None, UUID, multiple, base_flag, [Point_XY[0], Point_XY[1]], is_end,
                                                   Img_Number,
                                                   path_save,
                                                   task_info)
                    Img_Number = Img_Number + 1
        return 1

    def start(self, Taskinfo, slide_id, label_img, use_pump):
        """
                启动扫描程序，控制显微镜进行图像采集和处理。
                :param IDall: 全部标识符，用于更广泛的唯一标识扫描任务
                """
        self.flage_run = True
        time_start = time.time()  # 开始计时
        try:
            if not Taskinfo:
                self.updata_textEdit_log_microscope.emit('扫描参数未正确配置，扫描结束')
                self.write_log_microscope.emit(1, '扫描参数未正确配置，扫描结束')
            else:
                self.updata_textEdit_log_microscope.emit('开始扫描')
                self.write_log_microscope.emit(0, '开始扫描')
                if Taskinfo['sys'] == 'single':
                    # 单镜头系统
                    focu_number = Taskinfo['focu_number']
                    step = Taskinfo['focu_size']
                    center_x = Taskinfo['center_x']
                    center_y = Taskinfo['center_y']
                    zpos_start = Taskinfo['zpos_start']
                    region_w = Taskinfo['region_w']
                    region_h = Taskinfo['region_h']
                    calibration = Taskinfo['calibration']
                    ImageStitchSize = Taskinfo['ImageStitchSize']
                    fcous_Gap = Taskinfo['fcous_Gap']
                    multiple = Taskinfo['multiple']

                    self.number = focu_number
                    self.step = step
                    # 移动到预设位置
                    self.action_microscope.microscope_move_y_to(center_y)
                    self.action_microscope.microscope_move_x_to(center_x)
                    self.action_microscope.microscope_move_z_to(zpos_start)
                    self.action_microscope.set_only_light()
                    self.action_microscope.turn_on_light()
                    img = self.action_microscope.get_image_camera_one()
                    # 路径
                    points_4, points_xy, points_xy_real, number_x, number_y = Route.get_route(img,
                                                                                              center_x,
                                                                                              center_y,
                                                                                              region_w,
                                                                                              region_h,
                                                                                              calibration)
                    # 清空点位
                    self.updata_rectangle_clear.emit()
                    self.updata_point_rectangle.emit([region_w, region_h])
                    self.draw_grid.emit([number_x, number_y])
                    self.updata_textEdit_log_microscope.emit('扫描任务玻片ID为：' + str(slide_id))
                    self.Image_Saver.image_stitch_all = Image.new("RGB",
                                                                  (number_y * ImageStitchSize,
                                                                   number_x * ImageStitchSize))
                    if Taskinfo['pre_request_flag']:
                        save_flag = False
                        path_save = None
                    else:
                        year, month, day = get_time_2()
                        # 检查文件夹路径是否存在
                        path_save = Taskinfo[
                                        'savepath'] + '/' + year + '/' + month + '/' + day + '/' + Taskinfo[
                                        'task_id'] + '/' + str(slide_id)
                        folder_path = os.path.join(path_save)
                        if not os.path.exists(folder_path):
                            # 如果路径不存在，则创建文件夹
                            os.makedirs(folder_path)
                        name = slide_id + '_label.png'
                        cv2.imencode('.png', cv2.cvtColor(label_img, cv2.COLOR_RGB2BGR))[1].tofile(
                            os.path.join(path_save, name))
                        save_flag = True

                    if multiple >= 20:
                        base_flag = 'high'
                    else:
                        base_flag = 'low'
                    if Taskinfo['FocusMode'] == 1:
                        # 快速模式1
                        result = self.Scan_Mode_one(zpos_start, points_xy, points_xy_real,
                                                    self.action_microscope.get_image_camera_one, slide_id, path_save,
                                                    save_flag, multiple, True, base_flag, Taskinfo)
                        if result == 0:
                            self.updata_textEdit_log_microscope.emit('对焦失败')
                    elif Taskinfo['FocusMode'] == 2:
                        # 快速模式2
                        result = self.Scan_Mode_two(zpos_start, points_4, points_xy, points_xy_real,
                                                    self.action_microscope.get_image_camera_one, slide_id, path_save,
                                                    save_flag, multiple, True, base_flag, Taskinfo)
                        if result == 0:
                            self.updata_textEdit_log_microscope.emit('对焦失败')
                    elif Taskinfo['FocusMode'] == 3:
                        # 快速模式3
                        result = self.Scan_Mode_three(zpos_start, points_xy, points_xy_real,
                                                      self.action_microscope.get_image_camera_one, fcous_Gap, slide_id,
                                                      path_save, save_flag, multiple, True, base_flag, Taskinfo)
                        if result == 0:
                            self.updata_textEdit_log_microscope.emit('对焦失败')
                elif Taskinfo['sys'] == 'double':
                    # 双镜头系统
                    if Taskinfo['scanmode']:
                        # 启用低倍预扫，高倍精准扫描
                        focu_number_low = Taskinfo['focu_number_low']
                        step_low = Taskinfo['focu_size_low']
                        focu_number_high = Taskinfo['focu_number_high']
                        step_high = Taskinfo['focu_size_high']
                        center_x_low = Taskinfo['center_x_low']
                        center_y_low = Taskinfo['center_y_low']
                        center_x_high = Taskinfo['center_x_high']
                        center_y_high = Taskinfo['center_y_high']
                        zpos_start_high = Taskinfo['zpos_start_high']
                        zpos_start_low = Taskinfo['zpos_start_low']
                        region_w_low = Taskinfo['region_w_low']
                        region_h_low = Taskinfo['region_h_low']
                        region_w_high = Taskinfo['region_w_high']
                        region_h_high = Taskinfo['region_h_high']
                        calibration_high = Taskinfo['calibration_high']
                        calibration_low = Taskinfo['calibration_low']
                        ImageStitchSize = Taskinfo['ImageStitchSize']
                        fcous_Gap_low = Taskinfo['fcous_Gap_low']
                        fcous_Gap_high = Taskinfo['fcous_Gap_high']
                        lens_gap_x = Taskinfo['lens_gap_x']
                        lens_gap_y = Taskinfo['lens_gap_y']
                        Taskinfo['pre_request_flag'] = False
                        Multiple_low = Taskinfo['Multiple_low']
                        Multiple_high = Taskinfo['Multiple_high']

                        self.number = focu_number_low
                        self.step = step_low

                        # 移动到预设位置
                        self.request_flag = True
                        self.low_2_high_method = None
                        self.points_xy_real_high = []
                        self.action_microscope.microscope_move_y_to(center_y_low)
                        self.action_microscope.microscope_move_x_to(center_x_low)
                        self.action_microscope.microscope_move_z_to(zpos_start_low)
                        #
                        self.action_microscope.set_low_light()
                        self.action_microscope.turn_on_light()
                        img = self.action_microscope.get_image_camera_low()
                        if len(img.shape) == 2:
                            h, w = img.shape
                        else:
                            h, w, _ = img.shape
                        # 路径
                        points_4, points_xy, points_xy_real, number_x, number_y = Route.get_route(img,
                                                                                                  center_x_low,
                                                                                                  center_y_low,
                                                                                                  region_w_low,
                                                                                                  region_h_low,
                                                                                                  calibration_low)
                        self.updata_rectangle_clear.emit()
                        self.updata_point_rectangle.emit([region_w_low, region_h_low])
                        self.draw_grid.emit([number_x, number_y])
                        self.updata_textEdit_log_microscope.emit(
                            '扫描任务玻片ID为：' + str(slide_id))
                        self.Image_Saver.image_stitch_all = Image.new("RGB",
                                                                      (number_y * ImageStitchSize,
                                                                       number_x * ImageStitchSize))
                        # 检查文件夹路径是否存在
                        if Taskinfo['pre_request_flag']:
                            save_flag = False
                            path_save = None
                        else:
                            year, month, day = get_time_2()
                            # 检查文件夹路径是否存在
                            path_save = Taskinfo[
                                            'savepath'] + '/' + year + '/' + month + '/' + day + '/' + Taskinfo[
                                            'task_id'] + '/' + str(slide_id)
                            folder_path = os.path.join(path_save)
                            if not os.path.exists(folder_path):
                                # 如果路径不存在，则创建文件夹
                                os.makedirs(folder_path)
                            name = slide_id + '_label.png'
                            cv2.imencode('.png', cv2.cvtColor(label_img, cv2.COLOR_RGB2BGR))[1].tofile(
                                os.path.join(path_save, name))
                            save_flag = True
                        Taskinfo['flag_create_view'] = False

                        if Taskinfo['FocusMode_low'] == 1:
                            # 快速模式1
                            result = self.Scan_Mode_one(zpos_start_low, points_xy, points_xy_real,
                                                        self.action_microscope.get_image_camera_low, slide_id,
                                                        path_save,
                                                        save_flag, Multiple_low, True, 'low', Taskinfo)
                            if result == 0:
                                self.updata_textEdit_log_microscope.emit('对焦失败')
                        elif Taskinfo['FocusMode_low'] == 2:
                            # 快速模式2
                            result = self.Scan_Mode_two(zpos_start_low, points_4, points_xy, points_xy_real,
                                                        self.action_microscope.get_image_camera_low, slide_id,
                                                        path_save,
                                                        save_flag, Multiple_low, True, 'low', Taskinfo)
                            if result == 0:
                                self.updata_textEdit_log_microscope.emit('对焦失败')
                        elif Taskinfo['FocusMode_low'] == 3:
                            # 快速模式3
                            result = self.Scan_Mode_three(zpos_start_low, points_xy, points_xy_real,
                                                          self.action_microscope.get_image_camera_low, fcous_Gap_low,
                                                          slide_id,
                                                          path_save, save_flag, Multiple_low, True, 'low', Taskinfo)
                            if result == 0:
                                self.updata_textEdit_log_microscope.emit('对焦失败')

                        self.action_microscope.turn_off_light()
                        if self.flage_run:
                            pass
                        else:
                            self.updata_textEdit_log_microscope.emit('显微镜平台扫描停止')
                            self.write_log_microscope.emit(1, '显微镜平台扫描停止')
                            return
                        # 如果是给拼接图片
                        t0 = time.time()
                        while not self.Image_Saver.image_stitch_flag:
                            time.sleep(0.005)
                            if time.time() - t0 > 10:
                                self.updata_textEdit_log_microscope.emit('等待低倍拼图完成')
                                break
                        if Taskinfo['recommend_view_source'] == 'slide_pic':
                            cv_image = numpy.array(self.Image_Saver.image_stitch_all)
                            self.Message_Woker.enqueue(cv_image, slide_id, Multiple_low, 'low',
                                                       [0, 0], True, 0, path_save, Taskinfo)
                        self.Image_Saver.clear_stitch_all()
                        # 低倍扫描完毕
                        self.action_microscope.microscope_home_z()
                        # 给出高倍需要扫描的points_xy
                        # 高倍扫描
                        Taskinfo['flag_create_view'] = True
                        self.number = focu_number_high
                        self.step = step_high
                        t0 = time.time()
                        while self.request_flag:
                            time.sleep(0.005)
                            if time.time() - t0 > 120:
                                self.updata_textEdit_log_microscope.emit('等待高倍推荐视野超时或者不合格')
                                self.points_xy_real_high = []
                                points_xy_location = []
                                break
                        if len(self.points_xy_real_high) > 0:
                            self.updata_textEdit_log_microscope.emit('开始扫描高倍推荐视野')
                            self.action_microscope.set_high_light()
                            self.action_microscope.turn_on_light()
                            # 低倍到高倍坐标转换
                            # 低倍起始点
                            # 得到高倍下的视野
                            print(self.low_2_high_method)
                            if self.low_2_high_method is None:
                                pass
                            elif self.low_2_high_method == 'box':
                                # 染色体扫描
                                # 滴油
                                if Taskinfo['pump']:
                                    self.action_microscope.microscope_move_x_to(15.226)
                                    self.action_microscope.microscope_move_y_to(21.7827)
                                    use_pump()
                                if len(self.points_xy_real_high) >= Taskinfo['max_views']:
                                    # 随机点位
                                    # self.points_xy_real_high = random.sample(self.points_xy_real_high,
                                    #                                          Taskinfo['max_views'])
                                    self.points_xy_real_high = self.points_xy_real_high[:Taskinfo['max_views']]
                                # 按照第一个元素 排序
                                self.points_xy_real_high = Route.swap_farthest_with_first(self.points_xy_real_high)
                                self.points_xy_real_high = Route.sort_by_closeness(self.points_xy_real_high)
                                self.write_log_microscope.emit(0, '高倍推荐视野:' + str(self.points_xy_real_high))
                                result = self.low_for_high_Scan_Mode_three_box(zpos_start_high,
                                                                               self.points_xy_real_high,
                                                                               self.action_microscope.get_image_camera_high,
                                                                               1, slide_id, path_save,
                                                                               save_flag, Multiple_high, False, 'high',
                                                                               Taskinfo)
                                if result == 0:
                                    self.updata_textEdit_log_microscope.emit('对焦失败')
                            elif self.low_2_high_method == 'view_filed':
                                print(self.low_2_high_method)
                                self.write_log_microscope.emit(0, '高倍推荐视野:' + str(self.points_xy_real_high))
                                # 微生物扫描
                                print(self.points_xy_real_high)
                                if len(self.points_xy_real_high) > 0:
                                    result = self.low_for_high_Scan_Mode_three_view_filed(zpos_start_high,
                                                                                          self.points_xy_real_high,
                                                                                          self.action_microscope.get_image_camera_high,
                                                                                          1, slide_id, path_save,
                                                                                          save_flag,
                                                                                          Multiple_high, False, 'high',
                                                                                          Taskinfo)
                                    if result == 0:
                                        self.updata_textEdit_log_microscope.emit('对焦失败')

                        else:
                            self.updata_textEdit_log_microscope.emit('高倍扫描无推荐视野')
                    else:
                        if Taskinfo['scanmultiple'] == 'high':
                            focu_number = Taskinfo['focu_number_high']
                            step = Taskinfo['focu_size_high']
                            center_x_high = Taskinfo['center_x_high']
                            center_y_high = Taskinfo['center_y_high']
                            zpos_start_high = Taskinfo['zpos_start_high']
                            region_w = Taskinfo['region_w_high']
                            region_h = Taskinfo['region_h_high']
                            calibration_high = Taskinfo['calibration_high']
                            ImageStitchSize = Taskinfo['ImageStitchSize']
                            fcous_Gap = Taskinfo['fcous_Gap_high']
                            Multiple = Taskinfo['Multiple_high']
                            self.number = focu_number
                            self.step = step
                            # 移动到预设位置
                            self.action_microscope.microscope_move_y_to(center_y_high)
                            self.action_microscope.microscope_move_x_to(center_x_high)
                            self.action_microscope.microscope_move_z_to(zpos_start_high)
                            #
                            self.action_microscope.set_high_light()
                            self.action_microscope.turn_on_light()
                            img = self.action_microscope.get_image_camera_high()
                            # 路径
                            points_4, points_xy, points_xy_real, number_x, number_y = Route.get_route(
                                img,
                                center_x_high,
                                center_y_high,
                                region_w,
                                region_h,
                                calibration_high)
                            self.updata_rectangle_clear.emit()
                            self.updata_point_rectangle.emit([region_w, region_h])
                            self.draw_grid.emit([number_x, number_y])
                            self.updata_textEdit_log_microscope.emit(
                                '扫描任务玻片ID为：' + str(slide_id))
                            self.Image_Saver.image_stitch_all = Image.new("RGB",
                                                                          (number_y * ImageStitchSize,
                                                                           number_x * ImageStitchSize))
                            if Taskinfo['pre_request_flag']:
                                save_flag = False
                                path_save = None
                            else:
                                year, month, day = get_time_2()
                                # 检查文件夹路径是否存在
                                path_save = Taskinfo[
                                                'savepath'] + '/' + year + '/' + month + '/' + day + '/' + Taskinfo[
                                                'task_id'] + '/' + str(slide_id)
                                folder_path = os.path.join(path_save)
                                if not os.path.exists(folder_path):
                                    # 如果路径不存在，则创建文件夹
                                    os.makedirs(folder_path)
                                name = slide_id + '_label.png'
                                cv2.imencode('.png', cv2.cvtColor(label_img, cv2.COLOR_RGB2BGR))[1].tofile(
                                    os.path.join(path_save, name))
                                save_flag = True

                            if Taskinfo['FocusMode_high'] == 1:
                                # 快速模式1
                                result = self.Scan_Mode_one(zpos_start_high, points_xy, points_xy_real,
                                                            self.action_microscope.get_image_camera_high, slide_id,
                                                            path_save,
                                                            save_flag, Multiple, True, 'high', Taskinfo)
                                if result == 0:
                                    self.updata_textEdit_log_microscope.emit('对焦失败')
                            elif Taskinfo['FocusMode_high'] == 2:
                                # 快速模式2
                                result = self.Scan_Mode_two(zpos_start_high, points_4, points_xy, points_xy_real,
                                                            self.action_microscope.get_image_camera_high, slide_id,
                                                            path_save,
                                                            save_flag, Multiple, True, 'high', Taskinfo)
                                if result == 0:
                                    self.updata_textEdit_log_microscope.emit('对焦失败')
                            elif Taskinfo['FocusMode_high'] == 3:
                                # 快速模式3
                                result = self.Scan_Mode_three(zpos_start_high, points_xy, points_xy_real,
                                                              self.action_microscope.get_image_camera_high, fcous_Gap,
                                                              slide_id,
                                                              path_save, save_flag, Multiple, True, 'high', Taskinfo)
                                if result == 0:
                                    self.updata_textEdit_log_microscope.emit('对焦失败')

                        elif Taskinfo['scanmultiple'] == 'low':
                            focu_number = Taskinfo['focu_number_low']
                            step = Taskinfo['focu_size_low']
                            center_x_low = Taskinfo['center_x_low']
                            center_y_low = Taskinfo['center_y_low']
                            zpos_start_low = Taskinfo['zpos_start_low']
                            region_w = Taskinfo['region_w_low']
                            region_h = Taskinfo['region_h_low']
                            calibration_low = Taskinfo['calibration_low']
                            ImageStitchSize = Taskinfo['ImageStitchSize']
                            fcous_Gap = Taskinfo['fcous_Gap_low']
                            Multiple = Taskinfo['Multiple_low']
                            self.number = focu_number
                            self.step = step
                            # 移动到预设位置
                            self.action_microscope.microscope_move_y_to(center_y_low)
                            self.action_microscope.microscope_move_x_to(center_x_low)
                            self.action_microscope.microscope_move_z_to(zpos_start_low)
                            #
                            self.action_microscope.set_low_light()
                            self.action_microscope.turn_on_light()
                            img = self.action_microscope.get_image_camera_low()
                            # 路径
                            points_4, points_xy, points_xy_real, number_x, number_y = Route.get_route(
                                img,
                                center_x_low,
                                center_y_low,
                                region_w,
                                region_h,
                                calibration_low)
                            self.updata_rectangle_clear.emit()
                            self.updata_point_rectangle.emit([region_w, region_h])
                            self.draw_grid.emit([number_x, number_y])
                            self.updata_textEdit_log_microscope.emit(
                                '扫描任务玻片ID为：' + str(slide_id))
                            self.Image_Saver.image_stitch_all = Image.new("RGB",
                                                                          (number_y * ImageStitchSize,
                                                                           number_x * ImageStitchSize))
                            if Taskinfo['pre_request_flag']:
                                save_flag = False
                                path_save = None
                            else:
                                year, month, day = get_time_2()
                                # 检查文件夹路径是否存在
                                path_save = Taskinfo[
                                                'savepath'] + '/' + year + '/' + month + '/' + day + '/' + Taskinfo[
                                                'task_id'] + '/' + str(slide_id)
                                folder_path = os.path.join(path_save)
                                if not os.path.exists(folder_path):
                                    # 如果路径不存在，则创建文件夹
                                    os.makedirs(folder_path)
                                name = slide_id + '_label.png'
                                cv2.imencode('.png', cv2.cvtColor(label_img, cv2.COLOR_RGB2BGR))[1].tofile(
                                    os.path.join(path_save, name))
                                save_flag = True
                            if Taskinfo['FocusMode_low'] == 1:
                                # 快速模式1
                                result = self.Scan_Mode_one(zpos_start_low, points_xy, points_xy_real,
                                                            self.action_microscope.get_image_camera_low, slide_id,
                                                            path_save,
                                                            save_flag, Multiple, True, 'low', Taskinfo)
                                if result == 0:
                                    self.updata_textEdit_log_microscope.emit('对焦失败')
                            elif Taskinfo['FocusMode_low'] == 2:
                                # 快速模式2
                                result = self.Scan_Mode_two(zpos_start_low, points_4, points_xy, points_xy_real,
                                                            self.action_microscope.get_image_camera_low, slide_id,
                                                            path_save,
                                                            save_flag, Multiple, True, 'low', Taskinfo)
                                if result == 0:
                                    self.updata_textEdit_log_microscope.emit('对焦失败')
                            elif Taskinfo['FocusMode_low'] == 3:
                                # 快速模式3
                                result = self.Scan_Mode_three(zpos_start_low, points_xy, points_xy_real,
                                                              self.action_microscope.get_image_camera_low, fcous_Gap,
                                                              slide_id,
                                                              path_save, save_flag, Multiple, True, 'low', Taskinfo)
                                if result == 0:
                                    self.updata_textEdit_log_microscope.emit('对焦失败')
                self.action_microscope.turn_off_light()
                time_end = time.time()  # 结束计时
                time_c = time_end - time_start  # 运行所花时间
                if self.flage_run:
                    self.updata_textEdit_log_microscope.emit('显微镜平台扫描完成')
                    self.write_log_microscope.emit(0, '显微镜平台扫描完成')
                    self.updata_textEdit_log_microscope.emit('显微镜平台扫描费时' + str(time_c))
                    self.write_log_microscope.emit(0, '显微镜平台扫描费时' + str(time_c))
                self.action_microscope.microscope_home_z()
        except Exception as e:
            self.action_microscope.turn_off_light()
            self.action_microscope.microscope_home_z()
            self.updata_textEdit_log_microscope.emit('显微镜平台扫描失败')
            self.write_log_microscope.emit(1, '显微镜平台扫描停止:' + str(e))
