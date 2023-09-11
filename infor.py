import multiprocessing

import cv2
from ultralytics import YOLO

from UI.Data.Graph import Graph
from control.img_func import gray_world_algorithm


class model:
    def __init__(self):
        super().__init__()
        self.model = YOLO('UI/model/best.pt')
        self.model(cv2.imread('UI/model/test.png'), device='cuda:0', conf=0.5, nms=True)

    def infor(self, ID):
        p = multiprocessing.Process(target=self.infor2(ID))
        p.start()

    def infor2(self, ID):
        Graph_class = Graph()
        numberID = Graph_class.get_IDfromCode(ID + '_低倍20x')
        number = Graph_class.get_node_info(numberID)['Data']['视野数量']
        for i in range(number):
            UUID = Graph_class.get_IDfromCode('Img' + ID + '_' + str(i + 1))
            img = cv2.imread(Graph_class.get_node_info(UUID)['Data']['Image'])
            img = gray_world_algorithm(img)
            results = self.model(img, device='cuda:0', conf=0.5, nms=True)
            # bbox: x,y,w,h
            data = {}
            data['bbox'] = results[0].boxes.xywhn.tolist()
            data['Annotation'] = [int(x) for x in results[0].boxes.cls.tolist()]
            data['Confidence'] = results[0].boxes.conf.tolist()
            Graph_class.set_attr_node(UUID, data)
            Graph_class.save()
        print('完成')
