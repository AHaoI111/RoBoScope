import base64
import threading

import cv2
import requests
import PySide6.QtCore
from PySide6.QtCore import Signal, QObject, Slot
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from uvicorn import Server, Config


def remove_specific_keys(json_obj, target_keys):
    """
    从 JSON 对象中删除特定的多个键（包括嵌套的键）。

    参数:
    json_obj (dict): JSON 对象。
    target_keys (list of str): 要删除的键名列表，必须是字符串列表。

    返回:
    dict: 更新后的 JSON 对象。
    """

    def remove_keys_from_dict(d, keys_to_remove):
        """
        从字典中递归删除指定的多个键。

        参数:
        d (dict): 字典对象。
        keys_to_remove (set of str): 要删除的键名集合，必须是字符串集合。

        返回:
        dict: 更新后的字典。
        """
        updated_dict = {}
        for k, v in d.items():
            if k in keys_to_remove:
                continue
            if isinstance(v, dict):
                updated_dict[k] = remove_keys_from_dict(v, keys_to_remove)
            elif isinstance(v, list):
                updated_dict[k] = [remove_keys_from_dict(item, keys_to_remove) if isinstance(item, dict) else item for
                                   item in v]
            else:
                updated_dict[k] = v
        return updated_dict

    # 确保 target_keys 是一个集合，以便更快的查找
    if not isinstance(target_keys, list):
        raise ValueError("target_keys 必须是一个字符串列表")

    target_keys_set = set(target_keys)

    if isinstance(json_obj, dict):
        return remove_keys_from_dict(json_obj, target_keys_set)
    elif isinstance(json_obj, list):
        return [remove_specific_keys(item, target_keys) if isinstance(item, dict) else item for item in json_obj]
    else:
        return json_obj


def cv2_img_to_base64(img):
    """
    将 OpenCV 图像（BGR 格式）转换为 Base64 编码的字符串。

    :param img: OpenCV 读取的图像（BGR 格式）
    :return: 图像的 Base64 编码字符串
    """
    # 将图像编码为 PNG 格式
    _, buffer = cv2.imencode('.png', img)

    # 将编码后的字节流转换为 Base64 编码
    img_base64 = base64.b64encode(buffer).decode('utf-8')

    return img_base64


class PreScanPicRequest(BaseModel):
    guid: str
    width: int
    hight: int
    return_api: str


class PreScanLabelRequest(BaseModel):
    guid: str
    return_api: str
    scan_model_id: str


class Com2scope(QObject):
    # Define a signal
    send_scan_pic = Signal(str, str, int, int)
    send_scan_label = Signal(str, str, str)
    test_send_scan_pic = Signal(str, str, int, int)
    test_send_scan_label = Signal(str, str, str)

    def __init__(self):
        super().__init__()
        self.device_info = None
        self.led_camera = []
        self.test_send_scan_pic.connect(self.test_request2server_send_pre_scan_pic)
        self.test_send_scan_label.connect(self.test_request2server_send_pre_pic_label)

    @Slot(str, str, int, int)
    def test_request2server_send_pre_scan_pic(self, task_guid, api, w, h):
        img = cv2.imread('pic.png')
        print(w)
        print(h)
        base_64_img = cv2_img_to_base64(img)
        data = {
            "guid": task_guid,
            "image": base_64_img
        }
        # 发送 POST 请求
        response = requests.post('http://192.168.0.47:8000' + api, json=data)
        # 打印响应状态码和内容
        return response.status_code, response.json()

    @Slot(str, str, str)
    def test_request2server_send_pre_pic_label(self, task_guid, api, scan_model_id):
        img = cv2.imread('label.png')
        base_64_img = cv2_img_to_base64(img)
        data = {
            "guid": task_guid,
            "image": base_64_img,
            "scan_model_id": scan_model_id
        }
        # 发送 POST 请求
        response = requests.post('http://192.168.0.47:8000' + api, json=data)
        # 打印响应状态码和内容
        return response.status_code, response.json()


def test_pic_request(img, task_guid, api):
    base_64_img = cv2_img_to_base64(img)
    data = {
        "guid": task_guid,
        "image": base_64_img
    }
    print('http://192.168.0.47:8000' + api)
    # 发送 POST 请求
    response = requests.post('http://192.168.0.47:8000' + api, json=data)

    # 打印响应状态码和内容
    print("Status Code:", response.status_code)
    print("Response JSON:", response.json())


class HTTPServer(threading.Thread, QObject):

    def __init__(self, ipadd, port):
        super().__init__()
        self.Com2scope = Com2scope()
        self.app = FastAPI()
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"]
        )
        self.config = Config(app=self.app, host=ipadd, port=port)
        self.server = Server(self.config)
        self._stop_event = threading.Event()

        # 注册 FastAPI 事件处理程序
        self.app.add_event_handler("startup", self.startup_event)
        self.app.add_event_handler("shutdown", self.shutdown_event)

        @self.app.get("/")
        async def root():
            return {
                "获取设备信息": "http://" + ipadd + ":" + str(port) + "/roboscope_info",
                "预扫描拼图": "http://" + ipadd + ":" + str(port) + "/pre_scan_pic",
                "预扫描标签图": "http://" + ipadd + ":" + str(port) + "/pre_scan_label"}

        @self.app.get("/roboscope_info")
        async def get_device_info():
            try:
                info = {}
                if self.Com2scope.device_info['Microscope']['sys']['当前系统'] == 'single':
                    key_to_remove = ['low', 'high']
                    updated_json = remove_specific_keys(self.Com2scope.device_info, key_to_remove)
                    info = {'sn': "roboscope006",
                            "sys": self.Com2scope.device_info['Microscope']['sys']['当前系统'],
                            "MultipleSingle": self.Com2scope.device_info['Microscope']['single']['单镜头倍数'],
                            "MultipleLow": "None",
                            "MultipleHigh": "None",
                            "focus_mode": [
                                {
                                    "id": 1,
                                    "name": "中心对焦",
                                    "Gap_flag": "false"
                                },
                                {
                                    "id": 2,
                                    "name": "4点对焦",
                                    "Gap_flag": "false"

                                },
                                {
                                    "id": 3,
                                    "name": "间隔对焦",
                                    "Gap_flag": "true"
                                }
                            ],
                            "ALL_info": updated_json}
                elif self.Com2scope.device_info['Microscope']['sys']['当前系统'] == 'double':
                    key_to_remove = ['single']
                    updated_json = remove_specific_keys(self.Com2scope.device_info, key_to_remove)
                    info = {'sn': "roboscope006",
                            "sys": self.Com2scope.device_info['Microscope']['sys']['当前系统'],
                            "MultipleSingle": "None",
                            "MultipleLow": self.Com2scope.device_info['Microscope']['low']['低倍倍数'],
                            "MultipleHigh": self.Com2scope.device_info['Microscope']['high']['高倍倍数'],
                            "focus_mode": [
                                {
                                    "id": 1,
                                    "name": "中心对焦",
                                    "Gap_flag": "false"

                                },
                                {
                                    "id": 2,
                                    "name": "4点对焦",
                                    "Gap_flag": "false"
                                },
                                {
                                    "id": 3,
                                    "name": "间隔对焦",
                                    "Gap_flag": "true"

                                }
                            ],
                            "ALL_info": updated_json}
                return info
            except Exception as e:
                return {
                    "result": "error",
                    "msg": str(e)
                }

        @self.app.post("/pre_scan_pic")
        async def pre_scan_pic(info: PreScanPicRequest):
            try:
                self.Com2scope.send_scan_pic.emit(info.guid, info.return_api, info.width, info.hight)
                return {
                    "result": "success",
                    "msg": "调用成功"}
            except Exception as e:
                return {
                    "result": "error",
                    "msg": str(e)
                }

        @self.app.post("/test_pre_scan_pic")
        async def test_pre_scan_pic(info: PreScanPicRequest):
            try:
                self.Com2scope.test_send_scan_pic.emit(info.guid, info.return_api, info.width, info.hight)
                return {
                    "result": "success",
                    "msg": "调用成功"}
            except Exception as e:
                return {
                    "result": "error",
                    "msg": str(e)
                }

        @self.app.post("/pre_scan_label")
        async def pre_scan_label(info: PreScanLabelRequest):
            try:
                self.Com2scope.send_scan_label.emit(info.guid, info.return_api, info.scan_model_id)
                return {
                    "result": "success",
                    "msg": "调用成功"
                }
            except Exception as e:
                return {
                    "result": "error",
                    "msg": str(e)
                }

        @self.app.post("/test_pre_scan_label")
        async def test_pre_scan_label(info: PreScanLabelRequest):
            try:
                self.Com2scope.test_send_scan_label.emit(info.guid, info.return_api, info.scan_model_id)
                print(info.scan_model_id)
                return {
                    "result": "success",
                    "msg": "调用成功"
                }
            except Exception as e:
                return {
                    "result": "error",
                    "msg": str(e)
                }

        @self.app.get("/run")
        async def run():
            return {"message": "开始扫描"}

    def run(self):
        # 启动 FastAPI 应用
        self.server.run()

    def stop(self):
        # 停止 FastAPI 应用
        self.server.should_exit = True  # 设置退出标志
        self._stop_event.set()

    def startup_event(self):
        print("FastAPI application starting up")

    def shutdown_event(self):
        print("FastAPI application shutting down")
