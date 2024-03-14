import sys

from PySide6.QtCore import QProcess
from PySide6.QtWidgets import QApplication

app = QApplication(sys.argv)

if __name__ == "__main__":

    # 创建一个新的进程
    process = QProcess()
    # 设置进程程序和参数，指定要执行的可执行文件路径
    process.start('./src//GifSplashScreen.exe')
    # 等待进程结束

    from src.UI import GUI_bioscope
    mainWindow = GUI_bioscope.MyMainWindow()
    mainWindow.showMaximized()
    mainWindow.show()
    process.close()

    sys.exit(app.exec())
