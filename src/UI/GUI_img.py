from PySide6.QtCore import Qt, QRectF
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import QMainWindow, QGraphicsPixmapItem, QGraphicsScene, QGraphicsView

from src.UI.ui_img import Ui_MainWindow


class MyQMainWindow(QMainWindow):
    def __init__(self, qpixmap, number_ec, number_wbc):
        super().__init__()
        self.qpixmap = qpixmap
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.graphicsView.setDragMode(QGraphicsView.ScrollHandDrag)
        self.ui.graphicsView.setRenderHint(QPainter.Antialiasing)
        self.ui.graphicsView.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.ui.graphicsView.setResizeAnchor(QGraphicsView.AnchorUnderMouse)
        self.showMaximized()
        self.moren()
        self.ui.label_data.setText('上皮细胞数量：' + str(number_ec) + '/n' +
                                   '白细胞数量：' + str(number_wbc))

    def moren(self):
        item = QGraphicsPixmapItem(self.qpixmap)
        # 设置到场景中
        scene = QGraphicsScene(self)
        scene.addItem(item)
        self.ui.graphicsView.setScene(scene)
        # self.ui.graphicsView.fitInView(item, Qt.KeepAspectRatio)
        self.ui.graphicsView.fitInView(QRectF(item.pixmap().rect()), Qt.KeepAspectRatio)

    def wheelEvent(self, event):
        # 处理鼠标滚轮事件
        zoom_in_factor = 1.25
        zoom_out_factor = 0.8
        zoom_direction = event.angleDelta().y() / 120
        if zoom_direction > 0:
            self.ui.graphicsView.scale(zoom_in_factor, zoom_in_factor)
        else:
            self.ui.graphicsView.scale(zoom_out_factor, zoom_out_factor)


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     dialog = MyQMainWindow()
#     dialog.showMaximized()
#     dialog.show()
#     sys.exit(app.exec())
