# -*- encoding: utf-8 -*-
"""
@Description:
扫描过程中的数据存储
@File    :   data.py
@Time    :   2024/07/16
@Author  :   Li QingHao
@Version :   2.0
@Time_END :  最后修改时间：
@Developers_END :  最后修改作者：
"""

import os
import statistics
from datetime import datetime

import cv2
import numpy

from DataSaver.Graph import Graph_slide
import torch


# 解析数据
class data_processing:
    def __init__(self, code, numberw, numberh):
        self.PP_code = None
        self.numberw = numberw
        self.numberh = numberh
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.image_stitch_part = []
        self.image_stitch_all = []
        self.image_wbc = torch.zeros((numberw, numberh), dtype=torch.float64, device=self.device)
        self.image_ec = torch.zeros((numberw, numberh), dtype=torch.float64, device=self.device)
        self.image_bacteria = torch.zeros((numberw, numberh), dtype=torch.float64, device=self.device)
        #
        self.G = Graph_slide(code)

    def Save_data_1(self, code, label):
        # 录入数据库
        # 一级
        data = {'Code': code, 'label': label}
        root_id = self.G.add_node(data)
        data = {'root ID': root_id}
        self.G.set_attr_node(root_id, data)
        return root_id

    def Save_data_2(self, root_id, multiple, path, path_slide):
        # 录入数据库
        # 二级
        Code = multiple
        data = {}
        parent_code = self.G.get_node_info(root_id)['Data']['Code']
        data['Code'] = parent_code + '_' + Code
        data['label'] = Code
        data['视野数量'] = self.numberw * self.numberh
        data['视野长宽'] = [self.numberw, self.numberh]
        data['Image'] = path
        data['Image_slide'] = path_slide
        self.PP_code = self.G.add_node(data, root_id)
        return self.PP_code

    def Save_data_3(self, image, ID, Z, a, XY, point_xy_real, path, results_cell, results_bacteria, xylist,
                    formatted_a):
        try:
            # 录入数据库
            # 三级节点(多少张图就多少个)
            result_boxes_bacteria = []
            result_cls_bacteria = []
            RGB = []
            for results_bacteria_part, xy in zip(results_bacteria, xylist):
                result_cls_bacteria.extend([int(x) for x in results_bacteria_part.boxes.cls.tolist()])
                for box in results_bacteria_part.boxes:
                    box_list = box.xyxy[0].tolist()
                    box_list[0] = box_list[0] + xy[0]
                    box_list[1] = box_list[1] + xy[1]
                    box_list[2] = box_list[2] + xy[0]
                    box_list[3] = box_list[3] + xy[1]
                    result_boxes_bacteria.append(box_list)
                    img = image[int(box_list[1]):int(box_list[3]), int(box_list[0]):int(box_list[2])]
                    b, g, r = cv2.split(img)
                    RGB.append([numpy.mean(r), numpy.mean(g), numpy.mean(b)])
            data = {}
            data['Code'] = 'Img' + ID + '_' + str(formatted_a)
            data['label'] = data['Code']
            data['Date'] = str(datetime.now())
            data['Pos_XY'] = [XY[0], XY[1]]
            data['Pos_XY_real'] = point_xy_real
            data['Pos_Z'] = [Z]
            data['Desc'] = '区域扫描'
            data['Image'] = path
            data['bbox_cell'] = results_cell[0].boxes.xyxy.tolist()
            data['bbox_bacteria'] = result_boxes_bacteria
            data['Annotation_cell'] = [int(x) for x in results_cell[0].boxes.cls.tolist()]
            data['Annotation_bacteria'] = result_cls_bacteria
            data['Confidence'] = results_cell[0].boxes.conf.tolist()
            data['RGB'] = RGB
            unique_id = self.G.add_node(data, self.PP_code)
            self.result_statistics(a, XY, results_cell, result_cls_bacteria, ID)
        except Exception as e:
            with open("log.txt", "a") as log_file:
                log_file.write(str(e))

    def result_statistics(self, a, Point_XY, results_cell, result_cls_bacteria, ID):
        # 推荐结果
        with torch.no_grad():
            self.image_ec = self.update_tensor(self.image_ec, Point_XY,
                                               sum(1 for x in results_cell[0].boxes.cls.tolist() if x == 1))
            self.image_wbc = self.update_tensor(self.image_wbc, Point_XY,
                                                sum(1 for x in results_cell[0].boxes.cls.tolist() if
                                                    x == 0))
            self.image_bacteria = self.update_tensor(self.image_bacteria, Point_XY,
                                                     sum(1 for x in result_cls_bacteria if x == 0))
        if a == self.numberw * self.numberh:
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
                        list_window.append([row * self.numberw + col + 1, row * self.numberw + col + 2,
                                            row * self.numberw + col + 1 + 2 * (self.image_wbc.shape[1] - 1 - col),
                                            row * self.numberw + col + 2 + 2 * (self.image_wbc.shape[1] - 1 - col)])
                        list_window_bacteria.append([row * self.numberw + col + 1, row * self.numberw + col + 2,
                                                     row * self.numberw + col + 1 + 2 * (
                                                             self.image_wbc.shape[1] - 1 - col),
                                                     row * self.numberw + col + 2 + 2 * (
                                                             self.image_wbc.shape[1] - 1 - col)])
                        list_window_wbc.append(sum_wbc)
                        list_window_ec.append(sum_ec)
                        number_list_window_bacteria.append(sum_bacteria)
                    else:
                        if sum_wbc > min(list_window_wbc):
                            index = list_window_wbc.index(min(list_window_wbc))
                            list_window[index] = [row * self.numberw + col + 1, row * self.numberw + col + 2,
                                                  row * self.numberw + col + 1 + 2 * (
                                                          self.image_wbc.shape[1] - 1 - col),
                                                  row * self.numberw + col + 2 + 2 * (
                                                          self.image_wbc.shape[1] - 1 - col)]
                            list_window_wbc[index] = sum_wbc
                            list_window_ec[index] = sum_ec
                        if sum_bacteria > min(number_list_window_bacteria):
                            index = number_list_window_bacteria.index(min(number_list_window_bacteria))
                            list_window_bacteria[index] = [row * self.numberw + col + 1, row * self.numberw + col + 2,
                                                           row * self.numberw + col + 1 + 2 * (
                                                                   self.image_wbc.shape[1] - 1 - col),
                                                           row * self.numberw + col + 2 + 2 * (
                                                                   self.image_wbc.shape[1] - 1 - col)]
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
            self.G.set_attr_node(self.PP_code, data_)
            self.G.save('./data/' + ID + '/' + ID + '.dat')

    def update_tensor(self, tensor, point_xy, value):
        with torch.no_grad():
            new_tensor = tensor.clone()  # 克隆原始张量
            new_tensor[point_xy[0], point_xy[1]] = value  # 更新指定位置的值
            return new_tensor
