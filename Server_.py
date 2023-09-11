import socket
import threading
import time
import psutil

import infor


class Server:
    def __init__(self, host='127.0.0.1', port=8888):
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

    def start(self):
        print(f"等待客户端连接：{self.host}:{self.port}")
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
                # client_socket.sendall(response)
            client_socket.close()

    def process_data(self):
        while True:
            if len(self.IDlist) > 0:
                time.sleep(0.1)
                # 处理接收到的数据
                print(f"接收到玻片ID：{self.IDlist[0]}")
                self.model.infor2(self.IDlist[0])
                self.IDlist.remove(self.IDlist[0])


if __name__ == "__main__":
    server = Server(host='127.0.0.1', port=8888)
    server.start()
