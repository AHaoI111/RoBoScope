# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QFrame, QGraphicsView, QHBoxLayout, QLCDNumber,
    QLabel, QLineEdit, QMainWindow, QPlainTextEdit,
    QProgressBar, QPushButton, QScrollArea, QSizePolicy,
    QSlider, QSpinBox, QStackedWidget, QTabWidget,
    QToolBox, QVBoxLayout, QWidget)
from . resources_rc import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1260, 852)
        MainWindow.setMinimumSize(QSize(940, 560))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background"
                        "-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-image: url(:/images/images/images/PyDracula.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: rgb(18"
                        "9, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb("
                        "189, 147, 249);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(189, 147, 249)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border"
                        "-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-sty"
                        "le: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb"
                        "(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-co"
                        "lor: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-c"
                        "olor: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
""
                        "QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     su"
                        "bcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	back"
                        "ground-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subco"
                        "ntrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    h"
                        "eight: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLi"
                        "nkButton {	\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"")
        self.horizontalLayout_35 = QHBoxLayout(self.styleSheet)
        self.horizontalLayout_35.setSpacing(0)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 5, 42, 42))
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setStyleSheet(u"background-image: url(:/images/images/images/kms.ico);")
        self.topLogo.setFrameShape(QFrame.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semibold"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        self.titleLeftDescription.setFont(font2)
        self.titleLeftDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);")

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_scan = QPushButton(self.topMenu)
        self.btn_scan.setObjectName(u"btn_scan")
        sizePolicy.setHeightForWidth(self.btn_scan.sizePolicy().hasHeightForWidth())
        self.btn_scan.setSizePolicy(sizePolicy)
        self.btn_scan.setMinimumSize(QSize(0, 45))
        self.btn_scan.setFont(font)
        self.btn_scan.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_scan.setLayoutDirection(Qt.LeftToRight)
        self.btn_scan.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-caret-right.png);")

        self.verticalLayout_8.addWidget(self.btn_scan)

        self.btn_setting = QPushButton(self.topMenu)
        self.btn_setting.setObjectName(u"btn_setting")
        sizePolicy.setHeightForWidth(self.btn_setting.sizePolicy().hasHeightForWidth())
        self.btn_setting.setSizePolicy(sizePolicy)
        self.btn_setting.setMinimumSize(QSize(0, 45))
        self.btn_setting.setFont(font)
        self.btn_setting.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_setting.setLayoutDirection(Qt.LeftToRight)
        self.btn_setting.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_settings.png);")

        self.verticalLayout_8.addWidget(self.btn_setting)

        self.btn_test = QPushButton(self.topMenu)
        self.btn_test.setObjectName(u"btn_test")
        sizePolicy.setHeightForWidth(self.btn_test.sizePolicy().hasHeightForWidth())
        self.btn_test.setSizePolicy(sizePolicy)
        self.btn_test.setMinimumSize(QSize(0, 45))
        self.btn_test.setFont(font)
        self.btn_test.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_test.setLayoutDirection(Qt.LeftToRight)
        self.btn_test.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-camera.png);")

        self.verticalLayout_8.addWidget(self.btn_test)

        self.btn_internet = QPushButton(self.topMenu)
        self.btn_internet.setObjectName(u"btn_internet")
        sizePolicy.setHeightForWidth(self.btn_internet.sizePolicy().hasHeightForWidth())
        self.btn_internet.setSizePolicy(sizePolicy)
        self.btn_internet.setMinimumSize(QSize(0, 45))
        self.btn_internet.setFont(font)
        self.btn_internet.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_internet.setLayoutDirection(Qt.LeftToRight)
        self.btn_internet.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-rss.png);")

        self.verticalLayout_8.addWidget(self.btn_internet)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)

        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy1)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy2)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        self.titleRightInfo.setFont(font)
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minimizeAppBtn.setIcon(icon)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font3)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.maximizeRestoreAppBtn.setIcon(icon1)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.closeAppBtn.setIcon(icon2)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setStyleSheet(u"background-image: url(:/images/images/images/kms.tif);\n"
"background-position: center;\n"
"background-repeat: no-repeat;")
        self.stackedWidget.addWidget(self.home)
        self.setting = QWidget()
        self.setting.setObjectName(u"setting")
        self.verticalLayout_5 = QVBoxLayout(self.setting)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.scrollArea_2 = QScrollArea(self.setting)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 1136, 960))
        self.verticalLayout_31 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_65 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_65.setObjectName(u"label_65")

        self.verticalLayout_13.addWidget(self.label_65)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.checkBox_1 = QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_1.setObjectName(u"checkBox_1")
        self.checkBox_1.setMinimumSize(QSize(150, 30))
        self.checkBox_1.setMaximumSize(QSize(150, 30))
        self.checkBox_1.setAutoFillBackground(False)
        self.checkBox_1.setStyleSheet(u"")

        self.horizontalLayout_28.addWidget(self.checkBox_1)

        self.checkBox_2 = QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setMinimumSize(QSize(150, 30))
        self.checkBox_2.setMaximumSize(QSize(150, 30))
        self.checkBox_2.setAutoFillBackground(False)
        self.checkBox_2.setStyleSheet(u"")

        self.horizontalLayout_28.addWidget(self.checkBox_2)

        self.checkBox_3 = QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setMinimumSize(QSize(150, 30))
        self.checkBox_3.setMaximumSize(QSize(150, 30))
        self.checkBox_3.setAutoFillBackground(False)
        self.checkBox_3.setStyleSheet(u"")

        self.horizontalLayout_28.addWidget(self.checkBox_3)

        self.checkBox_4 = QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setMinimumSize(QSize(150, 30))
        self.checkBox_4.setMaximumSize(QSize(150, 30))
        self.checkBox_4.setAutoFillBackground(False)
        self.checkBox_4.setStyleSheet(u"")

        self.horizontalLayout_28.addWidget(self.checkBox_4)

        self.label_66 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setMinimumSize(QSize(40, 30))
        self.label_66.setMaximumSize(QSize(40, 30))

        self.horizontalLayout_28.addWidget(self.label_66)

        self.spinBox_slide_number = QSpinBox(self.scrollAreaWidgetContents_2)
        self.spinBox_slide_number.setObjectName(u"spinBox_slide_number")
        self.spinBox_slide_number.setMinimumSize(QSize(150, 30))
        self.spinBox_slide_number.setMaximumSize(QSize(150, 30))

        self.horizontalLayout_28.addWidget(self.spinBox_slide_number)

        self.label_69 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_69.setObjectName(u"label_69")

        self.horizontalLayout_28.addWidget(self.label_69)


        self.verticalLayout_13.addLayout(self.horizontalLayout_28)


        self.verticalLayout_31.addLayout(self.verticalLayout_13)

        self.verticalLayout_35 = QVBoxLayout()
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.label_67 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_67.setObjectName(u"label_67")

        self.verticalLayout_35.addWidget(self.label_67)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_68 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setMinimumSize(QSize(40, 30))
        self.label_68.setMaximumSize(QSize(40, 30))

        self.horizontalLayout_29.addWidget(self.label_68)

        self.spinBox_cameranumber = QSpinBox(self.scrollAreaWidgetContents_2)
        self.spinBox_cameranumber.setObjectName(u"spinBox_cameranumber")
        self.spinBox_cameranumber.setMinimumSize(QSize(150, 30))
        self.spinBox_cameranumber.setMaximumSize(QSize(150, 30))
        self.spinBox_cameranumber.setMaximum(5)

        self.horizontalLayout_29.addWidget(self.spinBox_cameranumber)

        self.checkBox_microscopeflage = QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_microscopeflage.setObjectName(u"checkBox_microscopeflage")
        self.checkBox_microscopeflage.setMinimumSize(QSize(150, 30))
        self.checkBox_microscopeflage.setMaximumSize(QSize(150, 30))
        self.checkBox_microscopeflage.setAutoFillBackground(False)
        self.checkBox_microscopeflage.setStyleSheet(u"")

        self.horizontalLayout_29.addWidget(self.checkBox_microscopeflage)

        self.checkBox_loaderflage = QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_loaderflage.setObjectName(u"checkBox_loaderflage")
        self.checkBox_loaderflage.setMinimumSize(QSize(150, 30))
        self.checkBox_loaderflage.setMaximumSize(QSize(150, 30))
        self.checkBox_loaderflage.setAutoFillBackground(False)
        self.checkBox_loaderflage.setStyleSheet(u"")

        self.horizontalLayout_29.addWidget(self.checkBox_loaderflage)

        self.label_71 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_71.setObjectName(u"label_71")

        self.horizontalLayout_29.addWidget(self.label_71)


        self.verticalLayout_35.addLayout(self.horizontalLayout_29)


        self.verticalLayout_31.addLayout(self.verticalLayout_35)

        self.label_367 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_367.setObjectName(u"label_367")

        self.verticalLayout_31.addWidget(self.label_367)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label_375 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_375.setObjectName(u"label_375")
        self.label_375.setMinimumSize(QSize(120, 30))
        self.label_375.setMaximumSize(QSize(120, 30))

        self.horizontalLayout_30.addWidget(self.label_375)

        self.spinBox_maxworkers = QSpinBox(self.scrollAreaWidgetContents_2)
        self.spinBox_maxworkers.setObjectName(u"spinBox_maxworkers")
        self.spinBox_maxworkers.setMinimumSize(QSize(150, 30))
        self.spinBox_maxworkers.setMaximumSize(QSize(150, 30))
        self.spinBox_maxworkers.setMaximum(20)

        self.horizontalLayout_30.addWidget(self.spinBox_maxworkers)

        self.label_376 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_376.setObjectName(u"label_376")
        self.label_376.setMinimumSize(QSize(120, 30))
        self.label_376.setMaximumSize(QSize(120, 30))

        self.horizontalLayout_30.addWidget(self.label_376)

        self.spinBox_imagestitchsize = QSpinBox(self.scrollAreaWidgetContents_2)
        self.spinBox_imagestitchsize.setObjectName(u"spinBox_imagestitchsize")
        self.spinBox_imagestitchsize.setMinimumSize(QSize(150, 30))
        self.spinBox_imagestitchsize.setMaximumSize(QSize(150, 30))
        self.spinBox_imagestitchsize.setMaximum(2560)

        self.horizontalLayout_30.addWidget(self.spinBox_imagestitchsize)

        self.label_377 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_377.setObjectName(u"label_377")
        self.label_377.setMinimumSize(QSize(120, 30))
        self.label_377.setMaximumSize(QSize(120, 30))

        self.horizontalLayout_30.addWidget(self.label_377)

        self.spinBox_queuenumber = QSpinBox(self.scrollAreaWidgetContents_2)
        self.spinBox_queuenumber.setObjectName(u"spinBox_queuenumber")
        self.spinBox_queuenumber.setMinimumSize(QSize(150, 30))
        self.spinBox_queuenumber.setMaximumSize(QSize(150, 30))
        self.spinBox_queuenumber.setMaximum(2000)

        self.horizontalLayout_30.addWidget(self.spinBox_queuenumber)

        self.label_378 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_378.setObjectName(u"label_378")
        self.label_378.setMinimumSize(QSize(120, 30))
        self.label_378.setMaximumSize(QSize(120, 30))

        self.horizontalLayout_30.addWidget(self.label_378)

        self.spinBox_imagequailty = QSpinBox(self.scrollAreaWidgetContents_2)
        self.spinBox_imagequailty.setObjectName(u"spinBox_imagequailty")
        self.spinBox_imagequailty.setMinimumSize(QSize(150, 30))
        self.spinBox_imagequailty.setMaximumSize(QSize(150, 30))
        self.spinBox_imagequailty.setMaximum(100)

        self.horizontalLayout_30.addWidget(self.spinBox_imagequailty)

        self.label_72 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_72.setObjectName(u"label_72")

        self.horizontalLayout_30.addWidget(self.label_72)


        self.verticalLayout_31.addLayout(self.horizontalLayout_30)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_379 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_379.setObjectName(u"label_379")
        self.label_379.setMinimumSize(QSize(120, 30))
        self.label_379.setMaximumSize(QSize(120, 30))

        self.horizontalLayout_9.addWidget(self.label_379)

        self.comboBox_pixelformat = QComboBox(self.scrollAreaWidgetContents_2)
        self.comboBox_pixelformat.addItem("")
        self.comboBox_pixelformat.addItem("")
        self.comboBox_pixelformat.addItem("")
        self.comboBox_pixelformat.setObjectName(u"comboBox_pixelformat")
        self.comboBox_pixelformat.setMinimumSize(QSize(150, 30))
        self.comboBox_pixelformat.setMaximumSize(QSize(150, 30))
        self.comboBox_pixelformat.setFont(font)
        self.comboBox_pixelformat.setAutoFillBackground(False)
        self.comboBox_pixelformat.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.comboBox_pixelformat.setIconSize(QSize(16, 16))
        self.comboBox_pixelformat.setFrame(True)

        self.horizontalLayout_9.addWidget(self.comboBox_pixelformat)

        self.label_SavePath = QLabel(self.scrollAreaWidgetContents_2)
        self.label_SavePath.setObjectName(u"label_SavePath")
        self.label_SavePath.setMinimumSize(QSize(120, 30))
        self.label_SavePath.setMaximumSize(QSize(120, 30))

        self.horizontalLayout_9.addWidget(self.label_SavePath)

        self.label_savepath = QLabel(self.scrollAreaWidgetContents_2)
        self.label_savepath.setObjectName(u"label_savepath")
        self.label_savepath.setMinimumSize(QSize(120, 30))
        self.label_savepath.setMaximumSize(QSize(120, 30))

        self.horizontalLayout_9.addWidget(self.label_savepath)

        self.pushButton_savepath = QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_savepath.setObjectName(u"pushButton_savepath")
        self.pushButton_savepath.setMinimumSize(QSize(150, 30))
        self.pushButton_savepath.setMaximumSize(QSize(150, 30))
        self.pushButton_savepath.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/cil-save.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_savepath.setIcon(icon3)

        self.horizontalLayout_9.addWidget(self.pushButton_savepath)

        self.label_73 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_73.setObjectName(u"label_73")

        self.horizontalLayout_9.addWidget(self.label_73)


        self.verticalLayout_31.addLayout(self.horizontalLayout_9)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_368 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_368.setObjectName(u"label_368")

        self.verticalLayout_12.addWidget(self.label_368)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_371 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_371.setObjectName(u"label_371")

        self.verticalLayout.addWidget(self.label_371)

        self.plainTextEdit_micro_sys = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.plainTextEdit_micro_sys.setObjectName(u"plainTextEdit_micro_sys")
        self.plainTextEdit_micro_sys.setMinimumSize(QSize(0, 200))
        self.plainTextEdit_micro_sys.setMaximumSize(QSize(16777215, 16777215))
        self.plainTextEdit_micro_sys.setStyleSheet(u"\n"
" border: 3px solid #000000; /* \u8bbe\u7f6e\u8fb9\u6846\u4e3a\u6df1\u9ed1\u8272 */\n"
"                 ")

        self.verticalLayout.addWidget(self.plainTextEdit_micro_sys)


        self.horizontalLayout_11.addLayout(self.verticalLayout)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_372 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_372.setObjectName(u"label_372")

        self.verticalLayout_7.addWidget(self.label_372)

        self.plainTextEdit_micro_single = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.plainTextEdit_micro_single.setObjectName(u"plainTextEdit_micro_single")
        self.plainTextEdit_micro_single.setMinimumSize(QSize(0, 200))
        self.plainTextEdit_micro_single.setMaximumSize(QSize(16777215, 16777215))
        self.plainTextEdit_micro_single.setStyleSheet(u"\n"
" border: 3px solid #000000; /* \u8bbe\u7f6e\u8fb9\u6846\u4e3a\u6df1\u9ed1\u8272 */\n"
"                 ")

        self.verticalLayout_7.addWidget(self.plainTextEdit_micro_single)


        self.horizontalLayout_11.addLayout(self.verticalLayout_7)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_373 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_373.setObjectName(u"label_373")

        self.verticalLayout_10.addWidget(self.label_373)

        self.plainTextEdit_micro_low = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.plainTextEdit_micro_low.setObjectName(u"plainTextEdit_micro_low")
        self.plainTextEdit_micro_low.setMinimumSize(QSize(0, 200))
        self.plainTextEdit_micro_low.setMaximumSize(QSize(16777215, 16777215))
        self.plainTextEdit_micro_low.setStyleSheet(u"\n"
" border: 3px solid #000000; /* \u8bbe\u7f6e\u8fb9\u6846\u4e3a\u6df1\u9ed1\u8272 */\n"
"                 ")

        self.verticalLayout_10.addWidget(self.plainTextEdit_micro_low)


        self.horizontalLayout_11.addLayout(self.verticalLayout_10)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_374 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_374.setObjectName(u"label_374")

        self.verticalLayout_16.addWidget(self.label_374)

        self.plainTextEdit_micro_high = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.plainTextEdit_micro_high.setObjectName(u"plainTextEdit_micro_high")
        self.plainTextEdit_micro_high.setMinimumSize(QSize(0, 200))
        self.plainTextEdit_micro_high.setMaximumSize(QSize(16777215, 16777215))
        self.plainTextEdit_micro_high.setStyleSheet(u"\n"
" border: 3px solid #000000; /* \u8bbe\u7f6e\u8fb9\u6846\u4e3a\u6df1\u9ed1\u8272 */\n"
"                 ")

        self.verticalLayout_16.addWidget(self.plainTextEdit_micro_high)


        self.horizontalLayout_11.addLayout(self.verticalLayout_16)


        self.verticalLayout_12.addLayout(self.horizontalLayout_11)


        self.verticalLayout_31.addLayout(self.verticalLayout_12)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_369 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_369.setObjectName(u"label_369")

        self.verticalLayout_17.addWidget(self.label_369)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_380 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_380.setObjectName(u"label_380")

        self.verticalLayout_11.addWidget(self.label_380)

        self.plainTextEdit_camera_single = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.plainTextEdit_camera_single.setObjectName(u"plainTextEdit_camera_single")
        self.plainTextEdit_camera_single.setMinimumSize(QSize(0, 200))
        self.plainTextEdit_camera_single.setMaximumSize(QSize(16777215, 16777215))
        self.plainTextEdit_camera_single.setStyleSheet(u"\n"
" border: 3px solid #000000; /* \u8bbe\u7f6e\u8fb9\u6846\u4e3a\u6df1\u9ed1\u8272 */\n"
"                 ")

        self.verticalLayout_11.addWidget(self.plainTextEdit_camera_single)


        self.horizontalLayout_12.addLayout(self.verticalLayout_11)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_381 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_381.setObjectName(u"label_381")

        self.verticalLayout_18.addWidget(self.label_381)

        self.plainTextEdit_camera_low = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.plainTextEdit_camera_low.setObjectName(u"plainTextEdit_camera_low")
        self.plainTextEdit_camera_low.setMinimumSize(QSize(0, 200))
        self.plainTextEdit_camera_low.setMaximumSize(QSize(16777215, 16777215))
        self.plainTextEdit_camera_low.setStyleSheet(u"\n"
" border: 3px solid #000000; /* \u8bbe\u7f6e\u8fb9\u6846\u4e3a\u6df1\u9ed1\u8272 */\n"
"                 ")

        self.verticalLayout_18.addWidget(self.plainTextEdit_camera_low)


        self.horizontalLayout_12.addLayout(self.verticalLayout_18)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_382 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_382.setObjectName(u"label_382")

        self.verticalLayout_19.addWidget(self.label_382)

        self.plainTextEdit_camera_high = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.plainTextEdit_camera_high.setObjectName(u"plainTextEdit_camera_high")
        self.plainTextEdit_camera_high.setMinimumSize(QSize(0, 200))
        self.plainTextEdit_camera_high.setMaximumSize(QSize(16777215, 16777215))
        self.plainTextEdit_camera_high.setStyleSheet(u"\n"
" border: 3px solid #000000; /* \u8bbe\u7f6e\u8fb9\u6846\u4e3a\u6df1\u9ed1\u8272 */\n"
"                 ")

        self.verticalLayout_19.addWidget(self.plainTextEdit_camera_high)


        self.horizontalLayout_12.addLayout(self.verticalLayout_19)


        self.verticalLayout_17.addLayout(self.horizontalLayout_12)


        self.verticalLayout_31.addLayout(self.verticalLayout_17)

        self.verticalLayout_30 = QVBoxLayout()
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.label_370 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_370.setObjectName(u"label_370")

        self.verticalLayout_30.addWidget(self.label_370)

        self.plainTextEdit_loader = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.plainTextEdit_loader.setObjectName(u"plainTextEdit_loader")
        self.plainTextEdit_loader.setMinimumSize(QSize(0, 200))
        self.plainTextEdit_loader.setMaximumSize(QSize(16777215, 16777215))
        self.plainTextEdit_loader.setStyleSheet(u"\n"
" border: 3px solid #000000; /* \u8bbe\u7f6e\u8fb9\u6846\u4e3a\u6df1\u9ed1\u8272 */\n"
"                 ")

        self.verticalLayout_30.addWidget(self.plainTextEdit_loader)


        self.verticalLayout_31.addLayout(self.verticalLayout_30)

        self.pushButton_save = QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_save.setObjectName(u"pushButton_save")
        self.pushButton_save.setMinimumSize(QSize(150, 30))
        self.pushButton_save.setMaximumSize(QSize(150, 30))
        self.pushButton_save.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.pushButton_save.setIcon(icon3)

        self.verticalLayout_31.addWidget(self.pushButton_save)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_5.addWidget(self.scrollArea_2)

        self.stackedWidget.addWidget(self.setting)
        self.test = QWidget()
        self.test.setObjectName(u"test")
        self.horizontalLayout_33 = QHBoxLayout(self.test)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.verticalLayout_29 = QVBoxLayout()
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_28 = QVBoxLayout()
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.pushButton_test_micro_movex2 = QPushButton(self.test)
        self.pushButton_test_micro_movex2.setObjectName(u"pushButton_test_micro_movex2")
        self.pushButton_test_micro_movex2.setMinimumSize(QSize(120, 30))
        self.pushButton_test_micro_movex2.setMaximumSize(QSize(120, 30))
        self.pushButton_test_micro_movex2.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/cil-arrow-right.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_test_micro_movex2.setIcon(icon4)

        self.horizontalLayout_10.addWidget(self.pushButton_test_micro_movex2)

        self.doubleSpinBox_test_micro_movex2 = QDoubleSpinBox(self.test)
        self.doubleSpinBox_test_micro_movex2.setObjectName(u"doubleSpinBox_test_micro_movex2")
        self.doubleSpinBox_test_micro_movex2.setMinimumSize(QSize(120, 30))
        self.doubleSpinBox_test_micro_movex2.setMaximumSize(QSize(120, 30))
        self.doubleSpinBox_test_micro_movex2.setDecimals(3)
        self.doubleSpinBox_test_micro_movex2.setMaximum(63.000000000000000)
        self.doubleSpinBox_test_micro_movex2.setSingleStep(0.001000000000000)

        self.horizontalLayout_10.addWidget(self.doubleSpinBox_test_micro_movex2)


        self.verticalLayout_28.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.pushButton_test_micro_movey2 = QPushButton(self.test)
        self.pushButton_test_micro_movey2.setObjectName(u"pushButton_test_micro_movey2")
        self.pushButton_test_micro_movey2.setMinimumSize(QSize(120, 30))
        self.pushButton_test_micro_movey2.setMaximumSize(QSize(120, 30))
        self.pushButton_test_micro_movey2.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.pushButton_test_micro_movey2.setIcon(icon4)

        self.horizontalLayout_13.addWidget(self.pushButton_test_micro_movey2)

        self.doubleSpinBox_test_micro_movey2 = QDoubleSpinBox(self.test)
        self.doubleSpinBox_test_micro_movey2.setObjectName(u"doubleSpinBox_test_micro_movey2")
        self.doubleSpinBox_test_micro_movey2.setMinimumSize(QSize(120, 30))
        self.doubleSpinBox_test_micro_movey2.setMaximumSize(QSize(120, 30))
        self.doubleSpinBox_test_micro_movey2.setDecimals(3)
        self.doubleSpinBox_test_micro_movey2.setMaximum(63.000000000000000)
        self.doubleSpinBox_test_micro_movey2.setSingleStep(0.001000000000000)

        self.horizontalLayout_13.addWidget(self.doubleSpinBox_test_micro_movey2)


        self.verticalLayout_28.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.pushButton_test_micro_movez2 = QPushButton(self.test)
        self.pushButton_test_micro_movez2.setObjectName(u"pushButton_test_micro_movez2")
        self.pushButton_test_micro_movez2.setMinimumSize(QSize(120, 30))
        self.pushButton_test_micro_movez2.setMaximumSize(QSize(120, 30))
        self.pushButton_test_micro_movez2.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.pushButton_test_micro_movez2.setIcon(icon4)

        self.horizontalLayout_14.addWidget(self.pushButton_test_micro_movez2)

        self.doubleSpinBox_test_micro_movez2 = QDoubleSpinBox(self.test)
        self.doubleSpinBox_test_micro_movez2.setObjectName(u"doubleSpinBox_test_micro_movez2")
        self.doubleSpinBox_test_micro_movez2.setMinimumSize(QSize(120, 30))
        self.doubleSpinBox_test_micro_movez2.setMaximumSize(QSize(120, 30))
        self.doubleSpinBox_test_micro_movez2.setDecimals(3)
        self.doubleSpinBox_test_micro_movez2.setMaximum(63.000000000000000)
        self.doubleSpinBox_test_micro_movez2.setSingleStep(0.001000000000000)

        self.horizontalLayout_14.addWidget(self.doubleSpinBox_test_micro_movez2)


        self.verticalLayout_28.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.pushButton_test_loader_movex2 = QPushButton(self.test)
        self.pushButton_test_loader_movex2.setObjectName(u"pushButton_test_loader_movex2")
        self.pushButton_test_loader_movex2.setMinimumSize(QSize(120, 30))
        self.pushButton_test_loader_movex2.setMaximumSize(QSize(120, 30))
        self.pushButton_test_loader_movex2.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.pushButton_test_loader_movex2.setIcon(icon4)

        self.horizontalLayout_15.addWidget(self.pushButton_test_loader_movex2)

        self.doubleSpinBox_test_loader_movex2 = QDoubleSpinBox(self.test)
        self.doubleSpinBox_test_loader_movex2.setObjectName(u"doubleSpinBox_test_loader_movex2")
        self.doubleSpinBox_test_loader_movex2.setMinimumSize(QSize(120, 30))
        self.doubleSpinBox_test_loader_movex2.setMaximumSize(QSize(120, 30))
        self.doubleSpinBox_test_loader_movex2.setDecimals(3)
        self.doubleSpinBox_test_loader_movex2.setMaximum(310.000000000000000)
        self.doubleSpinBox_test_loader_movex2.setSingleStep(0.001000000000000)

        self.horizontalLayout_15.addWidget(self.doubleSpinBox_test_loader_movex2)


        self.verticalLayout_28.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.pushButton_test_loader_movey2 = QPushButton(self.test)
        self.pushButton_test_loader_movey2.setObjectName(u"pushButton_test_loader_movey2")
        self.pushButton_test_loader_movey2.setMinimumSize(QSize(120, 30))
        self.pushButton_test_loader_movey2.setMaximumSize(QSize(120, 30))
        self.pushButton_test_loader_movey2.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.pushButton_test_loader_movey2.setIcon(icon4)

        self.horizontalLayout_16.addWidget(self.pushButton_test_loader_movey2)

        self.doubleSpinBox_test_loader_movey2 = QDoubleSpinBox(self.test)
        self.doubleSpinBox_test_loader_movey2.setObjectName(u"doubleSpinBox_test_loader_movey2")
        self.doubleSpinBox_test_loader_movey2.setMinimumSize(QSize(120, 30))
        self.doubleSpinBox_test_loader_movey2.setMaximumSize(QSize(120, 30))
        self.doubleSpinBox_test_loader_movey2.setDecimals(3)
        self.doubleSpinBox_test_loader_movey2.setMinimum(-92.000000000000000)
        self.doubleSpinBox_test_loader_movey2.setMaximum(-1.000000000000000)
        self.doubleSpinBox_test_loader_movey2.setSingleStep(0.001000000000000)

        self.horizontalLayout_16.addWidget(self.doubleSpinBox_test_loader_movey2)


        self.verticalLayout_28.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.pushButton_test_loader_movez2 = QPushButton(self.test)
        self.pushButton_test_loader_movez2.setObjectName(u"pushButton_test_loader_movez2")
        self.pushButton_test_loader_movez2.setMinimumSize(QSize(120, 30))
        self.pushButton_test_loader_movez2.setMaximumSize(QSize(120, 30))
        self.pushButton_test_loader_movez2.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.pushButton_test_loader_movez2.setIcon(icon4)

        self.horizontalLayout_17.addWidget(self.pushButton_test_loader_movez2)

        self.doubleSpinBox_test_loader_movez2 = QDoubleSpinBox(self.test)
        self.doubleSpinBox_test_loader_movez2.setObjectName(u"doubleSpinBox_test_loader_movez2")
        self.doubleSpinBox_test_loader_movez2.setMinimumSize(QSize(120, 30))
        self.doubleSpinBox_test_loader_movez2.setMaximumSize(QSize(120, 30))
        self.doubleSpinBox_test_loader_movez2.setDecimals(3)
        self.doubleSpinBox_test_loader_movez2.setMaximum(180.000000000000000)
        self.doubleSpinBox_test_loader_movez2.setSingleStep(0.001000000000000)

        self.horizontalLayout_17.addWidget(self.doubleSpinBox_test_loader_movez2)


        self.verticalLayout_28.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.pushButton_micro_reset = QPushButton(self.test)
        self.pushButton_micro_reset.setObjectName(u"pushButton_micro_reset")
        self.pushButton_micro_reset.setMinimumSize(QSize(120, 30))
        self.pushButton_micro_reset.setMaximumSize(QSize(120, 30))
        self.pushButton_micro_reset.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon5 = QIcon()
        icon5.addFile(u":/icons/images/icons/cil-loop.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_micro_reset.setIcon(icon5)

        self.horizontalLayout_7.addWidget(self.pushButton_micro_reset)

        self.pushButton_loader_reset = QPushButton(self.test)
        self.pushButton_loader_reset.setObjectName(u"pushButton_loader_reset")
        self.pushButton_loader_reset.setMinimumSize(QSize(120, 30))
        self.pushButton_loader_reset.setMaximumSize(QSize(120, 30))
        self.pushButton_loader_reset.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.pushButton_loader_reset.setIcon(icon5)

        self.horizontalLayout_7.addWidget(self.pushButton_loader_reset)


        self.verticalLayout_28.addLayout(self.horizontalLayout_7)


        self.verticalLayout_29.addLayout(self.verticalLayout_28)

        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.labelBoxBlenderInstalation_2 = QLabel(self.test)
        self.labelBoxBlenderInstalation_2.setObjectName(u"labelBoxBlenderInstalation_2")
        self.labelBoxBlenderInstalation_2.setMinimumSize(QSize(0, 15))
        self.labelBoxBlenderInstalation_2.setMaximumSize(QSize(16777215, 15))
        self.labelBoxBlenderInstalation_2.setFont(font)
        self.labelBoxBlenderInstalation_2.setStyleSheet(u"")

        self.verticalLayout_14.addWidget(self.labelBoxBlenderInstalation_2)

        self.spinBox_exposure = QSpinBox(self.test)
        self.spinBox_exposure.setObjectName(u"spinBox_exposure")
        self.spinBox_exposure.setMinimumSize(QSize(230, 30))
        self.spinBox_exposure.setMaximumSize(QSize(240, 30))
        self.spinBox_exposure.setMaximum(1000000)

        self.verticalLayout_14.addWidget(self.spinBox_exposure)

        self.horizontalSlider_exposure = QSlider(self.test)
        self.horizontalSlider_exposure.setObjectName(u"horizontalSlider_exposure")
        self.horizontalSlider_exposure.setMinimumSize(QSize(240, 30))
        self.horizontalSlider_exposure.setMaximumSize(QSize(240, 30))
        self.horizontalSlider_exposure.setMaximum(1000000)
        self.horizontalSlider_exposure.setOrientation(Qt.Horizontal)

        self.verticalLayout_14.addWidget(self.horizontalSlider_exposure)


        self.verticalLayout_25.addLayout(self.verticalLayout_14)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.pushButton_open_cameraonly = QPushButton(self.test)
        self.pushButton_open_cameraonly.setObjectName(u"pushButton_open_cameraonly")
        self.pushButton_open_cameraonly.setMinimumSize(QSize(120, 30))
        self.pushButton_open_cameraonly.setMaximumSize(QSize(120, 30))
        self.pushButton_open_cameraonly.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon6 = QIcon()
        icon6.addFile(u":/icons/images/icons/cil-camera.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_open_cameraonly.setIcon(icon6)

        self.horizontalLayout_18.addWidget(self.pushButton_open_cameraonly)

        self.pushButton_close_cameraonly = QPushButton(self.test)
        self.pushButton_close_cameraonly.setObjectName(u"pushButton_close_cameraonly")
        self.pushButton_close_cameraonly.setMinimumSize(QSize(120, 30))
        self.pushButton_close_cameraonly.setMaximumSize(QSize(120, 30))
        self.pushButton_close_cameraonly.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.pushButton_close_cameraonly.setIcon(icon6)

        self.horizontalLayout_18.addWidget(self.pushButton_close_cameraonly)


        self.verticalLayout_25.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.pushButton_open_camera_low = QPushButton(self.test)
        self.pushButton_open_camera_low.setObjectName(u"pushButton_open_camera_low")
        self.pushButton_open_camera_low.setMinimumSize(QSize(120, 30))
        self.pushButton_open_camera_low.setMaximumSize(QSize(120, 30))
        self.pushButton_open_camera_low.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.pushButton_open_camera_low.setIcon(icon6)

        self.horizontalLayout_19.addWidget(self.pushButton_open_camera_low)

        self.pushButton_close_camera_low = QPushButton(self.test)
        self.pushButton_close_camera_low.setObjectName(u"pushButton_close_camera_low")
        self.pushButton_close_camera_low.setMinimumSize(QSize(120, 30))
        self.pushButton_close_camera_low.setMaximumSize(QSize(120, 30))
        self.pushButton_close_camera_low.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.pushButton_close_camera_low.setIcon(icon6)

        self.horizontalLayout_19.addWidget(self.pushButton_close_camera_low)


        self.verticalLayout_25.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.pushButton_open_camera_high = QPushButton(self.test)
        self.pushButton_open_camera_high.setObjectName(u"pushButton_open_camera_high")
        self.pushButton_open_camera_high.setMinimumSize(QSize(120, 30))
        self.pushButton_open_camera_high.setMaximumSize(QSize(120, 30))
        self.pushButton_open_camera_high.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.pushButton_open_camera_high.setIcon(icon6)

        self.horizontalLayout_20.addWidget(self.pushButton_open_camera_high)

        self.pushButton_close_camera_high = QPushButton(self.test)
        self.pushButton_close_camera_high.setObjectName(u"pushButton_close_camera_high")
        self.pushButton_close_camera_high.setMinimumSize(QSize(120, 30))
        self.pushButton_close_camera_high.setMaximumSize(QSize(120, 30))
        self.pushButton_close_camera_high.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.pushButton_close_camera_high.setIcon(icon6)

        self.horizontalLayout_20.addWidget(self.pushButton_close_camera_high)


        self.verticalLayout_25.addLayout(self.horizontalLayout_20)


        self.verticalLayout_29.addLayout(self.verticalLayout_25)

        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.labelBoxBlenderInstalation_3 = QLabel(self.test)
        self.labelBoxBlenderInstalation_3.setObjectName(u"labelBoxBlenderInstalation_3")
        self.labelBoxBlenderInstalation_3.setMinimumSize(QSize(0, 15))
        self.labelBoxBlenderInstalation_3.setMaximumSize(QSize(16777215, 15))
        self.labelBoxBlenderInstalation_3.setFont(font)
        self.labelBoxBlenderInstalation_3.setStyleSheet(u"")

        self.verticalLayout_27.addWidget(self.labelBoxBlenderInstalation_3)

        self.spinBox_led_intensity = QSpinBox(self.test)
        self.spinBox_led_intensity.setObjectName(u"spinBox_led_intensity")
        self.spinBox_led_intensity.setMinimumSize(QSize(230, 30))
        self.spinBox_led_intensity.setMaximumSize(QSize(240, 30))
        self.spinBox_led_intensity.setMaximum(100)

        self.verticalLayout_27.addWidget(self.spinBox_led_intensity)

        self.horizontalSlider_led_intensity = QSlider(self.test)
        self.horizontalSlider_led_intensity.setObjectName(u"horizontalSlider_led_intensity")
        self.horizontalSlider_led_intensity.setMinimumSize(QSize(240, 30))
        self.horizontalSlider_led_intensity.setMaximumSize(QSize(240, 30))
        self.horizontalSlider_led_intensity.setMaximum(100)
        self.horizontalSlider_led_intensity.setOrientation(Qt.Horizontal)

        self.verticalLayout_27.addWidget(self.horizontalSlider_led_intensity)


        self.verticalLayout_26.addLayout(self.verticalLayout_27)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.pushButton_open_led_only = QPushButton(self.test)
        self.pushButton_open_led_only.setObjectName(u"pushButton_open_led_only")
        self.pushButton_open_led_only.setMinimumSize(QSize(120, 30))
        self.pushButton_open_led_only.setMaximumSize(QSize(120, 30))
        self.pushButton_open_led_only.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon7 = QIcon()
        icon7.addFile(u":/icons/images/icons/cil-lightbulb.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_open_led_only.setIcon(icon7)

        self.horizontalLayout_21.addWidget(self.pushButton_open_led_only)

        self.pushButton_close_led_only = QPushButton(self.test)
        self.pushButton_close_led_only.setObjectName(u"pushButton_close_led_only")
        self.pushButton_close_led_only.setMinimumSize(QSize(120, 30))
        self.pushButton_close_led_only.setMaximumSize(QSize(120, 30))
        self.pushButton_close_led_only.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.pushButton_close_led_only.setIcon(icon7)

        self.horizontalLayout_21.addWidget(self.pushButton_close_led_only)


        self.verticalLayout_26.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.pushButton_open_led_low = QPushButton(self.test)
        self.pushButton_open_led_low.setObjectName(u"pushButton_open_led_low")
        self.pushButton_open_led_low.setMinimumSize(QSize(120, 30))
        self.pushButton_open_led_low.setMaximumSize(QSize(120, 30))
        self.pushButton_open_led_low.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.pushButton_open_led_low.setIcon(icon7)

        self.horizontalLayout_22.addWidget(self.pushButton_open_led_low)

        self.pushButton_close_led_low = QPushButton(self.test)
        self.pushButton_close_led_low.setObjectName(u"pushButton_close_led_low")
        self.pushButton_close_led_low.setMinimumSize(QSize(120, 30))
        self.pushButton_close_led_low.setMaximumSize(QSize(120, 30))
        self.pushButton_close_led_low.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.pushButton_close_led_low.setIcon(icon7)

        self.horizontalLayout_22.addWidget(self.pushButton_close_led_low)


        self.verticalLayout_26.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.pushButton_open_led_high = QPushButton(self.test)
        self.pushButton_open_led_high.setObjectName(u"pushButton_open_led_high")
        self.pushButton_open_led_high.setMinimumSize(QSize(120, 30))
        self.pushButton_open_led_high.setMaximumSize(QSize(120, 30))
        self.pushButton_open_led_high.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.pushButton_open_led_high.setIcon(icon7)

        self.horizontalLayout_23.addWidget(self.pushButton_open_led_high)

        self.pushButton_close_led_high = QPushButton(self.test)
        self.pushButton_close_led_high.setObjectName(u"pushButton_close_led_high")
        self.pushButton_close_led_high.setMinimumSize(QSize(120, 30))
        self.pushButton_close_led_high.setMaximumSize(QSize(120, 30))
        self.pushButton_close_led_high.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.pushButton_close_led_high.setIcon(icon7)

        self.horizontalLayout_23.addWidget(self.pushButton_close_led_high)


        self.verticalLayout_26.addLayout(self.horizontalLayout_23)

        self.pushButton_savepic = QPushButton(self.test)
        self.pushButton_savepic.setObjectName(u"pushButton_savepic")
        self.pushButton_savepic.setMinimumSize(QSize(120, 30))
        self.pushButton_savepic.setMaximumSize(QSize(120, 30))
        self.pushButton_savepic.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.pushButton_savepic.setIcon(icon6)

        self.verticalLayout_26.addWidget(self.pushButton_savepic)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.pushButton_save_scan = QPushButton(self.test)
        self.pushButton_save_scan.setObjectName(u"pushButton_save_scan")
        self.pushButton_save_scan.setMinimumSize(QSize(120, 30))
        self.pushButton_save_scan.setMaximumSize(QSize(120, 30))
        self.pushButton_save_scan.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon8 = QIcon()
        icon8.addFile(u":/icons/images/icons/cil-cursor-move.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_save_scan.setIcon(icon8)

        self.horizontalLayout_24.addWidget(self.pushButton_save_scan)

        self.pushButton_save_exposure = QPushButton(self.test)
        self.pushButton_save_exposure.setObjectName(u"pushButton_save_exposure")
        self.pushButton_save_exposure.setMinimumSize(QSize(120, 30))
        self.pushButton_save_exposure.setMaximumSize(QSize(120, 30))
        self.pushButton_save_exposure.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.pushButton_save_exposure.setIcon(icon3)

        self.horizontalLayout_24.addWidget(self.pushButton_save_exposure)


        self.verticalLayout_26.addLayout(self.horizontalLayout_24)


        self.verticalLayout_29.addLayout(self.verticalLayout_26)

        self.labelBoxBlenderInstalation_4 = QLabel(self.test)
        self.labelBoxBlenderInstalation_4.setObjectName(u"labelBoxBlenderInstalation_4")
        self.labelBoxBlenderInstalation_4.setFont(font)
        self.labelBoxBlenderInstalation_4.setStyleSheet(u"")

        self.verticalLayout_29.addWidget(self.labelBoxBlenderInstalation_4)


        self.horizontalLayout_33.addLayout(self.verticalLayout_29)

        self.scrollArea = QScrollArea(self.test)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(200, 200))
        self.scrollArea.setMaximumSize(QSize(16777215, 16777215))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 569, 721))
        self.horizontalLayout_25 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.graphicsView_live = QGraphicsView(self.scrollAreaWidgetContents)
        self.graphicsView_live.setObjectName(u"graphicsView_live")
        self.graphicsView_live.setMinimumSize(QSize(0, 0))
        self.graphicsView_live.setStyleSheet(u"background-color: black\uff1b")

        self.horizontalLayout_25.addWidget(self.graphicsView_live)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_33.addWidget(self.scrollArea)

        self.stackedWidget.addWidget(self.test)
        self.internet = QWidget()
        self.internet.setObjectName(u"internet")
        self.verticalLayout_33 = QVBoxLayout(self.internet)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.checkBox_IP = QCheckBox(self.internet)
        self.checkBox_IP.setObjectName(u"checkBox_IP")
        self.checkBox_IP.setMinimumSize(QSize(150, 30))
        self.checkBox_IP.setMaximumSize(QSize(150, 30))
        self.checkBox_IP.setAutoFillBackground(False)
        self.checkBox_IP.setStyleSheet(u"")

        self.verticalLayout_33.addWidget(self.checkBox_IP)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_70 = QLabel(self.internet)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setMinimumSize(QSize(150, 30))
        self.label_70.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_26.addWidget(self.label_70)

        self.label_IP = QLabel(self.internet)
        self.label_IP.setObjectName(u"label_IP")
        self.label_IP.setMinimumSize(QSize(150, 30))
        self.label_IP.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_26.addWidget(self.label_IP)

        self.label_74 = QLabel(self.internet)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setMinimumSize(QSize(150, 30))
        self.label_74.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_26.addWidget(self.label_74)

        self.label_post = QLabel(self.internet)
        self.label_post.setObjectName(u"label_post")
        self.label_post.setMinimumSize(QSize(150, 30))
        self.label_post.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_26.addWidget(self.label_post)

        self.label_76 = QLabel(self.internet)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setMinimumSize(QSize(150, 30))
        self.label_76.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_26.addWidget(self.label_76)


        self.verticalLayout_33.addLayout(self.horizontalLayout_26)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_79 = QLabel(self.internet)
        self.label_79.setObjectName(u"label_79")
        self.label_79.setMinimumSize(QSize(150, 30))
        self.label_79.setMaximumSize(QSize(150, 30))

        self.horizontalLayout_27.addWidget(self.label_79)

        self.lineEdit_IP = QLineEdit(self.internet)
        self.lineEdit_IP.setObjectName(u"lineEdit_IP")
        self.lineEdit_IP.setMinimumSize(QSize(150, 30))
        self.lineEdit_IP.setMaximumSize(QSize(150, 30))

        self.horizontalLayout_27.addWidget(self.lineEdit_IP)

        self.label_80 = QLabel(self.internet)
        self.label_80.setObjectName(u"label_80")
        self.label_80.setMinimumSize(QSize(150, 30))
        self.label_80.setMaximumSize(QSize(150, 30))

        self.horizontalLayout_27.addWidget(self.label_80)

        self.lineEdit_port = QLineEdit(self.internet)
        self.lineEdit_port.setObjectName(u"lineEdit_port")
        self.lineEdit_port.setMinimumSize(QSize(150, 30))
        self.lineEdit_port.setMaximumSize(QSize(150, 30))

        self.horizontalLayout_27.addWidget(self.lineEdit_port)

        self.pushButton_set_ip = QPushButton(self.internet)
        self.pushButton_set_ip.setObjectName(u"pushButton_set_ip")
        self.pushButton_set_ip.setMinimumSize(QSize(120, 30))
        self.pushButton_set_ip.setMaximumSize(QSize(120, 30))
        self.pushButton_set_ip.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon9 = QIcon()
        icon9.addFile(u":/icons/images/icons/cil-screen-desktop.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_set_ip.setIcon(icon9)

        self.horizontalLayout_27.addWidget(self.pushButton_set_ip)

        self.label_77 = QLabel(self.internet)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setMinimumSize(QSize(150, 30))
        self.label_77.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_27.addWidget(self.label_77)


        self.verticalLayout_33.addLayout(self.horizontalLayout_27)

        self.verticalLayout_32 = QVBoxLayout()
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.label_75 = QLabel(self.internet)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setMinimumSize(QSize(150, 30))
        self.label_75.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_32.addWidget(self.label_75)

        self.plainTextEdit_internetinfo = QPlainTextEdit(self.internet)
        self.plainTextEdit_internetinfo.setObjectName(u"plainTextEdit_internetinfo")
        self.plainTextEdit_internetinfo.setMinimumSize(QSize(0, 200))
        self.plainTextEdit_internetinfo.setMaximumSize(QSize(16777215, 16777215))
        self.plainTextEdit_internetinfo.setStyleSheet(u"\n"
" border: 3px solid #000000; /* \u8bbe\u7f6e\u8fb9\u6846\u4e3a\u6df1\u9ed1\u8272 */\n"
"                 ")

        self.verticalLayout_32.addWidget(self.plainTextEdit_internetinfo)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.pushButton_get = QPushButton(self.internet)
        self.pushButton_get.setObjectName(u"pushButton_get")
        self.pushButton_get.setMinimumSize(QSize(120, 30))
        self.pushButton_get.setMaximumSize(QSize(120, 30))
        self.pushButton_get.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.pushButton_get.setIcon(icon4)

        self.horizontalLayout_31.addWidget(self.pushButton_get)

        self.label_78 = QLabel(self.internet)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setMinimumSize(QSize(150, 30))
        self.label_78.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_31.addWidget(self.label_78)


        self.verticalLayout_32.addLayout(self.horizontalLayout_31)


        self.verticalLayout_33.addLayout(self.verticalLayout_32)

        self.stackedWidget.addWidget(self.internet)
        self.scan = QWidget()
        self.scan.setObjectName(u"scan")
        self.horizontalLayout_34 = QHBoxLayout(self.scan)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.toolBox = QToolBox(self.scan)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setMinimumSize(QSize(300, 0))
        self.toolBox.setMaximumSize(QSize(300, 16777215))
        self.toolBox.setStyleSheet(u"    QToolBox {\n"
"        background: transparent;\n"
"        border: 2px solid #aaa; /* \u8fb9\u6846 */\n"
"        border-radius: 5px; /* \u5706\u89d2 */\n"
"    }\n"
"    QToolBox::tab {\n"
"        background: transparent;\n"
"        border: 1px solid #ccc; /* \u8fb9\u6846 */\n"
"        border-radius: 4px; /* \u5706\u89d2 */\n"
"\n"
"    }\n"
"    QToolBox::tab:selected {\n"
"        background-color: #1a1a2e; /* \u9009\u4e2d\u7684\u9009\u9879\u5361\u989c\u8272 */\n"
"        font-weight: bold; /* \u52a0\u7c97\u5b57\u4f53 */\n"
"    }\n"
"    QToolBox::tab:!selected {\n"
"        background-color: transparent; /* \u975e\u9009\u4e2d\u7684\u9009\u9879\u5361\u989c\u8272 */\n"
"    }")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 296, 667))
        self.verticalLayout_34 = QVBoxLayout(self.page)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.comboBox_Task = QComboBox(self.page)
        self.comboBox_Task.setObjectName(u"comboBox_Task")
        self.comboBox_Task.setMinimumSize(QSize(240, 30))
        self.comboBox_Task.setMaximumSize(QSize(240, 30))
        self.comboBox_Task.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.verticalLayout_21.addWidget(self.comboBox_Task)

        self.pushButton_refresh_plan = QPushButton(self.page)
        self.pushButton_refresh_plan.setObjectName(u"pushButton_refresh_plan")
        self.pushButton_refresh_plan.setMinimumSize(QSize(120, 30))
        self.pushButton_refresh_plan.setMaximumSize(QSize(120, 30))
        self.pushButton_refresh_plan.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon10 = QIcon()
        icon10.addFile(u":/icons/images/icons/cil-loop-circular.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_refresh_plan.setIcon(icon10)

        self.verticalLayout_21.addWidget(self.pushButton_refresh_plan)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.pushButton_slide_task = QPushButton(self.page)
        self.pushButton_slide_task.setObjectName(u"pushButton_slide_task")
        self.pushButton_slide_task.setMinimumSize(QSize(120, 30))
        self.pushButton_slide_task.setMaximumSize(QSize(120, 30))
        self.pushButton_slide_task.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon11 = QIcon()
        icon11.addFile(u":/icons/images/icons/cil-movie.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_slide_task.setIcon(icon11)

        self.horizontalLayout_8.addWidget(self.pushButton_slide_task)

        self.pushButton_reset_slide_task = QPushButton(self.page)
        self.pushButton_reset_slide_task.setObjectName(u"pushButton_reset_slide_task")
        self.pushButton_reset_slide_task.setMinimumSize(QSize(120, 30))
        self.pushButton_reset_slide_task.setMaximumSize(QSize(120, 30))
        self.pushButton_reset_slide_task.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon12 = QIcon()
        icon12.addFile(u":/icons/images/icons/cil-reload.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_reset_slide_task.setIcon(icon12)

        self.horizontalLayout_8.addWidget(self.pushButton_reset_slide_task)


        self.verticalLayout_21.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.pushButton_run = QPushButton(self.page)
        self.pushButton_run.setObjectName(u"pushButton_run")
        self.pushButton_run.setMinimumSize(QSize(120, 30))
        self.pushButton_run.setMaximumSize(QSize(120, 30))
        self.pushButton_run.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon13 = QIcon()
        icon13.addFile(u":/icons/images/icons/cil-media-play.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_run.setIcon(icon13)

        self.horizontalLayout_6.addWidget(self.pushButton_run)

        self.pushButton_pause = QPushButton(self.page)
        self.pushButton_pause.setObjectName(u"pushButton_pause")
        self.pushButton_pause.setMinimumSize(QSize(120, 30))
        self.pushButton_pause.setMaximumSize(QSize(120, 30))
        self.pushButton_pause.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon14 = QIcon()
        icon14.addFile(u":/icons/images/icons/cil-media-pause.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_pause.setIcon(icon14)

        self.horizontalLayout_6.addWidget(self.pushButton_pause)


        self.verticalLayout_21.addLayout(self.horizontalLayout_6)

        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(240, 15))
        self.label_2.setMaximumSize(QSize(240, 15))

        self.verticalLayout_20.addWidget(self.label_2)

        self.label_slide = QLabel(self.page)
        self.label_slide.setObjectName(u"label_slide")
        self.label_slide.setMinimumSize(QSize(240, 80))
        self.label_slide.setMaximumSize(QSize(240, 80))
        self.label_slide.setStyleSheet(u"background-color: rgb(186,186,186);")

        self.verticalLayout_20.addWidget(self.label_slide)

        self.progressBar = QProgressBar(self.page)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMinimumSize(QSize(240, 30))
        self.progressBar.setMaximumSize(QSize(240, 30))
        self.progressBar.setStyleSheet(u"    QProgressBar {\n"
"        border: 2px solid gray; /* \u8fb9\u6846 */\n"
"        border-radius: 5px; /* \u5706\u89d2 */\n"
"        text-align: center; /* \u6587\u5b57\u5c45\u4e2d */\n"
"        height: 20px; /* \u9ad8\u5ea6 */\n"
"    }\n"
"    QProgressBar::chunk {\n"
"        background-color: green; /* \u8fdb\u5ea6\u6761\u989c\u8272 */\n"
"        width: 20px; /* \u8fdb\u5ea6\u5757\u5bbd\u5ea6 */\n"
"    }")
        self.progressBar.setValue(0)

        self.verticalLayout_20.addWidget(self.progressBar)

        self.label_progress = QLabel(self.page)
        self.label_progress.setObjectName(u"label_progress")
        self.label_progress.setMinimumSize(QSize(240, 15))
        self.label_progress.setMaximumSize(QSize(240, 15))

        self.verticalLayout_20.addWidget(self.label_progress)

        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.lcdNumber_hour = QLCDNumber(self.page)
        self.lcdNumber_hour.setObjectName(u"lcdNumber_hour")
        self.lcdNumber_hour.setMinimumSize(QSize(51, 21))
        self.lcdNumber_hour.setMaximumSize(QSize(51, 21))
        self.lcdNumber_hour.setProperty("intValue", 0)

        self.horizontalLayout_32.addWidget(self.lcdNumber_hour)

        self.label_NONE1_2 = QLabel(self.page)
        self.label_NONE1_2.setObjectName(u"label_NONE1_2")
        self.label_NONE1_2.setMinimumSize(QSize(0, 15))
        self.label_NONE1_2.setMaximumSize(QSize(240, 16777215))

        self.horizontalLayout_32.addWidget(self.label_NONE1_2)

        self.lcdNumber_min = QLCDNumber(self.page)
        self.lcdNumber_min.setObjectName(u"lcdNumber_min")
        self.lcdNumber_min.setMinimumSize(QSize(51, 21))
        self.lcdNumber_min.setMaximumSize(QSize(51, 21))
        self.lcdNumber_min.setProperty("intValue", 0)

        self.horizontalLayout_32.addWidget(self.lcdNumber_min)

        self.label_NONE1_3 = QLabel(self.page)
        self.label_NONE1_3.setObjectName(u"label_NONE1_3")
        self.label_NONE1_3.setMinimumSize(QSize(0, 15))
        self.label_NONE1_3.setMaximumSize(QSize(240, 16777215))

        self.horizontalLayout_32.addWidget(self.label_NONE1_3)

        self.lcdNumber_second = QLCDNumber(self.page)
        self.lcdNumber_second.setObjectName(u"lcdNumber_second")
        self.lcdNumber_second.setMinimumSize(QSize(51, 21))
        self.lcdNumber_second.setMaximumSize(QSize(51, 21))
        self.lcdNumber_second.setProperty("intValue", 0)

        self.horizontalLayout_32.addWidget(self.lcdNumber_second)

        self.label_NONE1_4 = QLabel(self.page)
        self.label_NONE1_4.setObjectName(u"label_NONE1_4")
        self.label_NONE1_4.setMinimumSize(QSize(0, 15))
        self.label_NONE1_4.setMaximumSize(QSize(240, 16777215))

        self.horizontalLayout_32.addWidget(self.label_NONE1_4)


        self.verticalLayout_20.addLayout(self.horizontalLayout_32)


        self.verticalLayout_21.addLayout(self.verticalLayout_20)


        self.verticalLayout_34.addLayout(self.verticalLayout_21)

        self.label_NONE1 = QLabel(self.page)
        self.label_NONE1.setObjectName(u"label_NONE1")
        self.label_NONE1.setMinimumSize(QSize(240, 15))
        self.label_NONE1.setMaximumSize(QSize(240, 16777215))

        self.verticalLayout_34.addWidget(self.label_NONE1)

        self.toolBox.addItem(self.page, u"\u626b\u63cf\u73bb\u7247")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 254, 102))
        self.verticalLayout_36 = QVBoxLayout(self.page_2)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label = QLabel(self.page_2)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(240, 15))
        self.label.setMaximumSize(QSize(240, 15))

        self.verticalLayout_22.addWidget(self.label)

        self.textEdit_log = QPlainTextEdit(self.page_2)
        self.textEdit_log.setObjectName(u"textEdit_log")
        self.textEdit_log.setMinimumSize(QSize(240, 0))
        self.textEdit_log.setMaximumSize(QSize(240, 16777215))
        self.textEdit_log.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.verticalLayout_22.addWidget(self.textEdit_log)


        self.verticalLayout_36.addLayout(self.verticalLayout_22)

        self.toolBox.addItem(self.page_2, u"\u65e5\u5fd7\u67e5\u770b")

        self.horizontalLayout_34.addWidget(self.toolBox)

        self.tabWidget = QTabWidget(self.scan)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"            QTabWidget::pane { /* The tab widget frame */\n"
"                border: 3px solid black; /* \u52a0\u7c97\u8fb9\u754c\u6846 */\n"
"                border-radius: 10px; /* \u5706\u89d2\u534a\u5f84 */\n"
"                background-color: rgb(52, 59, 72);\n"
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
"                background: rgb(50,10"
                        "9,245);\n"
"                margin-bottom: 0px; /* overlap with the frame border */\n"
"\n"
"            }\n"
"            QTabBar::tab:!selected {\n"
"                margin-top: 2px; /* make non-selected tabs look smaller */\n"
"            }")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_23 = QVBoxLayout(self.tab)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.graphicsView_fcous = QGraphicsView(self.tab)
        self.graphicsView_fcous.setObjectName(u"graphicsView_fcous")
        self.graphicsView_fcous.setStyleSheet(u"background-color: black\uff1b")

        self.verticalLayout_23.addWidget(self.graphicsView_fcous)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_24 = QVBoxLayout(self.tab_2)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.graphicsView = QGraphicsView(self.tab_2)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setStyleSheet(u"background-color: black\uff1b")

        self.verticalLayout_24.addWidget(self.graphicsView)

        self.tabWidget.addTab(self.tab_2, "")

        self.horizontalLayout_34.addWidget(self.tabWidget)

        self.stackedWidget.addWidget(self.scan)

        self.verticalLayout_15.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMinimumSize(QSize(80, 20))
        self.creditsLabel.setMaximumSize(QSize(80, 16))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setBold(False)
        font4.setItalic(False)
        self.creditsLabel.setFont(font4)
        self.creditsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.creditsLabel_2 = QLabel(self.bottomBar)
        self.creditsLabel_2.setObjectName(u"creditsLabel_2")
        self.creditsLabel_2.setMinimumSize(QSize(30, 16))
        self.creditsLabel_2.setMaximumSize(QSize(30, 16))
        self.creditsLabel_2.setFont(font4)
        self.creditsLabel_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel_2)

        self.label_SETX = QLabel(self.bottomBar)
        self.label_SETX.setObjectName(u"label_SETX")
        self.label_SETX.setMinimumSize(QSize(110, 16))
        self.label_SETX.setMaximumSize(QSize(110, 16))
        self.label_SETX.setFont(font4)
        self.label_SETX.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_SETX)

        self.creditsLabel_3 = QLabel(self.bottomBar)
        self.creditsLabel_3.setObjectName(u"creditsLabel_3")
        self.creditsLabel_3.setMinimumSize(QSize(30, 16))
        self.creditsLabel_3.setMaximumSize(QSize(30, 16))
        self.creditsLabel_3.setFont(font4)
        self.creditsLabel_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel_3)

        self.label_SETY = QLabel(self.bottomBar)
        self.label_SETY.setObjectName(u"label_SETY")
        self.label_SETY.setMinimumSize(QSize(110, 16))
        self.label_SETY.setMaximumSize(QSize(110, 16))
        self.label_SETY.setFont(font4)
        self.label_SETY.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_SETY)

        self.creditsLabel_4 = QLabel(self.bottomBar)
        self.creditsLabel_4.setObjectName(u"creditsLabel_4")
        self.creditsLabel_4.setMinimumSize(QSize(30, 16))
        self.creditsLabel_4.setMaximumSize(QSize(30, 16))
        self.creditsLabel_4.setFont(font4)
        self.creditsLabel_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel_4)

        self.label_SETZ = QLabel(self.bottomBar)
        self.label_SETZ.setObjectName(u"label_SETZ")
        self.label_SETZ.setMinimumSize(QSize(110, 16))
        self.label_SETZ.setMaximumSize(QSize(110, 16))
        self.label_SETZ.setFont(font4)
        self.label_SETZ.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_SETZ)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.horizontalLayout_35.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)
        self.spinBox_exposure.valueChanged.connect(self.horizontalSlider_exposure.setValue)
        self.horizontalSlider_exposure.sliderMoved.connect(self.spinBox_exposure.setValue)
        self.spinBox_led_intensity.valueChanged.connect(self.horizontalSlider_led_intensity.setValue)
        self.horizontalSlider_led_intensity.sliderMoved.connect(self.spinBox_led_intensity.setValue)

        self.stackedWidget.setCurrentIndex(4)
        self.toolBox.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"RoBoScope", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"KMS-roboscope", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"\u9690\u85cf\u529f\u80fd\u680f", None))
        self.btn_scan.setText(QCoreApplication.translate("MainWindow", u"\u626b\u63cf", None))
        self.btn_setting.setText(QCoreApplication.translate("MainWindow", u"\u53c2\u6570\u8bbe\u7f6e", None))
        self.btn_test.setText(QCoreApplication.translate("MainWindow", u"\u8c03\u8bd5", None))
        self.btn_internet.setText(QCoreApplication.translate("MainWindow", u"\u7f51\u7edc\u901a\u4fe1", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"KMS RoBoScope v1.0", None))
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"\u4efb\u52a1\u5206\u914d", None))
        self.checkBox_1.setText(QCoreApplication.translate("MainWindow", u"\u73bb\u7247\u4ed31\u53f7", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"\u73bb\u7247\u4ed32\u53f7", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"\u73bb\u7247\u4ed33\u53f7", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"\u73bb\u7247\u4ed34\u53f7", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"\u73bb\u7247\u6570\u91cf", None))
        self.label_69.setText("")
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u5907\u914d\u7f6e", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"\u76f8\u673a\u6570\u91cf", None))
        self.checkBox_microscopeflage.setText(QCoreApplication.translate("MainWindow", u"\u663e\u5fae\u955c\u8bbe\u5907", None))
        self.checkBox_loaderflage.setText(QCoreApplication.translate("MainWindow", u"\u88c5\u8f7d\u5668\u8bbe\u5907", None))
        self.label_71.setText("")
        self.label_367.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u50cf\u5b58\u50a8", None))
        self.label_375.setText(QCoreApplication.translate("MainWindow", u"maxworkers", None))
        self.label_376.setText(QCoreApplication.translate("MainWindow", u"imagestitchsize", None))
        self.label_377.setText(QCoreApplication.translate("MainWindow", u"queuenumber", None))
        self.label_378.setText(QCoreApplication.translate("MainWindow", u"imagequailty", None))
        self.label_72.setText("")
        self.label_379.setText(QCoreApplication.translate("MainWindow", u"pixelformat", None))
        self.comboBox_pixelformat.setItemText(0, QCoreApplication.translate("MainWindow", u"png", None))
        self.comboBox_pixelformat.setItemText(1, QCoreApplication.translate("MainWindow", u"jpg", None))
        self.comboBox_pixelformat.setItemText(2, QCoreApplication.translate("MainWindow", u"bmp", None))

        self.label_SavePath.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u8def\u5f84", None))
        self.label_savepath.setText(QCoreApplication.translate("MainWindow", u"./pic", None))
        self.pushButton_savepath.setText(QCoreApplication.translate("MainWindow", u"\u66f4\u6539\u56fe\u7247\u4fdd\u5b58\u5730\u5740", None))
        self.label_73.setText("")
        self.label_368.setText(QCoreApplication.translate("MainWindow", u"\u663e\u5fae\u955c\u53c2\u6570\u8bbe\u7f6e", None))
        self.label_371.setText(QCoreApplication.translate("MainWindow", u"\u663e\u5fae\u955c\u7cfb\u7edf", None))
        self.label_372.setText(QCoreApplication.translate("MainWindow", u"\u663e\u5fae\u955c\u5355\u955c\u5934\u7cfb\u7edf\u53c2\u6570", None))
        self.label_373.setText(QCoreApplication.translate("MainWindow", u"\u663e\u5fae\u955c\u53cc\u955c\u5934\u7cfb\u7edf\uff08\u4f4e\u500d\uff09\u53c2\u6570", None))
        self.label_374.setText(QCoreApplication.translate("MainWindow", u"\u663e\u5fae\u955c\u53cc\u955c\u5934\u7cfb\u7edf\uff08\u9ad8\u500d\uff09\u53c2\u6570", None))
        self.label_369.setText(QCoreApplication.translate("MainWindow", u"\u76f8\u673a\u53c2\u6570\u8bbe\u7f6e", None))
        self.label_380.setText(QCoreApplication.translate("MainWindow", u"\u5355\u955c\u5934\u76f8\u673a\u53c2\u6570\u8bbe\u7f6e", None))
        self.label_381.setText(QCoreApplication.translate("MainWindow", u"\u53cc\u955c\u5934\u76f8\u673a\uff08\u4f4e\u500d\uff09\u53c2\u6570\u8bbe\u7f6e", None))
        self.label_382.setText(QCoreApplication.translate("MainWindow", u"\u53cc\u955c\u5934\u76f8\u673a\uff08\u9ad8\u500d\uff09\u53c2\u6570\u8bbe\u7f6e", None))
        self.label_370.setText(QCoreApplication.translate("MainWindow", u"\u88c5\u8f7d\u5668\u53c2\u6570\u8bbe\u7f6e", None))
        self.pushButton_save.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u5f53\u524d\u8bbe\u7f6e\u53c2\u6570", None))
        self.pushButton_test_micro_movex2.setText(QCoreApplication.translate("MainWindow", u"\u663e\u5fae\u955cx\u79fb\u52a8\u81f3", None))
        self.pushButton_test_micro_movey2.setText(QCoreApplication.translate("MainWindow", u"\u663e\u5fae\u955cy\u79fb\u52a8\u81f3", None))
        self.pushButton_test_micro_movez2.setText(QCoreApplication.translate("MainWindow", u"\u663e\u5fae\u955cz\u79fb\u52a8\u81f3", None))
        self.pushButton_test_loader_movex2.setText(QCoreApplication.translate("MainWindow", u"\u88c5\u8f7d\u5668x\u79fb\u52a8\u81f3", None))
        self.pushButton_test_loader_movey2.setText(QCoreApplication.translate("MainWindow", u"\u88c5\u8f7d\u5668y\u79fb\u52a8\u81f3", None))
        self.pushButton_test_loader_movez2.setText(QCoreApplication.translate("MainWindow", u"\u88c5\u8f7d\u5668z\u79fb\u52a8\u81f3", None))
        self.pushButton_micro_reset.setText(QCoreApplication.translate("MainWindow", u"\u663e\u5fae\u955c\u590d\u4f4d", None))
        self.pushButton_loader_reset.setText(QCoreApplication.translate("MainWindow", u"\u88c5\u8f7d\u5668\u590d\u4f4d", None))
        self.labelBoxBlenderInstalation_2.setText(QCoreApplication.translate("MainWindow", u"\u76f8\u673a\u8c03\u8bd5", None))
        self.pushButton_open_cameraonly.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u5355\u955c\u5934\u76f8\u673a", None))
        self.pushButton_close_cameraonly.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed\u5355\u955c\u5934\u76f8\u673a", None))
        self.pushButton_open_camera_low.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u4f4e\u500d\u76f8\u673a", None))
        self.pushButton_close_camera_low.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed\u4f4e\u500d\u76f8\u673a", None))
        self.pushButton_open_camera_high.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u9ad8\u500d\u76f8\u673a", None))
        self.pushButton_close_camera_high.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed\u9ad8\u500d\u76f8\u673a", None))
        self.labelBoxBlenderInstalation_3.setText(QCoreApplication.translate("MainWindow", u"\u5149\u6e90", None))
        self.pushButton_open_led_only.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u5355\u955c\u5934\u5149\u6e90", None))
        self.pushButton_close_led_only.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed\u5355\u955c\u5934\u5149\u6e90", None))
        self.pushButton_open_led_low.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u4f4e\u500d\u5149\u6e90", None))
        self.pushButton_close_led_low.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed\u4f4e\u500d\u5149\u6e90", None))
        self.pushButton_open_led_high.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u9ad8\u500d\u5149\u6e90", None))
        self.pushButton_close_led_high.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed\u9ad8\u500d\u5149\u6e90", None))
        self.pushButton_savepic.setText(QCoreApplication.translate("MainWindow", u"\u6355\u83b7\u56fe\u7247", None))
        self.pushButton_save_scan.setText(QCoreApplication.translate("MainWindow", u"\u66f4\u6362\u626b\u63cf\u4e2d\u5fc3", None))
        self.pushButton_save_exposure.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u66dd\u5149\u53c2\u6570", None))
        self.labelBoxBlenderInstalation_4.setText("")
        self.checkBox_IP.setText(QCoreApplication.translate("MainWindow", u"\u542f\u7528\u7f51\u7edc\u670d\u52a1", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524dIP", None))
        self.label_IP.setText("")
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u7aef\u53e3", None))
        self.label_post.setText("")
        self.label_76.setText("")
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e\u5f53\u524dIP", None))
        self.label_80.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e\u5f53\u524d\u7aef\u53e3", None))
        self.pushButton_set_ip.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u5f53\u524dIP", None))
        self.label_77.setText("")
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"\u6d4b\u8bd5\u7a97\u53e3", None))
        self.pushButton_get.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u9001\u8bf7\u6c42", None))
        self.label_78.setText("")
        self.pushButton_refresh_plan.setText(QCoreApplication.translate("MainWindow", u"\u5237\u65b0\u4efb\u52a1\u65b9\u6848", None))
        self.pushButton_slide_task.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u770b\u73bb\u7247\u4ed3\u4efb\u52a1", None))
        self.pushButton_reset_slide_task.setText(QCoreApplication.translate("MainWindow", u"\u91cd\u7f6e\u73bb\u7247\u4ed3\u4efb\u52a1", None))
        self.pushButton_run.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u626b\u63cf", None))
        self.pushButton_pause.setText(QCoreApplication.translate("MainWindow", u"\u6682\u505c\u626b\u63cf", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u73bb\u7247\u626b\u63cf\u8fdb\u7a0b", None))
        self.label_slide.setText("")
        self.label_progress.setText(QCoreApplication.translate("MainWindow", u"\u8ddd\u79bb\u626b\u63cf\u7ed3\u675f\u8fd8\u5269\uff1a", None))
        self.label_NONE1_2.setText(QCoreApplication.translate("MainWindow", u"\u5c0f\u65f6", None))
        self.label_NONE1_3.setText(QCoreApplication.translate("MainWindow", u"\u5206\u949f", None))
        self.label_NONE1_4.setText(QCoreApplication.translate("MainWindow", u"\u79d2", None))
        self.label_NONE1.setText("")
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("MainWindow", u"\u626b\u63cf\u73bb\u7247", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u626b\u63cf\u65e5\u5fd7", None))
        self.textEdit_log.setPlainText(QCoreApplication.translate("MainWindow", u"\u663e\u793a\u65e5\u5fd7\u4fe1\u606f", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"\u65e5\u5fd7\u67e5\u770b", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u5bf9\u7126\u56fe\u50cf", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u626b\u63cf\u62fc\u56fe", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"Position", None))
        self.creditsLabel_2.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.label_SETX.setText("")
        self.creditsLabel_3.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.label_SETY.setText("")
        self.creditsLabel_4.setText(QCoreApplication.translate("MainWindow", u"Z", None))
        self.label_SETZ.setText("")
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1.0.0", None))
    # retranslateUi

