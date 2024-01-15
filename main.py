import sys


from PySide6.QtCore import QCoreApplication, Qt
from PySide6.QtGui import QMovie, QGuiApplication
from PySide6.QtWidgets import QApplication, QSplashScreen, QLabel

from src.UI import GUI_bioscope

app = None
app = QApplication(sys.argv)


def show_splash():
    # 创建一个 QSplashScreen 对象
    splash = QSplashScreen()

    # 创建一个 QLabel 用于显示动画
    movie = QMovie("./src/ICON/Bioscope.png")  # 替换为你的动画图片路径
    splash.resize(1186, 346)  # 替换为你想要的宽度和高度

    label = QLabel(splash)
    label.setMovie(movie)
    label.setAlignment(Qt.AlignCenter)

    # 设置启动界面的位置为屏幕正中间
    screen = QGuiApplication.primaryScreen()
    screen_geometry = screen.geometry()
    x = (screen_geometry.width() - splash.width()) // 2
    y = (screen_geometry.height() - splash.height()) // 2
    splash.move(x, y)

    # 显示动画提示
    movie.start()
    splash.show()
    # 强制刷新界面以确保动画提示显示出来
    QCoreApplication.processEvents()
    return splash


if __name__ == "__main__":
    splash = show_splash()
    mainWindow = GUI_bioscope.MyMainWindow()
    mainWindow.showMaximized()
    mainWindow.show()
    splash.finish(mainWindow)
    sys.exit(app.exec())
