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

from PySide6.QtCore import QObject
from PySide6.QtCore import Signal


def get_time_2():
    # 获取当前系统时间
    current_time = datetime.now()
    # 格式化时间显示
    year = current_time.strftime("%Y")
    month = current_time.strftime("%m")
    day = current_time.strftime("%d")
    return year, month, day


# 该文件用于做测试装载器与显微镜运动测试任务
class Key(object):
    none = b"\x00"
    pressed = b"\x01"
    released = b"\x02"


class Task(QObject):
    write_log_task = Signal(int, str)
    activate_pushbutton = Signal()
    updata_textEdit_log_task = Signal(str)
    set_pro = Signal(int)
    finish_task = Signal(str)

    test_single_step_pause = Signal()

    updata_Progress = Signal(float, float,float)  # 用于更新进度条的信号

    def __init__(self, action_loader, action_mircoscope):
        super().__init__()

        self.number_next = 0
        self.logger = None
        self.pic_label = None
        self.request = None

        self.action_loader = action_loader
        self.action_mircoscope = action_mircoscope
        self.action_mircoscope.flag = True
        self.action_mircoscope.flage_run = True

        self.test_single_step_pause_flag = True
        self.test_single_step_run_flag = True

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
            self.write_log_task.emit(0, "当前扫描配置" + str(Taskinfo))
            self.action_mircoscope.microscope_homezxy()
            self.action_loader.loader_reset()
            self.action_loader.open_slide_task_file()
            self.task_flag = True
            self.task_run_flag = True

            # 获取任务的ID
            task_id = str(uuid.uuid4())  # 生成一个 UUID
            Taskinfo['task_id'] = task_id
            Taskinfo['pre_request_flag'] = False
            Taskinfo['flag_create_view'] = False

            count_box = len(Taskinfo['boxes'])
            count_slide = 0
            # 遍历盒子
            for box in Taskinfo['boxes']:
                if self.task_run_flag:
                    pass
                else:
                    break
                # 该盒子需要扫描
                slide_tasks, slide__points = self.action_loader.get_box_points(box)
                self.write_log_task.emit(0, "玻片位置" + str(slide__points))
                number = list(range(1, len(slide__points) + 1))
                # 确保列表中存在0(0表示需要扫描玻片，1表示不需要扫描)
                if 0 in slide_tasks:
                    # 找最后一个0表示任务
                    last_zero_index = len(slide_tasks) - 1 - slide_tasks[::-1].index(0)
                else:
                    last_zero_index = -1
                for task, point_xz, num in zip(slide_tasks, slide__points, number):
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
                        self.action_loader.move_x_to(point_xz[0])
                        self.action_loader.move_z_to(point_xz[1])
                        self.write_log_task.emit(0, "移动到盒子取玻片处：" + str(point_xz[0]) + str(point_xz[1]))
                        # 取片(动作为y伸出、z上台、y回收)
                        self.action_loader.get_slide_from_box(point_xz[1])
                        self.write_log_task.emit(0, "取片：")
                        if self.action_loader.loader.is_warning:
                            self.updata_textEdit_log_task.emit("设备故障")
                            self.write_log_task.emit(1, "设备故障")
                            self.task_run_flag = False
                            break
                        # 发送本地玻片的uuid
                        slide_id = str(uuid.uuid4())
                        if slide_id is not None:
                            self.action_mircoscope.move_2_loader_get_wait(Taskinfo['Xend'], Taskinfo['Yend'])
                            self.write_log_task.emit(0, "显微镜开始移动至交接处")
                            # 移动至显微镜处
                            self.action_loader.move_2_microscope_give_location()
                            self.write_log_task.emit(0, "移动至显微镜处：")
                            # 显微镜移动至交接处(确认)
                            self.action_mircoscope.wait_busy()
                            # 显微镜移动至交接处
                            self.write_log_task.emit(0, "显微镜移动至交接处")
                            # 放片到载物台
                            self.action_loader.give_slide_to_microscope()
                            self.write_log_task.emit(0, "放片到载物台")
                            if self.action_loader.loader.is_warning:
                                self.updata_textEdit_log_task.emit("设备故障")
                                self.write_log_task.emit(1, "设备故障")
                                self.task_run_flag = False
                                break
                            # 避位
                            self.action_loader.loader_avoid()
                            self.write_log_task.emit(0, "避位")
                            # 扫描
                            self.write_log_task.emit(0, "扫描")
                            self.action_mircoscope.start(Taskinfo,slide_id)

                            # 显微镜移动至交接处
                            self.action_mircoscope.move_2_loader_give(Taskinfo['Xend'], Taskinfo['Yend'])
                            self.write_log_task.emit(0, "显微镜移动至交接处")
                            # 移动至显微镜处下方
                            self.action_loader.move_2_microscope_get_location()
                            self.write_log_task.emit(0, "移动至显微镜处下方")
                            # 取片
                            self.write_log_task.emit(0, "开始取片")
                            self.action_loader.get_slide_from_microscope()
                            self.write_log_task.emit(0, "完成取片")
                            if self.action_loader.loader.is_warning:
                                self.updata_textEdit_log_task.emit("设备故障")
                                self.write_log_task.emit(1, "设备故障")
                                self.task_run_flag = False
                                break
                            # 显微镜复位
                            self.write_log_task.emit(0, "开始显微镜复位")
                            self.action_mircoscope.microscope_homezxy_wait()
                            # 返回玻片仓位置放片
                            self.action_loader.move_x_to(point_xz[0])
                            self.action_loader.move_z_to(point_xz[1] - self.action_loader.boxzgap)
                            self.write_log_task.emit(0, "返回玻片仓位置放片")
                            # 放片
                            self.action_loader.give_slide_to_box(point_xz[1] - self.action_loader.boxzgap)
                            self.write_log_task.emit(0, "放片")
                            if self.action_loader.loader.is_warning:
                                self.updata_textEdit_log_task.emit("设备故障")
                                self.write_log_task.emit(1, "设备故障")
                                self.task_run_flag = False
                                break
                            self.action_mircoscope.wait_busy()
                            self.write_log_task.emit(0, "显微镜复位完成确认")
                            self.updata_textEdit_log_task.emit(
                                "完成当前玻片:第" + str(box) + "盒" + "第" + str(num) + "片")
                            # 更新任务
                            self.action_loader.update_slide_task(box, num, 1)
                            if num == (last_zero_index + 1):
                                # 处理最后一片
                                self.action_loader.last_slide_process(point_xz[1] - self.action_loader.boxzgap)
                        else:
                            # 移动回去放
                            # 返回玻片仓位置放片
                            self.updata_textEdit_log_task.emit("未识别出玻片ID，返回玻片仓位置放片")
                            self.action_loader.move_x_to(point_xz[0])
                            self.action_loader.move_z_to(point_xz[1] - self.action_loader.boxzgap)
                            self.write_log_task.emit(0, "返回玻片仓位置放片")
                            # 放片
                            self.action_loader.give_slide_to_box(point_xz[1] - self.action_loader.boxzgap)
                            self.write_log_task.emit(0, "放片")
                            if self.action_loader.loader.is_warning:
                                self.updata_textEdit_log_task.emit("设备故障")
                                self.write_log_task.emit(1, "设备故障")
                                self.task_run_flag = False
                                break
                            self.updata_textEdit_log_task.emit(
                                "完成当前玻片:第" + str(box) + "盒" + "第" + str(num) + "片")
                            # 更新任务
                            self.action_loader.update_slide_task(box, num, 1)
                            if num == (last_zero_index + 1):
                                # 处理最后一片
                                self.action_loader.last_slide_process(point_xz[1] - self.action_loader.boxzgap)

                        end_time = time.time()  # 记录结束时间
                        elapsed_time = end_time - start_time  # 计算耗时
                        self.updata_Progress.emit(float(float(count_slide) * 100 / (count_box * (last_zero_index + 1))),
                                                  elapsed_time, (count_box * (last_zero_index + 1)))
                    elif task == 1:
                        self.updata_textEdit_log_task.emit(
                            "第" + str(box) + "盒" + "第" + str(num) + "片" + "不需要扫描" + '\n')
                    count_slide = count_slide + 1

            if self.task_run_flag:
                self.action_loader.reset_slide_task()
                self.action_loader.loader_reset()
            else:
                pass
            self.activate_pushbutton.emit()
            self.updata_textEdit_log_task.emit("当前扫描完成" + '\n')

        except Exception as e:
            self.activate_pushbutton.emit()
            self.write_log_task.emit(0, "当前扫描失败" + str(e))
            self.updata_textEdit_log_task.emit("当前扫描失败" + '\n')

    def pause(self):
        self.task_flag = False
        self.action_mircoscope.pause()
        self.updata_textEdit_log_task.emit("正在暂停扫描..." + '\n')
