# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QComboBox,
    QDoubleSpinBox, QGraphicsView, QHBoxLayout, QLabel,
    QMainWindow, QMenu, QMenuBar, QProgressBar,
    QPushButton, QSizePolicy, QSlider, QSpinBox,
    QStatusBar, QTabWidget, QTextEdit, QToolBox,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1192, 1054)
        icon = QIcon(QIcon.fromTheme(u"applications-internet"))
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"background-color: rgb(69, 77, 98);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.actionlianxifangshi = QAction(MainWindow)
        self.actionlianxifangshi.setObjectName(u"actionlianxifangshi")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_19 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget_result_AI = QTabWidget(self.centralwidget)
        self.tabWidget_result_AI.setObjectName(u"tabWidget_result_AI")
        self.tabWidget_result_AI.setMinimumSize(QSize(201, 251))
        self.tabWidget_result_AI.setMaximumSize(QSize(201, 251))
        self.tabWidget_result_AI.setStyleSheet(u"            QTabWidget::pane { /* The tab widget frame */\n"
"                border: 3px solid black; /* \u52a0\u7c97\u8fb9\u754c\u6846 */\n"
"                border-radius: 10px; /* \u5706\u89d2\u534a\u5f84 */\n"
"                background: white;\n"
"            }\n"
"            QTabWidget::tab-bar {\n"
"                left: 5px; /* move to the right by 5px */\n"
"            }\n"
"            /* Style the tab using the tab sub-control. Note that it reads QTabBar not QTabWidget */\n"
"            QTabBar::tab {\n"
"                background: lightgray;\n"
"                border: 3px solid black;\n"
"                padding: 5px;\n"
"                border-top-left-radius: 5px; /* \u9876\u90e8\u5de6\u4fa7\u5706\u89d2 */\n"
"                border-top-right-radius: 5px; /* \u9876\u90e8\u53f3\u4fa7\u5706\u89d2 */\n"
"                font-size: 10px; /* \u8c03\u6574\u5b57\u4f53\u5927\u5c0f */\n"
"            }\n"
"            QTabBar::tab:selected {\n"
"                background: rgb(50,109,245);\n"
"    "
                        "            margin-bottom: 0px; /* overlap with the frame border */\n"
"\n"
"            }\n"
"            QTabBar::tab:!selected {\n"
"                margin-top: 2px; /* make non-selected tabs look smaller */\n"
"            }")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.horizontalLayout_2 = QHBoxLayout(self.tab_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_result_AI = QLabel(self.tab_3)
        self.label_result_AI.setObjectName(u"label_result_AI")
        self.label_result_AI.setMinimumSize(QSize(201, 251))
        self.label_result_AI.setMaximumSize(QSize(201, 251))
        self.label_result_AI.setStyleSheet(u"background-color: black\uff1b")

        self.horizontalLayout_2.addWidget(self.label_result_AI)

        self.tabWidget_result_AI.addTab(self.tab_3, "")

        self.verticalLayout.addWidget(self.tabWidget_result_AI)

        self.tabWidget_log = QTabWidget(self.centralwidget)
        self.tabWidget_log.setObjectName(u"tabWidget_log")
        self.tabWidget_log.setMinimumSize(QSize(201, 201))
        self.tabWidget_log.setMaximumSize(QSize(201, 16777215))
        self.tabWidget_log.setStyleSheet(u"            QTabWidget::pane { /* The tab widget frame */\n"
"                border: 3px solid black; /* \u52a0\u7c97\u8fb9\u754c\u6846 */\n"
"                border-radius: 10px; /* \u5706\u89d2\u534a\u5f84 */\n"
"                background: white;\n"
"            }\n"
"            QTabWidget::tab-bar {\n"
"                left: 5px; /* move to the right by 5px */\n"
"            }\n"
"            /* Style the tab using the tab sub-control. Note that it reads QTabBar not QTabWidget */\n"
"            QTabBar::tab {\n"
"                background: lightgray;\n"
"                border: 3px solid black;\n"
"                padding: 5px;\n"
"                border-top-left-radius: 5px; /* \u9876\u90e8\u5de6\u4fa7\u5706\u89d2 */\n"
"                border-top-right-radius: 5px; /* \u9876\u90e8\u53f3\u4fa7\u5706\u89d2 */\n"
"                font-size: 10px; /* \u8c03\u6574\u5b57\u4f53\u5927\u5c0f */\n"
"            }\n"
"            QTabBar::tab:selected {\n"
"                background: rgb(50,109,245);\n"
"    "
                        "            margin-bottom: 0px; /* overlap with the frame border */\n"
"\n"
"            }\n"
"            QTabBar::tab:!selected {\n"
"                margin-top: 2px; /* make non-selected tabs look smaller */\n"
"            }")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.horizontalLayout_3 = QHBoxLayout(self.tab_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.textEdit_log = QTextEdit(self.tab_4)
        self.textEdit_log.setObjectName(u"textEdit_log")
        self.textEdit_log.setMinimumSize(QSize(201, 201))
        self.textEdit_log.setMaximumSize(QSize(201, 16777215))
        self.textEdit_log.setStyleSheet(u"background-color: black\uff1b")

        self.horizontalLayout_3.addWidget(self.textEdit_log)

        self.tabWidget_log.addTab(self.tab_4, "")

        self.verticalLayout.addWidget(self.tabWidget_log)

        self.tabWidget_ID = QTabWidget(self.centralwidget)
        self.tabWidget_ID.setObjectName(u"tabWidget_ID")
        self.tabWidget_ID.setMinimumSize(QSize(201, 251))
        self.tabWidget_ID.setMaximumSize(QSize(201, 251))
        self.tabWidget_ID.setStyleSheet(u"            QTabWidget::pane { /* The tab widget frame */\n"
"                border: 3px solid black; /* \u52a0\u7c97\u8fb9\u754c\u6846 */\n"
"                border-radius: 10px; /* \u5706\u89d2\u534a\u5f84 */\n"
"                background: white;\n"
"            }\n"
"            QTabWidget::tab-bar {\n"
"                left: 5px; /* move to the right by 5px */\n"
"            }\n"
"            /* Style the tab using the tab sub-control. Note that it reads QTabBar not QTabWidget */\n"
"            QTabBar::tab {\n"
"                background: lightgray;\n"
"                border: 3px solid black;\n"
"                padding: 5px;\n"
"                border-top-left-radius: 5px; /* \u9876\u90e8\u5de6\u4fa7\u5706\u89d2 */\n"
"                border-top-right-radius: 5px; /* \u9876\u90e8\u53f3\u4fa7\u5706\u89d2 */\n"
"                font-size: 10px; /* \u8c03\u6574\u5b57\u4f53\u5927\u5c0f */\n"
"            }\n"
"            QTabBar::tab:selected {\n"
"                background: rgb(50,109,245);\n"
"    "
                        "            margin-bottom: 0px; /* overlap with the frame border */\n"
"\n"
"            }\n"
"            QTabBar::tab:!selected {\n"
"                margin-top: 2px; /* make non-selected tabs look smaller */\n"
"            }")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.horizontalLayout_4 = QHBoxLayout(self.tab_5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.textEdit_ID = QTextEdit(self.tab_5)
        self.textEdit_ID.setObjectName(u"textEdit_ID")
        self.textEdit_ID.setMinimumSize(QSize(201, 251))
        self.textEdit_ID.setMaximumSize(QSize(201, 251))
        self.textEdit_ID.setStyleSheet(u"background-color: black\uff1b")

        self.horizontalLayout_4.addWidget(self.textEdit_ID)

        self.tabWidget_ID.addTab(self.tab_5, "")

        self.verticalLayout.addWidget(self.tabWidget_ID)


        self.horizontalLayout_8.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMinimumSize(QSize(640, 480))
        self.tabWidget.setStyleSheet(u"            QTabWidget::pane { /* The tab widget frame */\n"
"                border: 3px solid black; /* \u52a0\u7c97\u8fb9\u754c\u6846 */\n"
"                border-radius: 10px; /* \u5706\u89d2\u534a\u5f84 */\n"
"                background: white;\n"
"            }\n"
"            QTabWidget::tab-bar {\n"
"                left: 5px; /* move to the right by 5px */\n"
"            }\n"
"            /* Style the tab using the tab sub-control. Note that it reads QTabBar not QTabWidget */\n"
"            QTabBar::tab {\n"
"                background: lightgray;\n"
"                border: 3px solid black;\n"
"                padding: 5px;\n"
"                border-top-left-radius: 5px; /* \u9876\u90e8\u5de6\u4fa7\u5706\u89d2 */\n"
"                border-top-right-radius: 5px; /* \u9876\u90e8\u53f3\u4fa7\u5706\u89d2 */\n"
"                font-size: 10px; /* \u8c03\u6574\u5b57\u4f53\u5927\u5c0f */\n"
"            }\n"
"            QTabBar::tab:selected {\n"
"                background: rgb(50,109,245);\n"
"    "
                        "            margin-bottom: 0px; /* overlap with the frame border */\n"
"\n"
"            }\n"
"            QTabBar::tab:!selected {\n"
"                margin-top: 2px; /* make non-selected tabs look smaller */\n"
"            }")
        self.tab_9 = QWidget()
        self.tab_9.setObjectName(u"tab_9")
        self.horizontalLayout_6 = QHBoxLayout(self.tab_9)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.graphicsView_fcous = QGraphicsView(self.tab_9)
        self.graphicsView_fcous.setObjectName(u"graphicsView_fcous")
        self.graphicsView_fcous.setMinimumSize(QSize(640, 480))
        self.graphicsView_fcous.setStyleSheet(u"background-color: black\uff1b")

        self.horizontalLayout_6.addWidget(self.graphicsView_fcous)

        self.tabWidget.addTab(self.tab_9, "")
        self.tab_10 = QWidget()
        self.tab_10.setObjectName(u"tab_10")
        self.horizontalLayout_7 = QHBoxLayout(self.tab_10)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.graphicsView = QGraphicsView(self.tab_10)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setMinimumSize(QSize(640, 480))
        self.graphicsView.setStyleSheet(u"background-color: black\uff1b")

        self.horizontalLayout_7.addWidget(self.graphicsView)

        self.tabWidget.addTab(self.tab_10, "")

        self.verticalLayout_2.addWidget(self.tabWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tabWidget_scan_process = QTabWidget(self.centralwidget)
        self.tabWidget_scan_process.setObjectName(u"tabWidget_scan_process")
        self.tabWidget_scan_process.setMinimumSize(QSize(317, 201))
        self.tabWidget_scan_process.setMaximumSize(QSize(16777215, 201))
        self.tabWidget_scan_process.setStyleSheet(u"            QTabWidget::pane { /* The tab widget frame */\n"
"                border: 3px solid black; /* \u52a0\u7c97\u8fb9\u754c\u6846 */\n"
"                border-radius: 10px; /* \u5706\u89d2\u534a\u5f84 */\n"
"                background: white;\n"
"            }\n"
"            QTabWidget::tab-bar {\n"
"                left: 5px; /* move to the right by 5px */\n"
"            }\n"
"            /* Style the tab using the tab sub-control. Note that it reads QTabBar not QTabWidget */\n"
"            QTabBar::tab {\n"
"                background: lightgray;\n"
"                border: 3px solid black;\n"
"                padding: 5px;\n"
"                border-top-left-radius: 5px; /* \u9876\u90e8\u5de6\u4fa7\u5706\u89d2 */\n"
"                border-top-right-radius: 5px; /* \u9876\u90e8\u53f3\u4fa7\u5706\u89d2 */\n"
"                font-size: 10px; /* \u8c03\u6574\u5b57\u4f53\u5927\u5c0f */\n"
"            }\n"
"            QTabBar::tab:selected {\n"
"                background: rgb(50,109,245);\n"
"    "
                        "            margin-bottom: 0px; /* overlap with the frame border */\n"
"\n"
"            }\n"
"            QTabBar::tab:!selected {\n"
"                margin-top: 2px; /* make non-selected tabs look smaller */\n"
"            }")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.horizontalLayout_20 = QHBoxLayout(self.tab_6)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.progressBar = QProgressBar(self.tab_6)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setStyleSheet(u"QProgressBar{\n"
"	font:9pt;\n"
"	border-radius:5px;\n"
"	text-align:center;\n"
"	border:1px solid #E8EDF2;\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-color: rgb(180, 180, 180);\n"
"    color:black;\n"
"}\n"
"QProgressBar:chunk{\n"
"	border-radius:5px;\n"
"	background-color:#1ABC9C;\n"
"}\n"
"")
        self.progressBar.setValue(0)

        self.horizontalLayout_20.addWidget(self.progressBar)

        self.tabWidget_scan_process.addTab(self.tab_6, "")

        self.horizontalLayout.addWidget(self.tabWidget_scan_process)

        self.tabWidget_silde_process = QTabWidget(self.centralwidget)
        self.tabWidget_silde_process.setObjectName(u"tabWidget_silde_process")
        self.tabWidget_silde_process.setMinimumSize(QSize(258, 201))
        self.tabWidget_silde_process.setMaximumSize(QSize(258, 201))
        self.tabWidget_silde_process.setStyleSheet(u"            QTabWidget::pane { /* The tab widget frame */\n"
"                border: 3px solid black; /* \u52a0\u7c97\u8fb9\u754c\u6846 */\n"
"                border-radius: 10px; /* \u5706\u89d2\u534a\u5f84 */\n"
"                background: white;\n"
"            }\n"
"            QTabWidget::tab-bar {\n"
"                left: 5px; /* move to the right by 5px */\n"
"            }\n"
"            /* Style the tab using the tab sub-control. Note that it reads QTabBar not QTabWidget */\n"
"            QTabBar::tab {\n"
"                background: lightgray;\n"
"                border: 3px solid black;\n"
"                padding: 5px;\n"
"                border-top-left-radius: 5px; /* \u9876\u90e8\u5de6\u4fa7\u5706\u89d2 */\n"
"                border-top-right-radius: 5px; /* \u9876\u90e8\u53f3\u4fa7\u5706\u89d2 */\n"
"                font-size: 10px; /* \u8c03\u6574\u5b57\u4f53\u5927\u5c0f */\n"
"            }\n"
"            QTabBar::tab:selected {\n"
"                background: rgb(50,109,245);\n"
"    "
                        "            margin-bottom: 0px; /* overlap with the frame border */\n"
"\n"
"            }\n"
"            QTabBar::tab:!selected {\n"
"                margin-top: 2px; /* make non-selected tabs look smaller */\n"
"            }")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.horizontalLayout_9 = QHBoxLayout(self.tab_7)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_slide = QLabel(self.tab_7)
        self.label_slide.setObjectName(u"label_slide")
        self.label_slide.setMinimumSize(QSize(240, 80))
        self.label_slide.setMaximumSize(QSize(240, 80))
        self.label_slide.setStyleSheet(u"background-color: rgb(186,186,186);")

        self.horizontalLayout_9.addWidget(self.label_slide)

        self.tabWidget_silde_process.addTab(self.tab_7, "")

        self.horizontalLayout.addWidget(self.tabWidget_silde_process)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.horizontalLayout_8.addLayout(self.verticalLayout_2)

        self.tabWidget_run = QTabWidget(self.centralwidget)
        self.tabWidget_run.setObjectName(u"tabWidget_run")
        self.tabWidget_run.setMinimumSize(QSize(325, 0))
        self.tabWidget_run.setMaximumSize(QSize(325, 16777215))
        self.tabWidget_run.setStyleSheet(u"            QTabWidget::pane { /* The tab widget frame */\n"
"                border: 3px solid black; /* \u52a0\u7c97\u8fb9\u754c\u6846 */\n"
"                border-radius: 10px; /* \u5706\u89d2\u534a\u5f84 */\n"
"                background: white;\n"
"            }\n"
"            QTabWidget::tab-bar {\n"
"                left: 5px; /* move to the right by 5px */\n"
"            }\n"
"            /* Style the tab using the tab sub-control. Note that it reads QTabBar not QTabWidget */\n"
"            QTabBar::tab {\n"
"                background: lightgray;\n"
"                border: 3px solid black;\n"
"                padding: 5px;\n"
"                border-top-left-radius: 5px; /* \u9876\u90e8\u5de6\u4fa7\u5706\u89d2 */\n"
"                border-top-right-radius: 5px; /* \u9876\u90e8\u53f3\u4fa7\u5706\u89d2 */\n"
"                font-size: 10px; /* \u8c03\u6574\u5b57\u4f53\u5927\u5c0f */\n"
"            }\n"
"            QTabBar::tab:selected {\n"
"                background: rgb(50,109,245);\n"
"    "
                        "            margin-bottom: 0px; /* overlap with the frame border */\n"
"\n"
"            }\n"
"            QTabBar::tab:!selected {\n"
"                margin-top: 2px; /* make non-selected tabs look smaller */\n"
"            }")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_3 = QVBoxLayout(self.tab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pushButton_run = QPushButton(self.tab)
        self.pushButton_run.setObjectName(u"pushButton_run")
        self.pushButton_run.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_run.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(240, 240, 240); /* \u66f4\u6d45\u7684\u80cc\u666f\u8272 */\n"
"    color: black; /* \u66f4\u6df1\u7684\u6587\u5b57\u989c\u8272 */\n"
"    border-radius: 10px; /* \u5706\u89d2\u534a\u5f84\u51cf\u5c0f\u4e3a10px */\n"
"    padding: 10px;\n"
"    font-size: 16px;\n"
"    border: 4px solid rgb(50,109,245); /* \u7b80\u5316\u8fb9\u6846\u6837\u5f0f */\n"
"    text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(200, 200, 200); /* \u60ac\u505c\u65f6\u7684\u6d45\u7070\u8272\u80cc\u666f */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(56, 64, 85); /* \u6309\u4e0b\u65f6\u7684\u7565\u6df1\u4e00\u4e9b\u7684\u7070\u8272\u80cc\u666f */\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(160, 160, 160); /* \u7981\u7528\u72b6\u6001\u7684\u7565\u6d45\u4e00\u4e9b\u7684\u7070\u8272\u80cc\u666f */\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.pushButton_run)

        self.pushButton_pause = QPushButton(self.tab)
        self.pushButton_pause.setObjectName(u"pushButton_pause")
        self.pushButton_pause.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_pause.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(240, 240, 240); /* \u66f4\u6d45\u7684\u80cc\u666f\u8272 */\n"
"    color: black; /* \u66f4\u6df1\u7684\u6587\u5b57\u989c\u8272 */\n"
"    border-radius: 10px; /* \u5706\u89d2\u534a\u5f84\u51cf\u5c0f\u4e3a10px */\n"
"    padding: 10px;\n"
"    font-size: 16px;\n"
"    border: 4px solid rgb(50,109,245); /* \u7b80\u5316\u8fb9\u6846\u6837\u5f0f */\n"
"    text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(200, 200, 200); /* \u60ac\u505c\u65f6\u7684\u6d45\u7070\u8272\u80cc\u666f */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(56, 64, 85); /* \u6309\u4e0b\u65f6\u7684\u7565\u6df1\u4e00\u4e9b\u7684\u7070\u8272\u80cc\u666f */\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(160, 160, 160); /* \u7981\u7528\u72b6\u6001\u7684\u7565\u6d45\u4e00\u4e9b\u7684\u7070\u8272\u80cc\u666f */\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.pushButton_pause)

        self.pushButton_micro_reset = QPushButton(self.tab)
        self.pushButton_micro_reset.setObjectName(u"pushButton_micro_reset")
        self.pushButton_micro_reset.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_micro_reset.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(240, 240, 240); /* \u66f4\u6d45\u7684\u80cc\u666f\u8272 */\n"
"    color: black; /* \u66f4\u6df1\u7684\u6587\u5b57\u989c\u8272 */\n"
"    border-radius: 10px; /* \u5706\u89d2\u534a\u5f84\u51cf\u5c0f\u4e3a10px */\n"
"    padding: 10px;\n"
"    font-size: 16px;\n"
"    border: 4px solid rgb(50,109,245); /* \u7b80\u5316\u8fb9\u6846\u6837\u5f0f */\n"
"    text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(200, 200, 200); /* \u60ac\u505c\u65f6\u7684\u6d45\u7070\u8272\u80cc\u666f */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(56, 64, 85); /* \u6309\u4e0b\u65f6\u7684\u7565\u6df1\u4e00\u4e9b\u7684\u7070\u8272\u80cc\u666f */\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(160, 160, 160); /* \u7981\u7528\u72b6\u6001\u7684\u7565\u6d45\u4e00\u4e9b\u7684\u7070\u8272\u80cc\u666f */\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.pushButton_micro_reset)

        self.pushButton_loader_reset = QPushButton(self.tab)
        self.pushButton_loader_reset.setObjectName(u"pushButton_loader_reset")
        self.pushButton_loader_reset.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_loader_reset.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(240, 240, 240); /* \u66f4\u6d45\u7684\u80cc\u666f\u8272 */\n"
"    color: black; /* \u66f4\u6df1\u7684\u6587\u5b57\u989c\u8272 */\n"
"    border-radius: 10px; /* \u5706\u89d2\u534a\u5f84\u51cf\u5c0f\u4e3a10px */\n"
"    padding: 10px;\n"
"    font-size: 16px;\n"
"    border: 4px solid rgb(50,109,245); /* \u7b80\u5316\u8fb9\u6846\u6837\u5f0f */\n"
"    text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(200, 200, 200); /* \u60ac\u505c\u65f6\u7684\u6d45\u7070\u8272\u80cc\u666f */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(56, 64, 85); /* \u6309\u4e0b\u65f6\u7684\u7565\u6df1\u4e00\u4e9b\u7684\u7070\u8272\u80cc\u666f */\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(160, 160, 160); /* \u7981\u7528\u72b6\u6001\u7684\u7565\u6d45\u4e00\u4e9b\u7684\u7070\u8272\u80cc\u666f */\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.pushButton_loader_reset)

        self.label_NONE1_9 = QLabel(self.tab)
        self.label_NONE1_9.setObjectName(u"label_NONE1_9")
        self.label_NONE1_9.setMinimumSize(QSize(0, 0))
        self.label_NONE1_9.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_3.addWidget(self.label_NONE1_9)

        self.tabWidget_run.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_7 = QVBoxLayout(self.tab_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.toolBox = QToolBox(self.tab_2)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setMinimumSize(QSize(0, 0))
        self.toolBox.setMaximumSize(QSize(16777215, 16777215))
        self.toolBox.setStyleSheet(u"            QToolBox {\n"
"                border: 2px solid rgb(50,109,245);\n"
"                border-radius: 6px;\n"
"                margin: 0px;\n"
"                padding: 0px;\n"
"            }\n"
"            QToolBox::tab {\n"
"                background-color:  rgb(69, 77, 98);\n"
"                color: white;\n"
"                border: 2px solid black;\n"
"                border-bottom: none;\n"
"                padding: 4px 0px;\n"
"            }\n"
"            QToolBox::tab:selected {\n"
"                background-color: rgb(50,109,245);\n"
"                border-color: gray;\n"
"                border-bottom: 1px solid white;\n"
"            }")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 303, 729))
        self.verticalLayout_9 = QVBoxLayout(self.page_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.checkBox_1 = QCheckBox(self.page_2)
        self.checkBox_1.setObjectName(u"checkBox_1")

        self.verticalLayout_8.addWidget(self.checkBox_1)

        self.checkBox_2 = QCheckBox(self.page_2)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.verticalLayout_8.addWidget(self.checkBox_2)

        self.checkBox_3 = QCheckBox(self.page_2)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.verticalLayout_8.addWidget(self.checkBox_3)

        self.checkBox_4 = QCheckBox(self.page_2)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.verticalLayout_8.addWidget(self.checkBox_4)


        self.verticalLayout_9.addLayout(self.verticalLayout_8)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_slide_number = QLabel(self.page_2)
        self.label_slide_number.setObjectName(u"label_slide_number")
        self.label_slide_number.setMinimumSize(QSize(0, 21))
        self.label_slide_number.setMaximumSize(QSize(16777215, 21))

        self.horizontalLayout_14.addWidget(self.label_slide_number)

        self.spinBox_slide_number = QSpinBox(self.page_2)
        self.spinBox_slide_number.setObjectName(u"spinBox_slide_number")
        self.spinBox_slide_number.setMinimumSize(QSize(0, 21))
        self.spinBox_slide_number.setMaximumSize(QSize(16777215, 21))
        self.spinBox_slide_number.setMaximum(30)

        self.horizontalLayout_14.addWidget(self.spinBox_slide_number)


        self.verticalLayout_9.addLayout(self.horizontalLayout_14)

        self.label_NONE1_2 = QLabel(self.page_2)
        self.label_NONE1_2.setObjectName(u"label_NONE1_2")
        self.label_NONE1_2.setMinimumSize(QSize(0, 0))
        self.label_NONE1_2.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_9.addWidget(self.label_NONE1_2)

        self.toolBox.addItem(self.page_2, u"\u4efb\u52a1\u5206\u914d")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setGeometry(QRect(0, 0, 303, 729))
        self.verticalLayout_11 = QVBoxLayout(self.page_3)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_maxworkers = QLabel(self.page_3)
        self.label_maxworkers.setObjectName(u"label_maxworkers")
        self.label_maxworkers.setMinimumSize(QSize(0, 21))
        self.label_maxworkers.setMaximumSize(QSize(16777215, 21))

        self.horizontalLayout_15.addWidget(self.label_maxworkers)

        self.spinBox_maxworkers = QSpinBox(self.page_3)
        self.spinBox_maxworkers.setObjectName(u"spinBox_maxworkers")
        self.spinBox_maxworkers.setMinimumSize(QSize(0, 21))
        self.spinBox_maxworkers.setMaximumSize(QSize(16777215, 21))
        self.spinBox_maxworkers.setMaximum(10)

        self.horizontalLayout_15.addWidget(self.spinBox_maxworkers)


        self.verticalLayout_10.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_imagestitchsize = QLabel(self.page_3)
        self.label_imagestitchsize.setObjectName(u"label_imagestitchsize")
        self.label_imagestitchsize.setMinimumSize(QSize(0, 21))
        self.label_imagestitchsize.setMaximumSize(QSize(16777215, 21))

        self.horizontalLayout_16.addWidget(self.label_imagestitchsize)

        self.spinBox_imagestitchsize = QSpinBox(self.page_3)
        self.spinBox_imagestitchsize.setObjectName(u"spinBox_imagestitchsize")
        self.spinBox_imagestitchsize.setMinimumSize(QSize(0, 21))
        self.spinBox_imagestitchsize.setMaximumSize(QSize(16777215, 21))
        self.spinBox_imagestitchsize.setMaximum(2560)

        self.horizontalLayout_16.addWidget(self.spinBox_imagestitchsize)


        self.verticalLayout_10.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_AIimage = QLabel(self.page_3)
        self.label_AIimage.setObjectName(u"label_AIimage")
        self.label_AIimage.setMinimumSize(QSize(0, 21))
        self.label_AIimage.setMaximumSize(QSize(16777215, 21))

        self.horizontalLayout_17.addWidget(self.label_AIimage)

        self.spinBox_AIimage = QSpinBox(self.page_3)
        self.spinBox_AIimage.setObjectName(u"spinBox_AIimage")
        self.spinBox_AIimage.setMinimumSize(QSize(0, 21))
        self.spinBox_AIimage.setMaximumSize(QSize(16777215, 21))
        self.spinBox_AIimage.setMaximum(2560)

        self.horizontalLayout_17.addWidget(self.spinBox_AIimage)


        self.verticalLayout_10.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_queuenumber = QLabel(self.page_3)
        self.label_queuenumber.setObjectName(u"label_queuenumber")
        self.label_queuenumber.setMinimumSize(QSize(0, 21))
        self.label_queuenumber.setMaximumSize(QSize(16777215, 21))

        self.horizontalLayout_18.addWidget(self.label_queuenumber)

        self.spinBox_queuenumber = QSpinBox(self.page_3)
        self.spinBox_queuenumber.setObjectName(u"spinBox_queuenumber")
        self.spinBox_queuenumber.setMinimumSize(QSize(0, 21))
        self.spinBox_queuenumber.setMaximumSize(QSize(16777215, 21))
        self.spinBox_queuenumber.setMaximum(2560)

        self.horizontalLayout_18.addWidget(self.spinBox_queuenumber)


        self.verticalLayout_10.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_pixelformat = QLabel(self.page_3)
        self.label_pixelformat.setObjectName(u"label_pixelformat")
        self.label_pixelformat.setMinimumSize(QSize(0, 21))
        self.label_pixelformat.setMaximumSize(QSize(16777215, 21))

        self.horizontalLayout_19.addWidget(self.label_pixelformat)

        self.comboBox_pixelformat = QComboBox(self.page_3)
        self.comboBox_pixelformat.addItem("")
        self.comboBox_pixelformat.addItem("")
        self.comboBox_pixelformat.addItem("")
        self.comboBox_pixelformat.setObjectName(u"comboBox_pixelformat")

        self.horizontalLayout_19.addWidget(self.comboBox_pixelformat)


        self.verticalLayout_10.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_imagequailty = QLabel(self.page_3)
        self.label_imagequailty.setObjectName(u"label_imagequailty")
        self.label_imagequailty.setMinimumSize(QSize(0, 21))
        self.label_imagequailty.setMaximumSize(QSize(16777215, 21))

        self.horizontalLayout_21.addWidget(self.label_imagequailty)

        self.spinBox_imagequailty = QSpinBox(self.page_3)
        self.spinBox_imagequailty.setObjectName(u"spinBox_imagequailty")
        self.spinBox_imagequailty.setMinimumSize(QSize(0, 21))
        self.spinBox_imagequailty.setMaximumSize(QSize(16777215, 21))
        self.spinBox_imagequailty.setMaximum(100)

        self.horizontalLayout_21.addWidget(self.spinBox_imagequailty)


        self.verticalLayout_10.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_89 = QHBoxLayout()
        self.horizontalLayout_89.setObjectName(u"horizontalLayout_89")
        self.label_SavePath = QLabel(self.page_3)
        self.label_SavePath.setObjectName(u"label_SavePath")
        self.label_SavePath.setMinimumSize(QSize(41, 21))
        self.label_SavePath.setMaximumSize(QSize(99999, 21))

        self.horizontalLayout_89.addWidget(self.label_SavePath)

        self.label_savepath = QLabel(self.page_3)
        self.label_savepath.setObjectName(u"label_savepath")
        self.label_savepath.setMinimumSize(QSize(0, 21))
        self.label_savepath.setMaximumSize(QSize(16777215, 21))

        self.horizontalLayout_89.addWidget(self.label_savepath)


        self.verticalLayout_10.addLayout(self.horizontalLayout_89)

        self.pushButton_savepath = QPushButton(self.page_3)
        self.pushButton_savepath.setObjectName(u"pushButton_savepath")
        self.pushButton_savepath.setMinimumSize(QSize(100, 20))
        self.pushButton_savepath.setMaximumSize(QSize(100, 20))
        self.pushButton_savepath.setStyleSheet(u"            QPushButton {\n"
"                border: 2px solid #333;  /* \u8bbe\u7f6e\u8fb9\u6846\u4e3a2px\u5bbd\u5ea6\u7684\u5b9e\u7ebf\uff0c\u989c\u8272\u4e3a\u6df1\u9ed1\u8272(#333) */\n"
"\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #d0d0d0;  /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #b0b0b0;  /* \u6309\u94ae\u6309\u4e0b\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"            }")

        self.verticalLayout_10.addWidget(self.pushButton_savepath)


        self.verticalLayout_11.addLayout(self.verticalLayout_10)

        self.label_NONE1_3 = QLabel(self.page_3)
        self.label_NONE1_3.setObjectName(u"label_NONE1_3")
        self.label_NONE1_3.setMinimumSize(QSize(0, 0))
        self.label_NONE1_3.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_11.addWidget(self.label_NONE1_3)

        self.toolBox.addItem(self.page_3, u"ImageSaver")
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.page_4.setGeometry(QRect(0, 0, 116, 96))
        self.verticalLayout_13 = QVBoxLayout(self.page_4)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_cameranumber = QLabel(self.page_4)
        self.label_cameranumber.setObjectName(u"label_cameranumber")
        self.label_cameranumber.setMinimumSize(QSize(0, 21))
        self.label_cameranumber.setMaximumSize(QSize(16777215, 21))

        self.horizontalLayout_22.addWidget(self.label_cameranumber)

        self.spinBox_cameranumber = QSpinBox(self.page_4)
        self.spinBox_cameranumber.setObjectName(u"spinBox_cameranumber")
        self.spinBox_cameranumber.setMinimumSize(QSize(0, 21))
        self.spinBox_cameranumber.setMaximumSize(QSize(16777215, 21))
        self.spinBox_cameranumber.setMaximum(2)

        self.horizontalLayout_22.addWidget(self.spinBox_cameranumber)


        self.verticalLayout_12.addLayout(self.horizontalLayout_22)

        self.checkBox_loaderflage = QCheckBox(self.page_4)
        self.checkBox_loaderflage.setObjectName(u"checkBox_loaderflage")

        self.verticalLayout_12.addWidget(self.checkBox_loaderflage)

        self.checkBox_microscopeflage = QCheckBox(self.page_4)
        self.checkBox_microscopeflage.setObjectName(u"checkBox_microscopeflage")

        self.verticalLayout_12.addWidget(self.checkBox_microscopeflage)


        self.verticalLayout_13.addLayout(self.verticalLayout_12)

        self.label_NONE1_4 = QLabel(self.page_4)
        self.label_NONE1_4.setObjectName(u"label_NONE1_4")
        self.label_NONE1_4.setMinimumSize(QSize(0, 0))
        self.label_NONE1_4.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_13.addWidget(self.label_NONE1_4)

        self.toolBox.addItem(self.page_4, u"Device")
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.page_5.setGeometry(QRect(0, 0, 303, 729))
        self.verticalLayout_5 = QVBoxLayout(self.page_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_MicroCom = QLabel(self.page_5)
        self.label_MicroCom.setObjectName(u"label_MicroCom")
        self.label_MicroCom.setMinimumSize(QSize(0, 21))
        self.label_MicroCom.setMaximumSize(QSize(16777215, 21))

        self.horizontalLayout_23.addWidget(self.label_MicroCom)

        self.comboBox_MicroCom = QComboBox(self.page_5)
        self.comboBox_MicroCom.addItem("")
        self.comboBox_MicroCom.addItem("")
        self.comboBox_MicroCom.addItem("")
        self.comboBox_MicroCom.addItem("")
        self.comboBox_MicroCom.addItem("")
        self.comboBox_MicroCom.addItem("")
        self.comboBox_MicroCom.addItem("")
        self.comboBox_MicroCom.addItem("")
        self.comboBox_MicroCom.addItem("")
        self.comboBox_MicroCom.addItem("")
        self.comboBox_MicroCom.addItem("")
        self.comboBox_MicroCom.addItem("")
        self.comboBox_MicroCom.addItem("")
        self.comboBox_MicroCom.addItem("")
        self.comboBox_MicroCom.addItem("")
        self.comboBox_MicroCom.addItem("")
        self.comboBox_MicroCom.addItem("")
        self.comboBox_MicroCom.addItem("")
        self.comboBox_MicroCom.addItem("")
        self.comboBox_MicroCom.addItem("")
        self.comboBox_MicroCom.setObjectName(u"comboBox_MicroCom")

        self.horizontalLayout_23.addWidget(self.comboBox_MicroCom)


        self.verticalLayout_4.addLayout(self.horizontalLayout_23)

        self.checkBox_LED = QCheckBox(self.page_5)
        self.checkBox_LED.setObjectName(u"checkBox_LED")

        self.verticalLayout_4.addWidget(self.checkBox_LED)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_50xcenterx = QLabel(self.page_5)
        self.label_50xcenterx.setObjectName(u"label_50xcenterx")
        self.label_50xcenterx.setMinimumSize(QSize(70, 21))
        self.label_50xcenterx.setMaximumSize(QSize(16777215, 21))

        self.horizontalLayout_24.addWidget(self.label_50xcenterx)

        self.doubleSpinBox_50xcenterx = QDoubleSpinBox(self.page_5)
        self.doubleSpinBox_50xcenterx.setObjectName(u"doubleSpinBox_50xcenterx")
        self.doubleSpinBox_50xcenterx.setDecimals(3)
        self.doubleSpinBox_50xcenterx.setMaximum(60.000000000000000)
        self.doubleSpinBox_50xcenterx.setSingleStep(0.100000000000000)

        self.horizontalLayout_24.addWidget(self.doubleSpinBox_50xcenterx)


        self.verticalLayout_4.addLayout(self.horizontalLayout_24)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_50xcentery = QLabel(self.page_5)
        self.label_50xcentery.setObjectName(u"label_50xcentery")
        self.label_50xcentery.setMinimumSize(QSize(0, 21))
        self.label_50xcentery.setMaximumSize(QSize(16777215, 21))

        self.horizontalLayout_25.addWidget(self.label_50xcentery)

        self.doubleSpinBox_50xcentery = QDoubleSpinBox(self.page_5)
        self.doubleSpinBox_50xcentery.setObjectName(u"doubleSpinBox_50xcentery")
        self.doubleSpinBox_50xcentery.setDecimals(3)
        self.doubleSpinBox_50xcentery.setMaximum(60.000000000000000)
        self.doubleSpinBox_50xcentery.setSingleStep(0.100000000000000)

        self.horizontalLayout_25.addWidget(self.doubleSpinBox_50xcentery)


        self.verticalLayout_4.addLayout(self.horizontalLayout_25)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_20xcenterx = QLabel(self.page_5)
        self.label_20xcenterx.setObjectName(u"label_20xcenterx")
        self.label_20xcenterx.setMinimumSize(QSize(0, 21))
        self.label_20xcenterx.setMaximumSize(QSize(16777215, 21))

        self.horizontalLayout_26.addWidget(self.label_20xcenterx)

        self.doubleSpinBox_20xcenterx = QDoubleSpinBox(self.page_5)
        self.doubleSpinBox_20xcenterx.setObjectName(u"doubleSpinBox_20xcenterx")
        self.doubleSpinBox_20xcenterx.setDecimals(3)
        self.doubleSpinBox_20xcenterx.setMaximum(60.000000000000000)
        self.doubleSpinBox_20xcenterx.setSingleStep(0.100000000000000)

        self.horizontalLayout_26.addWidget(self.doubleSpinBox_20xcenterx)


        self.verticalLayout_4.addLayout(self.horizontalLayout_26)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_20xcenterx_2 = QLabel(self.page_5)
        self.label_20xcenterx_2.setObjectName(u"label_20xcenterx_2")
        self.label_20xcenterx_2.setMinimumSize(QSize(0, 21))
        self.label_20xcenterx_2.setMaximumSize(QSize(16777215, 21))

        self.horizontalLayout_27.addWidget(self.label_20xcenterx_2)

        self.doubleSpinBox_20xcentery = QDoubleSpinBox(self.page_5)
        self.doubleSpinBox_20xcentery.setObjectName(u"doubleSpinBox_20xcentery")
        self.doubleSpinBox_20xcentery.setDecimals(3)
        self.doubleSpinBox_20xcentery.setMaximum(60.000000000000000)
        self.doubleSpinBox_20xcentery.setSingleStep(0.100000000000000)

        self.horizontalLayout_27.addWidget(self.doubleSpinBox_20xcentery)


        self.verticalLayout_4.addLayout(self.horizontalLayout_27)

        self.horizontalLayout_76 = QHBoxLayout()
        self.horizontalLayout_76.setObjectName(u"horizontalLayout_76")
        self.label_Onlycenterx = QLabel(self.page_5)
        self.label_Onlycenterx.setObjectName(u"label_Onlycenterx")
        self.label_Onlycenterx.setMinimumSize(QSize(0, 21))
        self.label_Onlycenterx.setMaximumSize(QSize(16777215, 21))

        self.horizontalLayout_76.addWidget(self.label_Onlycenterx)

        self.doubleSpinBox_Onlycenterx = QDoubleSpinBox(self.page_5)
        self.doubleSpinBox_Onlycenterx.setObjectName(u"doubleSpinBox_Onlycenterx")
        self.doubleSpinBox_Onlycenterx.setDecimals(3)
        self.doubleSpinBox_Onlycenterx.setMaximum(60.000000000000000)
        self.doubleSpinBox_Onlycenterx.setSingleStep(0.100000000000000)

        self.horizontalLayout_76.addWidget(self.doubleSpinBox_Onlycenterx)


        self.verticalLayout_4.addLayout(self.horizontalLayout_76)

        self.horizontalLayout_77 = QHBoxLayout()
        self.horizontalLayout_77.setObjectName(u"horizontalLayout_77")
        self.label_Onlycentery = QLabel(self.page_5)
        self.label_Onlycentery.setObjectName(u"label_Onlycentery")
        self.label_Onlycentery.setMinimumSize(QSize(0, 21))
        self.label_Onlycentery.setMaximumSize(QSize(16777215, 21))

        self.horizontalLayout_77.addWidget(self.label_Onlycentery)

        self.doubleSpinBox_Onlycentery = QDoubleSpinBox(self.page_5)
        self.doubleSpinBox_Onlycentery.setObjectName(u"doubleSpinBox_Onlycentery")
        self.doubleSpinBox_Onlycentery.setDecimals(3)
        self.doubleSpinBox_Onlycentery.setMaximum(60.000000000000000)
        self.doubleSpinBox_Onlycentery.setSingleStep(0.100000000000000)

        self.horizontalLayout_77.addWidget(self.doubleSpinBox_Onlycentery)


        self.verticalLayout_4.addLayout(self.horizontalLayout_77)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_scan_w = QLabel(self.page_5)
        self.label_scan_w.setObjectName(u"label_scan_w")
        self.label_scan_w.setMinimumSize(QSize(0, 21))
        self.label_scan_w.setMaximumSize(QSize(16777215, 21))

        self.horizontalLayout_28.addWidget(self.label_scan_w)

        self.spinBox_scan_w = QSpinBox(self.page_5)
        self.spinBox_scan_w.setObjectName(u"spinBox_scan_w")
        self.spinBox_scan_w.setMaximum(30)

        self.horizontalLayout_28.addWidget(self.spinBox_scan_w)


        self.verticalLayout_4.addLayout(self.horizontalLayout_28)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_scan_h = QLabel(self.page_5)
        self.label_scan_h.setObjectName(u"label_scan_h")
        self.label_scan_h.setMinimumSize(QSize(0, 21))
        self.label_scan_h.setMaximumSize(QSize(16777215, 21))

        self.horizontalLayout_29.addWidget(self.label_scan_h)

        self.spinBox_scan_h = QSpinBox(self.page_5)
        self.spinBox_scan_h.setObjectName(u"spinBox_scan_h")
        self.spinBox_scan_h.setMaximum(30)

        self.horizontalLayout_29.addWidget(self.spinBox_scan_h)


        self.verticalLayout_4.addLayout(self.horizontalLayout_29)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label_50xzfocus = QLabel(self.page_5)
        self.label_50xzfocus.setObjectName(u"label_50xzfocus")
        self.label_50xzfocus.setMinimumSize(QSize(0, 21))
        self.label_50xzfocus.setMaximumSize(QSize(16777215, 21))

        self.horizontalLayout_30.addWidget(self.label_50xzfocus)

        self.doubleSpinBox_50xzfocus = QDoubleSpinBox(self.page_5)
        self.doubleSpinBox_50xzfocus.setObjectName(u"doubleSpinBox_50xzfocus")
        self.doubleSpinBox_50xzfocus.setDecimals(3)
        self.doubleSpinBox_50xzfocus.setMaximum(8.000000000000000)
        self.doubleSpinBox_50xzfocus.setSingleStep(0.001000000000000)
        self.doubleSpinBox_50xzfocus.setStepType(QAbstractSpinBox.DefaultStepType)

        self.horizontalLayout_30.addWidget(self.doubleSpinBox_50xzfocus)


        self.verticalLayout_4.addLayout(self.horizontalLayout_30)

        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.label_20xzfocus = QLabel(self.page_5)
        self.label_20xzfocus.setObjectName(u"label_20xzfocus")
        self.label_20xzfocus.setMinimumSize(QSize(0, 21))
        self.label_20xzfocus.setMaximumSize(QSize(16777215, 21))

        self.horizontalLayout_32.addWidget(self.label_20xzfocus)

        self.doubleSpinBox_20xzfocus = QDoubleSpinBox(self.page_5)
        self.doubleSpinBox_20xzfocus.setObjectName(u"doubleSpinBox_20xzfocus")
        self.doubleSpinBox_20xzfocus.setDecimals(3)
        self.doubleSpinBox_20xzfocus.setMaximum(8.000000000000000)
        self.doubleSpinBox_20xzfocus.setSingleStep(0.001000000000000)

        self.horizontalLayout_32.addWidget(self.doubleSpinBox_20xzfocus)


        self.verticalLayout_4.addLayout(self.horizontalLayout_32)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.label_Onlyzfocus = QLabel(self.page_5)
        self.label_Onlyzfocus.setObjectName(u"label_Onlyzfocus")
        self.label_Onlyzfocus.setMinimumSize(QSize(0, 21))
        self.label_Onlyzfocus.setMaximumSize(QSize(16777215, 21))

        self.horizontalLayout_31.addWidget(self.label_Onlyzfocus)

        self.doubleSpinBox_Onlyzfocus = QDoubleSpinBox(self.page_5)
        self.doubleSpinBox_Onlyzfocus.setObjectName(u"doubleSpinBox_Onlyzfocus")
        self.doubleSpinBox_Onlyzfocus.setDecimals(3)
        self.doubleSpinBox_Onlyzfocus.setMaximum(8.000000000000000)
        self.doubleSpinBox_Onlyzfocus.setSingleStep(0.001000000000000)
        self.doubleSpinBox_Onlyzfocus.setStepType(QAbstractSpinBox.DefaultStepType)

        self.horizontalLayout_31.addWidget(self.doubleSpinBox_Onlyzfocus)


        self.verticalLayout_4.addLayout(self.horizontalLayout_31)

        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.label_FocusMethod = QLabel(self.page_5)
        self.label_FocusMethod.setObjectName(u"label_FocusMethod")
        self.label_FocusMethod.setMinimumSize(QSize(0, 21))
        self.label_FocusMethod.setMaximumSize(QSize(16777215, 21))

        self.horizontalLayout_33.addWidget(self.label_FocusMethod)

        self.comboBox_FocusMethod = QComboBox(self.page_5)
        self.comboBox_FocusMethod.addItem("")
        self.comboBox_FocusMethod.addItem("")
        self.comboBox_FocusMethod.addItem("")
        self.comboBox_FocusMethod.setObjectName(u"comboBox_FocusMethod")

        self.horizontalLayout_33.addWidget(self.comboBox_FocusMethod)


        self.verticalLayout_4.addLayout(self.horizontalLayout_33)

        self.horizontalLayout_85 = QHBoxLayout()
        self.horizontalLayout_85.setObjectName(u"horizontalLayout_85")
        self.label_system = QLabel(self.page_5)
        self.label_system.setObjectName(u"label_system")
        self.label_system.setMinimumSize(QSize(0, 21))
        self.label_system.setMaximumSize(QSize(16777215, 21))

        self.horizontalLayout_85.addWidget(self.label_system)

        self.comboBox_Objective_SYS = QComboBox(self.page_5)
        self.comboBox_Objective_SYS.addItem("")
        self.comboBox_Objective_SYS.addItem("")
        self.comboBox_Objective_SYS.setObjectName(u"comboBox_Objective_SYS")

        self.horizontalLayout_85.addWidget(self.comboBox_Objective_SYS)


        self.verticalLayout_4.addLayout(self.horizontalLayout_85)

        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.label_Objective = QLabel(self.page_5)
        self.label_Objective.setObjectName(u"label_Objective")
        self.label_Objective.setMinimumSize(QSize(0, 21))
        self.label_Objective.setMaximumSize(QSize(16777215, 21))

        self.horizontalLayout_34.addWidget(self.label_Objective)

        self.comboBox_Objective = QComboBox(self.page_5)
        self.comboBox_Objective.addItem("")
        self.comboBox_Objective.addItem("")
        self.comboBox_Objective.addItem("")
        self.comboBox_Objective.addItem("")
        self.comboBox_Objective.setObjectName(u"comboBox_Objective")

        self.horizontalLayout_34.addWidget(self.comboBox_Objective)


        self.verticalLayout_4.addLayout(self.horizontalLayout_34)

        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.label_FocusNumber = QLabel(self.page_5)
        self.label_FocusNumber.setObjectName(u"label_FocusNumber")
        self.label_FocusNumber.setMinimumSize(QSize(0, 21))
        self.label_FocusNumber.setMaximumSize(QSize(16777215, 21))

        self.horizontalLayout_35.addWidget(self.label_FocusNumber)

        self.spinBox_FocusNumber = QSpinBox(self.page_5)
        self.spinBox_FocusNumber.setObjectName(u"spinBox_FocusNumber")
        self.spinBox_FocusNumber.setMaximum(100)

        self.horizontalLayout_35.addWidget(self.spinBox_FocusNumber)


        self.verticalLayout_4.addLayout(self.horizontalLayout_35)

        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.label_FocusStep = QLabel(self.page_5)
        self.label_FocusStep.setObjectName(u"label_FocusStep")
        self.label_FocusStep.setMinimumSize(QSize(0, 21))
        self.label_FocusStep.setMaximumSize(QSize(16777215, 21))

        self.horizontalLayout_36.addWidget(self.label_FocusStep)

        self.doubleSpinBox_FocusStep = QDoubleSpinBox(self.page_5)
        self.doubleSpinBox_FocusStep.setObjectName(u"doubleSpinBox_FocusStep")
        self.doubleSpinBox_FocusStep.setDecimals(3)
        self.doubleSpinBox_FocusStep.setMaximum(0.100000000000000)
        self.doubleSpinBox_FocusStep.setSingleStep(0.001000000000000)

        self.horizontalLayout_36.addWidget(self.doubleSpinBox_FocusStep)


        self.verticalLayout_4.addLayout(self.horizontalLayout_36)

        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.label_FocusGap_number = QLabel(self.page_5)
        self.label_FocusGap_number.setObjectName(u"label_FocusGap_number")
        self.label_FocusGap_number.setMinimumSize(QSize(0, 21))
        self.label_FocusGap_number.setMaximumSize(QSize(16777215, 21))

        self.horizontalLayout_37.addWidget(self.label_FocusGap_number)

        self.spinBox_FocusGap_number = QSpinBox(self.page_5)
        self.spinBox_FocusGap_number.setObjectName(u"spinBox_FocusGap_number")
        self.spinBox_FocusGap_number.setMaximum(30)

        self.horizontalLayout_37.addWidget(self.spinBox_FocusGap_number)


        self.verticalLayout_4.addLayout(self.horizontalLayout_37)

        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.label_connect_loader_x = QLabel(self.page_5)
        self.label_connect_loader_x.setObjectName(u"label_connect_loader_x")
        self.label_connect_loader_x.setMinimumSize(QSize(0, 21))
        self.label_connect_loader_x.setMaximumSize(QSize(16777215, 21))

        self.horizontalLayout_38.addWidget(self.label_connect_loader_x)

        self.doubleSpinBox_connect_loader_x = QDoubleSpinBox(self.page_5)
        self.doubleSpinBox_connect_loader_x.setObjectName(u"doubleSpinBox_connect_loader_x")
        self.doubleSpinBox_connect_loader_x.setDecimals(3)
        self.doubleSpinBox_connect_loader_x.setMaximum(60.000000000000000)
        self.doubleSpinBox_connect_loader_x.setSingleStep(0.100000000000000)

        self.horizontalLayout_38.addWidget(self.doubleSpinBox_connect_loader_x)


        self.verticalLayout_4.addLayout(self.horizontalLayout_38)

        self.horizontalLayout_39 = QHBoxLayout()
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.label_connect_loader_y = QLabel(self.page_5)
        self.label_connect_loader_y.setObjectName(u"label_connect_loader_y")
        self.label_connect_loader_y.setMinimumSize(QSize(0, 21))
        self.label_connect_loader_y.setMaximumSize(QSize(16777215, 21))

        self.horizontalLayout_39.addWidget(self.label_connect_loader_y)

        self.doubleSpinBox_connect_loader_y = QDoubleSpinBox(self.page_5)
        self.doubleSpinBox_connect_loader_y.setObjectName(u"doubleSpinBox_connect_loader_y")
        self.doubleSpinBox_connect_loader_y.setDecimals(3)
        self.doubleSpinBox_connect_loader_y.setMaximum(60.000000000000000)
        self.doubleSpinBox_connect_loader_y.setSingleStep(0.100000000000000)

        self.horizontalLayout_39.addWidget(self.doubleSpinBox_connect_loader_y)


        self.verticalLayout_4.addLayout(self.horizontalLayout_39)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.label_NONE1_5 = QLabel(self.page_5)
        self.label_NONE1_5.setObjectName(u"label_NONE1_5")
        self.label_NONE1_5.setMinimumSize(QSize(0, 0))
        self.label_NONE1_5.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_5.addWidget(self.label_NONE1_5)

        self.toolBox.addItem(self.page_5, u"Microscope")
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.page_6.setGeometry(QRect(0, 0, 168, 349))
        self.verticalLayout_17 = QVBoxLayout(self.page_6)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.horizontalLayout_40 = QHBoxLayout()
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.label_50xCalibration = QLabel(self.page_6)
        self.label_50xCalibration.setObjectName(u"label_50xCalibration")
        self.label_50xCalibration.setMinimumSize(QSize(0, 21))
        self.label_50xCalibration.setMaximumSize(QSize(16777215, 21))

        self.horizontalLayout_40.addWidget(self.label_50xCalibration)

        self.doubleSpinBox_50xCalibration = QDoubleSpinBox(self.page_6)
        self.doubleSpinBox_50xCalibration.setObjectName(u"doubleSpinBox_50xCalibration")
        self.doubleSpinBox_50xCalibration.setDecimals(6)
        self.doubleSpinBox_50xCalibration.setMaximum(10.000000000000000)
        self.doubleSpinBox_50xCalibration.setSingleStep(0.100000000000000)

        self.horizontalLayout_40.addWidget(self.doubleSpinBox_50xCalibration)


        self.verticalLayout_16.addLayout(self.horizontalLayout_40)

        self.horizontalLayout_41 = QHBoxLayout()
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.label_20xCalibration = QLabel(self.page_6)
        self.label_20xCalibration.setObjectName(u"label_20xCalibration")
        self.label_20xCalibration.setMinimumSize(QSize(0, 21))
        self.label_20xCalibration.setMaximumSize(QSize(16777215, 21))

        self.horizontalLayout_41.addWidget(self.label_20xCalibration)

        self.doubleSpinBox_20xCalibration = QDoubleSpinBox(self.page_6)
        self.doubleSpinBox_20xCalibration.setObjectName(u"doubleSpinBox_20xCalibration")
        self.doubleSpinBox_20xCalibration.setDecimals(6)
        self.doubleSpinBox_20xCalibration.setMaximum(10.000000000000000)
        self.doubleSpinBox_20xCalibration.setSingleStep(0.100000000000000)

        self.horizontalLayout_41.addWidget(self.doubleSpinBox_20xCalibration)


        self.verticalLayout_16.addLayout(self.horizontalLayout_41)

        self.horizontalLayout_78 = QHBoxLayout()
        self.horizontalLayout_78.setObjectName(u"horizontalLayout_78")
        self.label_OnlyCalibration = QLabel(self.page_6)
        self.label_OnlyCalibration.setObjectName(u"label_OnlyCalibration")
        self.label_OnlyCalibration.setMinimumSize(QSize(0, 21))
        self.label_OnlyCalibration.setMaximumSize(QSize(16777215, 21))

        self.horizontalLayout_78.addWidget(self.label_OnlyCalibration)

        self.doubleSpinBox_OnlyCalibration = QDoubleSpinBox(self.page_6)
        self.doubleSpinBox_OnlyCalibration.setObjectName(u"doubleSpinBox_OnlyCalibration")
        self.doubleSpinBox_OnlyCalibration.setDecimals(6)
        self.doubleSpinBox_OnlyCalibration.setMaximum(10.000000000000000)
        self.doubleSpinBox_OnlyCalibration.setSingleStep(0.100000000000000)

        self.horizontalLayout_78.addWidget(self.doubleSpinBox_OnlyCalibration)


        self.verticalLayout_16.addLayout(self.horizontalLayout_78)

        self.horizontalLayout_42 = QHBoxLayout()
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.label_50xWB_R = QLabel(self.page_6)
        self.label_50xWB_R.setObjectName(u"label_50xWB_R")
        self.label_50xWB_R.setMinimumSize(QSize(0, 21))
        self.label_50xWB_R.setMaximumSize(QSize(16777215, 21))

        self.horizontalLayout_42.addWidget(self.label_50xWB_R)

        self.doubleSpinBox_50xWB_R = QDoubleSpinBox(self.page_6)
        self.doubleSpinBox_50xWB_R.setObjectName(u"doubleSpinBox_50xWB_R")
        self.doubleSpinBox_50xWB_R.setDecimals(6)
        self.doubleSpinBox_50xWB_R.setMaximum(10.000000000000000)
        self.doubleSpinBox_50xWB_R.setSingleStep(0.100000000000000)

        self.horizontalLayout_42.addWidget(self.doubleSpinBox_50xWB_R)


        self.verticalLayout_16.addLayout(self.horizontalLayout_42)

        self.horizontalLayout_43 = QHBoxLayout()
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.label_50xWB_G = QLabel(self.page_6)
        self.label_50xWB_G.setObjectName(u"label_50xWB_G")
        self.label_50xWB_G.setMinimumSize(QSize(0, 21))
        self.label_50xWB_G.setMaximumSize(QSize(16777215, 21))

        self.horizontalLayout_43.addWidget(self.label_50xWB_G)

        self.doubleSpinBox_50xWB_G = QDoubleSpinBox(self.page_6)
        self.doubleSpinBox_50xWB_G.setObjectName(u"doubleSpinBox_50xWB_G")
        self.doubleSpinBox_50xWB_G.setDecimals(6)
        self.doubleSpinBox_50xWB_G.setMaximum(10.000000000000000)
        self.doubleSpinBox_50xWB_G.setSingleStep(0.100000000000000)

        self.horizontalLayout_43.addWidget(self.doubleSpinBox_50xWB_G)


        self.verticalLayout_16.addLayout(self.horizontalLayout_43)

        self.horizontalLayout_44 = QHBoxLayout()
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.label_50xWB_B = QLabel(self.page_6)
        self.label_50xWB_B.setObjectName(u"label_50xWB_B")
        self.label_50xWB_B.setMinimumSize(QSize(0, 21))
        self.label_50xWB_B.setMaximumSize(QSize(16777215, 21))

        self.horizontalLayout_44.addWidget(self.label_50xWB_B)

        self.doubleSpinBox_50xWB_B = QDoubleSpinBox(self.page_6)
        self.doubleSpinBox_50xWB_B.setObjectName(u"doubleSpinBox_50xWB_B")
        self.doubleSpinBox_50xWB_B.setDecimals(6)
        self.doubleSpinBox_50xWB_B.setMaximum(10.000000000000000)
        self.doubleSpinBox_50xWB_B.setSingleStep(0.100000000000000)

        self.horizontalLayout_44.addWidget(self.doubleSpinBox_50xWB_B)


        self.verticalLayout_16.addLayout(self.horizontalLayout_44)

        self.horizontalLayout_45 = QHBoxLayout()
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.label_20xWB_R = QLabel(self.page_6)
        self.label_20xWB_R.setObjectName(u"label_20xWB_R")
        self.label_20xWB_R.setMinimumSize(QSize(0, 21))
        self.label_20xWB_R.setMaximumSize(QSize(16777215, 21))

        self.horizontalLayout_45.addWidget(self.label_20xWB_R)

        self.doubleSpinBox_20xWB_R = QDoubleSpinBox(self.page_6)
        self.doubleSpinBox_20xWB_R.setObjectName(u"doubleSpinBox_20xWB_R")
        self.doubleSpinBox_20xWB_R.setDecimals(6)
        self.doubleSpinBox_20xWB_R.setMaximum(10.000000000000000)
        self.doubleSpinBox_20xWB_R.setSingleStep(0.100000000000000)

        self.horizontalLayout_45.addWidget(self.doubleSpinBox_20xWB_R)


        self.verticalLayout_16.addLayout(self.horizontalLayout_45)

        self.horizontalLayout_46 = QHBoxLayout()
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.label_20xWB_G = QLabel(self.page_6)
        self.label_20xWB_G.setObjectName(u"label_20xWB_G")
        self.label_20xWB_G.setMinimumSize(QSize(0, 21))
        self.label_20xWB_G.setMaximumSize(QSize(16777215, 21))

        self.horizontalLayout_46.addWidget(self.label_20xWB_G)

        self.doubleSpinBox_20xWB_G = QDoubleSpinBox(self.page_6)
        self.doubleSpinBox_20xWB_G.setObjectName(u"doubleSpinBox_20xWB_G")
        self.doubleSpinBox_20xWB_G.setDecimals(6)
        self.doubleSpinBox_20xWB_G.setMaximum(10.000000000000000)
        self.doubleSpinBox_20xWB_G.setSingleStep(0.100000000000000)

        self.horizontalLayout_46.addWidget(self.doubleSpinBox_20xWB_G)


        self.verticalLayout_16.addLayout(self.horizontalLayout_46)

        self.horizontalLayout_47 = QHBoxLayout()
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.label_20xWB_B = QLabel(self.page_6)
        self.label_20xWB_B.setObjectName(u"label_20xWB_B")
        self.label_20xWB_B.setMinimumSize(QSize(0, 21))
        self.label_20xWB_B.setMaximumSize(QSize(16777215, 21))

        self.horizontalLayout_47.addWidget(self.label_20xWB_B)

        self.doubleSpinBox_20xWB_B = QDoubleSpinBox(self.page_6)
        self.doubleSpinBox_20xWB_B.setObjectName(u"doubleSpinBox_20xWB_B")
        self.doubleSpinBox_20xWB_B.setDecimals(6)
        self.doubleSpinBox_20xWB_B.setMaximum(10.000000000000000)
        self.doubleSpinBox_20xWB_B.setSingleStep(0.100000000000000)

        self.horizontalLayout_47.addWidget(self.doubleSpinBox_20xWB_B)


        self.verticalLayout_16.addLayout(self.horizontalLayout_47)

        self.horizontalLayout_48 = QHBoxLayout()
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.label_OnlyWB_R = QLabel(self.page_6)
        self.label_OnlyWB_R.setObjectName(u"label_OnlyWB_R")
        self.label_OnlyWB_R.setMinimumSize(QSize(0, 21))
        self.label_OnlyWB_R.setMaximumSize(QSize(16777215, 21))

        self.horizontalLayout_48.addWidget(self.label_OnlyWB_R)

        self.doubleSpinBox_OnlyWB_R = QDoubleSpinBox(self.page_6)
        self.doubleSpinBox_OnlyWB_R.setObjectName(u"doubleSpinBox_OnlyWB_R")
        self.doubleSpinBox_OnlyWB_R.setDecimals(6)
        self.doubleSpinBox_OnlyWB_R.setMaximum(10.000000000000000)
        self.doubleSpinBox_OnlyWB_R.setSingleStep(0.100000000000000)

        self.horizontalLayout_48.addWidget(self.doubleSpinBox_OnlyWB_R)


        self.verticalLayout_16.addLayout(self.horizontalLayout_48)

        self.horizontalLayout_49 = QHBoxLayout()
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.label_OnlyWB_G = QLabel(self.page_6)
        self.label_OnlyWB_G.setObjectName(u"label_OnlyWB_G")
        self.label_OnlyWB_G.setMinimumSize(QSize(0, 21))
        self.label_OnlyWB_G.setMaximumSize(QSize(16777215, 21))

        self.horizontalLayout_49.addWidget(self.label_OnlyWB_G)

        self.doubleSpinBox_OnlyWB_G = QDoubleSpinBox(self.page_6)
        self.doubleSpinBox_OnlyWB_G.setObjectName(u"doubleSpinBox_OnlyWB_G")
        self.doubleSpinBox_OnlyWB_G.setDecimals(6)
        self.doubleSpinBox_OnlyWB_G.setMaximum(10.000000000000000)
        self.doubleSpinBox_OnlyWB_G.setSingleStep(0.100000000000000)

        self.horizontalLayout_49.addWidget(self.doubleSpinBox_OnlyWB_G)


        self.verticalLayout_16.addLayout(self.horizontalLayout_49)

        self.horizontalLayout_50 = QHBoxLayout()
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.label_OnlyWB_B = QLabel(self.page_6)
        self.label_OnlyWB_B.setObjectName(u"label_OnlyWB_B")
        self.label_OnlyWB_B.setMinimumSize(QSize(0, 21))
        self.label_OnlyWB_B.setMaximumSize(QSize(16777215, 21))

        self.horizontalLayout_50.addWidget(self.label_OnlyWB_B)

        self.doubleSpinBox_OnlyWB_B = QDoubleSpinBox(self.page_6)
        self.doubleSpinBox_OnlyWB_B.setObjectName(u"doubleSpinBox_OnlyWB_B")
        self.doubleSpinBox_OnlyWB_B.setDecimals(6)
        self.doubleSpinBox_OnlyWB_B.setMaximum(10.000000000000000)
        self.doubleSpinBox_OnlyWB_B.setSingleStep(0.100000000000000)

        self.horizontalLayout_50.addWidget(self.doubleSpinBox_OnlyWB_B)


        self.verticalLayout_16.addLayout(self.horizontalLayout_50)


        self.verticalLayout_17.addLayout(self.verticalLayout_16)

        self.label_NONE1_6 = QLabel(self.page_6)
        self.label_NONE1_6.setObjectName(u"label_NONE1_6")
        self.label_NONE1_6.setMinimumSize(QSize(0, 0))
        self.label_NONE1_6.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_17.addWidget(self.label_NONE1_6)

        self.toolBox.addItem(self.page_6, u"Camera")
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.page_7.setGeometry(QRect(0, 0, 137, 674))
        self.verticalLayout_18 = QVBoxLayout(self.page_7)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_51 = QHBoxLayout()
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.label_LoaderCom = QLabel(self.page_7)
        self.label_LoaderCom.setObjectName(u"label_LoaderCom")
        self.label_LoaderCom.setMinimumSize(QSize(0, 21))
        self.label_LoaderCom.setMaximumSize(QSize(16777215, 21))

        self.horizontalLayout_51.addWidget(self.label_LoaderCom)

        self.comboBox_LoaderCom = QComboBox(self.page_7)
        self.comboBox_LoaderCom.addItem("")
        self.comboBox_LoaderCom.addItem("")
        self.comboBox_LoaderCom.addItem("")
        self.comboBox_LoaderCom.addItem("")
        self.comboBox_LoaderCom.addItem("")
        self.comboBox_LoaderCom.addItem("")
        self.comboBox_LoaderCom.addItem("")
        self.comboBox_LoaderCom.addItem("")
        self.comboBox_LoaderCom.addItem("")
        self.comboBox_LoaderCom.addItem("")
        self.comboBox_LoaderCom.addItem("")
        self.comboBox_LoaderCom.addItem("")
        self.comboBox_LoaderCom.addItem("")
        self.comboBox_LoaderCom.addItem("")
        self.comboBox_LoaderCom.addItem("")
        self.comboBox_LoaderCom.addItem("")
        self.comboBox_LoaderCom.addItem("")
        self.comboBox_LoaderCom.addItem("")
        self.comboBox_LoaderCom.addItem("")
        self.comboBox_LoaderCom.addItem("")
        self.comboBox_LoaderCom.setObjectName(u"comboBox_LoaderCom")

        self.horizontalLayout_51.addWidget(self.comboBox_LoaderCom)


        self.verticalLayout_6.addLayout(self.horizontalLayout_51)

        self.horizontalLayout_52 = QHBoxLayout()
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.label_Box1_startx = QLabel(self.page_7)
        self.label_Box1_startx.setObjectName(u"label_Box1_startx")
        self.label_Box1_startx.setMinimumSize(QSize(0, 21))
        self.label_Box1_startx.setMaximumSize(QSize(16777215, 21))

        self.horizontalLayout_52.addWidget(self.label_Box1_startx)

        self.doubleSpinBox_Box1_startx = QDoubleSpinBox(self.page_7)
        self.doubleSpinBox_Box1_startx.setObjectName(u"doubleSpinBox_Box1_startx")
        self.doubleSpinBox_Box1_startx.setDecimals(3)
        self.doubleSpinBox_Box1_startx.setMaximum(330.000000000000000)
        self.doubleSpinBox_Box1_startx.setSingleStep(0.100000000000000)

        self.horizontalLayout_52.addWidget(self.doubleSpinBox_Box1_startx)


        self.verticalLayout_6.addLayout(self.horizontalLayout_52)

        self.horizontalLayout_53 = QHBoxLayout()
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.label_Box1_startz = QLabel(self.page_7)
        self.label_Box1_startz.setObjectName(u"label_Box1_startz")
        self.label_Box1_startz.setMinimumSize(QSize(0, 21))
        self.label_Box1_startz.setMaximumSize(QSize(16777215, 21))

        self.horizontalLayout_53.addWidget(self.label_Box1_startz)

        self.doubleSpinBox_Box1_startz = QDoubleSpinBox(self.page_7)
        self.doubleSpinBox_Box1_startz.setObjectName(u"doubleSpinBox_Box1_startz")
        self.doubleSpinBox_Box1_startz.setDecimals(3)
        self.doubleSpinBox_Box1_startz.setMaximum(150.000000000000000)
        self.doubleSpinBox_Box1_startz.setSingleStep(0.100000000000000)

        self.horizontalLayout_53.addWidget(self.doubleSpinBox_Box1_startz)


        self.verticalLayout_6.addLayout(self.horizontalLayout_53)

        self.horizontalLayout_54 = QHBoxLayout()
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.label_Box2_startx = QLabel(self.page_7)
        self.label_Box2_startx.setObjectName(u"label_Box2_startx")
        self.label_Box2_startx.setMinimumSize(QSize(0, 21))
        self.label_Box2_startx.setMaximumSize(QSize(16777215, 21))

        self.horizontalLayout_54.addWidget(self.label_Box2_startx)

        self.doubleSpinBox_Box2_startx = QDoubleSpinBox(self.page_7)
        self.doubleSpinBox_Box2_startx.setObjectName(u"doubleSpinBox_Box2_startx")
        self.doubleSpinBox_Box2_startx.setDecimals(3)
        self.doubleSpinBox_Box2_startx.setMaximum(330.000000000000000)
        self.doubleSpinBox_Box2_startx.setSingleStep(0.100000000000000)

        self.horizontalLayout_54.addWidget(self.doubleSpinBox_Box2_startx)


        self.verticalLayout_6.addLayout(self.horizontalLayout_54)

        self.horizontalLayout_55 = QHBoxLayout()
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.label_Box2_startz = QLabel(self.page_7)
        self.label_Box2_startz.setObjectName(u"label_Box2_startz")
        self.label_Box2_startz.setMinimumSize(QSize(0, 21))
        self.label_Box2_startz.setMaximumSize(QSize(16777215, 21))

        self.horizontalLayout_55.addWidget(self.label_Box2_startz)

        self.doubleSpinBox_Box2_startz = QDoubleSpinBox(self.page_7)
        self.doubleSpinBox_Box2_startz.setObjectName(u"doubleSpinBox_Box2_startz")
        self.doubleSpinBox_Box2_startz.setDecimals(3)
        self.doubleSpinBox_Box2_startz.setMaximum(150.000000000000000)
        self.doubleSpinBox_Box2_startz.setSingleStep(0.100000000000000)

        self.horizontalLayout_55.addWidget(self.doubleSpinBox_Box2_startz)


        self.verticalLayout_6.addLayout(self.horizontalLayout_55)

        self.horizontalLayout_56 = QHBoxLayout()
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.label_Box3_startx = QLabel(self.page_7)
        self.label_Box3_startx.setObjectName(u"label_Box3_startx")
        self.label_Box3_startx.setMinimumSize(QSize(0, 21))
        self.label_Box3_startx.setMaximumSize(QSize(16777215, 21))

        self.horizontalLayout_56.addWidget(self.label_Box3_startx)

        self.doubleSpinBox_Box3_startx = QDoubleSpinBox(self.page_7)
        self.doubleSpinBox_Box3_startx.setObjectName(u"doubleSpinBox_Box3_startx")
        self.doubleSpinBox_Box3_startx.setDecimals(3)
        self.doubleSpinBox_Box3_startx.setMaximum(330.000000000000000)
        self.doubleSpinBox_Box3_startx.setSingleStep(0.100000000000000)

        self.horizontalLayout_56.addWidget(self.doubleSpinBox_Box3_startx)


        self.verticalLayout_6.addLayout(self.horizontalLayout_56)

        self.horizontalLayout_57 = QHBoxLayout()
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.label_Box3_startz = QLabel(self.page_7)
        self.label_Box3_startz.setObjectName(u"label_Box3_startz")
        self.label_Box3_startz.setMinimumSize(QSize(0, 21))
        self.label_Box3_startz.setMaximumSize(QSize(16777215, 21))

        self.horizontalLayout_57.addWidget(self.label_Box3_startz)

        self.doubleSpinBox_Box3_startz = QDoubleSpinBox(self.page_7)
        self.doubleSpinBox_Box3_startz.setObjectName(u"doubleSpinBox_Box3_startz")
        self.doubleSpinBox_Box3_startz.setDecimals(3)
        self.doubleSpinBox_Box3_startz.setMaximum(150.000000000000000)
        self.doubleSpinBox_Box3_startz.setSingleStep(0.100000000000000)

        self.horizontalLayout_57.addWidget(self.doubleSpinBox_Box3_startz)


        self.verticalLayout_6.addLayout(self.horizontalLayout_57)

        self.horizontalLayout_58 = QHBoxLayout()
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.label_Box4_startx = QLabel(self.page_7)
        self.label_Box4_startx.setObjectName(u"label_Box4_startx")
        self.label_Box4_startx.setMinimumSize(QSize(0, 21))
        self.label_Box4_startx.setMaximumSize(QSize(16777215, 21))

        self.horizontalLayout_58.addWidget(self.label_Box4_startx)

        self.doubleSpinBox_Box4_startx = QDoubleSpinBox(self.page_7)
        self.doubleSpinBox_Box4_startx.setObjectName(u"doubleSpinBox_Box4_startx")
        self.doubleSpinBox_Box4_startx.setDecimals(3)
        self.doubleSpinBox_Box4_startx.setMaximum(330.000000000000000)
        self.doubleSpinBox_Box4_startx.setSingleStep(0.001000000000000)

        self.horizontalLayout_58.addWidget(self.doubleSpinBox_Box4_startx)


        self.verticalLayout_6.addLayout(self.horizontalLayout_58)

        self.horizontalLayout_59 = QHBoxLayout()
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.label_Box4_startz = QLabel(self.page_7)
        self.label_Box4_startz.setObjectName(u"label_Box4_startz")
        self.label_Box4_startz.setMinimumSize(QSize(0, 21))
        self.label_Box4_startz.setMaximumSize(QSize(16777215, 21))

        self.horizontalLayout_59.addWidget(self.label_Box4_startz)

        self.doubleSpinBox_Box4_startz = QDoubleSpinBox(self.page_7)
        self.doubleSpinBox_Box4_startz.setObjectName(u"doubleSpinBox_Box4_startz")
        self.doubleSpinBox_Box4_startz.setDecimals(3)
        self.doubleSpinBox_Box4_startz.setMaximum(150.000000000000000)
        self.doubleSpinBox_Box4_startz.setSingleStep(0.001000000000000)

        self.horizontalLayout_59.addWidget(self.doubleSpinBox_Box4_startz)


        self.verticalLayout_6.addLayout(self.horizontalLayout_59)

        self.horizontalLayout_60 = QHBoxLayout()
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.label_BoxXGap = QLabel(self.page_7)
        self.label_BoxXGap.setObjectName(u"label_BoxXGap")
        self.label_BoxXGap.setMinimumSize(QSize(0, 21))
        self.label_BoxXGap.setMaximumSize(QSize(16777215, 21))

        self.horizontalLayout_60.addWidget(self.label_BoxXGap)

        self.doubleSpinBox_BoxXGap = QDoubleSpinBox(self.page_7)
        self.doubleSpinBox_BoxXGap.setObjectName(u"doubleSpinBox_BoxXGap")
        self.doubleSpinBox_BoxXGap.setDecimals(3)
        self.doubleSpinBox_BoxXGap.setMaximum(70.000000000000000)
        self.doubleSpinBox_BoxXGap.setSingleStep(0.100000000000000)

        self.horizontalLayout_60.addWidget(self.doubleSpinBox_BoxXGap)


        self.verticalLayout_6.addLayout(self.horizontalLayout_60)

        self.horizontalLayout_63 = QHBoxLayout()
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.label_BoxZGap = QLabel(self.page_7)
        self.label_BoxZGap.setObjectName(u"label_BoxZGap")
        self.label_BoxZGap.setMinimumSize(QSize(0, 21))
        self.label_BoxZGap.setMaximumSize(QSize(16777215, 21))

        self.horizontalLayout_63.addWidget(self.label_BoxZGap)

        self.doubleSpinBox_BoxZGap = QDoubleSpinBox(self.page_7)
        self.doubleSpinBox_BoxZGap.setObjectName(u"doubleSpinBox_BoxZGap")
        self.doubleSpinBox_BoxZGap.setDecimals(3)
        self.doubleSpinBox_BoxZGap.setMaximum(6.000000000000000)
        self.doubleSpinBox_BoxZGap.setSingleStep(0.010000000000000)

        self.horizontalLayout_63.addWidget(self.doubleSpinBox_BoxZGap)


        self.verticalLayout_6.addLayout(self.horizontalLayout_63)

        self.horizontalLayout_61 = QHBoxLayout()
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.label_slide_push = QLabel(self.page_7)
        self.label_slide_push.setObjectName(u"label_slide_push")
        self.label_slide_push.setMinimumSize(QSize(0, 21))
        self.label_slide_push.setMaximumSize(QSize(16777215, 21))

        self.horizontalLayout_61.addWidget(self.label_slide_push)

        self.spinBox_slide_push = QSpinBox(self.page_7)
        self.spinBox_slide_push.setObjectName(u"spinBox_slide_push")
        self.spinBox_slide_push.setMaximum(2000)

        self.horizontalLayout_61.addWidget(self.spinBox_slide_push)


        self.verticalLayout_6.addLayout(self.horizontalLayout_61)

        self.horizontalLayout_62 = QHBoxLayout()
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.label_slide_return = QLabel(self.page_7)
        self.label_slide_return.setObjectName(u"label_slide_return")
        self.label_slide_return.setMinimumSize(QSize(0, 21))
        self.label_slide_return.setMaximumSize(QSize(16777215, 21))

        self.horizontalLayout_62.addWidget(self.label_slide_return)

        self.spinBox_slide_return = QSpinBox(self.page_7)
        self.spinBox_slide_return.setObjectName(u"spinBox_slide_return")
        self.spinBox_slide_return.setMaximum(800)

        self.horizontalLayout_62.addWidget(self.spinBox_slide_return)


        self.verticalLayout_6.addLayout(self.horizontalLayout_62)

        self.horizontalLayout_67 = QHBoxLayout()
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.label_Xavoid = QLabel(self.page_7)
        self.label_Xavoid.setObjectName(u"label_Xavoid")
        self.label_Xavoid.setMinimumSize(QSize(0, 21))
        self.label_Xavoid.setMaximumSize(QSize(16777215, 21))

        self.horizontalLayout_67.addWidget(self.label_Xavoid)

        self.doubleSpinBox_Xavoid = QDoubleSpinBox(self.page_7)
        self.doubleSpinBox_Xavoid.setObjectName(u"doubleSpinBox_Xavoid")
        self.doubleSpinBox_Xavoid.setDecimals(3)
        self.doubleSpinBox_Xavoid.setMaximum(6.000000000000000)
        self.doubleSpinBox_Xavoid.setSingleStep(0.010000000000000)

        self.horizontalLayout_67.addWidget(self.doubleSpinBox_Xavoid)


        self.verticalLayout_6.addLayout(self.horizontalLayout_67)

        self.horizontalLayout_64 = QHBoxLayout()
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.label_Zlift = QLabel(self.page_7)
        self.label_Zlift.setObjectName(u"label_Zlift")
        self.label_Zlift.setMinimumSize(QSize(0, 21))
        self.label_Zlift.setMaximumSize(QSize(16777215, 21))

        self.horizontalLayout_64.addWidget(self.label_Zlift)

        self.doubleSpinBox_Zlift = QDoubleSpinBox(self.page_7)
        self.doubleSpinBox_Zlift.setObjectName(u"doubleSpinBox_Zlift")
        self.doubleSpinBox_Zlift.setDecimals(3)
        self.doubleSpinBox_Zlift.setMaximum(6.000000000000000)
        self.doubleSpinBox_Zlift.setSingleStep(0.010000000000000)

        self.horizontalLayout_64.addWidget(self.doubleSpinBox_Zlift)


        self.verticalLayout_6.addLayout(self.horizontalLayout_64)

        self.horizontalLayout_65 = QHBoxLayout()
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.label_connect_micro_x = QLabel(self.page_7)
        self.label_connect_micro_x.setObjectName(u"label_connect_micro_x")
        self.label_connect_micro_x.setMinimumSize(QSize(0, 21))
        self.label_connect_micro_x.setMaximumSize(QSize(16777215, 21))

        self.horizontalLayout_65.addWidget(self.label_connect_micro_x)

        self.doubleSpinBox_connect_micro_x = QDoubleSpinBox(self.page_7)
        self.doubleSpinBox_connect_micro_x.setObjectName(u"doubleSpinBox_connect_micro_x")
        self.doubleSpinBox_connect_micro_x.setDecimals(3)
        self.doubleSpinBox_connect_micro_x.setMaximum(100.000000000000000)
        self.doubleSpinBox_connect_micro_x.setSingleStep(0.100000000000000)

        self.horizontalLayout_65.addWidget(self.doubleSpinBox_connect_micro_x)


        self.verticalLayout_6.addLayout(self.horizontalLayout_65)

        self.horizontalLayout_66 = QHBoxLayout()
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.label_connect_micro_z = QLabel(self.page_7)
        self.label_connect_micro_z.setObjectName(u"label_connect_micro_z")
        self.label_connect_micro_z.setMinimumSize(QSize(0, 21))
        self.label_connect_micro_z.setMaximumSize(QSize(16777215, 21))

        self.horizontalLayout_66.addWidget(self.label_connect_micro_z)

        self.doubleSpinBox_connect_micro_z = QDoubleSpinBox(self.page_7)
        self.doubleSpinBox_connect_micro_z.setObjectName(u"doubleSpinBox_connect_micro_z")
        self.doubleSpinBox_connect_micro_z.setDecimals(3)
        self.doubleSpinBox_connect_micro_z.setMaximum(200.000000000000000)
        self.doubleSpinBox_connect_micro_z.setSingleStep(0.100000000000000)

        self.horizontalLayout_66.addWidget(self.doubleSpinBox_connect_micro_z)


        self.verticalLayout_6.addLayout(self.horizontalLayout_66)

        self.horizontalLayout_68 = QHBoxLayout()
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.label_cameraindex = QLabel(self.page_7)
        self.label_cameraindex.setObjectName(u"label_cameraindex")
        self.label_cameraindex.setMinimumSize(QSize(0, 21))
        self.label_cameraindex.setMaximumSize(QSize(16777215, 21))

        self.horizontalLayout_68.addWidget(self.label_cameraindex)

        self.spinBox_cameraindex = QSpinBox(self.page_7)
        self.spinBox_cameraindex.setObjectName(u"spinBox_cameraindex")

        self.horizontalLayout_68.addWidget(self.spinBox_cameraindex)


        self.verticalLayout_6.addLayout(self.horizontalLayout_68)

        self.horizontalLayout_69 = QHBoxLayout()
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.label_cameraexposure = QLabel(self.page_7)
        self.label_cameraexposure.setObjectName(u"label_cameraexposure")
        self.label_cameraexposure.setMinimumSize(QSize(0, 21))
        self.label_cameraexposure.setMaximumSize(QSize(16777215, 21))

        self.horizontalLayout_69.addWidget(self.label_cameraexposure)

        self.spinBox_cameraexposure = QSpinBox(self.page_7)
        self.spinBox_cameraexposure.setObjectName(u"spinBox_cameraexposure")
        self.spinBox_cameraexposure.setMinimum(-10)
        self.spinBox_cameraexposure.setMaximum(10)

        self.horizontalLayout_69.addWidget(self.spinBox_cameraexposure)


        self.verticalLayout_6.addLayout(self.horizontalLayout_69)

        self.horizontalLayout_70 = QHBoxLayout()
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.label_zcamera = QLabel(self.page_7)
        self.label_zcamera.setObjectName(u"label_zcamera")
        self.label_zcamera.setMinimumSize(QSize(0, 21))
        self.label_zcamera.setMaximumSize(QSize(16777215, 21))

        self.horizontalLayout_70.addWidget(self.label_zcamera)

        self.doubleSpinBox_zcamera = QDoubleSpinBox(self.page_7)
        self.doubleSpinBox_zcamera.setObjectName(u"doubleSpinBox_zcamera")
        self.doubleSpinBox_zcamera.setDecimals(3)
        self.doubleSpinBox_zcamera.setMaximum(130.000000000000000)
        self.doubleSpinBox_zcamera.setSingleStep(0.010000000000000)

        self.horizontalLayout_70.addWidget(self.doubleSpinBox_zcamera)


        self.verticalLayout_6.addLayout(self.horizontalLayout_70)

        self.horizontalLayout_71 = QHBoxLayout()
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.label_rectangleX1 = QLabel(self.page_7)
        self.label_rectangleX1.setObjectName(u"label_rectangleX1")
        self.label_rectangleX1.setMinimumSize(QSize(0, 21))
        self.label_rectangleX1.setMaximumSize(QSize(16777215, 21))

        self.horizontalLayout_71.addWidget(self.label_rectangleX1)

        self.spinBox_rectangleX1 = QSpinBox(self.page_7)
        self.spinBox_rectangleX1.setObjectName(u"spinBox_rectangleX1")
        self.spinBox_rectangleX1.setMaximum(2000)

        self.horizontalLayout_71.addWidget(self.spinBox_rectangleX1)


        self.verticalLayout_6.addLayout(self.horizontalLayout_71)

        self.horizontalLayout_72 = QHBoxLayout()
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.label_rectangleY1 = QLabel(self.page_7)
        self.label_rectangleY1.setObjectName(u"label_rectangleY1")
        self.label_rectangleY1.setMinimumSize(QSize(0, 21))
        self.label_rectangleY1.setMaximumSize(QSize(16777215, 21))

        self.horizontalLayout_72.addWidget(self.label_rectangleY1)

        self.spinBox_rectangleY1 = QSpinBox(self.page_7)
        self.spinBox_rectangleY1.setObjectName(u"spinBox_rectangleY1")
        self.spinBox_rectangleY1.setMaximum(2000)

        self.horizontalLayout_72.addWidget(self.spinBox_rectangleY1)


        self.verticalLayout_6.addLayout(self.horizontalLayout_72)

        self.horizontalLayout_73 = QHBoxLayout()
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.label_rectangleX2 = QLabel(self.page_7)
        self.label_rectangleX2.setObjectName(u"label_rectangleX2")
        self.label_rectangleX2.setMinimumSize(QSize(0, 21))
        self.label_rectangleX2.setMaximumSize(QSize(16777215, 21))

        self.horizontalLayout_73.addWidget(self.label_rectangleX2)

        self.spinBox_rectangleX2 = QSpinBox(self.page_7)
        self.spinBox_rectangleX2.setObjectName(u"spinBox_rectangleX2")
        self.spinBox_rectangleX2.setMaximum(2000)

        self.horizontalLayout_73.addWidget(self.spinBox_rectangleX2)


        self.verticalLayout_6.addLayout(self.horizontalLayout_73)

        self.horizontalLayout_74 = QHBoxLayout()
        self.horizontalLayout_74.setObjectName(u"horizontalLayout_74")
        self.label_rectangleY2 = QLabel(self.page_7)
        self.label_rectangleY2.setObjectName(u"label_rectangleY2")
        self.label_rectangleY2.setMinimumSize(QSize(0, 21))
        self.label_rectangleY2.setMaximumSize(QSize(16777215, 21))

        self.horizontalLayout_74.addWidget(self.label_rectangleY2)

        self.spinBox_rectangleY2 = QSpinBox(self.page_7)
        self.spinBox_rectangleY2.setObjectName(u"spinBox_rectangleY2")
        self.spinBox_rectangleY2.setMaximum(2000)

        self.horizontalLayout_74.addWidget(self.spinBox_rectangleY2)


        self.verticalLayout_6.addLayout(self.horizontalLayout_74)


        self.verticalLayout_18.addLayout(self.verticalLayout_6)

        self.label_NONE1_7 = QLabel(self.page_7)
        self.label_NONE1_7.setObjectName(u"label_NONE1_7")
        self.label_NONE1_7.setMinimumSize(QSize(0, 0))
        self.label_NONE1_7.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_18.addWidget(self.label_NONE1_7)

        self.toolBox.addItem(self.page_7, u"Loader")

        self.verticalLayout_7.addWidget(self.toolBox)

        self.pushButton_save = QPushButton(self.tab_2)
        self.pushButton_save.setObjectName(u"pushButton_save")
        self.pushButton_save.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(240, 240, 240); /* \u66f4\u6d45\u7684\u80cc\u666f\u8272 */\n"
"    color: black; /* \u66f4\u6df1\u7684\u6587\u5b57\u989c\u8272 */\n"
"    border-radius: 10px; /* \u5706\u89d2\u534a\u5f84\u51cf\u5c0f\u4e3a10px */\n"
"    padding: 10px;\n"
"    font-size: 16px;\n"
"    border: 4px solid rgb(50,109,245); /* \u7b80\u5316\u8fb9\u6846\u6837\u5f0f */\n"
"    text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(200, 200, 200); /* \u60ac\u505c\u65f6\u7684\u6d45\u7070\u8272\u80cc\u666f */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(56, 64, 85); /* \u6309\u4e0b\u65f6\u7684\u7565\u6df1\u4e00\u4e9b\u7684\u7070\u8272\u80cc\u666f */\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(160, 160, 160); /* \u7981\u7528\u72b6\u6001\u7684\u7565\u6d45\u4e00\u4e9b\u7684\u7070\u8272\u80cc\u666f */\n"
"}\n"
"")

        self.verticalLayout_7.addWidget(self.pushButton_save)

        self.tabWidget_run.addTab(self.tab_2, "")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.verticalLayout_22 = QVBoxLayout(self.tab_8)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_micro = QLabel(self.tab_8)
        self.label_micro.setObjectName(u"label_micro")
        self.label_micro.setMinimumSize(QSize(111, 16))
        self.label_micro.setMaximumSize(QSize(99999, 16))

        self.verticalLayout_20.addWidget(self.label_micro)

        self.horizontalLayout_75 = QHBoxLayout()
        self.horizontalLayout_75.setObjectName(u"horizontalLayout_75")
        self.doubleSpinBox_test_micro_movex2 = QDoubleSpinBox(self.tab_8)
        self.doubleSpinBox_test_micro_movex2.setObjectName(u"doubleSpinBox_test_micro_movex2")
        self.doubleSpinBox_test_micro_movex2.setDecimals(3)
        self.doubleSpinBox_test_micro_movex2.setMaximum(60.000000000000000)

        self.horizontalLayout_75.addWidget(self.doubleSpinBox_test_micro_movex2)

        self.pushButton_test_micro_movex2 = QPushButton(self.tab_8)
        self.pushButton_test_micro_movex2.setObjectName(u"pushButton_test_micro_movex2")
        self.pushButton_test_micro_movex2.setMinimumSize(QSize(117, 49))
        self.pushButton_test_micro_movex2.setMaximumSize(QSize(117, 49))
        self.pushButton_test_micro_movex2.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(240, 240, 240); /* \u66f4\u6d45\u7684\u80cc\u666f\u8272 */\n"
"    color: black; /* \u66f4\u6df1\u7684\u6587\u5b57\u989c\u8272 */\n"
"    border-radius: 10px; /* \u5706\u89d2\u534a\u5f84\u51cf\u5c0f\u4e3a10px */\n"
"    padding: 10px;\n"
"    font-size: 16px;\n"
"    border: 4px solid rgb(50,109,245); /* \u7b80\u5316\u8fb9\u6846\u6837\u5f0f */\n"
"    text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(200, 200, 200); /* \u60ac\u505c\u65f6\u7684\u6d45\u7070\u8272\u80cc\u666f */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(56, 64, 85); /* \u6309\u4e0b\u65f6\u7684\u7565\u6df1\u4e00\u4e9b\u7684\u7070\u8272\u80cc\u666f */\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(160, 160, 160); /* \u7981\u7528\u72b6\u6001\u7684\u7565\u6d45\u4e00\u4e9b\u7684\u7070\u8272\u80cc\u666f */\n"
"}\n"
"")

        self.horizontalLayout_75.addWidget(self.pushButton_test_micro_movex2)


        self.verticalLayout_20.addLayout(self.horizontalLayout_75)

        self.horizontalLayout_79 = QHBoxLayout()
        self.horizontalLayout_79.setObjectName(u"horizontalLayout_79")
        self.doubleSpinBox_test_micro_movey2 = QDoubleSpinBox(self.tab_8)
        self.doubleSpinBox_test_micro_movey2.setObjectName(u"doubleSpinBox_test_micro_movey2")
        self.doubleSpinBox_test_micro_movey2.setDecimals(3)
        self.doubleSpinBox_test_micro_movey2.setMaximum(60.000000000000000)

        self.horizontalLayout_79.addWidget(self.doubleSpinBox_test_micro_movey2)

        self.pushButton_test_micro_movey2 = QPushButton(self.tab_8)
        self.pushButton_test_micro_movey2.setObjectName(u"pushButton_test_micro_movey2")
        self.pushButton_test_micro_movey2.setMinimumSize(QSize(117, 49))
        self.pushButton_test_micro_movey2.setMaximumSize(QSize(117, 49))
        self.pushButton_test_micro_movey2.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(240, 240, 240); /* \u66f4\u6d45\u7684\u80cc\u666f\u8272 */\n"
"    color: black; /* \u66f4\u6df1\u7684\u6587\u5b57\u989c\u8272 */\n"
"    border-radius: 10px; /* \u5706\u89d2\u534a\u5f84\u51cf\u5c0f\u4e3a10px */\n"
"    padding: 10px;\n"
"    font-size: 16px;\n"
"    border: 4px solid rgb(50,109,245); /* \u7b80\u5316\u8fb9\u6846\u6837\u5f0f */\n"
"    text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(200, 200, 200); /* \u60ac\u505c\u65f6\u7684\u6d45\u7070\u8272\u80cc\u666f */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(56, 64, 85); /* \u6309\u4e0b\u65f6\u7684\u7565\u6df1\u4e00\u4e9b\u7684\u7070\u8272\u80cc\u666f */\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(160, 160, 160); /* \u7981\u7528\u72b6\u6001\u7684\u7565\u6d45\u4e00\u4e9b\u7684\u7070\u8272\u80cc\u666f */\n"
"}\n"
"")

        self.horizontalLayout_79.addWidget(self.pushButton_test_micro_movey2)


        self.verticalLayout_20.addLayout(self.horizontalLayout_79)

        self.horizontalLayout_80 = QHBoxLayout()
        self.horizontalLayout_80.setObjectName(u"horizontalLayout_80")
        self.doubleSpinBox_test_micro_movez2 = QDoubleSpinBox(self.tab_8)
        self.doubleSpinBox_test_micro_movez2.setObjectName(u"doubleSpinBox_test_micro_movez2")
        self.doubleSpinBox_test_micro_movez2.setDecimals(3)
        self.doubleSpinBox_test_micro_movez2.setMaximum(8.000000000000000)

        self.horizontalLayout_80.addWidget(self.doubleSpinBox_test_micro_movez2)

        self.pushButton_test_micro_movez2 = QPushButton(self.tab_8)
        self.pushButton_test_micro_movez2.setObjectName(u"pushButton_test_micro_movez2")
        self.pushButton_test_micro_movez2.setMinimumSize(QSize(117, 49))
        self.pushButton_test_micro_movez2.setMaximumSize(QSize(117, 49))
        self.pushButton_test_micro_movez2.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(240, 240, 240); /* \u66f4\u6d45\u7684\u80cc\u666f\u8272 */\n"
"    color: black; /* \u66f4\u6df1\u7684\u6587\u5b57\u989c\u8272 */\n"
"    border-radius: 10px; /* \u5706\u89d2\u534a\u5f84\u51cf\u5c0f\u4e3a10px */\n"
"    padding: 10px;\n"
"    font-size: 16px;\n"
"    border: 4px solid rgb(50,109,245); /* \u7b80\u5316\u8fb9\u6846\u6837\u5f0f */\n"
"    text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(200, 200, 200); /* \u60ac\u505c\u65f6\u7684\u6d45\u7070\u8272\u80cc\u666f */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(56, 64, 85); /* \u6309\u4e0b\u65f6\u7684\u7565\u6df1\u4e00\u4e9b\u7684\u7070\u8272\u80cc\u666f */\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(160, 160, 160); /* \u7981\u7528\u72b6\u6001\u7684\u7565\u6d45\u4e00\u4e9b\u7684\u7070\u8272\u80cc\u666f */\n"
"}\n"
"")

        self.horizontalLayout_80.addWidget(self.pushButton_test_micro_movez2)


        self.verticalLayout_20.addLayout(self.horizontalLayout_80)


        self.verticalLayout_22.addLayout(self.verticalLayout_20)

        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_micro_2 = QLabel(self.tab_8)
        self.label_micro_2.setObjectName(u"label_micro_2")
        self.label_micro_2.setMinimumSize(QSize(111, 16))
        self.label_micro_2.setMaximumSize(QSize(99999, 16))

        self.verticalLayout_21.addWidget(self.label_micro_2)

        self.horizontalLayout_81 = QHBoxLayout()
        self.horizontalLayout_81.setObjectName(u"horizontalLayout_81")
        self.doubleSpinBox_test_loader_movex2 = QDoubleSpinBox(self.tab_8)
        self.doubleSpinBox_test_loader_movex2.setObjectName(u"doubleSpinBox_test_loader_movex2")
        self.doubleSpinBox_test_loader_movex2.setDecimals(3)
        self.doubleSpinBox_test_loader_movex2.setMaximum(330.000000000000000)

        self.horizontalLayout_81.addWidget(self.doubleSpinBox_test_loader_movex2)

        self.pushButton_test_loader_movex2 = QPushButton(self.tab_8)
        self.pushButton_test_loader_movex2.setObjectName(u"pushButton_test_loader_movex2")
        self.pushButton_test_loader_movex2.setMinimumSize(QSize(117, 49))
        self.pushButton_test_loader_movex2.setMaximumSize(QSize(117, 49))
        self.pushButton_test_loader_movex2.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(240, 240, 240); /* \u66f4\u6d45\u7684\u80cc\u666f\u8272 */\n"
"    color: black; /* \u66f4\u6df1\u7684\u6587\u5b57\u989c\u8272 */\n"
"    border-radius: 10px; /* \u5706\u89d2\u534a\u5f84\u51cf\u5c0f\u4e3a10px */\n"
"    padding: 10px;\n"
"    font-size: 16px;\n"
"    border: 4px solid rgb(50,109,245); /* \u7b80\u5316\u8fb9\u6846\u6837\u5f0f */\n"
"    text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(200, 200, 200); /* \u60ac\u505c\u65f6\u7684\u6d45\u7070\u8272\u80cc\u666f */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(56, 64, 85); /* \u6309\u4e0b\u65f6\u7684\u7565\u6df1\u4e00\u4e9b\u7684\u7070\u8272\u80cc\u666f */\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(160, 160, 160); /* \u7981\u7528\u72b6\u6001\u7684\u7565\u6d45\u4e00\u4e9b\u7684\u7070\u8272\u80cc\u666f */\n"
"}\n"
"")

        self.horizontalLayout_81.addWidget(self.pushButton_test_loader_movex2)


        self.verticalLayout_21.addLayout(self.horizontalLayout_81)

        self.horizontalLayout_82 = QHBoxLayout()
        self.horizontalLayout_82.setObjectName(u"horizontalLayout_82")
        self.doubleSpinBox_test_loader_movey2 = QDoubleSpinBox(self.tab_8)
        self.doubleSpinBox_test_loader_movey2.setObjectName(u"doubleSpinBox_test_loader_movey2")
        self.doubleSpinBox_test_loader_movey2.setDecimals(3)
        self.doubleSpinBox_test_loader_movey2.setMaximum(2000.000000000000000)

        self.horizontalLayout_82.addWidget(self.doubleSpinBox_test_loader_movey2)

        self.pushButton_test_loader_movey2 = QPushButton(self.tab_8)
        self.pushButton_test_loader_movey2.setObjectName(u"pushButton_test_loader_movey2")
        self.pushButton_test_loader_movey2.setMinimumSize(QSize(117, 49))
        self.pushButton_test_loader_movey2.setMaximumSize(QSize(117, 49))
        self.pushButton_test_loader_movey2.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(240, 240, 240); /* \u66f4\u6d45\u7684\u80cc\u666f\u8272 */\n"
"    color: black; /* \u66f4\u6df1\u7684\u6587\u5b57\u989c\u8272 */\n"
"    border-radius: 10px; /* \u5706\u89d2\u534a\u5f84\u51cf\u5c0f\u4e3a10px */\n"
"    padding: 10px;\n"
"    font-size: 16px;\n"
"    border: 4px solid rgb(50,109,245); /* \u7b80\u5316\u8fb9\u6846\u6837\u5f0f */\n"
"    text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(200, 200, 200); /* \u60ac\u505c\u65f6\u7684\u6d45\u7070\u8272\u80cc\u666f */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(56, 64, 85); /* \u6309\u4e0b\u65f6\u7684\u7565\u6df1\u4e00\u4e9b\u7684\u7070\u8272\u80cc\u666f */\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(160, 160, 160); /* \u7981\u7528\u72b6\u6001\u7684\u7565\u6d45\u4e00\u4e9b\u7684\u7070\u8272\u80cc\u666f */\n"
"}\n"
"")

        self.horizontalLayout_82.addWidget(self.pushButton_test_loader_movey2)


        self.verticalLayout_21.addLayout(self.horizontalLayout_82)

        self.horizontalLayout_83 = QHBoxLayout()
        self.horizontalLayout_83.setObjectName(u"horizontalLayout_83")
        self.doubleSpinBox_test_loader_movez2 = QDoubleSpinBox(self.tab_8)
        self.doubleSpinBox_test_loader_movez2.setObjectName(u"doubleSpinBox_test_loader_movez2")
        self.doubleSpinBox_test_loader_movez2.setDecimals(3)
        self.doubleSpinBox_test_loader_movez2.setMaximum(150.000000000000000)

        self.horizontalLayout_83.addWidget(self.doubleSpinBox_test_loader_movez2)

        self.pushButton_test_loader_movez2 = QPushButton(self.tab_8)
        self.pushButton_test_loader_movez2.setObjectName(u"pushButton_test_loader_movez2")
        self.pushButton_test_loader_movez2.setMinimumSize(QSize(117, 49))
        self.pushButton_test_loader_movez2.setMaximumSize(QSize(117, 49))
        self.pushButton_test_loader_movez2.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(240, 240, 240); /* \u66f4\u6d45\u7684\u80cc\u666f\u8272 */\n"
"    color: black; /* \u66f4\u6df1\u7684\u6587\u5b57\u989c\u8272 */\n"
"    border-radius: 10px; /* \u5706\u89d2\u534a\u5f84\u51cf\u5c0f\u4e3a10px */\n"
"    padding: 10px;\n"
"    font-size: 16px;\n"
"    border: 4px solid rgb(50,109,245); /* \u7b80\u5316\u8fb9\u6846\u6837\u5f0f */\n"
"    text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(200, 200, 200); /* \u60ac\u505c\u65f6\u7684\u6d45\u7070\u8272\u80cc\u666f */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(56, 64, 85); /* \u6309\u4e0b\u65f6\u7684\u7565\u6df1\u4e00\u4e9b\u7684\u7070\u8272\u80cc\u666f */\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(160, 160, 160); /* \u7981\u7528\u72b6\u6001\u7684\u7565\u6d45\u4e00\u4e9b\u7684\u7070\u8272\u80cc\u666f */\n"
"}\n"
"")

        self.horizontalLayout_83.addWidget(self.pushButton_test_loader_movez2)


        self.verticalLayout_21.addLayout(self.horizontalLayout_83)


        self.verticalLayout_22.addLayout(self.verticalLayout_21)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_micro_3 = QLabel(self.tab_8)
        self.label_micro_3.setObjectName(u"label_micro_3")
        self.label_micro_3.setMinimumSize(QSize(111, 16))
        self.label_micro_3.setMaximumSize(QSize(99999, 16))

        self.verticalLayout_14.addWidget(self.label_micro_3)

        self.spinBox_exposure = QSpinBox(self.tab_8)
        self.spinBox_exposure.setObjectName(u"spinBox_exposure")
        self.spinBox_exposure.setMinimumSize(QSize(100, 0))
        self.spinBox_exposure.setMaximum(1000000)
        self.spinBox_exposure.setValue(0)

        self.verticalLayout_14.addWidget(self.spinBox_exposure)

        self.horizontalSlider_exposure = QSlider(self.tab_8)
        self.horizontalSlider_exposure.setObjectName(u"horizontalSlider_exposure")
        self.horizontalSlider_exposure.setMinimumSize(QSize(0, 11))
        self.horizontalSlider_exposure.setMaximumSize(QSize(16777215, 11))
        self.horizontalSlider_exposure.setStyleSheet(u"QSlider::groove:horizontal {\n"
"        border: 1px solid #999999;\n"
"        height: 8px; /* \u8bbe\u7f6e\u6ed1\u5757\u7684\u9ad8\u5ea6 */\n"
"        background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4);\n"
"        margin: 2px 0;\n"
"    }\n"
"\n"
"    QSlider::handle:horizontal {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"                                    stop:0 #eeeeee, stop:1 #dddddd);\n"
"        border: 1px solid #5c5c5c;\n"
"        width: 18px; /* \u8bbe\u7f6e\u6ed1\u5757\u7684\u5bbd\u5ea6 */\n"
"        margin: -2px 0; /* \u8c03\u6574\u6ed1\u5757\u7684\u4f4d\u7f6e */\n"
"        border-radius: 3px; /* \u8bbe\u7f6e\u6ed1\u5757\u7684\u5706\u89d2 */\n"
"    }\n"
"\n"
"    QSlider::add-page:horizontal {\n"
"        background: #575757; /* \u8bbe\u7f6e\u6ed1\u52a8\u6761\u672a\u88ab\u6fc0\u6d3b\u533a\u57df\u7684\u989c\u8272 */\n"
"        border: 1px solid #999999;\n"
"        height: 8px;\n"
"        margin: 2px 0;\n"
"    }\n"
"\n"
"    QSlider"
                        "::sub-page:horizontal {\n"
"        background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #b1b1b1, stop:1 #c4c4c4);\n"
"        border: 1px solid #999999;\n"
"        height: 8px;\n"
"        margin: 2px 0;\n"
"    }")
        self.horizontalSlider_exposure.setMaximum(1000000)
        self.horizontalSlider_exposure.setOrientation(Qt.Horizontal)

        self.verticalLayout_14.addWidget(self.horizontalSlider_exposure)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.pushButton_open_cameraonly = QPushButton(self.tab_8)
        self.pushButton_open_cameraonly.setObjectName(u"pushButton_open_cameraonly")
        self.pushButton_open_cameraonly.setMinimumSize(QSize(150, 49))
        self.pushButton_open_cameraonly.setMaximumSize(QSize(150, 49))
        self.pushButton_open_cameraonly.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(240, 240, 240); /* \u66f4\u6d45\u7684\u80cc\u666f\u8272 */\n"
"    color: black; /* \u66f4\u6df1\u7684\u6587\u5b57\u989c\u8272 */\n"
"    border-radius: 10px; /* \u5706\u89d2\u534a\u5f84\u51cf\u5c0f\u4e3a10px */\n"
"    padding: 10px;\n"
"    font-size: 16px;\n"
"    border: 4px solid rgb(50,109,245); /* \u7b80\u5316\u8fb9\u6846\u6837\u5f0f */\n"
"    text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(200, 200, 200); /* \u60ac\u505c\u65f6\u7684\u6d45\u7070\u8272\u80cc\u666f */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(56, 64, 85); /* \u6309\u4e0b\u65f6\u7684\u7565\u6df1\u4e00\u4e9b\u7684\u7070\u8272\u80cc\u666f */\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(160, 160, 160); /* \u7981\u7528\u72b6\u6001\u7684\u7565\u6d45\u4e00\u4e9b\u7684\u7070\u8272\u80cc\u666f */\n"
"}\n"
"")

        self.horizontalLayout_12.addWidget(self.pushButton_open_cameraonly)

        self.pushButton_close_cameraonly = QPushButton(self.tab_8)
        self.pushButton_close_cameraonly.setObjectName(u"pushButton_close_cameraonly")
        self.pushButton_close_cameraonly.setMinimumSize(QSize(150, 49))
        self.pushButton_close_cameraonly.setMaximumSize(QSize(150, 49))
        self.pushButton_close_cameraonly.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(240, 240, 240); /* \u66f4\u6d45\u7684\u80cc\u666f\u8272 */\n"
"    color: black; /* \u66f4\u6df1\u7684\u6587\u5b57\u989c\u8272 */\n"
"    border-radius: 10px; /* \u5706\u89d2\u534a\u5f84\u51cf\u5c0f\u4e3a10px */\n"
"    padding: 10px;\n"
"    font-size: 16px;\n"
"    border: 4px solid rgb(50,109,245); /* \u7b80\u5316\u8fb9\u6846\u6837\u5f0f */\n"
"    text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(200, 200, 200); /* \u60ac\u505c\u65f6\u7684\u6d45\u7070\u8272\u80cc\u666f */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(56, 64, 85); /* \u6309\u4e0b\u65f6\u7684\u7565\u6df1\u4e00\u4e9b\u7684\u7070\u8272\u80cc\u666f */\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(160, 160, 160); /* \u7981\u7528\u72b6\u6001\u7684\u7565\u6d45\u4e00\u4e9b\u7684\u7070\u8272\u80cc\u666f */\n"
"}\n"
"")

        self.horizontalLayout_12.addWidget(self.pushButton_close_cameraonly)


        self.verticalLayout_14.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.pushButton_open_camera_1 = QPushButton(self.tab_8)
        self.pushButton_open_camera_1.setObjectName(u"pushButton_open_camera_1")
        self.pushButton_open_camera_1.setMinimumSize(QSize(150, 49))
        self.pushButton_open_camera_1.setMaximumSize(QSize(150, 49))
        self.pushButton_open_camera_1.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(240, 240, 240); /* \u66f4\u6d45\u7684\u80cc\u666f\u8272 */\n"
"    color: black; /* \u66f4\u6df1\u7684\u6587\u5b57\u989c\u8272 */\n"
"    border-radius: 10px; /* \u5706\u89d2\u534a\u5f84\u51cf\u5c0f\u4e3a10px */\n"
"    padding: 10px;\n"
"    font-size: 16px;\n"
"    border: 4px solid rgb(50,109,245); /* \u7b80\u5316\u8fb9\u6846\u6837\u5f0f */\n"
"    text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(200, 200, 200); /* \u60ac\u505c\u65f6\u7684\u6d45\u7070\u8272\u80cc\u666f */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(56, 64, 85); /* \u6309\u4e0b\u65f6\u7684\u7565\u6df1\u4e00\u4e9b\u7684\u7070\u8272\u80cc\u666f */\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(160, 160, 160); /* \u7981\u7528\u72b6\u6001\u7684\u7565\u6d45\u4e00\u4e9b\u7684\u7070\u8272\u80cc\u666f */\n"
"}\n"
"")

        self.horizontalLayout_13.addWidget(self.pushButton_open_camera_1)

        self.pushButton_close_camera_1 = QPushButton(self.tab_8)
        self.pushButton_close_camera_1.setObjectName(u"pushButton_close_camera_1")
        self.pushButton_close_camera_1.setMinimumSize(QSize(150, 49))
        self.pushButton_close_camera_1.setMaximumSize(QSize(150, 49))
        self.pushButton_close_camera_1.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(240, 240, 240); /* \u66f4\u6d45\u7684\u80cc\u666f\u8272 */\n"
"    color: black; /* \u66f4\u6df1\u7684\u6587\u5b57\u989c\u8272 */\n"
"    border-radius: 10px; /* \u5706\u89d2\u534a\u5f84\u51cf\u5c0f\u4e3a10px */\n"
"    padding: 10px;\n"
"    font-size: 16px;\n"
"    border: 4px solid rgb(50,109,245); /* \u7b80\u5316\u8fb9\u6846\u6837\u5f0f */\n"
"    text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(200, 200, 200); /* \u60ac\u505c\u65f6\u7684\u6d45\u7070\u8272\u80cc\u666f */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(56, 64, 85); /* \u6309\u4e0b\u65f6\u7684\u7565\u6df1\u4e00\u4e9b\u7684\u7070\u8272\u80cc\u666f */\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(160, 160, 160); /* \u7981\u7528\u72b6\u6001\u7684\u7565\u6d45\u4e00\u4e9b\u7684\u7070\u8272\u80cc\u666f */\n"
"}\n"
"")

        self.horizontalLayout_13.addWidget(self.pushButton_close_camera_1)


        self.verticalLayout_14.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_84 = QHBoxLayout()
        self.horizontalLayout_84.setObjectName(u"horizontalLayout_84")
        self.pushButton_open_camera_2 = QPushButton(self.tab_8)
        self.pushButton_open_camera_2.setObjectName(u"pushButton_open_camera_2")
        self.pushButton_open_camera_2.setMinimumSize(QSize(150, 49))
        self.pushButton_open_camera_2.setMaximumSize(QSize(150, 49))
        self.pushButton_open_camera_2.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(240, 240, 240); /* \u66f4\u6d45\u7684\u80cc\u666f\u8272 */\n"
"    color: black; /* \u66f4\u6df1\u7684\u6587\u5b57\u989c\u8272 */\n"
"    border-radius: 10px; /* \u5706\u89d2\u534a\u5f84\u51cf\u5c0f\u4e3a10px */\n"
"    padding: 10px;\n"
"    font-size: 16px;\n"
"    border: 4px solid rgb(50,109,245); /* \u7b80\u5316\u8fb9\u6846\u6837\u5f0f */\n"
"    text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(200, 200, 200); /* \u60ac\u505c\u65f6\u7684\u6d45\u7070\u8272\u80cc\u666f */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(56, 64, 85); /* \u6309\u4e0b\u65f6\u7684\u7565\u6df1\u4e00\u4e9b\u7684\u7070\u8272\u80cc\u666f */\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(160, 160, 160); /* \u7981\u7528\u72b6\u6001\u7684\u7565\u6d45\u4e00\u4e9b\u7684\u7070\u8272\u80cc\u666f */\n"
"}\n"
"")

        self.horizontalLayout_84.addWidget(self.pushButton_open_camera_2)

        self.pushButton_close_camera_2 = QPushButton(self.tab_8)
        self.pushButton_close_camera_2.setObjectName(u"pushButton_close_camera_2")
        self.pushButton_close_camera_2.setMinimumSize(QSize(150, 49))
        self.pushButton_close_camera_2.setMaximumSize(QSize(150, 49))
        self.pushButton_close_camera_2.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(240, 240, 240); /* \u66f4\u6d45\u7684\u80cc\u666f\u8272 */\n"
"    color: black; /* \u66f4\u6df1\u7684\u6587\u5b57\u989c\u8272 */\n"
"    border-radius: 10px; /* \u5706\u89d2\u534a\u5f84\u51cf\u5c0f\u4e3a10px */\n"
"    padding: 10px;\n"
"    font-size: 16px;\n"
"    border: 4px solid rgb(50,109,245); /* \u7b80\u5316\u8fb9\u6846\u6837\u5f0f */\n"
"    text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(200, 200, 200); /* \u60ac\u505c\u65f6\u7684\u6d45\u7070\u8272\u80cc\u666f */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(56, 64, 85); /* \u6309\u4e0b\u65f6\u7684\u7565\u6df1\u4e00\u4e9b\u7684\u7070\u8272\u80cc\u666f */\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(160, 160, 160); /* \u7981\u7528\u72b6\u6001\u7684\u7565\u6d45\u4e00\u4e9b\u7684\u7070\u8272\u80cc\u666f */\n"
"}\n"
"")

        self.horizontalLayout_84.addWidget(self.pushButton_close_camera_2)


        self.verticalLayout_14.addLayout(self.horizontalLayout_84)


        self.verticalLayout_22.addLayout(self.verticalLayout_14)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_micro_4 = QLabel(self.tab_8)
        self.label_micro_4.setObjectName(u"label_micro_4")
        self.label_micro_4.setMinimumSize(QSize(111, 16))
        self.label_micro_4.setMaximumSize(QSize(99999, 16))

        self.verticalLayout_15.addWidget(self.label_micro_4)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSlider_led_intensity = QSlider(self.tab_8)
        self.horizontalSlider_led_intensity.setObjectName(u"horizontalSlider_led_intensity")
        self.horizontalSlider_led_intensity.setMinimumSize(QSize(0, 11))
        self.horizontalSlider_led_intensity.setMaximumSize(QSize(16777215, 11))
        self.horizontalSlider_led_intensity.setStyleSheet(u"QSlider::groove:horizontal {\n"
"        border: 1px solid #999999;\n"
"        height: 8px; /* \u8bbe\u7f6e\u6ed1\u5757\u7684\u9ad8\u5ea6 */\n"
"        background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4);\n"
"        margin: 2px 0;\n"
"    }\n"
"\n"
"    QSlider::handle:horizontal {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"                                    stop:0 #eeeeee, stop:1 #dddddd);\n"
"        border: 1px solid #5c5c5c;\n"
"        width: 18px; /* \u8bbe\u7f6e\u6ed1\u5757\u7684\u5bbd\u5ea6 */\n"
"        margin: -2px 0; /* \u8c03\u6574\u6ed1\u5757\u7684\u4f4d\u7f6e */\n"
"        border-radius: 3px; /* \u8bbe\u7f6e\u6ed1\u5757\u7684\u5706\u89d2 */\n"
"    }\n"
"\n"
"    QSlider::add-page:horizontal {\n"
"        background: #575757; /* \u8bbe\u7f6e\u6ed1\u52a8\u6761\u672a\u88ab\u6fc0\u6d3b\u533a\u57df\u7684\u989c\u8272 */\n"
"        border: 1px solid #999999;\n"
"        height: 8px;\n"
"        margin: 2px 0;\n"
"    }\n"
"\n"
"    QSlider"
                        "::sub-page:horizontal {\n"
"        background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #b1b1b1, stop:1 #c4c4c4);\n"
"        border: 1px solid #999999;\n"
"        height: 8px;\n"
"        margin: 2px 0;\n"
"    }")
        self.horizontalSlider_led_intensity.setMaximum(100)
        self.horizontalSlider_led_intensity.setOrientation(Qt.Horizontal)

        self.horizontalLayout_11.addWidget(self.horizontalSlider_led_intensity)

        self.spinBox_led_intensity = QSpinBox(self.tab_8)
        self.spinBox_led_intensity.setObjectName(u"spinBox_led_intensity")
        self.spinBox_led_intensity.setMinimumSize(QSize(100, 0))
        self.spinBox_led_intensity.setMaximum(100)
        self.spinBox_led_intensity.setValue(0)

        self.horizontalLayout_11.addWidget(self.spinBox_led_intensity)


        self.verticalLayout_15.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_86 = QHBoxLayout()
        self.horizontalLayout_86.setObjectName(u"horizontalLayout_86")
        self.pushButton_open_led_only = QPushButton(self.tab_8)
        self.pushButton_open_led_only.setObjectName(u"pushButton_open_led_only")
        self.pushButton_open_led_only.setMinimumSize(QSize(150, 49))
        self.pushButton_open_led_only.setMaximumSize(QSize(150, 49))
        self.pushButton_open_led_only.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(240, 240, 240); /* \u66f4\u6d45\u7684\u80cc\u666f\u8272 */\n"
"    color: black; /* \u66f4\u6df1\u7684\u6587\u5b57\u989c\u8272 */\n"
"    border-radius: 10px; /* \u5706\u89d2\u534a\u5f84\u51cf\u5c0f\u4e3a10px */\n"
"    padding: 10px;\n"
"    font-size: 16px;\n"
"    border: 4px solid rgb(50,109,245); /* \u7b80\u5316\u8fb9\u6846\u6837\u5f0f */\n"
"    text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(200, 200, 200); /* \u60ac\u505c\u65f6\u7684\u6d45\u7070\u8272\u80cc\u666f */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(56, 64, 85); /* \u6309\u4e0b\u65f6\u7684\u7565\u6df1\u4e00\u4e9b\u7684\u7070\u8272\u80cc\u666f */\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(160, 160, 160); /* \u7981\u7528\u72b6\u6001\u7684\u7565\u6d45\u4e00\u4e9b\u7684\u7070\u8272\u80cc\u666f */\n"
"}\n"
"")

        self.horizontalLayout_86.addWidget(self.pushButton_open_led_only)

        self.pushButton_close_led_only = QPushButton(self.tab_8)
        self.pushButton_close_led_only.setObjectName(u"pushButton_close_led_only")
        self.pushButton_close_led_only.setMinimumSize(QSize(150, 49))
        self.pushButton_close_led_only.setMaximumSize(QSize(150, 49))
        self.pushButton_close_led_only.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(240, 240, 240); /* \u66f4\u6d45\u7684\u80cc\u666f\u8272 */\n"
"    color: black; /* \u66f4\u6df1\u7684\u6587\u5b57\u989c\u8272 */\n"
"    border-radius: 10px; /* \u5706\u89d2\u534a\u5f84\u51cf\u5c0f\u4e3a10px */\n"
"    padding: 10px;\n"
"    font-size: 16px;\n"
"    border: 4px solid rgb(50,109,245); /* \u7b80\u5316\u8fb9\u6846\u6837\u5f0f */\n"
"    text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(200, 200, 200); /* \u60ac\u505c\u65f6\u7684\u6d45\u7070\u8272\u80cc\u666f */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(56, 64, 85); /* \u6309\u4e0b\u65f6\u7684\u7565\u6df1\u4e00\u4e9b\u7684\u7070\u8272\u80cc\u666f */\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(160, 160, 160); /* \u7981\u7528\u72b6\u6001\u7684\u7565\u6d45\u4e00\u4e9b\u7684\u7070\u8272\u80cc\u666f */\n"
"}\n"
"")

        self.horizontalLayout_86.addWidget(self.pushButton_close_led_only)


        self.verticalLayout_15.addLayout(self.horizontalLayout_86)

        self.horizontalLayout_87 = QHBoxLayout()
        self.horizontalLayout_87.setObjectName(u"horizontalLayout_87")
        self.pushButton_open_led_1 = QPushButton(self.tab_8)
        self.pushButton_open_led_1.setObjectName(u"pushButton_open_led_1")
        self.pushButton_open_led_1.setMinimumSize(QSize(150, 49))
        self.pushButton_open_led_1.setMaximumSize(QSize(150, 49))
        self.pushButton_open_led_1.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(240, 240, 240); /* \u66f4\u6d45\u7684\u80cc\u666f\u8272 */\n"
"    color: black; /* \u66f4\u6df1\u7684\u6587\u5b57\u989c\u8272 */\n"
"    border-radius: 10px; /* \u5706\u89d2\u534a\u5f84\u51cf\u5c0f\u4e3a10px */\n"
"    padding: 10px;\n"
"    font-size: 16px;\n"
"    border: 4px solid rgb(50,109,245); /* \u7b80\u5316\u8fb9\u6846\u6837\u5f0f */\n"
"    text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(200, 200, 200); /* \u60ac\u505c\u65f6\u7684\u6d45\u7070\u8272\u80cc\u666f */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(56, 64, 85); /* \u6309\u4e0b\u65f6\u7684\u7565\u6df1\u4e00\u4e9b\u7684\u7070\u8272\u80cc\u666f */\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(160, 160, 160); /* \u7981\u7528\u72b6\u6001\u7684\u7565\u6d45\u4e00\u4e9b\u7684\u7070\u8272\u80cc\u666f */\n"
"}\n"
"")

        self.horizontalLayout_87.addWidget(self.pushButton_open_led_1)

        self.pushButton_close_led_1 = QPushButton(self.tab_8)
        self.pushButton_close_led_1.setObjectName(u"pushButton_close_led_1")
        self.pushButton_close_led_1.setMinimumSize(QSize(150, 49))
        self.pushButton_close_led_1.setMaximumSize(QSize(150, 49))
        self.pushButton_close_led_1.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(240, 240, 240); /* \u66f4\u6d45\u7684\u80cc\u666f\u8272 */\n"
"    color: black; /* \u66f4\u6df1\u7684\u6587\u5b57\u989c\u8272 */\n"
"    border-radius: 10px; /* \u5706\u89d2\u534a\u5f84\u51cf\u5c0f\u4e3a10px */\n"
"    padding: 10px;\n"
"    font-size: 16px;\n"
"    border: 4px solid rgb(50,109,245); /* \u7b80\u5316\u8fb9\u6846\u6837\u5f0f */\n"
"    text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(200, 200, 200); /* \u60ac\u505c\u65f6\u7684\u6d45\u7070\u8272\u80cc\u666f */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(56, 64, 85); /* \u6309\u4e0b\u65f6\u7684\u7565\u6df1\u4e00\u4e9b\u7684\u7070\u8272\u80cc\u666f */\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(160, 160, 160); /* \u7981\u7528\u72b6\u6001\u7684\u7565\u6d45\u4e00\u4e9b\u7684\u7070\u8272\u80cc\u666f */\n"
"}\n"
"")

        self.horizontalLayout_87.addWidget(self.pushButton_close_led_1)


        self.verticalLayout_15.addLayout(self.horizontalLayout_87)

        self.horizontalLayout_88 = QHBoxLayout()
        self.horizontalLayout_88.setObjectName(u"horizontalLayout_88")
        self.pushButton_open_led_2 = QPushButton(self.tab_8)
        self.pushButton_open_led_2.setObjectName(u"pushButton_open_led_2")
        self.pushButton_open_led_2.setMinimumSize(QSize(150, 49))
        self.pushButton_open_led_2.setMaximumSize(QSize(150, 49))
        self.pushButton_open_led_2.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(240, 240, 240); /* \u66f4\u6d45\u7684\u80cc\u666f\u8272 */\n"
"    color: black; /* \u66f4\u6df1\u7684\u6587\u5b57\u989c\u8272 */\n"
"    border-radius: 10px; /* \u5706\u89d2\u534a\u5f84\u51cf\u5c0f\u4e3a10px */\n"
"    padding: 10px;\n"
"    font-size: 16px;\n"
"    border: 4px solid rgb(50,109,245); /* \u7b80\u5316\u8fb9\u6846\u6837\u5f0f */\n"
"    text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(200, 200, 200); /* \u60ac\u505c\u65f6\u7684\u6d45\u7070\u8272\u80cc\u666f */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(56, 64, 85); /* \u6309\u4e0b\u65f6\u7684\u7565\u6df1\u4e00\u4e9b\u7684\u7070\u8272\u80cc\u666f */\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(160, 160, 160); /* \u7981\u7528\u72b6\u6001\u7684\u7565\u6d45\u4e00\u4e9b\u7684\u7070\u8272\u80cc\u666f */\n"
"}\n"
"")

        self.horizontalLayout_88.addWidget(self.pushButton_open_led_2)

        self.pushButton_close_led_2 = QPushButton(self.tab_8)
        self.pushButton_close_led_2.setObjectName(u"pushButton_close_led_2")
        self.pushButton_close_led_2.setMinimumSize(QSize(150, 49))
        self.pushButton_close_led_2.setMaximumSize(QSize(150, 49))
        self.pushButton_close_led_2.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(240, 240, 240); /* \u66f4\u6d45\u7684\u80cc\u666f\u8272 */\n"
"    color: black; /* \u66f4\u6df1\u7684\u6587\u5b57\u989c\u8272 */\n"
"    border-radius: 10px; /* \u5706\u89d2\u534a\u5f84\u51cf\u5c0f\u4e3a10px */\n"
"    padding: 10px;\n"
"    font-size: 16px;\n"
"    border: 4px solid rgb(50,109,245); /* \u7b80\u5316\u8fb9\u6846\u6837\u5f0f */\n"
"    text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(200, 200, 200); /* \u60ac\u505c\u65f6\u7684\u6d45\u7070\u8272\u80cc\u666f */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(56, 64, 85); /* \u6309\u4e0b\u65f6\u7684\u7565\u6df1\u4e00\u4e9b\u7684\u7070\u8272\u80cc\u666f */\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(160, 160, 160); /* \u7981\u7528\u72b6\u6001\u7684\u7565\u6d45\u4e00\u4e9b\u7684\u7070\u8272\u80cc\u666f */\n"
"}\n"
"")

        self.horizontalLayout_88.addWidget(self.pushButton_close_led_2)


        self.verticalLayout_15.addLayout(self.horizontalLayout_88)


        self.verticalLayout_22.addLayout(self.verticalLayout_15)

        self.pushButton_savepic = QPushButton(self.tab_8)
        self.pushButton_savepic.setObjectName(u"pushButton_savepic")
        self.pushButton_savepic.setMinimumSize(QSize(150, 49))
        self.pushButton_savepic.setMaximumSize(QSize(150, 49))
        self.pushButton_savepic.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(240, 240, 240); /* \u66f4\u6d45\u7684\u80cc\u666f\u8272 */\n"
"    color: black; /* \u66f4\u6df1\u7684\u6587\u5b57\u989c\u8272 */\n"
"    border-radius: 10px; /* \u5706\u89d2\u534a\u5f84\u51cf\u5c0f\u4e3a10px */\n"
"    padding: 10px;\n"
"    font-size: 16px;\n"
"    border: 4px solid rgb(50,109,245); /* \u7b80\u5316\u8fb9\u6846\u6837\u5f0f */\n"
"    text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(200, 200, 200); /* \u60ac\u505c\u65f6\u7684\u6d45\u7070\u8272\u80cc\u666f */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(56, 64, 85); /* \u6309\u4e0b\u65f6\u7684\u7565\u6df1\u4e00\u4e9b\u7684\u7070\u8272\u80cc\u666f */\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(160, 160, 160); /* \u7981\u7528\u72b6\u6001\u7684\u7565\u6d45\u4e00\u4e9b\u7684\u7070\u8272\u80cc\u666f */\n"
"}\n"
"")

        self.verticalLayout_22.addWidget(self.pushButton_savepic)

        self.label_NONE1_8 = QLabel(self.tab_8)
        self.label_NONE1_8.setObjectName(u"label_NONE1_8")
        self.label_NONE1_8.setMinimumSize(QSize(0, 0))
        self.label_NONE1_8.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_22.addWidget(self.label_NONE1_8)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.pushButton_save_scan = QPushButton(self.tab_8)
        self.pushButton_save_scan.setObjectName(u"pushButton_save_scan")
        self.pushButton_save_scan.setMinimumSize(QSize(150, 49))
        self.pushButton_save_scan.setMaximumSize(QSize(150, 49))
        self.pushButton_save_scan.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(240, 240, 240); /* \u66f4\u6d45\u7684\u80cc\u666f\u8272 */\n"
"    color: black; /* \u66f4\u6df1\u7684\u6587\u5b57\u989c\u8272 */\n"
"    border-radius: 10px; /* \u5706\u89d2\u534a\u5f84\u51cf\u5c0f\u4e3a10px */\n"
"    padding: 10px;\n"
"    font-size: 16px;\n"
"    border: 4px solid rgb(50,109,245); /* \u7b80\u5316\u8fb9\u6846\u6837\u5f0f */\n"
"    text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(200, 200, 200); /* \u60ac\u505c\u65f6\u7684\u6d45\u7070\u8272\u80cc\u666f */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(56, 64, 85); /* \u6309\u4e0b\u65f6\u7684\u7565\u6df1\u4e00\u4e9b\u7684\u7070\u8272\u80cc\u666f */\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(160, 160, 160); /* \u7981\u7528\u72b6\u6001\u7684\u7565\u6d45\u4e00\u4e9b\u7684\u7070\u8272\u80cc\u666f */\n"
"}\n"
"")

        self.horizontalLayout_10.addWidget(self.pushButton_save_scan)

        self.pushButton_save_exposure = QPushButton(self.tab_8)
        self.pushButton_save_exposure.setObjectName(u"pushButton_save_exposure")
        self.pushButton_save_exposure.setMinimumSize(QSize(150, 49))
        self.pushButton_save_exposure.setMaximumSize(QSize(150, 49))
        self.pushButton_save_exposure.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(240, 240, 240); /* \u66f4\u6d45\u7684\u80cc\u666f\u8272 */\n"
"    color: black; /* \u66f4\u6df1\u7684\u6587\u5b57\u989c\u8272 */\n"
"    border-radius: 10px; /* \u5706\u89d2\u534a\u5f84\u51cf\u5c0f\u4e3a10px */\n"
"    padding: 10px;\n"
"    font-size: 16px;\n"
"    border: 4px solid rgb(50,109,245); /* \u7b80\u5316\u8fb9\u6846\u6837\u5f0f */\n"
"    text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(200, 200, 200); /* \u60ac\u505c\u65f6\u7684\u6d45\u7070\u8272\u80cc\u666f */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(56, 64, 85); /* \u6309\u4e0b\u65f6\u7684\u7565\u6df1\u4e00\u4e9b\u7684\u7070\u8272\u80cc\u666f */\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(160, 160, 160); /* \u7981\u7528\u72b6\u6001\u7684\u7565\u6d45\u4e00\u4e9b\u7684\u7070\u8272\u80cc\u666f */\n"
"}\n"
"")

        self.horizontalLayout_10.addWidget(self.pushButton_save_exposure)


        self.verticalLayout_22.addLayout(self.horizontalLayout_10)

        self.tabWidget_run.addTab(self.tab_8, "")

        self.horizontalLayout_8.addWidget(self.tabWidget_run)


        self.verticalLayout_19.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(51, 16))
        self.label.setMaximumSize(QSize(51, 16))

        self.horizontalLayout_5.addWidget(self.label)

        self.label_X = QLabel(self.centralwidget)
        self.label_X.setObjectName(u"label_X")
        self.label_X.setMinimumSize(QSize(16, 16))
        self.label_X.setMaximumSize(QSize(16, 16))

        self.horizontalLayout_5.addWidget(self.label_X)

        self.label_SETX = QLabel(self.centralwidget)
        self.label_SETX.setObjectName(u"label_SETX")
        self.label_SETX.setMinimumSize(QSize(111, 16))
        self.label_SETX.setMaximumSize(QSize(111, 16))

        self.horizontalLayout_5.addWidget(self.label_SETX)

        self.label_Y = QLabel(self.centralwidget)
        self.label_Y.setObjectName(u"label_Y")
        self.label_Y.setMinimumSize(QSize(16, 16))
        self.label_Y.setMaximumSize(QSize(16, 16))

        self.horizontalLayout_5.addWidget(self.label_Y)

        self.label_SETY = QLabel(self.centralwidget)
        self.label_SETY.setObjectName(u"label_SETY")
        self.label_SETY.setMinimumSize(QSize(111, 16))
        self.label_SETY.setMaximumSize(QSize(111, 16))

        self.horizontalLayout_5.addWidget(self.label_SETY)

        self.label_Z = QLabel(self.centralwidget)
        self.label_Z.setObjectName(u"label_Z")
        self.label_Z.setMinimumSize(QSize(16, 16))
        self.label_Z.setMaximumSize(QSize(16, 16))

        self.horizontalLayout_5.addWidget(self.label_Z)

        self.label_SETZ = QLabel(self.centralwidget)
        self.label_SETZ.setObjectName(u"label_SETZ")
        self.label_SETZ.setMinimumSize(QSize(111, 16))
        self.label_SETZ.setMaximumSize(QSize(111, 16))

        self.horizontalLayout_5.addWidget(self.label_SETZ)

        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(111, 16))
        self.label_8.setMaximumSize(QSize(16777215, 16))

        self.horizontalLayout_5.addWidget(self.label_8)


        self.verticalLayout_19.addLayout(self.horizontalLayout_5)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1192, 17))
        self.menuhelp = QMenu(self.menubar)
        self.menuhelp.setObjectName(u"menuhelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuhelp.menuAction())
        self.menuhelp.addAction(self.actionlianxifangshi)

        self.retranslateUi(MainWindow)
        self.horizontalSlider_exposure.sliderMoved.connect(self.spinBox_exposure.setValue)
        self.spinBox_exposure.valueChanged.connect(self.horizontalSlider_exposure.setValue)
        self.horizontalSlider_led_intensity.sliderMoved.connect(self.spinBox_led_intensity.setValue)
        self.spinBox_led_intensity.valueChanged.connect(self.horizontalSlider_led_intensity.setValue)

        self.tabWidget_result_AI.setCurrentIndex(0)
        self.tabWidget_log.setCurrentIndex(0)
        self.tabWidget_ID.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_scan_process.setCurrentIndex(0)
        self.tabWidget_silde_process.setCurrentIndex(0)
        self.tabWidget_run.setCurrentIndex(0)
        self.toolBox.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"V1.0.1", None))
        self.actionlianxifangshi.setText(QCoreApplication.translate("MainWindow", u"\u8054\u7cfb\u65b9\u5f0f", None))
        self.label_result_AI.setText("")
        self.tabWidget_result_AI.setTabText(self.tabWidget_result_AI.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\u626b\u63cf\u7ed3\u679c", None))
        self.tabWidget_log.setTabText(self.tabWidget_log.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"\u626b\u63cf\u65e5\u5fd7", None))
        self.tabWidget_ID.setTabText(self.tabWidget_ID.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"\u5df2\u626b\u63cf\u73bb\u7247", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_9), QCoreApplication.translate("MainWindow", u"\u5bf9\u7126\u56fe\u50cf", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_10), QCoreApplication.translate("MainWindow", u"\u626b\u63cf\u62fc\u56fe", None))
        self.tabWidget_scan_process.setTabText(self.tabWidget_scan_process.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"\u626b\u63cf\u8fdb\u7a0b", None))
        self.label_slide.setText("")
        self.tabWidget_silde_process.setTabText(self.tabWidget_silde_process.indexOf(self.tab_7), QCoreApplication.translate("MainWindow", u"\u626b\u63cf\u73bb\u7247\u8fdb\u7a0b", None))
        self.pushButton_run.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u626b\u63cf", None))
        self.pushButton_pause.setText(QCoreApplication.translate("MainWindow", u"\u6682\u505c\u626b\u63cf", None))
        self.pushButton_micro_reset.setText(QCoreApplication.translate("MainWindow", u"\u663e\u5fae\u955c\u590d\u4f4d", None))
        self.pushButton_loader_reset.setText(QCoreApplication.translate("MainWindow", u"\u88c5\u8f7d\u5668\u590d\u4f4d", None))
        self.label_NONE1_9.setText("")
        self.tabWidget_run.setTabText(self.tabWidget_run.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u626b\u63cf\u4efb\u52a1", None))
        self.checkBox_1.setText(QCoreApplication.translate("MainWindow", u"\u73bb\u7247\u4ed31\u53f7", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"\u73bb\u7247\u4ed32\u53f7", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"\u73bb\u7247\u4ed33\u53f7", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"\u73bb\u7247\u4ed34\u53f7", None))
        self.label_slide_number.setText(QCoreApplication.translate("MainWindow", u"\u73bb\u7247\u6570\u91cf", None))
        self.label_NONE1_2.setText("")
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"\u4efb\u52a1\u5206\u914d", None))
        self.label_maxworkers.setText(QCoreApplication.translate("MainWindow", u"maxworkers", None))
        self.label_imagestitchsize.setText(QCoreApplication.translate("MainWindow", u"imagestitchsize", None))
        self.label_AIimage.setText(QCoreApplication.translate("MainWindow", u"AIimage", None))
        self.label_queuenumber.setText(QCoreApplication.translate("MainWindow", u"queuenumber", None))
        self.label_pixelformat.setText(QCoreApplication.translate("MainWindow", u"pixelformat", None))
        self.comboBox_pixelformat.setItemText(0, QCoreApplication.translate("MainWindow", u"jpg", None))
        self.comboBox_pixelformat.setItemText(1, QCoreApplication.translate("MainWindow", u"png", None))
        self.comboBox_pixelformat.setItemText(2, QCoreApplication.translate("MainWindow", u"bmp", None))

        self.label_imagequailty.setText(QCoreApplication.translate("MainWindow", u"imagequailty", None))
        self.label_SavePath.setText(QCoreApplication.translate("MainWindow", u"SavePath", None))
        self.label_savepath.setText(QCoreApplication.translate("MainWindow", u"./pic/", None))
        self.pushButton_savepath.setText(QCoreApplication.translate("MainWindow", u"\u66f4\u6539\u56fe\u7247\u4fdd\u5b58\u5730\u5740", None))
        self.label_NONE1_3.setText("")
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), QCoreApplication.translate("MainWindow", u"ImageSaver", None))
        self.label_cameranumber.setText(QCoreApplication.translate("MainWindow", u"cameranumber", None))
        self.checkBox_loaderflage.setText(QCoreApplication.translate("MainWindow", u"loaderflage", None))
        self.checkBox_microscopeflage.setText(QCoreApplication.translate("MainWindow", u"microscopeflage", None))
        self.label_NONE1_4.setText("")
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_4), QCoreApplication.translate("MainWindow", u"Device", None))
        self.label_MicroCom.setText(QCoreApplication.translate("MainWindow", u"\u4e32\u53e3", None))
        self.comboBox_MicroCom.setItemText(0, QCoreApplication.translate("MainWindow", u"COM1", None))
        self.comboBox_MicroCom.setItemText(1, QCoreApplication.translate("MainWindow", u"COM2", None))
        self.comboBox_MicroCom.setItemText(2, QCoreApplication.translate("MainWindow", u"COM3", None))
        self.comboBox_MicroCom.setItemText(3, QCoreApplication.translate("MainWindow", u"COM4", None))
        self.comboBox_MicroCom.setItemText(4, QCoreApplication.translate("MainWindow", u"COM5", None))
        self.comboBox_MicroCom.setItemText(5, QCoreApplication.translate("MainWindow", u"COM6", None))
        self.comboBox_MicroCom.setItemText(6, QCoreApplication.translate("MainWindow", u"COM7", None))
        self.comboBox_MicroCom.setItemText(7, QCoreApplication.translate("MainWindow", u"COM8", None))
        self.comboBox_MicroCom.setItemText(8, QCoreApplication.translate("MainWindow", u"COM9", None))
        self.comboBox_MicroCom.setItemText(9, QCoreApplication.translate("MainWindow", u"COM10", None))
        self.comboBox_MicroCom.setItemText(10, QCoreApplication.translate("MainWindow", u"COM11", None))
        self.comboBox_MicroCom.setItemText(11, QCoreApplication.translate("MainWindow", u"COM12", None))
        self.comboBox_MicroCom.setItemText(12, QCoreApplication.translate("MainWindow", u"COM13", None))
        self.comboBox_MicroCom.setItemText(13, QCoreApplication.translate("MainWindow", u"COM14", None))
        self.comboBox_MicroCom.setItemText(14, QCoreApplication.translate("MainWindow", u"COM15", None))
        self.comboBox_MicroCom.setItemText(15, QCoreApplication.translate("MainWindow", u"COM16", None))
        self.comboBox_MicroCom.setItemText(16, QCoreApplication.translate("MainWindow", u"COM17", None))
        self.comboBox_MicroCom.setItemText(17, QCoreApplication.translate("MainWindow", u"COM18", None))
        self.comboBox_MicroCom.setItemText(18, QCoreApplication.translate("MainWindow", u"COM19", None))
        self.comboBox_MicroCom.setItemText(19, QCoreApplication.translate("MainWindow", u"COM20", None))

        self.checkBox_LED.setText(QCoreApplication.translate("MainWindow", u"LED", None))
        self.label_50xcenterx.setText(QCoreApplication.translate("MainWindow", u"50X\u73bb\u7247\u626b\u63cf\u4e2d\u5fc3x", None))
        self.label_50xcentery.setText(QCoreApplication.translate("MainWindow", u"50X\u73bb\u7247\u626b\u63cf\u4e2d\u5fc3y", None))
        self.label_20xcenterx.setText(QCoreApplication.translate("MainWindow", u"20X\u73bb\u7247\u626b\u63cf\u4e2d\u5fc3x", None))
        self.label_20xcenterx_2.setText(QCoreApplication.translate("MainWindow", u"20X\u73bb\u7247\u626b\u63cf\u4e2d\u5fc3y", None))
        self.label_Onlycenterx.setText(QCoreApplication.translate("MainWindow", u"\u5355\u955c\u5934\u626b\u63cf\u4e2d\u5fc3x", None))
        self.label_Onlycentery.setText(QCoreApplication.translate("MainWindow", u"\u5355\u955c\u5934\u626b\u63cf\u4e2d\u5fc3y", None))
        self.label_scan_w.setText(QCoreApplication.translate("MainWindow", u"\u73bb\u7247\u626b\u63cf\u533a\u57df\u5bbd\u5ea6", None))
        self.label_scan_h.setText(QCoreApplication.translate("MainWindow", u"\u73bb\u7247\u626b\u63cf\u533a\u57df\u9ad8\u5ea6", None))
        self.label_50xzfocus.setText(QCoreApplication.translate("MainWindow", u"50x\u5bf9\u7126\u7ecf\u9a8c\u503c", None))
        self.label_20xzfocus.setText(QCoreApplication.translate("MainWindow", u"20x\u5bf9\u7126\u7ecf\u9a8c\u503c", None))
        self.label_Onlyzfocus.setText(QCoreApplication.translate("MainWindow", u"\u5355\u955c\u5934\u5bf9\u7126\u7ecf\u9a8c\u503c", None))
        self.label_FocusMethod.setText(QCoreApplication.translate("MainWindow", u"\u5bf9\u7126\u65b9\u5f0f", None))
        self.comboBox_FocusMethod.setItemText(0, QCoreApplication.translate("MainWindow", u"\u5feb\u901f\u626b\u63cf\u4e00", None))
        self.comboBox_FocusMethod.setItemText(1, QCoreApplication.translate("MainWindow", u"\u5feb\u901f\u626b\u63cf\u4e8c", None))
        self.comboBox_FocusMethod.setItemText(2, QCoreApplication.translate("MainWindow", u"\u5feb\u901f\u626b\u63cf\u4e09", None))

        self.label_system.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u7cfb\u7edf", None))
        self.comboBox_Objective_SYS.setItemText(0, QCoreApplication.translate("MainWindow", u"\u5355\u955c\u5934", None))
        self.comboBox_Objective_SYS.setItemText(1, QCoreApplication.translate("MainWindow", u"\u53cc\u955c\u5934", None))

        self.label_Objective.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u5bf9\u7126\u500d\u6570", None))
        self.comboBox_Objective.setItemText(0, QCoreApplication.translate("MainWindow", u"20X", None))
        self.comboBox_Objective.setItemText(1, QCoreApplication.translate("MainWindow", u"50X", None))
        self.comboBox_Objective.setItemText(2, QCoreApplication.translate("MainWindow", u"5X", None))
        self.comboBox_Objective.setItemText(3, QCoreApplication.translate("MainWindow", u"10X", None))

        self.label_FocusNumber.setText(QCoreApplication.translate("MainWindow", u"\u5bf9\u7126\u6b65\u6570", None))
        self.label_FocusStep.setText(QCoreApplication.translate("MainWindow", u"\u5bf9\u7126\u5206\u8fa8\u7387", None))
        self.label_FocusGap_number.setText(QCoreApplication.translate("MainWindow", u"\u9694\u70b9\u5bf9\u7126\u6b65\u957f", None))
        self.label_connect_loader_x.setText(QCoreApplication.translate("MainWindow", u"\u88c5\u8f7d\u5668\u4ea4\u63a5\u5904x", None))
        self.label_connect_loader_y.setText(QCoreApplication.translate("MainWindow", u"\u88c5\u8f7d\u5668\u4ea4\u63a5\u5904y", None))
        self.label_NONE1_5.setText("")
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_5), QCoreApplication.translate("MainWindow", u"Microscope", None))
        self.label_50xCalibration.setText(QCoreApplication.translate("MainWindow", u"50X\u6807\u5b9a\u53c2\u6570", None))
        self.label_20xCalibration.setText(QCoreApplication.translate("MainWindow", u"20X\u6807\u5b9a\u53c2\u6570", None))
        self.label_OnlyCalibration.setText(QCoreApplication.translate("MainWindow", u"\u5355\u955c\u5934\u6807\u5b9a\u53c2\u6570", None))
        self.label_50xWB_R.setText(QCoreApplication.translate("MainWindow", u"50X\u76f8\u673a\u767d\u5e73\u8861R", None))
        self.label_50xWB_G.setText(QCoreApplication.translate("MainWindow", u"50X\u76f8\u673a\u767d\u5e73\u8861G", None))
        self.label_50xWB_B.setText(QCoreApplication.translate("MainWindow", u"50X\u76f8\u673a\u767d\u5e73\u8861B", None))
        self.label_20xWB_R.setText(QCoreApplication.translate("MainWindow", u"20X\u76f8\u673a\u767d\u5e73\u8861R", None))
        self.label_20xWB_G.setText(QCoreApplication.translate("MainWindow", u"20X\u76f8\u673a\u767d\u5e73\u8861G", None))
        self.label_20xWB_B.setText(QCoreApplication.translate("MainWindow", u"20X\u76f8\u673a\u767d\u5e73\u8861B", None))
        self.label_OnlyWB_R.setText(QCoreApplication.translate("MainWindow", u"\u5355\u955c\u5934\u76f8\u673a\u767d\u5e73\u8861R", None))
        self.label_OnlyWB_G.setText(QCoreApplication.translate("MainWindow", u"\u5355\u955c\u5934\u76f8\u673a\u767d\u5e73\u8861G", None))
        self.label_OnlyWB_B.setText(QCoreApplication.translate("MainWindow", u"\u5355\u955c\u5934\u76f8\u673a\u767d\u5e73\u8861B", None))
        self.label_NONE1_6.setText("")
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_6), QCoreApplication.translate("MainWindow", u"Camera", None))
        self.label_LoaderCom.setText(QCoreApplication.translate("MainWindow", u"\u4e32\u53e3", None))
        self.comboBox_LoaderCom.setItemText(0, QCoreApplication.translate("MainWindow", u"COM1", None))
        self.comboBox_LoaderCom.setItemText(1, QCoreApplication.translate("MainWindow", u"COM2", None))
        self.comboBox_LoaderCom.setItemText(2, QCoreApplication.translate("MainWindow", u"COM3", None))
        self.comboBox_LoaderCom.setItemText(3, QCoreApplication.translate("MainWindow", u"COM4", None))
        self.comboBox_LoaderCom.setItemText(4, QCoreApplication.translate("MainWindow", u"COM5", None))
        self.comboBox_LoaderCom.setItemText(5, QCoreApplication.translate("MainWindow", u"COM6", None))
        self.comboBox_LoaderCom.setItemText(6, QCoreApplication.translate("MainWindow", u"COM7", None))
        self.comboBox_LoaderCom.setItemText(7, QCoreApplication.translate("MainWindow", u"COM8", None))
        self.comboBox_LoaderCom.setItemText(8, QCoreApplication.translate("MainWindow", u"COM9", None))
        self.comboBox_LoaderCom.setItemText(9, QCoreApplication.translate("MainWindow", u"COM10", None))
        self.comboBox_LoaderCom.setItemText(10, QCoreApplication.translate("MainWindow", u"COM11", None))
        self.comboBox_LoaderCom.setItemText(11, QCoreApplication.translate("MainWindow", u"COM12", None))
        self.comboBox_LoaderCom.setItemText(12, QCoreApplication.translate("MainWindow", u"COM13", None))
        self.comboBox_LoaderCom.setItemText(13, QCoreApplication.translate("MainWindow", u"COM14", None))
        self.comboBox_LoaderCom.setItemText(14, QCoreApplication.translate("MainWindow", u"COM15", None))
        self.comboBox_LoaderCom.setItemText(15, QCoreApplication.translate("MainWindow", u"COM16", None))
        self.comboBox_LoaderCom.setItemText(16, QCoreApplication.translate("MainWindow", u"COM17", None))
        self.comboBox_LoaderCom.setItemText(17, QCoreApplication.translate("MainWindow", u"COM18", None))
        self.comboBox_LoaderCom.setItemText(18, QCoreApplication.translate("MainWindow", u"COM19", None))
        self.comboBox_LoaderCom.setItemText(19, QCoreApplication.translate("MainWindow", u"COM20", None))

        self.label_Box1_startx.setText(QCoreApplication.translate("MainWindow", u"\u4e00\u53f7\u4ed3\u8d77\u59cb\u70b9x", None))
        self.label_Box1_startz.setText(QCoreApplication.translate("MainWindow", u"\u4e00\u53f7\u4ed3\u8d77\u59cb\u70b9z", None))
        self.label_Box2_startx.setText(QCoreApplication.translate("MainWindow", u"\u4e8c\u53f7\u4ed3\u8d77\u59cb\u70b9x", None))
        self.label_Box2_startz.setText(QCoreApplication.translate("MainWindow", u"\u4e8c\u53f7\u4ed3\u8d77\u59cb\u70b9z", None))
        self.label_Box3_startx.setText(QCoreApplication.translate("MainWindow", u"\u4e09\u53f7\u4ed3\u8d77\u59cb\u70b9x", None))
        self.label_Box3_startz.setText(QCoreApplication.translate("MainWindow", u"\u4e09\u53f7\u4ed3\u8d77\u59cb\u70b9z", None))
        self.label_Box4_startx.setText(QCoreApplication.translate("MainWindow", u"\u56db\u53f7\u4ed3\u8d77\u59cb\u70b9x", None))
        self.label_Box4_startz.setText(QCoreApplication.translate("MainWindow", u"\u56db\u53f7\u4ed3\u8d77\u59cb\u70b9z", None))
        self.label_BoxXGap.setText(QCoreApplication.translate("MainWindow", u"XGap", None))
        self.label_BoxZGap.setText(QCoreApplication.translate("MainWindow", u"ZGap", None))
        self.label_slide_push.setText(QCoreApplication.translate("MainWindow", u"\u4f38\u51fa\u73bb\u7247", None))
        self.label_slide_return.setText(QCoreApplication.translate("MainWindow", u"\u6536\u56de\u73bb\u7247", None))
        self.label_Xavoid.setText(QCoreApplication.translate("MainWindow", u"Xavoid", None))
        self.label_Zlift.setText(QCoreApplication.translate("MainWindow", u"ZLift", None))
        self.label_connect_micro_x.setText(QCoreApplication.translate("MainWindow", u"\u663e\u5fae\u955c\u4ea4\u63a5\u5904x", None))
        self.label_connect_micro_z.setText(QCoreApplication.translate("MainWindow", u"\u663e\u5fae\u955c\u4ea4\u63a5\u5904z", None))
        self.label_cameraindex.setText(QCoreApplication.translate("MainWindow", u"cameraindex", None))
        self.label_cameraexposure.setText(QCoreApplication.translate("MainWindow", u"cameraexposure", None))
        self.label_zcamera.setText(QCoreApplication.translate("MainWindow", u"zcamera", None))
        self.label_rectangleX1.setText(QCoreApplication.translate("MainWindow", u"rectangleX1", None))
        self.label_rectangleY1.setText(QCoreApplication.translate("MainWindow", u"rectangley1", None))
        self.label_rectangleX2.setText(QCoreApplication.translate("MainWindow", u"rectangleX2", None))
        self.label_rectangleY2.setText(QCoreApplication.translate("MainWindow", u"rectangleY2", None))
        self.label_NONE1_7.setText("")
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_7), QCoreApplication.translate("MainWindow", u"Loader", None))
        self.pushButton_save.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u53c2\u6570", None))
        self.tabWidget_run.setTabText(self.tabWidget_run.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u53c2\u6570\u8bbe\u7f6e", None))
        self.label_micro.setText(QCoreApplication.translate("MainWindow", u"\u663e\u5fae\u955c\u79fb\u52a8\u8c03\u8bd5", None))
        self.pushButton_test_micro_movex2.setText(QCoreApplication.translate("MainWindow", u"X\u79fb\u52a8\u5230", None))
        self.pushButton_test_micro_movey2.setText(QCoreApplication.translate("MainWindow", u"Y\u79fb\u52a8\u5230", None))
        self.pushButton_test_micro_movez2.setText(QCoreApplication.translate("MainWindow", u"Z\u79fb\u52a8\u5230", None))
        self.label_micro_2.setText(QCoreApplication.translate("MainWindow", u"\u88c5\u8f7d\u5668\u79fb\u52a8\u8c03\u8bd5", None))
        self.pushButton_test_loader_movex2.setText(QCoreApplication.translate("MainWindow", u"X\u79fb\u52a8\u5230", None))
        self.pushButton_test_loader_movey2.setText(QCoreApplication.translate("MainWindow", u"Y\u79fb\u52a8\u5230", None))
        self.pushButton_test_loader_movez2.setText(QCoreApplication.translate("MainWindow", u"Y\u79fb\u52a8\u5230", None))
        self.label_micro_3.setText(QCoreApplication.translate("MainWindow", u"\u76f8\u673a\u8c03\u8bd5", None))
        self.pushButton_open_cameraonly.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u5355\u955c\u5934\u76f8\u673a", None))
        self.pushButton_close_cameraonly.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed\u5355\u955c\u5934\u76f8\u673a", None))
        self.pushButton_open_camera_1.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u4f4e\u500d\u76f8\u673a", None))
        self.pushButton_close_camera_1.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed\u4f4e\u500d\u76f8\u673a", None))
        self.pushButton_open_camera_2.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u9ad8\u500d\u76f8\u673a", None))
        self.pushButton_close_camera_2.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed\u9ad8\u500d\u76f8\u673a", None))
        self.label_micro_4.setText(QCoreApplication.translate("MainWindow", u"\u706f\u4eae\u5ea6\u8c03\u8bd5", None))
        self.pushButton_open_led_only.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u5355\u955c\u5934\u5149\u6e90", None))
        self.pushButton_close_led_only.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed\u5355\u955c\u5934\u5149\u6e90", None))
        self.pushButton_open_led_1.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u4f4e\u500d\u5149\u6e90", None))
        self.pushButton_close_led_1.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed\u4f4e\u500d\u5149\u6e90", None))
        self.pushButton_open_led_2.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u9ad8\u500d\u5149\u6e902", None))
        self.pushButton_close_led_2.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed\u9ad8\u500d\u5149\u6e90", None))
        self.pushButton_savepic.setText(QCoreApplication.translate("MainWindow", u"\u6355\u83b7\u56fe\u7247", None))
        self.label_NONE1_8.setText("")
        self.pushButton_save_scan.setText(QCoreApplication.translate("MainWindow", u"\u66f4\u6362\u626b\u63cf\u4e2d\u5fc3", None))
        self.pushButton_save_exposure.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u66dd\u5149\u53c2\u6570", None))
        self.tabWidget_run.setTabText(self.tabWidget_run.indexOf(self.tab_8), QCoreApplication.translate("MainWindow", u"\u8c03\u8bd5\u8bbe\u7f6e", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Position", None))
        self.label_X.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.label_SETX.setText("")
        self.label_Y.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.label_SETY.setText("")
        self.label_Z.setText(QCoreApplication.translate("MainWindow", u"Z", None))
        self.label_SETZ.setText("")
        self.label_8.setText("")
        self.menuhelp.setTitle(QCoreApplication.translate("MainWindow", u"help", None))
    # retranslateUi

