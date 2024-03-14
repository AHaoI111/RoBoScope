from ultralytics import YOLO


class Model_YOLO_cell:
    def __init__(self, path):
        self.model = YOLO(path)
        self.pre_test()

    def pre_test(self):
        self.model.predict('./src/model/test.png')

    def pre(self, image):
        results = self.model.predict(image, device='cuda:0', conf=0.25, iou=0.75, classes=[0, 1])
        return results


class Model_YOLO_bacteria:
    def __init__(self, path):
        self.model = YOLO(path)
        self.pre_test()

    def pre_test(self):
        self.model.predict('./src/model/test.png')

    def pre(self, image):
        results = self.model.predict(image, device='cuda:0', imgsz=640,
                                                                 show_labels=False,
                                                                 line_width=1,
                                                                 conf=0.353, verbose=False,
                                                                 agnostic_nms=True)
        return results
