import sys
from PySide6.QtWidgets import QApplication
import UI.GUI_BIO as GUI_BIO

if __name__ == "__main__":
    app = QApplication.instance()  # 检查是否已经有实例存在
    if not app:  # 如果不存在就创建一个新实例
        app = QApplication(sys.argv)
        app.setStyle("Fusion")
    MyWindow = GUI_BIO.MyWindow()
    MyWindow.showMaximized()
    MyWindow.show()
    sys.exit(app.exec())
