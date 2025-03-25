# -*- encoding: utf-8 -*-
"""
@Description:
该文件用于做测试装载器与显微镜运动测试任务
@File    :   taskwork_test_loader.py
@Time    :   2024/07/16
@Author  :   Li QingHao
@Version :   3.0
@Time_END :  最后修改时间：20240905
@Developers_END :  最后修改作者：
"""

import time
import uuid
from datetime import datetime

from PySide6.QtCore import QObject, Slot
from PySide6.QtCore import Signal


def get_time_2():
    # 获取当前系统时间
    current_time = datetime.now()
    # 格式化时间显示
    year = current_time.strftime("%Y")
    month = current_time.strftime("%m")
    day = current_time.strftime("%d")
    return year, month, day


class Task(QObject):
    write_log_task = Signal(int, str)
    activate_pushbutton = Signal()
    updata_textEdit_log_task = Signal(str)
    set_pro = Signal(int)
    stop_task = Signal()


    updata_Progress = Signal(float, float, float)  # 用于更新进度条的信号

    def __init__(self, action_loader, action_mircoscope, Scanning):
        super().__init__()

        self.number_next = 0
        self.logger = None
        self.pic_label = None
        self.request = None
        self.slide_task = None

        self.action_loader = action_loader
        self.action_mircoscope = action_mircoscope
        self.Scanning = Scanning
        self.action_mircoscope.flag = True
        self.action_mircoscope.flage_run = True

        self.task_flag = True
        self.task_run_flag = True

    def run(self, Taskinfo):
        """
        执行自动送片加扫描的任务流程。
        此方法首先使设备复位，然后按照预设的点位信息进行片子的自动取出、送至显微镜、扫描、再放回装载器的过程。
        该过程中涉及显微镜与装载器的多次协作动作。
        """
        try:
            # 复位
            self.number_next = 0
            self.write_log_task.emit(0, "当前扫描配置" + str(Taskinfo))
            self.action_mircoscope.microscope_homezxy()
            # self.action_loader.loader_reset()
            self.action_loader.open_slide_task_file()
            self.task_flag = True
            self.task_run_flag = True
            elapsed_time = 0
            # 获取任务的ID
            if Taskinfo['task_id'] is None:
                task_id = str(uuid.uuid4())  # 生成一个 UUID
                Taskinfo['task_id'] = task_id
            else:
                task_id = Taskinfo['task_id']
            # self.action_loader.open_camera()
            if Taskinfo['pre_request_flag']:
                Taskinfo['boxes'] = [1]

            count_box = len(Taskinfo['boxes'])
            count_slide = 0
            # 遍历盒子
            for box in Taskinfo['boxes']:
                if self.task_run_flag:
                    pass
                else:
                    break
                # 该盒子需要扫描
                if Taskinfo['pre_request_flag']:
                    slide_tasks, slide__points = self.action_loader.pre_get_box_points(box)
                else:
                    slide_tasks, slide__points = self.action_loader.get_box_points(box)
                number = list(range(1, len(slide__points) + 1))
                # 确保列表中存在0(0表示需要扫描玻片，1表示不需要扫描)
                if 0 in slide_tasks:
                    self.write_log_task.emit(0, "玻片任务" + str(slide_tasks))
                    self.write_log_task.emit(0, "玻片位置" + str(slide__points))
                    # 找最后一个0表示任务
                    last_zero_index = len(slide_tasks) - 1 - slide_tasks[::-1].index(0)
                else:
                    last_zero_index = -1
                for task, point_xz, num in zip(slide_tasks, slide__points, number):
                    if self.number_next >= 2:
                        self.updata_textEdit_log_task.emit(
                            "连续两片空的,该盒子无需扫描" + '\n')
                        self.write_log_task.emit(0, "连续两片空的,该盒子无需扫描")
                        break
                    if task == 0:
                        if self.task_flag:
                            pass
                        else:
                            while not self.task_flag:
                                time.sleep(0.01)
                        if self.task_run_flag:
                            pass
                        else:
                            break
                        start_time = time.time()  # 记录开始时间
                        # 移动到盒子取玻片处
                        self.updata_textEdit_log_task.emit("移动到盒子取玻片处：" + str(point_xz[0]) + str(point_xz[1]))
                        self.write_log_task.emit(0, "移动到盒子取玻片处：" + str(point_xz[0]) + str(point_xz[1]))
                        self.action_loader.move_x_to(point_xz[0])
                        self.action_loader.move_z_to(point_xz[1])
                        # 取片(动作为y伸出、z上台、y回收)
                        self.updata_textEdit_log_task.emit("正在取片")
                        self.write_log_task.emit(0, "正在取片")
                        self.action_loader.get_slide_from_box(point_xz[1])
                        if self.action_loader.loader.is_warning:
                            self.updata_textEdit_log_task.emit("设备故障")
                            self.write_log_task.emit(1, "设备故障")
                            self.task_run_flag = False
                            break
                        # 移动至拍摄
                        self.updata_textEdit_log_task.emit("玻片移动至拍标签位置")
                        self.write_log_task.emit(0, "玻片移动至拍标签位置")
                        self.action_loader.loader_move2_camera()
                        # 相机拍摄玻片图片
                        label_img = self.action_loader.capture_image()
                        self.pic_label = label_img
                        # 发送请求玻片的uuid
                        if Taskinfo['pre_request_flag']:
                            slide_id = str(uuid.uuid4())
                            self.updata_textEdit_log_task.emit("生成预扫玻片id:" + slide_id)
                            self.write_log_task.emit(0, "生成预扫玻片id:" + slide_id)
                        else:
                            if self.request is None:
                                slide_id = str(uuid.uuid4())
                                self.updata_textEdit_log_task.emit("生成玻片id:" + slide_id)
                                self.write_log_task.emit(0, "生成玻片id:" + slide_id)
                                Taskinfo['flag_create_view'] = False
                            else:
                                year, month, day = get_time_2()
                                self.updata_textEdit_log_task.emit("发送请求申请slide ID")
                                self.write_log_task.emit(0, "发送请求申请slide ID")
                                slide_id = self.request.create_slide_id(Taskinfo['task_id'],
                                                                        '/' + year + '/' + month + '/' + day + '/' +
                                                                        Taskinfo['task_id'] + '/',
                                                                        label_img)
                                if slide_id is not None:
                                    self.updata_textEdit_log_task.emit("生成玻片id:" + slide_id)
                                    self.write_log_task.emit(0, "生成玻片id:" + slide_id)
                                else:
                                    self.updata_textEdit_log_task.emit("发送请求申请slide ID失败")
                                    self.write_log_task.emit(1, "发送请求申请slide ID失败")
                                Taskinfo['flag_create_view'] = True
                        if slide_id is not None:
                            self.updata_textEdit_log_task.emit("显微镜开始移动至交接处")
                            self.write_log_task.emit(0, "显微镜开始移动至交接处")
                            self.action_mircoscope.move_2_loader_get_wait(Taskinfo['Xend'], Taskinfo['Yend'])
                            self.number_next = 0
                            # 移动至显微镜处
                            self.updata_textEdit_log_task.emit("移动至显微镜处")
                            self.write_log_task.emit(0, "移动至显微镜处")
                            self.action_loader.move_2_microscope_give_location()
                            # 显微镜移动至交接处(确认)
                            self.action_mircoscope.wait_busy()
                            # 放片到载物台
                            self.updata_textEdit_log_task.emit("放片到载物台")
                            self.write_log_task.emit(0, "放片到载物台")
                            self.action_loader.give_slide_to_microscope()
                            if self.action_loader.loader.is_warning:
                                self.updata_textEdit_log_task.emit("设备故障")
                                self.write_log_task.emit(1, "设备故障")
                                self.task_run_flag = False
                                break
                            # 避位
                            self.updata_textEdit_log_task.emit("装载器避位")
                            self.write_log_task.emit(0, "装载器避位")
                            self.action_loader.loader_avoid()
                            self.action_loader.disenble_motor()
                            # 扫描
                            self.updata_textEdit_log_task.emit("显微镜正在扫描")
                            self.write_log_task.emit(0, "显微镜正在扫描")
                            self.Scanning.start(Taskinfo, slide_id, self.pic_label, use_pump=self.action_loader.pump)
                            # 显微镜移动至交接处
                            self.updata_textEdit_log_task.emit("显微镜移动至交接处")
                            self.write_log_task.emit(0, "显微镜移动至交接处")
                            self.action_mircoscope.move_2_loader_give(Taskinfo['Xend'], Taskinfo['Yend'])
                            # 移动至显微镜处下方
                            self.updata_textEdit_log_task.emit("移动至显微镜处下方")
                            self.write_log_task.emit(0, "移动至显微镜处下方")
                            self.action_loader.move_2_microscope_get_location()
                            # 取片
                            self.updata_textEdit_log_task.emit("开始取片")
                            self.write_log_task.emit(0, "开始取片")
                            self.action_loader.get_slide_from_microscope()
                            self.updata_textEdit_log_task.emit("完成取片")
                            self.write_log_task.emit(0, "完成取片")
                            if self.action_loader.loader.is_warning:
                                self.updata_textEdit_log_task.emit("设备故障")
                                self.write_log_task.emit(1, "设备故障")
                                self.task_run_flag = False
                                break
                            # 显微镜复位
                            self.updata_textEdit_log_task.emit("开始显微镜复位")
                            self.write_log_task.emit(0, "开始显微镜复位")
                            self.action_mircoscope.microscope_homezxy_wait()
                            # 返回玻片仓位置放片
                            self.updata_textEdit_log_task.emit("返回玻片仓位置放片")
                            self.write_log_task.emit(0, "返回玻片仓位置放片")
                            self.action_loader.move_x_to(point_xz[0])
                            self.action_loader.move_z_to(point_xz[1] - self.action_loader.boxzgap)
                            # 放片
                            self.updata_textEdit_log_task.emit("放片")
                            self.write_log_task.emit(0, "放片")
                            self.action_loader.give_slide_to_box(point_xz[1] - self.action_loader.boxzgap)
                            if self.action_loader.loader.is_warning:
                                self.updata_textEdit_log_task.emit("设备故障")
                                self.write_log_task.emit(1, "设备故障")
                                self.task_run_flag = False
                                break
                            self.action_mircoscope.wait_busy()
                            self.updata_textEdit_log_task.emit("显微镜复位完成确认")
                            self.write_log_task.emit(0, "显微镜复位完成确认")
                            self.updata_textEdit_log_task.emit(
                                "完成当前玻片:第" + str(box) + "盒" + "第" + str(num) + "片")
                            self.write_log_task.emit(0, "完成当前玻片:第" + str(box) + "盒" + "第" + str(num) + "片")
                            # 更新任务
                            self.action_loader.update_slide_task(box, num, 1)
                            if num == (last_zero_index + 1):
                                # 处理最后一片
                                if Taskinfo['pre_request_flag']:
                                    pass
                                else:
                                    self.action_loader.last_slide_process(point_xz[1] - self.action_loader.boxzgap)
                        else:
                            # 移动回去放
                            self.number_next = self.number_next + 1
                            # 返回玻片仓位置放片
                            self.updata_textEdit_log_task.emit("未识别出玻片ID，返回玻片仓位置放片")
                            self.write_log_task.emit(0, "未识别出玻片ID，返回玻片仓位置放片")
                            self.action_loader.move_x_to(point_xz[0])
                            self.action_loader.move_z_to(point_xz[1] - self.action_loader.boxzgap)
                            self.updata_textEdit_log_task.emit("返回玻片仓位置放片")
                            self.write_log_task.emit(0, "返回玻片仓位置放片")
                            # 放片
                            self.action_loader.give_slide_to_box(point_xz[1] - self.action_loader.boxzgap)
                            self.updata_textEdit_log_task.emit("放片")
                            self.write_log_task.emit(0, "放片")
                            if self.action_loader.loader.is_warning:
                                self.updata_textEdit_log_task.emit("设备故障")
                                self.write_log_task.emit(1, "设备故障")
                                self.task_run_flag = False
                                break
                            self.updata_textEdit_log_task.emit(
                                "完成当前玻片:第" + str(box) + "盒" + "第" + str(num) + "片")
                            self.write_log_task.emit(0, "完成当前玻片:第" + str(box) + "盒" + "第" + str(num) + "片")
                            # 更新任务
                            self.action_loader.update_slide_task(box, num, 1)
                            if num == (last_zero_index + 1):
                                # 处理最后一片
                                if Taskinfo['pre_request_flag']:
                                    pass
                                else:
                                    self.action_loader.last_slide_process(point_xz[1] - self.action_loader.boxzgap)
                        end_time = time.time()  # 记录结束时间
                        elapsed_time = end_time - start_time  # 计算耗时
                        self.updata_Progress.emit(float(float(count_slide) * 100 / (count_box * (last_zero_index + 1))),
                                                  elapsed_time, (count_box * (last_zero_index + 1)))
                    elif task == 1:
                        self.updata_textEdit_log_task.emit(
                            "第" + str(box) + "盒" + "第" + str(num) + "片" + "不需要扫描" + '\n')
                        self.write_log_task.emit(0,
                                                 "第" + str(box) + "盒" + "第" + str(num) + "片" + "不需要扫描" + '\n')
                    count_slide = count_slide + 1

            if self.task_run_flag:
                self.updata_textEdit_log_task.emit("当前扫描完成" + '\n')
                self.write_log_task.emit(0, "当前扫描完成")
                self.updata_Progress.emit(100, elapsed_time, (count_box * (last_zero_index + 1)))
                if self.request is not None:
                    status, data = self.request.finfish_task(task_id)
                self.action_loader.save_slide_task_file(self.slide_task)
                self.action_loader.slide_task = self.slide_task

                self.action_loader.loader_move_xyz_0()
            else:
                self.updata_Progress.emit(float(float(count_slide) * 100 / (count_box * (last_zero_index + 1))),
                                          -1, (count_box * (last_zero_index + 1)))
                self.updata_textEdit_log_task.emit("当前扫描停止" + '\n')
                self.write_log_task.emit(0, "当前扫描停止")
                self.stop_task.emit()
            self.activate_pushbutton.emit()

        except Exception as e:
            self.activate_pushbutton.emit()
            self.write_log_task.emit(0, "当前扫描失败:" + str(e))
            self.updata_textEdit_log_task.emit("当前扫描失败:" + str(e) + '\n')

    def pause(self):
        self.task_flag = False
        self.Scanning.pause()
        self.updata_textEdit_log_task.emit("正在暂停扫描..." + '\n')
        self.write_log_task.emit(0, "正在暂停扫描")

    # 发送预扫描标签
    @Slot(str, str, str)
    def send2_request_pre_pic_label(self, guid, api, scan_model_id):
        self.updata_textEdit_log_task.emit("发送预扫描标签")
        self.write_log_task.emit(0, "发送预扫描标签")
        status, data = self.request.request2server_send_pre_scan_label(self.pic_label, guid, api, scan_model_id)
