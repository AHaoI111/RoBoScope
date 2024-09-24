import base64

import cv2
import numpy as np
import requests

import utils.read_config as read_config


def cv2_img_to_base64(img):
    """
    将 OpenCV 图像（BGR 格式）转换为 Base64 编码的字符串。

    :param img: OpenCV 读取的图像（BGR 格式）
    :return: 图像的 Base64 编码字符串
    """
    if not isinstance(img, np.ndarray):
        raise ValueError("Input must be an OpenCV image (numpy ndarray)")

    try:
        # 将图像编码为 PNG 格式
        _, buffer = cv2.imencode('.png', img)

        # 将编码后的字节流转换为 Base64 编码
        img_base64 = base64.b64encode(buffer).decode('utf-8')
    except Exception as e:
        print(f"Error occurred: {e}")
        return None

    return img_base64


class Request:
    def __init__(self, serverip, serverport, localip, localport):
        self.url_server = 'http://' + str(serverip) + ':' + str(serverport)
        self.url_local = 'http://' + str(localip) + ':' + str(localport)

    def request2local_get_info(self, api):
        response = requests.get(self.url_local + api)
        return response.status_code, response.json()

    # 发送预扫描拼图

    def request2server_send_pre_scan_pic(self, pre_img, task_guid, api):
        base_64_img = cv2_img_to_base64(pre_img)
        data = {
            "guid": task_guid,
            "image": base_64_img

        }
        # 发送 POST 请求
        response = requests.post(self.url_server + api, json=data)
        # 打印响应状态码和内容
        return response.status_code, response.json()

    # 发送预扫描标签

    def request2server_send_pre_scan_label(self, img_label, task_guid, api,scan_model_id):
        base_64_img = cv2_img_to_base64(img_label)
        data = {
            "guid": task_guid,
            "image": base_64_img,
            "scan_model_id": scan_model_id
        }
        # 发送 POST 请求
        response = requests.post(self.url_server + api, json=data)
        return response.status_code, response.json()

    # 发送扫描拼图

    def request2server_send_scan_pic_low(self, img, api):
        base_64_img = cv2_img_to_base64(img)
        data = {
            "images": base_64_img
        }
        # 发送 POST 请求
        response = requests.post(api, json=data)
        # 打印响应状态码和内容
        return response.status_code, response.json()

    # 获取任务方案

    def get_plan_from_server(self, sn):
        params = {
            "device_sn": sn  # 将这个值替换为你想要的设备序列号
        }
        response = requests.get(self.url_server + "/api/v1_0/task/types", params=params)
        return response.status_code, response.json()

    # 创建任务
    def create_task(self, task_type_id, path):
        data = {
            "task_type_id": task_type_id,
            "devcie_path": path  # 将这个值替换为你想要的设备序列号
        }
        print(data)
        response = requests.post(self.url_server + "/api/v1_0/task", params=data)
        if response.status_code == 200:
            return str(response.json()['task_id'])
        else:
            return None

    # 创建玻片id
    def create_slide_id(self, task_id, sub_path, location_type, cv_img, row, col):
        base_64_img = cv2_img_to_base64(cv_img)
        data = {
            "task_id": task_id,
            "sub_path": sub_path,
            "location_type": location_type,
            "label_pic_base64": base_64_img,
            "row": row,
            "col": col
        }
        response = requests.post(self.url_server + "/api/v1_0/slide", json=data)
        if response.status_code == 200:
            print(response.json())
            return str(response.json()['data']['slide_id'])
        else:
            return None

    # 完成玻片扫描
    def finish_silde(self, slide_id, slide_pic):
        data = {
            "slide_id": slide_id,
            "slide_pic": slide_pic
        }
        response = requests.put(self.url_server + "/api/v1_0/slide/finish", params=data)
        return response.status_code, response.json()

    # 完成视野扫描
    def create_view(self, slide_id, file_paht, file_name, points):
        data = {
            "slide_id": slide_id,
            "file_path": file_paht,
            "file_name": file_name,
            "location": points
        }
        response = requests.post(self.url_server + "/api/v1_0/view_filed", json=data)
        return response.status_code, response.json()

    def finfish_task(self, task_id):
        data = {
            "task_id": task_id,
        }
        response = requests.post(self.url_server + "/api/v1_0/task/finish", params=data)
        return response.status_code, response.json()
