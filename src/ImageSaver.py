import statistics

import cv2
import numpy
from queue import Queue
from threading import Thread, Lock
from PySide6.QtCore import *
from src import data
from src.Data import Graph


class ImageSaver(QObject):
    def __init__(self, model):
        QObject.__init__(self)

        self.queue = Queue(625)
        self.image_lock = Lock()
        self.model = model
        self.thread = Thread(target=self.process_queue)
        self.thread.start()

    def process_queue(self):
        while True:
            try:
                [image, Graph_class, PP_code, ID, ZPoint, a, Point_XY, timesave, path_save,
                 Stitch_pic, numberw, numberh, ok, point_xy_real] = self.queue.get(
                    timeout=0.1)
                self.image_lock.acquire(True)

                if image is not None:
                    if a == 1:
                        image_wbc = numpy.zeros((numberw, numberh), dtype=numpy.uint8)
                        image_ec = numpy.zeros((numberw, numberh), dtype=numpy.uint8)
                    # 存图
                    cv2.imwrite(path_save + '\\' + timesave + '_' + ID + '_' + str(a) + '.png', image)
                    # 推理
                    results = self.model(image, device='cuda:0', conf=0.25, iou=0.75, classes=[0, 1])
                    # 保存结果
                    data.Save_data_3(Graph_class, PP_code, ID, ZPoint, a, Point_XY, timesave, results,point_xy_real)
                    image_ec[Point_XY[0], Point_XY[1]] = [int(x) for x in
                                                          results[0].boxes.cls.tolist()].count(1)
                    image_wbc[Point_XY[0], Point_XY[1]] = [int(x) for x in
                                                           results[0].boxes.cls.tolist()].count(0)
                    if a == numberw * numberh:
                        Stitch_pic = numpy.array(Stitch_pic)
                        Stitch_pic = cv2.cvtColor(Stitch_pic, cv2.COLOR_RGB2BGR)
                        list_window = []
                        list_window_wbc = []
                        list_window_ec = []
                        # 窗口大小
                        window_size = (2, 2)
                        # 滑动窗口并计算每个窗口的灰度值综合
                        for row in range(0, image_wbc.shape[0] - window_size[0] + 1, 2):
                            for col in range(0, image_wbc.shape[1] - window_size[1] + 1, 2):
                                # 获取当前窗口
                                window_wbc = image_wbc[row:row + window_size[0], col:col + window_size[1]]
                                window_ec = image_ec[row:row + window_size[0], col:col + window_size[1]]
                                # 计算窗口的细胞数综合
                                sum_wbc = window_wbc.sum()
                                sum_ec = window_ec.sum()
                                if len(list_window) < 20:
                                    list_window.append([row * numberw + col + 1, row * numberw + col + 2,
                                                        (row + 1) * numberw + col + 1, (row + 1) * numberw + col + 2])
                                    list_window_wbc.append(sum_wbc)
                                    list_window_ec.append(sum_ec)
                                else:
                                    if sum_wbc > min(list_window_wbc):
                                        index = list_window_wbc.index(min(list_window_wbc))
                                        list_window[index] = [row * numberw + col + 1, row * numberw + col + 2,
                                                              (row + 1) * numberw + col + 1,
                                                              (row + 1) * numberw + col + 2]
                                        list_window_wbc[index] = sum_wbc
                                        list_window_ec[index] = sum_ec
                        # wbc
                        mean_wbc = sum(list_window_wbc) / len(list_window_wbc)
                        median_wbc = median = statistics.median(list_window_wbc)
                        # ec
                        mean_ec = sum(list_window_ec) / len(list_window_ec)
                        median_ec = median = statistics.median(list_window_ec)
                        GRAPH = Graph.Graph()
                        UUID = GRAPH.get_IDfromCode(ID + '_' + '50x')
                        node_info = GRAPH.get_node_info(UUID)
                        data_ = {}
                        data_['推荐视野'] = list_window
                        data_['白细胞平均数'] = mean_wbc
                        data_['白细胞中位数'] = median_wbc
                        data_['上皮细胞平均数'] = mean_ec
                        data_['上皮细胞中位数'] = median_ec
                        PP_code = GRAPH.set_attr_node(UUID, data_)
                        GRAPH.save()
                        # 前20
                        cv2.imwrite('pic\\' + ID + '\\' + ID + '.png', Stitch_pic)
                        ok.emit(ID)
                        return
                self.queue.task_done()
                self.image_lock.release()
            except:
                pass

    def enqueue(self, image, Graph_class, PP_code, ID, ZPoint, a, Point_XY, timesave, path_save, Stitch_pic,
                numberw, numberh, ok, point_xy_real):
        try:
            self.queue.put_nowait(
                [image, Graph_class, PP_code, ID, ZPoint, a, Point_XY, timesave, path_save, Stitch_pic,
                 numberw, numberh, ok, point_xy_real])
        except:
            print('imageSaver queue is full, image discarded')
