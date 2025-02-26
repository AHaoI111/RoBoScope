# -*- encoding: utf-8 -*-
from PySide6.QtCore import Signal
from PySide6.QtGui import QColor, QBrush, QFont
from PySide6.QtWidgets import (QDialog, QListWidgetItem)
from UI.modules import ui_box
import numpy as np

font = QFont()
font.setPointSize(12)  # 设置字体大小为10


class Dialog(QDialog):
    reset_slide = Signal()
    save_slide = Signal(np.ndarray)
    def __init__(self, parent=None, slide_task=None, slide_points=None,):
        super().__init__(parent)
        self.ui = ui_box.Ui_Dialog()
        self.ui.setupUi(self)
        self.slide_task = slide_task
        self.slide_points = slide_points
        self.checkbox_map_1 = {
            1: self.ui.checkBox_1_1,
            2: self.ui.checkBox_1_2,
            3: self.ui.checkBox_1_3,
            4: self.ui.checkBox_1_4,
            5: self.ui.checkBox_1_5,
            6: self.ui.checkBox_1_6,
            7: self.ui.checkBox_1_7,
            8: self.ui.checkBox_1_8,
            9: self.ui.checkBox_1_9,
            10: self.ui.checkBox_1_10,
            11: self.ui.checkBox_1_11,
            12: self.ui.checkBox_1_12,
            13: self.ui.checkBox_1_13,
            14: self.ui.checkBox_1_14,
            15: self.ui.checkBox_1_15,
            16: self.ui.checkBox_1_16,
            17: self.ui.checkBox_1_17,
            18: self.ui.checkBox_1_18,
            19: self.ui.checkBox_1_19,
            20: self.ui.checkBox_1_20,
            21: self.ui.checkBox_1_21,
            22: self.ui.checkBox_1_22,
            23: self.ui.checkBox_1_23,
            24: self.ui.checkBox_1_24
        }
        self.checkbox_map_2 = {
            1: self.ui.checkBox_2_1,
            2: self.ui.checkBox_2_2,
            3: self.ui.checkBox_2_3,
            4: self.ui.checkBox_2_4,
            5: self.ui.checkBox_2_5,
            6: self.ui.checkBox_2_6,
            7: self.ui.checkBox_2_7,
            8: self.ui.checkBox_2_8,
            9: self.ui.checkBox_2_9,
            10: self.ui.checkBox_2_10,
            11: self.ui.checkBox_2_11,
            12: self.ui.checkBox_2_12,
            13: self.ui.checkBox_2_13,
            14: self.ui.checkBox_2_14,
            15: self.ui.checkBox_2_15,
            16: self.ui.checkBox_2_16,
            17: self.ui.checkBox_2_17,
            18: self.ui.checkBox_2_18,
            19: self.ui.checkBox_2_19,
            20: self.ui.checkBox_2_20,
            21: self.ui.checkBox_2_21,
            22: self.ui.checkBox_2_22,
            23: self.ui.checkBox_2_23,
            24: self.ui.checkBox_2_24
        }
        self.checkbox_map_3 = {
            1: self.ui.checkBox_3_1,
            2: self.ui.checkBox_3_2,
            3: self.ui.checkBox_3_3,
            4: self.ui.checkBox_3_4,
            5: self.ui.checkBox_3_5,
            6: self.ui.checkBox_3_6,
            7: self.ui.checkBox_3_7,
            8: self.ui.checkBox_3_8,
            9: self.ui.checkBox_3_9,
            10: self.ui.checkBox_3_10,
            11: self.ui.checkBox_3_11,
            12: self.ui.checkBox_3_12,
            13: self.ui.checkBox_3_13,
            14: self.ui.checkBox_3_14,
            15: self.ui.checkBox_3_15,
            16: self.ui.checkBox_3_16,
            17: self.ui.checkBox_3_17,
            18: self.ui.checkBox_3_18,
            19: self.ui.checkBox_3_19,
            20: self.ui.checkBox_3_20,
            21: self.ui.checkBox_3_21,
            22: self.ui.checkBox_3_22,
            23: self.ui.checkBox_3_23,
            24: self.ui.checkBox_3_24
        }
        self.checkbox_map_4 = {
            1: self.ui.checkBox_4_1,
            2: self.ui.checkBox_4_2,
            3: self.ui.checkBox_4_3,
            4: self.ui.checkBox_4_4,
            5: self.ui.checkBox_4_5,
            6: self.ui.checkBox_4_6,
            7: self.ui.checkBox_4_7,
            8: self.ui.checkBox_4_8,
            9: self.ui.checkBox_4_9,
            10: self.ui.checkBox_4_10,
            11: self.ui.checkBox_4_11,
            12: self.ui.checkBox_4_12,
            13: self.ui.checkBox_4_13,
            14: self.ui.checkBox_4_14,
            15: self.ui.checkBox_4_15,
            16: self.ui.checkBox_4_16,
            17: self.ui.checkBox_4_17,
            18: self.ui.checkBox_4_18,
            19: self.ui.checkBox_4_19,
            20: self.ui.checkBox_4_20,
            21: self.ui.checkBox_4_21,
            22: self.ui.checkBox_4_22,
            23: self.ui.checkBox_4_23,
            24: self.ui.checkBox_4_24
        }
        self.flash()

    def flash(self):
        if self.slide_task is not None and self.slide_points is not None:
            boxs = list(range(0, len(self.slide_points)))

            for tasks, points, num in zip(self.slide_task, self.slide_points, boxs):
                list_points = points.tolist()
                # list_points.reverse()
                list_tasks = tasks.tolist()
                # list_tasks.reverse()
                if num == 0:
                    a = 1
                    for task, point in zip(list_tasks, list_points):
                        if task == 0:
                            if a in self.checkbox_map_1:
                                self.checkbox_map_1[a].setChecked(True)
                        else:
                            if a in self.checkbox_map_1:
                                self.checkbox_map_1[a].setChecked(False)
                        a = a + 1
                elif num == 1:
                    a = 1
                    for task, point in zip(list_tasks, list_points):
                        if task == 0:
                            if a in self.checkbox_map_2:
                                self.checkbox_map_2[a].setChecked(True)
                        else:
                            if a in self.checkbox_map_2:
                                self.checkbox_map_2[a].setChecked(False)
                        a = a + 1
                elif num == 2:
                    a = 1
                    for task, point in zip(list_tasks, list_points):
                        if task == 0:
                            if a in self.checkbox_map_3:
                                self.checkbox_map_3[a].setChecked(True)
                        else:
                            if a in self.checkbox_map_3:
                                self.checkbox_map_3[a].setChecked(False)
                        a = a + 1
                elif num == 3:
                    a = 1
                    for task, point in zip(list_tasks, list_points):
                        if task == 0:
                            if a in self.checkbox_map_4:
                                self.checkbox_map_4[a].setChecked(True)
                        else:
                            if a in self.checkbox_map_4:
                                self.checkbox_map_4[a].setChecked(False)
                        a = a + 1
        self.ui.pushButton_reset.clicked.connect(self.updata_slide)
        self.ui.pushButton_save.clicked.connect(self.save_slide_setting)

    def updata_slide(self):
        self.reset_slide.emit()
        
    def save_slide_setting(self):
        slide_task = self.slide_task
        for key, checkbox in self.checkbox_map_1.items():
            if checkbox.isChecked() is True:
                slide_task[0][key - 1] = 0
            else:
                slide_task[0][key - 1] = 1
        for key, checkbox in self.checkbox_map_2.items():
            if checkbox.isChecked() is True:
                slide_task[1][key - 1] = 0
            else:
                slide_task[1][key - 1] = 1
        for key, checkbox in self.checkbox_map_3.items():
            if checkbox.isChecked() is True:
                slide_task[2][key - 1] = 0
            else:
                slide_task[2][key - 1] = 1
        for key, checkbox in self.checkbox_map_4.items():
            if checkbox.isChecked() is True:
                slide_task[3][key - 1] = 0
            else:
                slide_task[3][key - 1] = 1
        self.save_slide.emit(slide_task)
    
