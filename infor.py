import multiprocessing
import threading
import time

import cv2
import numpy
from ultralytics import YOLO

from UI.Data.Graph import Graph


class model:
    def __init__(self):
        super().__init__()
        self.model = YOLO('UI/model/best.pt')
        self.model(cv2.imread('UI/model/test.png'), device='cuda:0', conf=0.7, nms=True)

    def infor(self, ID):
        p = multiprocessing.Process(target=self.infor2(ID))
        p.start()
        p.join()

    def infor2(self, ID):

        time_start = time.time()  # 开始计时
        Graph_class = Graph()
        numberID = Graph_class.get_IDfromCode(ID + '_高倍50x')
        number = Graph_class.get_node_info(numberID)['Data']['视野数量']
        wh = Graph_class.get_node_info(numberID)['Data']['视野长宽']
        path_Stitch_pic = Graph_class.get_node_info(numberID)['Data']['拼接图']
        image_wbc = numpy.zeros((wh[1] + 2, wh[0] + 2), dtype=numpy.uint8)
        image_ec = numpy.zeros((wh[1] + 2, wh[0] + 2), dtype=numpy.uint8)

        for i in range(number):
            UUID = Graph_class.get_IDfromCode('Img' + ID + '_' + str(i + 1))
            img = cv2.imread(Graph_class.get_node_info(UUID)['Data']['Image'])
            # img = gray_world_algorithm(img)
            results = self.model(img, device='cuda:0', conf=0.7, nms=True)
            # bbox: x,y,w,h
            data = {}
            data['bbox'] = results[0].boxes.xywhn.tolist()
            data['Annotation'] = [int(x) for x in results[0].boxes.cls.tolist()]
            data['Confidence'] = results[0].boxes.conf.tolist()
            Graph_class.set_attr_node(UUID, data)
            Graph_class.save()
            node_info = Graph_class.get_node_info(UUID)
            pos_xy = node_info['Data']['Pos_XY']
            image_ec[wh[1] - pos_xy[1], pos_xy[0]] = [int(x) for x in results[0].boxes.cls.tolist()].count(1)
            image_wbc[wh[1] - pos_xy[1], pos_xy[0]] = [int(x) for x in results[0].boxes.cls.tolist()].count(0)

        list_window = []
        list_window_wbc = []
        # 窗口大小
        window_size = (2, 2)
        # 滑动窗口并计算每个窗口的灰度值综合
        for row in range(0, image_wbc.shape[0] - window_size[0] + 1, 2):
            for col in range(0, image_wbc.shape[1] - window_size[1] + 1, 2):
                # 获取当前窗口
                window_wbc = image_wbc[row:row + window_size[0], col:col + window_size[1]]
                # window_ec = image_ec[row:row + window_size[0], col:col + window_size[1]]
                # 计算窗口的细胞数综合
                sum_wbc = window_wbc.sum()
                # sum_ec = window_ec.sum()
                if len(list_window) < 40:
                    list_window.append([col, row, col + window_size[1], row + window_size[0]])
                    list_window_wbc.append(sum_wbc)
                else:
                    if sum_wbc > min(list_window_wbc):
                        index = list_window_wbc.index(min(list_window_wbc))
                        list_window[index] = [col, row, col + window_size[1], row + window_size[0]]
                        list_window_wbc[index] = sum_wbc
                # if sum_wbc > 25:
                #     if window_ec < 10:
                #         list_window.append([col, row, col + window_size[1], row + window_size[0]])
        Stitch_pic = cv2.imread(path_Stitch_pic)

        for point in list_window:
            cv2.circle(Stitch_pic,
                       (int((point[0] * 320 + point[2] * 320) / 2), int((point[1] * 320 + point[3] * 320) / 2)), 320,
                       (0, 255, 0), 5)
            # cv2.rectangle(Stitch_pic, (point[0] * 256, point[1] * 256), (point[2] * 256, point[3] * 256), (0, 255, 0),
            #               5)
        # cv2.imwrite('wbc.png', image_wbc)
        # cv2.imwrite('ec.png', image_ec)
        cv2.imwrite(path_Stitch_pic, Stitch_pic)

        print('完成')
        time_end = time.time()  # 结束计时
        time_c = time_end - time_start  # 运行所花时间
        print('time cost', time_c, 's')
        return list_window
