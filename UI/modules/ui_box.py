# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QListWidget, QListWidgetItem, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1200, 883)
        Dialog.setMinimumSize(QSize(1200, 883))
        Dialog.setMaximumSize(QSize(1200, 883))
        Dialog.setStyleSheet(u"    background: rgb(128,128,128);")
        self.horizontalLayout = QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.listWidget_4 = QListWidget(Dialog)
        self.listWidget_4.setObjectName(u"listWidget_4")
        self.listWidget_4.setMinimumSize(QSize(150, 0))
        self.listWidget_4.setMaximumSize(QSize(150, 16777215))
        self.listWidget_4.setStyleSheet(u"QListWidget {\n"
"    border: 1px solid #ccc;\n"
"    gridline-color: #eee;\n"
"    padding: 0;\n"
"}\n"
"\n"
"QListWidget::item {\n"
"    width: 20px; /* \u6839\u636e\u9700\u8981\u8c03\u6574 */\n"
"    height: 10px; /* \u6839\u636e\u9700\u8981\u8c03\u6574 */\n"
"    border: 1px solid #ddd;\n"
"    border-radius: 5px;\n"
"    margin: 4.5px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"    background: #aaf;\n"
"    border: 1px solid #77f;\n"
"}\n"
"")

        self.verticalLayout_4.addWidget(self.listWidget_4)

        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 26))
        self.label_4.setMaximumSize(QSize(16777215, 26))
        font = QFont()
        font.setPointSize(20)
        self.label_4.setFont(font)

        self.verticalLayout_4.addWidget(self.label_4)


        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.listWidget_3 = QListWidget(Dialog)
        self.listWidget_3.setObjectName(u"listWidget_3")
        self.listWidget_3.setMinimumSize(QSize(150, 0))
        self.listWidget_3.setMaximumSize(QSize(150, 16777215))
        self.listWidget_3.setStyleSheet(u"QListWidget {\n"
"    border: 1px solid #ccc;\n"
"    gridline-color: #eee;\n"
"    padding: 0;\n"
"}\n"
"\n"
"QListWidget::item {\n"
"    width: 20px; /* \u6839\u636e\u9700\u8981\u8c03\u6574 */\n"
"    height: 10px; /* \u6839\u636e\u9700\u8981\u8c03\u6574 */\n"
"    border: 1px solid #ddd;\n"
"    border-radius: 5px;\n"
"    margin: 4.5px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"    background: #aaf;\n"
"    border: 1px solid #77f;\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.listWidget_3)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 26))
        self.label_3.setMaximumSize(QSize(16777215, 26))
        self.label_3.setFont(font)

        self.verticalLayout_3.addWidget(self.label_3)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.listWidget_2 = QListWidget(Dialog)
        self.listWidget_2.setObjectName(u"listWidget_2")
        self.listWidget_2.setMinimumSize(QSize(150, 0))
        self.listWidget_2.setMaximumSize(QSize(150, 16777215))
        self.listWidget_2.setStyleSheet(u"QListWidget {\n"
"    border: 1px solid #ccc;\n"
"    gridline-color: #eee;\n"
"    padding: 0;\n"
"}\n"
"\n"
"QListWidget::item {\n"
"    width: 20px; /* \u6839\u636e\u9700\u8981\u8c03\u6574 */\n"
"    height: 10px; /* \u6839\u636e\u9700\u8981\u8c03\u6574 */\n"
"    border: 1px solid #ddd;\n"
"    border-radius: 5px;\n"
"    margin: 4.5px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"    background: #aaf;\n"
"    border: 1px solid #77f;\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.listWidget_2)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 26))
        self.label_2.setMaximumSize(QSize(16777215, 26))
        self.label_2.setFont(font)

        self.verticalLayout_2.addWidget(self.label_2)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.listWidget_1 = QListWidget(Dialog)
        self.listWidget_1.setObjectName(u"listWidget_1")
        self.listWidget_1.setMinimumSize(QSize(150, 0))
        self.listWidget_1.setMaximumSize(QSize(150, 16777215))
        self.listWidget_1.setStyleSheet(u"QListWidget {\n"
"    border: 1px solid #ccc;\n"
"    gridline-color: #eee;\n"
"    padding: 0;\n"
"}\n"
"\n"
"QListWidget::item {\n"
"    width: 20px; /* \u6839\u636e\u9700\u8981\u8c03\u6574 */\n"
"    height: 10px; /* \u6839\u636e\u9700\u8981\u8c03\u6574 */\n"
"    border: 1px solid #ddd;\n"
"    border-radius: 5px;\n"
"    margin: 4.5px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"    background: #aaf;\n"
"    border: 1px solid #77f;\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.listWidget_1)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(150, 26))
        self.label.setMaximumSize(QSize(16777215, 26))
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"4\u53f7\u73bb\u7247\u4ed3", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"3\u53f7\u73bb\u7247\u4ed3", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"2\u53f7\u73bb\u7247\u4ed3", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"1\u53f7\u73bb\u7247\u4ed3", None))
    # retranslateUi

