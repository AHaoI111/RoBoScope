import codecs
import sys

# from  PictureBrowser import Ui_Pic
import yaml
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QPainter, QPen
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QScrollArea, QScrollBar

import UI.Data.DataExplorer as DataExplorer
from UI.Data.model import Graph2Model

app = None
app = QApplication(sys.argv)


class QmyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = DataExplorer.Ui_Form()
        self.ui.setupUi(self)
        self.model = Graph2Model()
        self.ui.treeView.setModel(self.model)
        self.ui.treeView.clicked.connect(self.treeView_clicked)
        self.ui.tableView.doubleClicked.connect(self.tableView_doubleclicked)
        yaml_file = 'config.yaml'
        with codecs.open(yaml_file, 'r', 'utf8') as f:
            cfg = yaml.safe_load(f)
        # print(cfg['Annotation'])

        self.annotation_dict = cfg['Annotation']  # {0:'上皮细胞',1:'白细胞',2:'白细胞'}
        self.setGeometry(200, 50, 1024, 768)

    def treeView_clicked(self, index):

        # ID = node_info['ID']
        # node_data = Graphy.get_node_info(self.model.G,ID)['Data']
        # #当前选中的节点数据
        self.node_info = self.model.itemFromIndex(index).data()['Data']
        # 根据当前选中的节点数据构造标准数据模型，用于设置表格窗口
        self.node_item_model = self.model.get_item_data(index)

        self.ui.tableView.setModel(self.node_item_model)
        self.ui.tableView.setColumnWidth(1, 500)

    def tableView_doubleclicked(self, index):
        # 建立对话框界面

        self.picBrower = picBrowser()

        self.picBrower.setGeometry(200, 50, 1024, 768)
        # self.dialog.setWindowTitle('图像浏览')
        # w = dialog.width()
        # h = dialog.height()

        # scroll_area.setParent(verticalLayout)
        # QHBoxLayout(label)
        # label.setGeometry(0, 0, 800, 600)
        # browser_pic = Ui_Pic()

        # row = self.node_item_model.itemFromIndex(index).row()
        # column = self.node_item_model.itemFromIndex(index).column()

        value = self.node_item_model.data(index)
        bbox_list = list(self.node_info['bbox'])
        confidence_list = list(self.node_info['Confidence'])
        label_list = list(self.node_info['Annotation'])

        pic_type = ['JPG', 'BMP', 'JPEG', 'PNG']
        if len(value.split('.')) < 2:
            return
        if value.split('.')[1].upper() in pic_type:
            self.pixmap = QPixmap(value)

            pixmap_width = self.pixmap.size().width()
            pixmap_height = self.pixmap.size().height()
            label_pixmap = self.draw_bbox(self.pixmap, bbox_list, label_list, confidence_list, pixmap_width,
                                          pixmap_height)

            # print(pixmap_width,pixmap_height)

            self.picBrower.label.setGeometry(0, 0, pixmap_width, pixmap_height)

            self.picBrower.label.setPixmap(label_pixmap)
            self.picBrower.pixmap = self.pixmap

            # label.setScaledContents(True)
            self.picBrower.setWindowTitle(value)

        # else:
        #    label.setText('文件类型必须是',str(pic_type))
        self.picBrower.show()

    def draw_bbox(self, pixmap, bbox_list, label_list, confidence_list, width, height):

        painter = QPainter()
        painter.begin(pixmap)

        pen = QPen()
        pen.setWidth(1)
        painter.setPen(pen)
        for bbox, label, confidence in zip(bbox_list, label_list, confidence_list):
            # bbox = list(bbox)
            # print(bbox)
            w = bbox[2] * width
            h = bbox[3] * height
            x = bbox[0] * width - 0.5 * w
            y = bbox[1] * height - 0.5 * h
            # confidence = format(confidence,".3f")*100
            str_confidence = f"{confidence:.2f}"
            # print(x,y)
            painter.drawRect(x, y, w, h)
            try:
                annotation_text = self.annotation_dict[label]
            except:
                annotation_text = label
            # annotation_text =label
            if y < 10:
                y = y + h + 10
            painter.drawText(x, y, annotation_text + ":" + str_confidence)
        return pixmap


class picBrowser(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        # 创建一个Label用于加载图片

        self.label = QLabel()
        # label.setParent(self.dialog) # setParent()方法
        self.zoom = QScrollBar()
        self.zoom.setRange(1, 5)
        self.zoom.setValue(1)
        self.zoom.setSingleStep(1)
        self.zoom.setOrientation(Qt.Horizontal)
        # self.zoom.setTickInterval(1)
        self.zoom.setTracking(False)
        # self.zoom.setGeometry(0,0,1000,20)
        self.pixmap = QPixmap()
        # 创建一个垂直布局
        verticalLayout = QVBoxLayout(self)
        # verticalLayout.setObjectName(u"verticalLayout")
        # 将Label放入垂直布局
        # verticalLayout.addWidget(label)
        # 创建一个滚动区域
        scroll_area = QScrollArea()
        # 将Label关联滚动区域

        scroll_area.setWidget(self.label)
        # 将滚动区域放入垂直布局
        verticalLayout.addWidget(self.zoom, 0, Qt.AlignCenter)
        verticalLayout.addWidget(scroll_area)
        # verticalLayout.setSizeConstraint()
        verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.zoom.valueChanged.connect(self.resize_image)

    '''    
    def wheelEvent(self, event):
        if event.angleDelta().y()>0:
            self.resize_image(2)
        elif event.angleDelta.y()<0:
            self.resize_image(-2)
    '''

    # 修改图片的大小
    def resize_image(self):
        # pixmap = self.label.pixmap()
        scale_factor = self.zoom.value()
        print(scale_factor)
        if scale_factor == 0:
            return

        if self.pixmap is not None:
            new_pixmap = self.pixmap.scaled(self.pixmap.width() * scale_factor, self.pixmap.height() * scale_factor,
                                            Qt.AspectRatioMode.KeepAspectRatio)
            self.label.setPixmap(new_pixmap)
            pixmap_width = self.label.pixmap().width()
            pixmap_height = self.label.pixmap().height()
            self.label.setGeometry(0, 0, pixmap_width, pixmap_height)


def display():
    myWindow = QmyWidget()
    myWindow.show()
    app.exec()



if __name__ == '__main__':
    # app = QApplication(sys.argv)
    # myWindow = QmyWidget()
    # myWindow.show()
    # sys.exit(app.exec())
    display()
