import sys

from qtpy.QtWidgets import *

import UI.GUI_BIO as GUI_BIO

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    dialog = GUI_BIO.MyWindow()
    dialog.showMaximized()
    dialog.show()
    sys.exit(app.exec_())
