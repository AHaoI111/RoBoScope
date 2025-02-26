# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(841, 928)
        Dialog.setMinimumSize(QSize(841, 928))
        Dialog.setMaximumSize(QSize(841, 928))
        Dialog.setStyleSheet(u"    background: rgb(128,128,128);")
        self.verticalLayout_5 = QVBoxLayout(Dialog)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.checkBox_1_24 = QCheckBox(Dialog)
        self.checkBox_1_24.setObjectName(u"checkBox_1_24")
        self.checkBox_1_24.setMinimumSize(QSize(120, 30))
        self.checkBox_1_24.setMaximumSize(QSize(120, 30))
        self.checkBox_1_24.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.checkBox_1_24)

        self.checkBox_1_23 = QCheckBox(Dialog)
        self.checkBox_1_23.setObjectName(u"checkBox_1_23")
        self.checkBox_1_23.setMinimumSize(QSize(120, 30))
        self.checkBox_1_23.setMaximumSize(QSize(120, 30))
        self.checkBox_1_23.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.checkBox_1_23)

        self.checkBox_1_22 = QCheckBox(Dialog)
        self.checkBox_1_22.setObjectName(u"checkBox_1_22")
        self.checkBox_1_22.setMinimumSize(QSize(120, 30))
        self.checkBox_1_22.setMaximumSize(QSize(120, 30))
        self.checkBox_1_22.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.checkBox_1_22)

        self.checkBox_1_21 = QCheckBox(Dialog)
        self.checkBox_1_21.setObjectName(u"checkBox_1_21")
        self.checkBox_1_21.setMinimumSize(QSize(120, 30))
        self.checkBox_1_21.setMaximumSize(QSize(120, 30))
        self.checkBox_1_21.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.checkBox_1_21)

        self.checkBox_1_20 = QCheckBox(Dialog)
        self.checkBox_1_20.setObjectName(u"checkBox_1_20")
        self.checkBox_1_20.setMinimumSize(QSize(120, 30))
        self.checkBox_1_20.setMaximumSize(QSize(120, 30))
        self.checkBox_1_20.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.checkBox_1_20)

        self.checkBox_1_19 = QCheckBox(Dialog)
        self.checkBox_1_19.setObjectName(u"checkBox_1_19")
        self.checkBox_1_19.setMinimumSize(QSize(120, 30))
        self.checkBox_1_19.setMaximumSize(QSize(120, 30))
        self.checkBox_1_19.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.checkBox_1_19)

        self.checkBox_1_18 = QCheckBox(Dialog)
        self.checkBox_1_18.setObjectName(u"checkBox_1_18")
        self.checkBox_1_18.setMinimumSize(QSize(120, 30))
        self.checkBox_1_18.setMaximumSize(QSize(120, 30))
        self.checkBox_1_18.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.checkBox_1_18)

        self.checkBox_1_17 = QCheckBox(Dialog)
        self.checkBox_1_17.setObjectName(u"checkBox_1_17")
        self.checkBox_1_17.setMinimumSize(QSize(120, 30))
        self.checkBox_1_17.setMaximumSize(QSize(120, 30))
        self.checkBox_1_17.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.checkBox_1_17)

        self.checkBox_1_16 = QCheckBox(Dialog)
        self.checkBox_1_16.setObjectName(u"checkBox_1_16")
        self.checkBox_1_16.setMinimumSize(QSize(120, 30))
        self.checkBox_1_16.setMaximumSize(QSize(120, 30))
        self.checkBox_1_16.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.checkBox_1_16)

        self.checkBox_1_15 = QCheckBox(Dialog)
        self.checkBox_1_15.setObjectName(u"checkBox_1_15")
        self.checkBox_1_15.setMinimumSize(QSize(120, 30))
        self.checkBox_1_15.setMaximumSize(QSize(120, 30))
        self.checkBox_1_15.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.checkBox_1_15)

        self.checkBox_1_14 = QCheckBox(Dialog)
        self.checkBox_1_14.setObjectName(u"checkBox_1_14")
        self.checkBox_1_14.setMinimumSize(QSize(120, 30))
        self.checkBox_1_14.setMaximumSize(QSize(120, 30))
        self.checkBox_1_14.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.checkBox_1_14)

        self.checkBox_1_13 = QCheckBox(Dialog)
        self.checkBox_1_13.setObjectName(u"checkBox_1_13")
        self.checkBox_1_13.setMinimumSize(QSize(120, 30))
        self.checkBox_1_13.setMaximumSize(QSize(120, 30))
        self.checkBox_1_13.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.checkBox_1_13)

        self.checkBox_1_12 = QCheckBox(Dialog)
        self.checkBox_1_12.setObjectName(u"checkBox_1_12")
        self.checkBox_1_12.setMinimumSize(QSize(120, 30))
        self.checkBox_1_12.setMaximumSize(QSize(120, 30))
        self.checkBox_1_12.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.checkBox_1_12)

        self.checkBox_1_11 = QCheckBox(Dialog)
        self.checkBox_1_11.setObjectName(u"checkBox_1_11")
        self.checkBox_1_11.setMinimumSize(QSize(120, 30))
        self.checkBox_1_11.setMaximumSize(QSize(120, 30))
        self.checkBox_1_11.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.checkBox_1_11)

        self.checkBox_1_10 = QCheckBox(Dialog)
        self.checkBox_1_10.setObjectName(u"checkBox_1_10")
        self.checkBox_1_10.setMinimumSize(QSize(120, 30))
        self.checkBox_1_10.setMaximumSize(QSize(120, 30))
        self.checkBox_1_10.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.checkBox_1_10)

        self.checkBox_1_9 = QCheckBox(Dialog)
        self.checkBox_1_9.setObjectName(u"checkBox_1_9")
        self.checkBox_1_9.setMinimumSize(QSize(120, 30))
        self.checkBox_1_9.setMaximumSize(QSize(120, 30))
        self.checkBox_1_9.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.checkBox_1_9)

        self.checkBox_1_8 = QCheckBox(Dialog)
        self.checkBox_1_8.setObjectName(u"checkBox_1_8")
        self.checkBox_1_8.setMinimumSize(QSize(120, 30))
        self.checkBox_1_8.setMaximumSize(QSize(120, 30))
        self.checkBox_1_8.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.checkBox_1_8)

        self.checkBox_1_7 = QCheckBox(Dialog)
        self.checkBox_1_7.setObjectName(u"checkBox_1_7")
        self.checkBox_1_7.setMinimumSize(QSize(120, 30))
        self.checkBox_1_7.setMaximumSize(QSize(120, 30))
        self.checkBox_1_7.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.checkBox_1_7)

        self.checkBox_1_6 = QCheckBox(Dialog)
        self.checkBox_1_6.setObjectName(u"checkBox_1_6")
        self.checkBox_1_6.setMinimumSize(QSize(120, 30))
        self.checkBox_1_6.setMaximumSize(QSize(120, 30))
        self.checkBox_1_6.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.checkBox_1_6)

        self.checkBox_1_5 = QCheckBox(Dialog)
        self.checkBox_1_5.setObjectName(u"checkBox_1_5")
        self.checkBox_1_5.setMinimumSize(QSize(120, 30))
        self.checkBox_1_5.setMaximumSize(QSize(120, 30))
        self.checkBox_1_5.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.checkBox_1_5)

        self.checkBox_1_4 = QCheckBox(Dialog)
        self.checkBox_1_4.setObjectName(u"checkBox_1_4")
        self.checkBox_1_4.setMinimumSize(QSize(120, 30))
        self.checkBox_1_4.setMaximumSize(QSize(120, 30))
        self.checkBox_1_4.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.checkBox_1_4)

        self.checkBox_1_3 = QCheckBox(Dialog)
        self.checkBox_1_3.setObjectName(u"checkBox_1_3")
        self.checkBox_1_3.setMinimumSize(QSize(120, 30))
        self.checkBox_1_3.setMaximumSize(QSize(120, 30))
        self.checkBox_1_3.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.checkBox_1_3)

        self.checkBox_1_2 = QCheckBox(Dialog)
        self.checkBox_1_2.setObjectName(u"checkBox_1_2")
        self.checkBox_1_2.setMinimumSize(QSize(120, 30))
        self.checkBox_1_2.setMaximumSize(QSize(120, 30))
        self.checkBox_1_2.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.checkBox_1_2)

        self.checkBox_1_1 = QCheckBox(Dialog)
        self.checkBox_1_1.setObjectName(u"checkBox_1_1")
        self.checkBox_1_1.setMinimumSize(QSize(120, 30))
        self.checkBox_1_1.setMaximumSize(QSize(120, 30))
        self.checkBox_1_1.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.checkBox_1_1)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(120, 30))
        self.label.setMaximumSize(QSize(120, 30))
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.checkBox_2_24 = QCheckBox(Dialog)
        self.checkBox_2_24.setObjectName(u"checkBox_2_24")
        self.checkBox_2_24.setMinimumSize(QSize(120, 30))
        self.checkBox_2_24.setMaximumSize(QSize(120, 30))
        self.checkBox_2_24.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.checkBox_2_24)

        self.checkBox_2_23 = QCheckBox(Dialog)
        self.checkBox_2_23.setObjectName(u"checkBox_2_23")
        self.checkBox_2_23.setMinimumSize(QSize(120, 30))
        self.checkBox_2_23.setMaximumSize(QSize(120, 30))
        self.checkBox_2_23.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.checkBox_2_23)

        self.checkBox_2_22 = QCheckBox(Dialog)
        self.checkBox_2_22.setObjectName(u"checkBox_2_22")
        self.checkBox_2_22.setMinimumSize(QSize(120, 30))
        self.checkBox_2_22.setMaximumSize(QSize(120, 30))
        self.checkBox_2_22.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.checkBox_2_22)

        self.checkBox_2_21 = QCheckBox(Dialog)
        self.checkBox_2_21.setObjectName(u"checkBox_2_21")
        self.checkBox_2_21.setMinimumSize(QSize(120, 30))
        self.checkBox_2_21.setMaximumSize(QSize(120, 30))
        self.checkBox_2_21.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.checkBox_2_21)

        self.checkBox_2_20 = QCheckBox(Dialog)
        self.checkBox_2_20.setObjectName(u"checkBox_2_20")
        self.checkBox_2_20.setMinimumSize(QSize(120, 30))
        self.checkBox_2_20.setMaximumSize(QSize(120, 30))
        self.checkBox_2_20.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.checkBox_2_20)

        self.checkBox_2_19 = QCheckBox(Dialog)
        self.checkBox_2_19.setObjectName(u"checkBox_2_19")
        self.checkBox_2_19.setMinimumSize(QSize(120, 30))
        self.checkBox_2_19.setMaximumSize(QSize(120, 30))
        self.checkBox_2_19.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.checkBox_2_19)

        self.checkBox_2_18 = QCheckBox(Dialog)
        self.checkBox_2_18.setObjectName(u"checkBox_2_18")
        self.checkBox_2_18.setMinimumSize(QSize(120, 30))
        self.checkBox_2_18.setMaximumSize(QSize(120, 30))
        self.checkBox_2_18.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.checkBox_2_18)

        self.checkBox_2_17 = QCheckBox(Dialog)
        self.checkBox_2_17.setObjectName(u"checkBox_2_17")
        self.checkBox_2_17.setMinimumSize(QSize(120, 30))
        self.checkBox_2_17.setMaximumSize(QSize(120, 30))
        self.checkBox_2_17.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.checkBox_2_17)

        self.checkBox_2_16 = QCheckBox(Dialog)
        self.checkBox_2_16.setObjectName(u"checkBox_2_16")
        self.checkBox_2_16.setMinimumSize(QSize(120, 30))
        self.checkBox_2_16.setMaximumSize(QSize(120, 30))
        self.checkBox_2_16.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.checkBox_2_16)

        self.checkBox_2_15 = QCheckBox(Dialog)
        self.checkBox_2_15.setObjectName(u"checkBox_2_15")
        self.checkBox_2_15.setMinimumSize(QSize(120, 30))
        self.checkBox_2_15.setMaximumSize(QSize(120, 30))
        self.checkBox_2_15.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.checkBox_2_15)

        self.checkBox_2_14 = QCheckBox(Dialog)
        self.checkBox_2_14.setObjectName(u"checkBox_2_14")
        self.checkBox_2_14.setMinimumSize(QSize(120, 30))
        self.checkBox_2_14.setMaximumSize(QSize(120, 30))
        self.checkBox_2_14.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.checkBox_2_14)

        self.checkBox_2_13 = QCheckBox(Dialog)
        self.checkBox_2_13.setObjectName(u"checkBox_2_13")
        self.checkBox_2_13.setMinimumSize(QSize(120, 30))
        self.checkBox_2_13.setMaximumSize(QSize(120, 30))
        self.checkBox_2_13.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.checkBox_2_13)

        self.checkBox_2_12 = QCheckBox(Dialog)
        self.checkBox_2_12.setObjectName(u"checkBox_2_12")
        self.checkBox_2_12.setMinimumSize(QSize(120, 30))
        self.checkBox_2_12.setMaximumSize(QSize(120, 30))
        self.checkBox_2_12.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.checkBox_2_12)

        self.checkBox_2_11 = QCheckBox(Dialog)
        self.checkBox_2_11.setObjectName(u"checkBox_2_11")
        self.checkBox_2_11.setMinimumSize(QSize(120, 30))
        self.checkBox_2_11.setMaximumSize(QSize(120, 30))
        self.checkBox_2_11.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.checkBox_2_11)

        self.checkBox_2_10 = QCheckBox(Dialog)
        self.checkBox_2_10.setObjectName(u"checkBox_2_10")
        self.checkBox_2_10.setMinimumSize(QSize(120, 30))
        self.checkBox_2_10.setMaximumSize(QSize(120, 30))
        self.checkBox_2_10.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.checkBox_2_10)

        self.checkBox_2_9 = QCheckBox(Dialog)
        self.checkBox_2_9.setObjectName(u"checkBox_2_9")
        self.checkBox_2_9.setMinimumSize(QSize(120, 30))
        self.checkBox_2_9.setMaximumSize(QSize(120, 30))
        self.checkBox_2_9.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.checkBox_2_9)

        self.checkBox_2_8 = QCheckBox(Dialog)
        self.checkBox_2_8.setObjectName(u"checkBox_2_8")
        self.checkBox_2_8.setMinimumSize(QSize(120, 30))
        self.checkBox_2_8.setMaximumSize(QSize(120, 30))
        self.checkBox_2_8.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.checkBox_2_8)

        self.checkBox_2_7 = QCheckBox(Dialog)
        self.checkBox_2_7.setObjectName(u"checkBox_2_7")
        self.checkBox_2_7.setMinimumSize(QSize(120, 30))
        self.checkBox_2_7.setMaximumSize(QSize(120, 30))
        self.checkBox_2_7.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.checkBox_2_7)

        self.checkBox_2_6 = QCheckBox(Dialog)
        self.checkBox_2_6.setObjectName(u"checkBox_2_6")
        self.checkBox_2_6.setMinimumSize(QSize(120, 30))
        self.checkBox_2_6.setMaximumSize(QSize(120, 30))
        self.checkBox_2_6.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.checkBox_2_6)

        self.checkBox_2_5 = QCheckBox(Dialog)
        self.checkBox_2_5.setObjectName(u"checkBox_2_5")
        self.checkBox_2_5.setMinimumSize(QSize(120, 30))
        self.checkBox_2_5.setMaximumSize(QSize(120, 30))
        self.checkBox_2_5.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.checkBox_2_5)

        self.checkBox_2_4 = QCheckBox(Dialog)
        self.checkBox_2_4.setObjectName(u"checkBox_2_4")
        self.checkBox_2_4.setMinimumSize(QSize(120, 30))
        self.checkBox_2_4.setMaximumSize(QSize(120, 30))
        self.checkBox_2_4.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.checkBox_2_4)

        self.checkBox_2_3 = QCheckBox(Dialog)
        self.checkBox_2_3.setObjectName(u"checkBox_2_3")
        self.checkBox_2_3.setMinimumSize(QSize(120, 30))
        self.checkBox_2_3.setMaximumSize(QSize(120, 30))
        self.checkBox_2_3.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.checkBox_2_3)

        self.checkBox_2_2 = QCheckBox(Dialog)
        self.checkBox_2_2.setObjectName(u"checkBox_2_2")
        self.checkBox_2_2.setMinimumSize(QSize(120, 30))
        self.checkBox_2_2.setMaximumSize(QSize(120, 30))
        self.checkBox_2_2.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.checkBox_2_2)

        self.checkBox_2_1 = QCheckBox(Dialog)
        self.checkBox_2_1.setObjectName(u"checkBox_2_1")
        self.checkBox_2_1.setMinimumSize(QSize(120, 30))
        self.checkBox_2_1.setMaximumSize(QSize(120, 30))
        self.checkBox_2_1.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.checkBox_2_1)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(120, 30))
        self.label_2.setMaximumSize(QSize(120, 30))
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.checkBox_3_24 = QCheckBox(Dialog)
        self.checkBox_3_24.setObjectName(u"checkBox_3_24")
        self.checkBox_3_24.setMinimumSize(QSize(120, 30))
        self.checkBox_3_24.setMaximumSize(QSize(120, 30))
        self.checkBox_3_24.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.checkBox_3_24)

        self.checkBox_3_23 = QCheckBox(Dialog)
        self.checkBox_3_23.setObjectName(u"checkBox_3_23")
        self.checkBox_3_23.setMinimumSize(QSize(120, 30))
        self.checkBox_3_23.setMaximumSize(QSize(120, 30))
        self.checkBox_3_23.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.checkBox_3_23)

        self.checkBox_3_22 = QCheckBox(Dialog)
        self.checkBox_3_22.setObjectName(u"checkBox_3_22")
        self.checkBox_3_22.setMinimumSize(QSize(120, 30))
        self.checkBox_3_22.setMaximumSize(QSize(120, 30))
        self.checkBox_3_22.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.checkBox_3_22)

        self.checkBox_3_21 = QCheckBox(Dialog)
        self.checkBox_3_21.setObjectName(u"checkBox_3_21")
        self.checkBox_3_21.setMinimumSize(QSize(120, 30))
        self.checkBox_3_21.setMaximumSize(QSize(120, 30))
        self.checkBox_3_21.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.checkBox_3_21)

        self.checkBox_3_20 = QCheckBox(Dialog)
        self.checkBox_3_20.setObjectName(u"checkBox_3_20")
        self.checkBox_3_20.setMinimumSize(QSize(120, 30))
        self.checkBox_3_20.setMaximumSize(QSize(120, 30))
        self.checkBox_3_20.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.checkBox_3_20)

        self.checkBox_3_19 = QCheckBox(Dialog)
        self.checkBox_3_19.setObjectName(u"checkBox_3_19")
        self.checkBox_3_19.setMinimumSize(QSize(120, 30))
        self.checkBox_3_19.setMaximumSize(QSize(120, 30))
        self.checkBox_3_19.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.checkBox_3_19)

        self.checkBox_3_18 = QCheckBox(Dialog)
        self.checkBox_3_18.setObjectName(u"checkBox_3_18")
        self.checkBox_3_18.setMinimumSize(QSize(120, 30))
        self.checkBox_3_18.setMaximumSize(QSize(120, 30))
        self.checkBox_3_18.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.checkBox_3_18)

        self.checkBox_3_17 = QCheckBox(Dialog)
        self.checkBox_3_17.setObjectName(u"checkBox_3_17")
        self.checkBox_3_17.setMinimumSize(QSize(120, 30))
        self.checkBox_3_17.setMaximumSize(QSize(120, 30))
        self.checkBox_3_17.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.checkBox_3_17)

        self.checkBox_3_16 = QCheckBox(Dialog)
        self.checkBox_3_16.setObjectName(u"checkBox_3_16")
        self.checkBox_3_16.setMinimumSize(QSize(120, 30))
        self.checkBox_3_16.setMaximumSize(QSize(120, 30))
        self.checkBox_3_16.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.checkBox_3_16)

        self.checkBox_3_15 = QCheckBox(Dialog)
        self.checkBox_3_15.setObjectName(u"checkBox_3_15")
        self.checkBox_3_15.setMinimumSize(QSize(120, 30))
        self.checkBox_3_15.setMaximumSize(QSize(120, 30))
        self.checkBox_3_15.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.checkBox_3_15)

        self.checkBox_3_14 = QCheckBox(Dialog)
        self.checkBox_3_14.setObjectName(u"checkBox_3_14")
        self.checkBox_3_14.setMinimumSize(QSize(120, 30))
        self.checkBox_3_14.setMaximumSize(QSize(120, 30))
        self.checkBox_3_14.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.checkBox_3_14)

        self.checkBox_3_13 = QCheckBox(Dialog)
        self.checkBox_3_13.setObjectName(u"checkBox_3_13")
        self.checkBox_3_13.setMinimumSize(QSize(120, 30))
        self.checkBox_3_13.setMaximumSize(QSize(120, 30))
        self.checkBox_3_13.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.checkBox_3_13)

        self.checkBox_3_12 = QCheckBox(Dialog)
        self.checkBox_3_12.setObjectName(u"checkBox_3_12")
        self.checkBox_3_12.setMinimumSize(QSize(120, 30))
        self.checkBox_3_12.setMaximumSize(QSize(120, 30))
        self.checkBox_3_12.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.checkBox_3_12)

        self.checkBox_3_11 = QCheckBox(Dialog)
        self.checkBox_3_11.setObjectName(u"checkBox_3_11")
        self.checkBox_3_11.setMinimumSize(QSize(120, 30))
        self.checkBox_3_11.setMaximumSize(QSize(120, 30))
        self.checkBox_3_11.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.checkBox_3_11)

        self.checkBox_3_10 = QCheckBox(Dialog)
        self.checkBox_3_10.setObjectName(u"checkBox_3_10")
        self.checkBox_3_10.setMinimumSize(QSize(120, 30))
        self.checkBox_3_10.setMaximumSize(QSize(120, 30))
        self.checkBox_3_10.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.checkBox_3_10)

        self.checkBox_3_9 = QCheckBox(Dialog)
        self.checkBox_3_9.setObjectName(u"checkBox_3_9")
        self.checkBox_3_9.setMinimumSize(QSize(120, 30))
        self.checkBox_3_9.setMaximumSize(QSize(120, 30))
        self.checkBox_3_9.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.checkBox_3_9)

        self.checkBox_3_8 = QCheckBox(Dialog)
        self.checkBox_3_8.setObjectName(u"checkBox_3_8")
        self.checkBox_3_8.setMinimumSize(QSize(120, 30))
        self.checkBox_3_8.setMaximumSize(QSize(120, 30))
        self.checkBox_3_8.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.checkBox_3_8)

        self.checkBox_3_7 = QCheckBox(Dialog)
        self.checkBox_3_7.setObjectName(u"checkBox_3_7")
        self.checkBox_3_7.setMinimumSize(QSize(120, 30))
        self.checkBox_3_7.setMaximumSize(QSize(120, 30))
        self.checkBox_3_7.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.checkBox_3_7)

        self.checkBox_3_6 = QCheckBox(Dialog)
        self.checkBox_3_6.setObjectName(u"checkBox_3_6")
        self.checkBox_3_6.setMinimumSize(QSize(120, 30))
        self.checkBox_3_6.setMaximumSize(QSize(120, 30))
        self.checkBox_3_6.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.checkBox_3_6)

        self.checkBox_3_5 = QCheckBox(Dialog)
        self.checkBox_3_5.setObjectName(u"checkBox_3_5")
        self.checkBox_3_5.setMinimumSize(QSize(120, 30))
        self.checkBox_3_5.setMaximumSize(QSize(120, 30))
        self.checkBox_3_5.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.checkBox_3_5)

        self.checkBox_3_4 = QCheckBox(Dialog)
        self.checkBox_3_4.setObjectName(u"checkBox_3_4")
        self.checkBox_3_4.setMinimumSize(QSize(120, 30))
        self.checkBox_3_4.setMaximumSize(QSize(120, 30))
        self.checkBox_3_4.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.checkBox_3_4)

        self.checkBox_3_3 = QCheckBox(Dialog)
        self.checkBox_3_3.setObjectName(u"checkBox_3_3")
        self.checkBox_3_3.setMinimumSize(QSize(120, 30))
        self.checkBox_3_3.setMaximumSize(QSize(120, 30))
        self.checkBox_3_3.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.checkBox_3_3)

        self.checkBox_3_2 = QCheckBox(Dialog)
        self.checkBox_3_2.setObjectName(u"checkBox_3_2")
        self.checkBox_3_2.setMinimumSize(QSize(120, 30))
        self.checkBox_3_2.setMaximumSize(QSize(120, 30))
        self.checkBox_3_2.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.checkBox_3_2)

        self.checkBox_3_1 = QCheckBox(Dialog)
        self.checkBox_3_1.setObjectName(u"checkBox_3_1")
        self.checkBox_3_1.setMinimumSize(QSize(120, 30))
        self.checkBox_3_1.setMaximumSize(QSize(120, 30))
        self.checkBox_3_1.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.checkBox_3_1)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(120, 30))
        self.label_3.setMaximumSize(QSize(120, 30))
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_3)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.checkBox_4_24 = QCheckBox(Dialog)
        self.checkBox_4_24.setObjectName(u"checkBox_4_24")
        self.checkBox_4_24.setMinimumSize(QSize(120, 30))
        self.checkBox_4_24.setMaximumSize(QSize(120, 30))
        self.checkBox_4_24.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout_4.addWidget(self.checkBox_4_24)

        self.checkBox_4_23 = QCheckBox(Dialog)
        self.checkBox_4_23.setObjectName(u"checkBox_4_23")
        self.checkBox_4_23.setMinimumSize(QSize(120, 30))
        self.checkBox_4_23.setMaximumSize(QSize(120, 30))
        self.checkBox_4_23.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout_4.addWidget(self.checkBox_4_23)

        self.checkBox_4_22 = QCheckBox(Dialog)
        self.checkBox_4_22.setObjectName(u"checkBox_4_22")
        self.checkBox_4_22.setMinimumSize(QSize(120, 30))
        self.checkBox_4_22.setMaximumSize(QSize(120, 30))
        self.checkBox_4_22.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout_4.addWidget(self.checkBox_4_22)

        self.checkBox_4_21 = QCheckBox(Dialog)
        self.checkBox_4_21.setObjectName(u"checkBox_4_21")
        self.checkBox_4_21.setMinimumSize(QSize(120, 30))
        self.checkBox_4_21.setMaximumSize(QSize(120, 30))
        self.checkBox_4_21.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout_4.addWidget(self.checkBox_4_21)

        self.checkBox_4_20 = QCheckBox(Dialog)
        self.checkBox_4_20.setObjectName(u"checkBox_4_20")
        self.checkBox_4_20.setMinimumSize(QSize(120, 30))
        self.checkBox_4_20.setMaximumSize(QSize(120, 30))
        self.checkBox_4_20.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout_4.addWidget(self.checkBox_4_20)

        self.checkBox_4_19 = QCheckBox(Dialog)
        self.checkBox_4_19.setObjectName(u"checkBox_4_19")
        self.checkBox_4_19.setMinimumSize(QSize(120, 30))
        self.checkBox_4_19.setMaximumSize(QSize(120, 30))
        self.checkBox_4_19.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout_4.addWidget(self.checkBox_4_19)

        self.checkBox_4_18 = QCheckBox(Dialog)
        self.checkBox_4_18.setObjectName(u"checkBox_4_18")
        self.checkBox_4_18.setMinimumSize(QSize(120, 30))
        self.checkBox_4_18.setMaximumSize(QSize(120, 30))
        self.checkBox_4_18.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout_4.addWidget(self.checkBox_4_18)

        self.checkBox_4_17 = QCheckBox(Dialog)
        self.checkBox_4_17.setObjectName(u"checkBox_4_17")
        self.checkBox_4_17.setMinimumSize(QSize(120, 30))
        self.checkBox_4_17.setMaximumSize(QSize(120, 30))
        self.checkBox_4_17.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout_4.addWidget(self.checkBox_4_17)

        self.checkBox_4_16 = QCheckBox(Dialog)
        self.checkBox_4_16.setObjectName(u"checkBox_4_16")
        self.checkBox_4_16.setMinimumSize(QSize(120, 30))
        self.checkBox_4_16.setMaximumSize(QSize(120, 30))
        self.checkBox_4_16.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout_4.addWidget(self.checkBox_4_16)

        self.checkBox_4_15 = QCheckBox(Dialog)
        self.checkBox_4_15.setObjectName(u"checkBox_4_15")
        self.checkBox_4_15.setMinimumSize(QSize(120, 30))
        self.checkBox_4_15.setMaximumSize(QSize(120, 30))
        self.checkBox_4_15.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout_4.addWidget(self.checkBox_4_15)

        self.checkBox_4_14 = QCheckBox(Dialog)
        self.checkBox_4_14.setObjectName(u"checkBox_4_14")
        self.checkBox_4_14.setMinimumSize(QSize(120, 30))
        self.checkBox_4_14.setMaximumSize(QSize(120, 30))
        self.checkBox_4_14.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout_4.addWidget(self.checkBox_4_14)

        self.checkBox_4_13 = QCheckBox(Dialog)
        self.checkBox_4_13.setObjectName(u"checkBox_4_13")
        self.checkBox_4_13.setMinimumSize(QSize(120, 30))
        self.checkBox_4_13.setMaximumSize(QSize(120, 30))
        self.checkBox_4_13.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout_4.addWidget(self.checkBox_4_13)

        self.checkBox_4_12 = QCheckBox(Dialog)
        self.checkBox_4_12.setObjectName(u"checkBox_4_12")
        self.checkBox_4_12.setMinimumSize(QSize(120, 30))
        self.checkBox_4_12.setMaximumSize(QSize(120, 30))
        self.checkBox_4_12.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout_4.addWidget(self.checkBox_4_12)

        self.checkBox_4_11 = QCheckBox(Dialog)
        self.checkBox_4_11.setObjectName(u"checkBox_4_11")
        self.checkBox_4_11.setMinimumSize(QSize(120, 30))
        self.checkBox_4_11.setMaximumSize(QSize(120, 30))
        self.checkBox_4_11.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout_4.addWidget(self.checkBox_4_11)

        self.checkBox_4_10 = QCheckBox(Dialog)
        self.checkBox_4_10.setObjectName(u"checkBox_4_10")
        self.checkBox_4_10.setMinimumSize(QSize(120, 30))
        self.checkBox_4_10.setMaximumSize(QSize(120, 30))
        self.checkBox_4_10.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout_4.addWidget(self.checkBox_4_10)

        self.checkBox_4_9 = QCheckBox(Dialog)
        self.checkBox_4_9.setObjectName(u"checkBox_4_9")
        self.checkBox_4_9.setMinimumSize(QSize(120, 30))
        self.checkBox_4_9.setMaximumSize(QSize(120, 30))
        self.checkBox_4_9.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout_4.addWidget(self.checkBox_4_9)

        self.checkBox_4_8 = QCheckBox(Dialog)
        self.checkBox_4_8.setObjectName(u"checkBox_4_8")
        self.checkBox_4_8.setMinimumSize(QSize(120, 30))
        self.checkBox_4_8.setMaximumSize(QSize(120, 30))
        self.checkBox_4_8.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout_4.addWidget(self.checkBox_4_8)

        self.checkBox_4_7 = QCheckBox(Dialog)
        self.checkBox_4_7.setObjectName(u"checkBox_4_7")
        self.checkBox_4_7.setMinimumSize(QSize(120, 30))
        self.checkBox_4_7.setMaximumSize(QSize(120, 30))
        self.checkBox_4_7.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout_4.addWidget(self.checkBox_4_7)

        self.checkBox_4_6 = QCheckBox(Dialog)
        self.checkBox_4_6.setObjectName(u"checkBox_4_6")
        self.checkBox_4_6.setMinimumSize(QSize(120, 30))
        self.checkBox_4_6.setMaximumSize(QSize(120, 30))
        self.checkBox_4_6.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout_4.addWidget(self.checkBox_4_6)

        self.checkBox_4_5 = QCheckBox(Dialog)
        self.checkBox_4_5.setObjectName(u"checkBox_4_5")
        self.checkBox_4_5.setMinimumSize(QSize(120, 30))
        self.checkBox_4_5.setMaximumSize(QSize(120, 30))
        self.checkBox_4_5.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout_4.addWidget(self.checkBox_4_5)

        self.checkBox_4_4 = QCheckBox(Dialog)
        self.checkBox_4_4.setObjectName(u"checkBox_4_4")
        self.checkBox_4_4.setMinimumSize(QSize(120, 30))
        self.checkBox_4_4.setMaximumSize(QSize(120, 30))
        self.checkBox_4_4.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout_4.addWidget(self.checkBox_4_4)

        self.checkBox_4_3 = QCheckBox(Dialog)
        self.checkBox_4_3.setObjectName(u"checkBox_4_3")
        self.checkBox_4_3.setMinimumSize(QSize(120, 30))
        self.checkBox_4_3.setMaximumSize(QSize(120, 30))
        self.checkBox_4_3.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout_4.addWidget(self.checkBox_4_3)

        self.checkBox_4_2 = QCheckBox(Dialog)
        self.checkBox_4_2.setObjectName(u"checkBox_4_2")
        self.checkBox_4_2.setMinimumSize(QSize(120, 30))
        self.checkBox_4_2.setMaximumSize(QSize(120, 30))
        self.checkBox_4_2.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout_4.addWidget(self.checkBox_4_2)

        self.checkBox_4_1 = QCheckBox(Dialog)
        self.checkBox_4_1.setObjectName(u"checkBox_4_1")
        self.checkBox_4_1.setMinimumSize(QSize(120, 30))
        self.checkBox_4_1.setMaximumSize(QSize(120, 30))
        self.checkBox_4_1.setStyleSheet(u"QCheckBox {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid #aaa;  /* \u6dfb\u52a0\u8fb9\u6846 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    padding: 5px;             /* \u5185\u8fb9\u8ddd */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease; /* \u6dfb\u52a0\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border-color: #4CAF50;   /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:unchecked {\n"
"    background-color: red;\n"
"    color: black;\n"
"    border-color: #f44336;   /* \u672a\u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: #e0e0e0; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: 2px solid #2196F3; /* \u83b7\u53d6\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout_4.addWidget(self.checkBox_4_1)

        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(120, 30))
        self.label_4.setMaximumSize(QSize(120, 30))
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_4)


        self.horizontalLayout.addLayout(self.verticalLayout_4)


        self.verticalLayout_5.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_reset = QPushButton(Dialog)
        self.pushButton_reset.setObjectName(u"pushButton_reset")
        self.pushButton_reset.setMinimumSize(QSize(120, 30))
        self.pushButton_reset.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_2.addWidget(self.pushButton_reset)

        self.pushButton_save = QPushButton(Dialog)
        self.pushButton_save.setObjectName(u"pushButton_save")
        self.pushButton_save.setMinimumSize(QSize(120, 30))
        self.pushButton_save.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_2.addWidget(self.pushButton_save)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u73bb\u7247\u8bbe\u7f6e", None))
        self.checkBox_1_24.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72471-24", None))
        self.checkBox_1_23.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72471-23", None))
        self.checkBox_1_22.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72471-22", None))
        self.checkBox_1_21.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72471-21", None))
        self.checkBox_1_20.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72471-20", None))
        self.checkBox_1_19.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72471-19", None))
        self.checkBox_1_18.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72471-18", None))
        self.checkBox_1_17.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72471-17", None))
        self.checkBox_1_16.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72471-16", None))
        self.checkBox_1_15.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72471-15", None))
        self.checkBox_1_14.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72471-14", None))
        self.checkBox_1_13.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72471-13", None))
        self.checkBox_1_12.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72471-12", None))
        self.checkBox_1_11.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72471-11", None))
        self.checkBox_1_10.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72471-10", None))
        self.checkBox_1_9.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72471-9", None))
        self.checkBox_1_8.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72471-8", None))
        self.checkBox_1_7.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72471-7", None))
        self.checkBox_1_6.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72471-6", None))
        self.checkBox_1_5.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72471-5", None))
        self.checkBox_1_4.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72471-4", None))
        self.checkBox_1_3.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72471-3", None))
        self.checkBox_1_2.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72471-2", None))
        self.checkBox_1_1.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72471-1", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"1\u53f7\u73bb\u7247\u4ed3", None))
        self.checkBox_2_24.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72472-24", None))
        self.checkBox_2_23.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72472-23", None))
        self.checkBox_2_22.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72472-22", None))
        self.checkBox_2_21.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72472-21", None))
        self.checkBox_2_20.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72472-20", None))
        self.checkBox_2_19.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72472-19", None))
        self.checkBox_2_18.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72472-18", None))
        self.checkBox_2_17.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72472-17", None))
        self.checkBox_2_16.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72472-16", None))
        self.checkBox_2_15.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72472-15", None))
        self.checkBox_2_14.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72472-14", None))
        self.checkBox_2_13.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72472-13", None))
        self.checkBox_2_12.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72472-12", None))
        self.checkBox_2_11.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72472-11", None))
        self.checkBox_2_10.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72472-10", None))
        self.checkBox_2_9.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72472-9", None))
        self.checkBox_2_8.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72472-8", None))
        self.checkBox_2_7.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72472-7", None))
        self.checkBox_2_6.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72472-6", None))
        self.checkBox_2_5.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72472-5", None))
        self.checkBox_2_4.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72472-4", None))
        self.checkBox_2_3.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72472-3", None))
        self.checkBox_2_2.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72472-2", None))
        self.checkBox_2_1.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72472-1", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"2\u53f7\u73bb\u7247\u4ed3", None))
        self.checkBox_3_24.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72473-24", None))
        self.checkBox_3_23.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72473-23", None))
        self.checkBox_3_22.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72473-22", None))
        self.checkBox_3_21.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72473-21", None))
        self.checkBox_3_20.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72473-20", None))
        self.checkBox_3_19.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72473-19", None))
        self.checkBox_3_18.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72473-18", None))
        self.checkBox_3_17.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72473-17", None))
        self.checkBox_3_16.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72473-16", None))
        self.checkBox_3_15.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72473-15", None))
        self.checkBox_3_14.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72473-14", None))
        self.checkBox_3_13.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72473-13", None))
        self.checkBox_3_12.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72473-12", None))
        self.checkBox_3_11.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72473-11", None))
        self.checkBox_3_10.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72473-10", None))
        self.checkBox_3_9.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72473-9", None))
        self.checkBox_3_8.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72473-8", None))
        self.checkBox_3_7.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72473-7", None))
        self.checkBox_3_6.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72473-6", None))
        self.checkBox_3_5.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72473-5", None))
        self.checkBox_3_4.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72473-4", None))
        self.checkBox_3_3.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72473-3", None))
        self.checkBox_3_2.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72473-2", None))
        self.checkBox_3_1.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72473-1", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"3\u53f7\u73bb\u7247\u4ed3", None))
        self.checkBox_4_24.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72474-24", None))
        self.checkBox_4_23.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72474-23", None))
        self.checkBox_4_22.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72474-22", None))
        self.checkBox_4_21.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72474-21", None))
        self.checkBox_4_20.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72474-20", None))
        self.checkBox_4_19.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72474-19", None))
        self.checkBox_4_18.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72474-18", None))
        self.checkBox_4_17.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72474-17", None))
        self.checkBox_4_16.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72474-16", None))
        self.checkBox_4_15.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72474-15", None))
        self.checkBox_4_14.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72474-14", None))
        self.checkBox_4_13.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72474-13", None))
        self.checkBox_4_12.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72474-12", None))
        self.checkBox_4_11.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72474-11", None))
        self.checkBox_4_10.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72474-10", None))
        self.checkBox_4_9.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72474-9", None))
        self.checkBox_4_8.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72474-8", None))
        self.checkBox_4_7.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72474-7", None))
        self.checkBox_4_6.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72474-6", None))
        self.checkBox_4_5.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72474-5", None))
        self.checkBox_4_4.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72474-4", None))
        self.checkBox_4_3.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72474-3", None))
        self.checkBox_4_2.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72474-2", None))
        self.checkBox_4_1.setText(QCoreApplication.translate("Dialog", u"\u73bb\u72474-1", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"4\u53f7\u73bb\u7247\u4ed3", None))
        self.pushButton_reset.setText(QCoreApplication.translate("Dialog", u"\u91cd\u7f6e\u73bb\u7247\u4efb\u52a1", None))
        self.pushButton_save.setText(QCoreApplication.translate("Dialog", u"\u4fdd\u5b58\u5f53\u524d\u8bbe\u7f6e", None))
    # retranslateUi

