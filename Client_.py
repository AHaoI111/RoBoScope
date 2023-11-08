import socket


class Client:
    def __init__(self, host='127.0.0.1', port=8888):
        self.host = host
        self.port = port

    def send_data(self, data):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as self.s:
            self.s.connect((self.host, self.port))
            self.s.sendall(data.encode('utf-8'))
            # response = self.s.recv(1024)

        # print(f"接收到响应：{response.decode('utf-8')}")
