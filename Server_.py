import os
import socket
import threading
import time
from datetime import datetime

import psutil

import infor
import sys
from PySide6.QtWidgets import QApplication, QDialog
from UI.result import Ui_Dialog


def get_time():
    # 获取当前系统时间
    current_time = datetime.now()
    # 格式化时间显示
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_time


class ResultDialog(QDialog):
    def __init__(self, host='127.0.0.1', port=8888):
        super().__init__()

        # 初始化UI
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.host = host
        self.port = port
        try:
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_socket.bind((host, port))
            self.server_socket.listen(1)
        except OSError as e:
            if e.errno == 10048:  # 端口已被占用
                for conn in psutil.net_connections():
                    if conn.laddr.port == port:  # 找到占用该端口的进程
                        process = psutil.Process(conn.pid)
                        print(f"发现进程 {process.name()} (PID: {process.pid}) 占用端口 {port}")
                        process.terminate()  # 终止占用端口的进程
                        print("成功终止进程")
                        time.sleep(0.5)
                        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        self.server_socket.bind((host, port))
                        self.server_socket.listen(1)
                        print('重新连接成功')

                        break

        self.model = infor.model()
        self.IDlist = []
        self.thread1 = threading.Thread(target=self.start)
        self.thread1.start()

    def start(self):
        self.ui.result.append(f"等待客户端连接：{self.host}:{self.port}")
        self.thread1 = threading.Thread(target=self.process_data)
        self.thread1.start()
        while True:
            client_socket, client_address = self.server_socket.accept()
            print(f"已连接：{client_address[0]}:{client_address[1]}")

            # 接收数据并响应
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                # 处理接收到的数据
                self.IDlist.append(data.decode('utf-8'))

                # 发送响应数据
                # client_socket.sendall(bytes(self.acc))
            # client_socket.close()

    def process_data(self):
        while True:
            if len(self.IDlist) > 0:
                time.sleep(0.3)
                # 处理接收到的数据
                time_ = get_time()
                self.ui.result.append(time_ + '     ' + f"接收到玻片ID：{self.IDlist[0]}" + '      ' + '正在AI处理')
                list_window = self.model.infor2(self.IDlist[0])
                time_ = get_time()
                if not list_window:
                    self.ui.result.append(time_ + '     ' + self.IDlist[0] + '      ' + '不合格')
                else:
                    self.ui.result.append(time_ + '     ' + self.IDlist[0] + '      ' + '合格')
                self.IDlist.remove(self.IDlist[0])


if __name__ == '__main__':
    app = QApplication.instance()  # 检查是否已经有实例存在
    if not app:  # 如果不存在就创建一个新实例
        app = QApplication(sys.argv)
        app.setStyle("Fusion")
    dialog = ResultDialog()
    dialog.show()
    sys.exit(app.exec())

