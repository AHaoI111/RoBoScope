# -*- encoding: utf-8 -*-
from PySide6.QtGui import QColor, QBrush, QFont
from PySide6.QtWidgets import (QDialog, QListWidgetItem)
from UI.modules import ui_box

font = QFont()
font.setPointSize(12)  # 设置字体大小为10


class Dialog(QDialog):
    def __init__(self, parent=None, slide_task=None, slide_points=None, ):
        super().__init__(parent)
        self.ui = ui_box.Ui_Dialog()
        self.ui.setupUi(self)
        if slide_task is not None and slide_points is not None:
            boxs = list(range(0, len(slide_points)))
            for tasks, points, num in zip(slide_task, slide_points, boxs):
                list_points = points.tolist()
                list_points.reverse()
                list_tasks = tasks.tolist()
                list_tasks.reverse()

                if num == 0:
                    for task, point in zip(list_tasks, list_points):
                        item = QListWidgetItem(str(point))
                        item.setFont(font)
                        if task == 0:
                            item.setForeground(QColor("darkgreen"))
                        else:
                            item.setForeground(QColor("darkred"))
                        self.ui.listWidget_1.addItem(item)
                elif num == 1:
                    for task, point in zip(list_tasks, list_points):
                        item = QListWidgetItem(str(point))
                        item.setFont(font)
                        if task == 0:
                            item.setForeground(QColor("darkgreen"))
                        else:
                            item.setForeground(QColor("darkred"))
                        self.ui.listWidget_2.addItem(item)
                elif num == 2:
                    for task, point in zip(list_tasks, list_points):
                        item = QListWidgetItem(str(point))
                        item.setFont(font)
                        if task == 0:
                            item.setForeground(QColor("darkgreen"))
                        else:
                            item.setForeground(QColor("darkred"))
                        self.ui.listWidget_3.addItem(item)
                elif num == 3:
                    for task, point in zip(list_tasks, list_points):
                        item = QListWidgetItem(str(point))
                        item.setFont(font)
                        if task == 0:
                            item.setForeground(QColor("darkgreen"))
                        else:
                            item.setForeground(QColor("darkred"))
                        self.ui.listWidget_4.addItem(item)
