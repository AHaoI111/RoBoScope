# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'BIOscope.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
                               QMainWindow, QMenu, QMenuBar, QPushButton,
                               QSizePolicy, QStatusBar, QTextEdit, QVBoxLayout,
                               QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1207, 1247)
        MainWindow.setMinimumSize(QSize(1207, 1071))
        font = QFont()
        font.setFamilies([u"Microsoft YaHei"])
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u"UI/ICON/icon.jpg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QMainWindow {\n"
                                 "    background-color:  rgb(53, 55, 58);\n"
                                 "}\n"
                                 "QMainWindow::titleBar {\n"
                                 "    background-color:  rgb(120, 120, 120);\n"
                                 "    color: white;\n"
                                 "}\n"
                                 "")
        self.actionshuju = QAction(MainWindow)
        self.actionshuju.setObjectName(u"actionshuju")
        self.actionshezhi = QAction(MainWindow)
        self.actionshezhi.setObjectName(u"actionshezhi")
        self.actionopen = QAction(MainWindow)
        self.actionopen.setObjectName(u"actionopen")
        self.actionturn_on = QAction(MainWindow)
        self.actionturn_on.setObjectName(u"actionturn_on")
        self.actionturn_off = QAction(MainWindow)
        self.actionturn_off.setObjectName(u"actionturn_off")
        self.actionclose = QAction(MainWindow)
        self.actionclose.setObjectName(u"actionclose")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(400, 300))
        self.label.setMaximumSize(QSize(400, 300))
        self.label.setStyleSheet(u"background-color: rgb(30, 30, 30);")

        self.verticalLayout_2.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Sketch_map = QLabel(self.centralwidget)
        self.Sketch_map.setObjectName(u"Sketch_map")
        self.Sketch_map.setMinimumSize(QSize(328, 273))
        self.Sketch_map.setMaximumSize(QSize(328, 273))
        self.Sketch_map.setStyleSheet(u"background-color:  rgb(43, 45, 48);\n"
                                      "color: rgb(200, 200, 200);\n"
                                      "border:1px solid rgb(33,35, 38);")

        self.horizontalLayout.addWidget(self.Sketch_map)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pos_x = QLabel(self.centralwidget)
        self.pos_x.setObjectName(u"pos_x")
        self.pos_x.setMinimumSize(QSize(100, 30))
        self.pos_x.setMaximumSize(QSize(100, 30))
        self.pos_x.setStyleSheet(u"background-color:  rgb(43, 45, 48);\n"
                                 "color: rgb(200, 200, 200);\n"
                                 "border:1px solid rgb(33,35, 38);")

        self.verticalLayout.addWidget(self.pos_x)

        self.pos_y = QLabel(self.centralwidget)
        self.pos_y.setObjectName(u"pos_y")
        self.pos_y.setMinimumSize(QSize(100, 30))
        self.pos_y.setMaximumSize(QSize(100, 30))
        self.pos_y.setStyleSheet(u"background-color:  rgb(43, 45, 48);\n"
                                 "color: rgb(200, 200, 200);\n"
                                 "border:1px solid rgb(33,35, 38);")

        self.verticalLayout.addWidget(self.pos_y)

        self.pos_z = QLabel(self.centralwidget)
        self.pos_z.setObjectName(u"pos_z")
        self.pos_z.setMinimumSize(QSize(100, 30))
        self.pos_z.setMaximumSize(QSize(100, 30))
        self.pos_z.setStyleSheet(u"background-color:  rgb(43, 45, 48);\n"
                                 "color: rgb(200, 200, 200);\n"
                                 "border:1px solid rgb(33,35, 38);")

        self.verticalLayout.addWidget(self.pos_z)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.lineEdit_11 = QLineEdit(self.centralwidget)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        sizePolicy.setHeightForWidth(self.lineEdit_11.sizePolicy().hasHeightForWidth())
        self.lineEdit_11.setSizePolicy(sizePolicy)
        self.lineEdit_11.setMinimumSize(QSize(400, 30))
        self.lineEdit_11.setMaximumSize(QSize(400, 30))
        font1 = QFont()
        font1.setPointSize(10)
        self.lineEdit_11.setFont(font1)
        self.lineEdit_11.setStyleSheet(u"background-color:  rgb(43, 45, 48);\n"
                                       "color: rgb(200, 200, 200);\n"
                                       "border:1px solid rgb(33,35, 38);")

        self.verticalLayout_6.addWidget(self.lineEdit_11)

        self.result = QTextEdit(self.centralwidget)
        self.result.setObjectName(u"result")
        self.result.setMinimumSize(QSize(400, 20))
        self.result.setMaximumSize(QSize(400, 999999))
        self.result.setFont(font1)
        self.result.setStyleSheet(u"background-color:  rgb(43, 45, 48);\n"
                                  "color: rgb(200, 200, 200);\n"
                                  "border:1px solid rgb(33,35, 38);")

        self.verticalLayout_6.addWidget(self.result)

        self.verticalLayout_2.addLayout(self.verticalLayout_6)

        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        self.label_3.setMinimumSize(QSize(578, 463))
        self.label_3.setMaximumSize(QSize(16777215, 16777215))
        self.label_3.setStyleSheet(u"background-color:  rgb(43, 45, 48);\n"
                                   "color: rgb(200, 200, 200);\n"
                                   "border:1px solid rgb(33,35, 38);")

        self.verticalLayout_3.addWidget(self.label_3)

        self.lineEdit_information = QLineEdit(self.centralwidget)
        self.lineEdit_information.setObjectName(u"lineEdit_information")
        sizePolicy1.setHeightForWidth(self.lineEdit_information.sizePolicy().hasHeightForWidth())
        self.lineEdit_information.setSizePolicy(sizePolicy1)
        self.lineEdit_information.setMinimumSize(QSize(578, 30))
        self.lineEdit_information.setMaximumSize(QSize(99999, 30))
        self.lineEdit_information.setFont(font1)
        self.lineEdit_information.setStyleSheet(u"background-color:  rgb(43, 45, 48);\n"
                                                "color: rgb(200, 200, 200);\n"
                                                "border:1px solid rgb(33,35, 38);")

        self.verticalLayout_3.addWidget(self.lineEdit_information)

        self.lineEdit_12 = QLineEdit(self.centralwidget)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        sizePolicy1.setHeightForWidth(self.lineEdit_12.sizePolicy().hasHeightForWidth())
        self.lineEdit_12.setSizePolicy(sizePolicy1)
        self.lineEdit_12.setMinimumSize(QSize(578, 30))
        self.lineEdit_12.setMaximumSize(QSize(99999, 30))
        self.lineEdit_12.setFont(font1)
        self.lineEdit_12.setStyleSheet(u"background-color:  rgb(43, 45, 48);\n"
                                       "color: rgb(200, 200, 200);\n"
                                       "border:1px solid rgb(33,35, 38);")

        self.verticalLayout_3.addWidget(self.lineEdit_12)

        self.log = QTextEdit(self.centralwidget)
        self.log.setObjectName(u"log")
        self.log.setMinimumSize(QSize(578, 150))
        self.log.setMaximumSize(QSize(999999, 150))
        self.log.setStyleSheet(u"background-color:  rgb(43, 45, 48);\n"
                               "color: rgb(200, 200, 200);\n"
                               "border:1px solid rgb(33,35, 38);")

        self.verticalLayout_3.addWidget(self.log)

        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.Initialize_device = QPushButton(self.centralwidget)
        self.Initialize_device.setObjectName(u"Initialize_device")
        sizePolicy.setHeightForWidth(self.Initialize_device.sizePolicy().hasHeightForWidth())
        self.Initialize_device.setSizePolicy(sizePolicy)
        self.Initialize_device.setMinimumSize(QSize(80, 80))
        self.Initialize_device.setMaximumSize(QSize(80, 80))
        self.Initialize_device.setStyleSheet(u"background-color:  rgb(43, 45, 48);\n"
                                             "color: rgb(200, 200, 200);\n"
                                             "border:1px solid rgb(33,35, 38);")

        self.verticalLayout_4.addWidget(self.Initialize_device)

        self.move_only = QPushButton(self.centralwidget)
        self.move_only.setObjectName(u"move_only")
        sizePolicy.setHeightForWidth(self.move_only.sizePolicy().hasHeightForWidth())
        self.move_only.setSizePolicy(sizePolicy)
        self.move_only.setMinimumSize(QSize(80, 80))
        self.move_only.setMaximumSize(QSize(80, 80))
        self.move_only.setStyleSheet(u"background-color:  rgb(43, 45, 48);\n"
                                     "color: rgb(200, 200, 200);\n"
                                     "border:1px solid rgb(33,35, 38);")

        self.verticalLayout_4.addWidget(self.move_only)

        self.move_stop = QPushButton(self.centralwidget)
        self.move_stop.setObjectName(u"move_stop")
        sizePolicy.setHeightForWidth(self.move_stop.sizePolicy().hasHeightForWidth())
        self.move_stop.setSizePolicy(sizePolicy)
        self.move_stop.setMinimumSize(QSize(80, 80))
        self.move_stop.setMaximumSize(QSize(80, 80))
        self.move_stop.setStyleSheet(u"background-color:  rgb(43, 45, 48);\n"
                                     "color: rgb(200, 200, 200);\n"
                                     "border:1px solid rgb(33,35, 38);")

        self.verticalLayout_4.addWidget(self.move_stop)

        self.move_home = QPushButton(self.centralwidget)
        self.move_home.setObjectName(u"move_home")
        sizePolicy.setHeightForWidth(self.move_home.sizePolicy().hasHeightForWidth())
        self.move_home.setSizePolicy(sizePolicy)
        self.move_home.setMinimumSize(QSize(80, 80))
        self.move_home.setMaximumSize(QSize(80, 80))
        self.move_home.setStyleSheet(u"background-color:  rgb(43, 45, 48);\n"
                                     "color: rgb(200, 200, 200);\n"
                                     "border:1px solid rgb(33,35, 38);")

        self.verticalLayout_4.addWidget(self.move_home)

        self.move_go = QPushButton(self.centralwidget)
        self.move_go.setObjectName(u"move_go")
        sizePolicy.setHeightForWidth(self.move_go.sizePolicy().hasHeightForWidth())
        self.move_go.setSizePolicy(sizePolicy)
        self.move_go.setMinimumSize(QSize(80, 80))
        self.move_go.setMaximumSize(QSize(80, 80))
        self.move_go.setStyleSheet(u"background-color:  rgb(43, 45, 48);\n"
                                   "color: rgb(200, 200, 200);\n"
                                   "border:1px solid rgb(33,35, 38);")

        self.verticalLayout_4.addWidget(self.move_go)

        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1207, 21))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_data = QMenu(self.menubar)
        self.menu_data.setObjectName(u"menu_data")
        self.menu_set = QMenu(self.menubar)
        self.menu_set.setObjectName(u"menu_set")
        self.menu_control = QMenu(self.menubar)
        self.menu_control.setObjectName(u"menu_control")
        self.menuCamera = QMenu(self.menu_control)
        self.menuCamera.setObjectName(u"menuCamera")
        self.menuLED = QMenu(self.menu_control)
        self.menuLED.setObjectName(u"menuLED")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_data.menuAction())
        self.menubar.addAction(self.menu_set.menuAction())
        self.menubar.addAction(self.menu_control.menuAction())
        self.menu_data.addAction(self.actionshuju)
        self.menu_set.addAction(self.actionshezhi)
        self.menu_control.addAction(self.menuCamera.menuAction())
        self.menu_control.addAction(self.menuLED.menuAction())
        self.menuCamera.addAction(self.actionopen)
        self.menuCamera.addAction(self.actionclose)
        self.menuLED.addSeparator()
        self.menuLED.addSeparator()
        self.menuLED.addAction(self.actionturn_on)
        self.menuLED.addAction(self.actionturn_off)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"BIOscope", None))
        self.actionshuju.setText(QCoreApplication.translate("MainWindow", u"数据浏览", None))
        self.actionshezhi.setText(QCoreApplication.translate("MainWindow", u"设置中心", None))
        self.actionopen.setText(QCoreApplication.translate("MainWindow", u"打开", None))
        self.actionturn_on.setText(QCoreApplication.translate("MainWindow", u"打开", None))
        self.actionturn_off.setText(QCoreApplication.translate("MainWindow", u"关闭", None))
        self.actionclose.setText(QCoreApplication.translate("MainWindow", u"关闭", None))
        self.label.setText("")
        self.Sketch_map.setText("")
        self.pos_x.setText("")
        self.pos_y.setText("")
        self.pos_z.setText("")
        self.lineEdit_11.setText(QCoreApplication.translate("MainWindow", u"\u5df2\u626b\u63cf", None))
        self.label_3.setText("")
        self.lineEdit_information.setText("")
        self.lineEdit_12.setText(QCoreApplication.translate("MainWindow", u"\u65e5\u5fd7\u5217\u8868", None))
        self.Initialize_device.setText(QCoreApplication.translate("MainWindow", u"\u521d\u59cb\u5316\n"
                                                                                "\u8bbe\u5907", None))
        self.move_only.setText(QCoreApplication.translate("MainWindow", u"\u5355\u5f20", None))
        self.move_stop.setText(QCoreApplication.translate("MainWindow", u"\u505c\u6b62", None))
        self.move_home.setText(QCoreApplication.translate("MainWindow", u"\u590d\u4f4d", None))
        self.move_go.setText(QCoreApplication.translate("MainWindow", u"\u5f39\u51fa\u8f7d\u7269\u53f0", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
        self.menu_data.setTitle(QCoreApplication.translate("MainWindow", u"\u6570\u636e", None))
        self.menu_set.setTitle(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
        self.menu_control.setTitle(QCoreApplication.translate("MainWindow", u"\u63a7\u5236", None))
        self.menuCamera.setTitle(QCoreApplication.translate("MainWindow", u"Camera", None))
        self.menuLED.setTitle(QCoreApplication.translate("MainWindow", u"LED", None))
    # retranslateUi
