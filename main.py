import pyqt5_test
import sys

if __name__ == "__main__":
    app = pyqt5_test.QApplication(sys.argv)
    app.setStyle('Fusion')
    dialog = pyqt5_test.MyDialog()
    dialog.showMaximized()
    sys.exit(app.exec_())



