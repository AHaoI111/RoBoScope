# -*- encoding: utf-8 -*-
"""
@Description:
程序主函数入口
@File    :   main.py
@Time    :   2024/07/16
@Author  :   Li QingHao
@Version :   2.0
@Time_END :  最后修改时间：
@Developers_END :  最后修改作者：
"""

import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QSplashScreen

app = QApplication(sys.argv)

if __name__ == "__main__":
    # 创建启动画面
    splash_pix = QPixmap("./apply/ICON/kms.jpg")  # 替换为你的启动画面图片路径
    splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
    splash.show()

    from apply import GUI_bioscope

    # 创建主窗口
    mainWindow = GUI_bioscope.MyMainWindow(splash)
    mainWindow.showMaximized()
    mainWindow.show()
    # 关闭启动画面
    splash.finish(mainWindow)

    # 执行主循环
    sys.exit(app.exec())
