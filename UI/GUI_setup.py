from qtpy.QtWidgets import *
from UI.set_upUI import Ui_Dialog
import sys
import configparser


class MyDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        # 将 ui 设置为当前窗口的界面
        self.ui.setupUi(self)
        # 创建 QMessageBox 对象
        self.message_box = QMessageBox()

        # 设置对话框标题
        self.message_box.setWindowTitle("提示")
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')
        self.center_x = self.config.get('Setup', '玻片扫描中心x')
        self.center_y = (self.config.get('Setup', '玻片扫描中心y'))
        self.scan_w = (self.config.get('Setup', '玻片扫描区域宽度'))
        self.scan_h = (self.config.get('Setup', '玻片扫描区域高度'))
        self.calibration = (self.config.get('Setup', '像素标定'))
        self.comboBox = (self.config.get('Setup', '对焦方式'))
        self.posz = (self.config.get('Setup', '对焦经验值'))
        self.multiple = (self.config.get('Setup', '对焦倍数'))

        self.ui.center_x.setText(self.center_x)
        self.ui.center_y.setText(self.center_y)
        self.ui.scan_w.setText(self.scan_w)
        self.ui.scan_h.setText(self.scan_h)
        self.ui.calibration.setText(self.calibration)
        self.ui.comboBox.setItemText(0, self.comboBox)
        self.ui.posz.setText(self.posz)
        self.ui.comboBox_multiple.setItemText(0, self.multiple)

        # 保存设置
        self.ui.pushButton_save.clicked.connect(self.save)

    def save(self):
        try:
            self.config.set('Setup', '玻片扫描中心X', self.ui.center_x.text())

            self.config.set('Setup', '玻片扫描中心Y', self.ui.center_y.text())

            self.config.set('Setup', '玻片扫描区域宽度', self.ui.scan_w.text())

            self.config.set('Setup', '玻片扫描区域高度', self.ui.scan_h.text())

            self.config.set('Setup', '像素标定', self.ui.calibration.text())
            self.config.set('Setup', '对焦经验值', self.ui.posz.text())
            self.config.set('Setup', '对焦方式', self.ui.comboBox.currentText())
            self.config.set('Setup', '对焦倍数', self.ui.comboBox_multiple.currentText())
            with open('config.ini', 'w') as configfile:
                self.config.write(configfile)
            self.message_box.setText("保存成功！")
            # 显示弹窗，并等待用户响应
            response = self.message_box.exec()

        except:
            self.message_box.setText("保存失败！")
            # 显示弹窗，并等待用户响应
            response = self.message_box.exec()









if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = MyDialog()
    dialog.show()
    sys.exit(app.exec_())
