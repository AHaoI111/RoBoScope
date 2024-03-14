import sys

from PySide6.QtCore import QCoreApplication, Qt
from PySide6.QtGui import QMovie, QGuiApplication
from PySide6.QtWidgets import QApplication, QSplashScreen, QLabel


class MySplashScreen(QSplashScreen):
    def mousePressEvent(self, event):
        event.ignore()


app = QApplication(sys.argv)
app.setQuitOnLastWindowClosed(False)


def show_splash():
    splash = MySplashScreen()
    movie = QMovie("./src/UI/ICON/loading.gif")  # 替换为你的动画图片路径
    splash.resize(1186, 346)  # 替换为你想要的宽度和高度
    label = QLabel(splash)
    label.setMovie(movie)
    label.setAlignment(Qt.AlignCenter)

    screen = QGuiApplication.primaryScreen()
    screen_geometry = screen.geometry()
    x = (screen_geometry.width() - splash.width()) // 2
    y = (screen_geometry.height() - splash.height()) // 2
    splash.move(x, y)

    movie.start()
    splash.show()
    QCoreApplication.processEvents()

    return splash


if __name__ == "__main__":
    splash = show_splash()
    app.aboutToQuit.connect(splash.close)  # 在应用程序退出前关闭启动画面
    sys.exit(app.exec())
