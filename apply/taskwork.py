import configparser
import io
import pdb
import sys
import time
import tkinter as tk

from PySide6.QtCore import QObject
from PySide6.QtCore import Signal


class Key(object):
    none = b"\x00"
    pressed = b"\x01"
    released = b"\x02"


class Task(QObject):
    write_log_task = Signal(int, str)
    activate_pushbutton = Signal()
    updata_textEdit_log_task = Signal(str)
    set_pro = Signal(int)

    def __init__(self, action_loader, action_mircoscope, config_info):
        super().__init__()

        self.box = []
        self.root = None
        self.number_next = 0
        self.logger = None
        try:
            self.last_slide_continue = []

            self.Key = Key()
            # 加载配置
            self.config = config_info
            self.slidenumber = int(self.config['Task']['slidenumber'])

        except Exception as e:
            self.updata_textEdit_log_task.emit("config文件不存在" + str(e))
            self.write_log_task.emit(1, "config文件不存在" + str(e))
        self.action_loader = action_loader
        self.action_mircoscope = action_mircoscope
        self.Flage = True

    def show_message_box(self):
        if self.root is not None:
            try:
                self.root.destroy()
            except Exception as e:
                print(f"Error destroying root: {e}")
        self.root = tk.Tk()
        self.root.withdraw()  # 隐藏主窗口

        # 创建自定义消息框
        custom_box = tk.Toplevel(self.root)
        custom_box.title("消息")

        label = tk.Label(custom_box, text="进入暂停！是否继续执行？")
        label.pack(pady=10)

        button1 = tk.Button(custom_box, text="是",
                            command=lambda: [self.goon_(), custom_box.destroy()])
        button1.pack(side=tk.LEFT, padx=10, pady=10)

        button2 = tk.Button(custom_box, text="否",
                            command=lambda: [self.quit_(), custom_box.destroy()])
        button2.pack(side=tk.LEFT, padx=10, pady=10)

        self.root.mainloop()

    def show_message_box_2(self, warning_info):
        if self.root is not None:
            try:
                self.root.destroy()
            except Exception as e:
                print(f"Error destroying root: {e}")
        self.root = tk.Tk()
        self.root.withdraw()  # 隐藏主窗口

        # 创建自定义消息框
        custom_box = tk.Toplevel(self.root)
        custom_box.title("警告！！！")

        label = tk.Label(custom_box, text=warning_info)
        label.pack(pady=10)

        button1 = tk.Button(custom_box, text="伸出",
                            command=lambda: [self.action_loader.move_y_to(self.action_loader.y_push_start)])
        button1.pack(side=tk.LEFT, padx=10, pady=10)

        button2 = tk.Button(custom_box, text="收回",
                            command=lambda: [self.action_loader.move_y_to(self.action_loader.y_return)])
        button2.pack(side=tk.LEFT, padx=10, pady=10)

        button3 = tk.Button(custom_box, text="继续扫描",
                            command=lambda: [self.goon_(), custom_box.destroy()])
        button3.pack(side=tk.LEFT, padx=10, pady=10)

        button4 = tk.Button(custom_box, text="退出扫描",
                            command=lambda: [self.quit_(), custom_box.destroy()])
        button4.pack(side=tk.LEFT, padx=10, pady=10)

        self.root.mainloop()

    def goon_(self):
        self.Flage = True
        # 用户点击了"是"按钮
        self.continue_execution()
        self.root.quit()
        # self.root.destroy()
        print("goon_ok")

    def quit_(self):
        self.Flage = False
        # 用户点击了"是"按钮
        self.continue_execution()
        self.root.quit()
        # self.root.destroy()
        print("quit_ok")

    def continue_execution(self):
        # 模拟控制台输入 `c` 和回车
        user_input = 'c\n'  # 注意，这里的 `\n` 表示回车
        sys.stdin = io.StringIO(user_input)

    # 判断断点
    def judge_pdb(self, warning_info):
        # 主动停止
        if self.Flage is not True:
            if warning_info == "当前已经停止":
                self.show_message_box()
            else:
                self.show_message_box_2(warning_info)
            pdb.set_trace()
            if self.Flage:
                self.Flage = True
            else:
                self.Flage = False

    def run(self, box):
        """
        执行自动送片加扫描的任务流程。
        此方法首先使设备复位，然后按照预设的点位信息进行片子的自动取出、送至显微镜、扫描、再放回装载器的过程。
        该过程中涉及显微镜与装载器的多次协作动作。
        """
        if self.config['Device']['microscope'] == 'True':
            self.box = box
            try:
                # 设备复位，包括显微镜和装载器的复位动作
                # 加载配置
                # 记录是否恶意退出
                config = configparser.ConfigParser()
                config.read('config.ini')
                config.set('Device', 'microscope', str(False))
                with open('config.ini', 'w') as configfile:
                    config.write(configfile)

                self.action_mircoscope.microscope_homezxy()
                self.action_loader.loader_reset()
                # 打开识别玻片的相机
                self.action_loader.open_camera()
                self.updata_textEdit_log_task.emit("本次扫描包括" + str(self.box) + "仓位" + '\n')
                self.write_log_task.emit(0, "本次扫描包括" + str(self.box) + "仓位")
                # 设置灯颜色
                for box in self.box:
                    self.action_loader.set_led(box - 1, self.action_loader.color.green)
                for box in self.box:
                    self.action_loader.set_led(box - 1, self.action_loader.color.red)
                    self.number_next = 0
                    self.updata_textEdit_log_task.emit("开始扫描" + str(box) + "号仓位" + '\n')
                    self.write_log_task.emit(0, "开始扫描" + str(box) + "号仓位")
                    if self.Flage:
                        # 获取片子的取片点位信息第几个盒子多少片
                        slide_points_xz = self.action_loader.get_box_points(box, self.slidenumber)
                        # 移动至第一个取片点
                        self.judge_pdb("当前已经停止")
                        if self.Flage:
                            pass
                        else:
                            self.action_loader.release_camera()
                            self.updata_textEdit_log_task.emit("提前退出")
                            self.write_log_task.emit(0, "提前退出")
                            break
                        self.action_loader.move_x_to(slide_points_xz[0][0])
                        self.write_log_task.emit(0, "X移动到位置： " + str(slide_points_xz[0][0]))
                        # 遍历所有点位进行取片、送片、扫描操作
                        for i in range(len(slide_points_xz)):
                            self.updata_textEdit_log_task.emit(
                                "开始扫描玻片：仓位号：" + str(box) + "第" + str(i + 1) + "片" + '!!!' + '\n')
                            self.write_log_task.emit(0,
                                                     "开始扫描玻片：仓位号：" + str(box) + "第" + str(
                                                         i + 1) + "片" + '!!!')
                            self.set_pro.emit(int(i+1))
                            self.judge_pdb("当前已经停止")

                            if self.Flage:
                                pass
                            else:
                                self.action_loader.release_camera()
                                self.updata_textEdit_log_task.emit("提前退出")
                                self.write_log_task.emit(0, "提前退出")
                                break
                            # 根据点位信息进行z轴移动到取片位置
                            self.action_loader.move_z_to(slide_points_xz[i][1])
                            self.write_log_task.emit(0, "Z移动到位置： " + str(slide_points_xz[i][1]))

                            self.judge_pdb("当前已经停止")
                            if self.Flage:
                                pass
                            else:
                                self.action_loader.release_camera()
                                self.updata_textEdit_log_task.emit("提前退出")
                                self.write_log_task.emit(0, "提前退出")
                                break
                            # 在装载器处取片
                            loader_flage = self.action_loader.get_slide_from_box()
                            if loader_flage == 1:
                                self.write_log_task.emit(0, "从玻片仓取片成功")
                                pass
                            else:
                                self.updata_textEdit_log_task.emit(
                                    "从玻片仓取片时卡住玻片：仓位号：" + str(box) + "第" + str(i + 1) + "片" + '\n')
                                self.write_log_task.emit(1, "从玻片仓取片失败")
                                self.Flage = False
                                self.judge_pdb("取片失败警告！！！")
                                if self.Flage:
                                    pass
                                else:
                                    self.action_loader.release_camera()
                                    break
                            # 识别玻片ID######################################################
                            self.action_loader.loader_move2_camera()
                            # 拍照识别玻片
                            img = self.action_loader.capture_image()
                            # 裁剪区域
                            crop_img = self.action_loader.crop_image(img)
                            # 识别
                            result = self.action_loader.get_ocr_result(crop_img)
                            # 匹配ID
                            ID, IDall = self.action_loader.match_ID(result[0], 10)
                            # ID = ["20240611"]
                            # IDall = ["20240611"]
                            self.judge_pdb("当前已经停止")
                            if self.Flage:
                                pass
                            else:
                                self.action_loader.release_camera()
                                self.updata_textEdit_log_task.emit("提前退出")
                                self.write_log_task.emit(0, "提前退出")
                                break
                            # 判断有无玻片如果有则进行扫描
                            if len(IDall) > 0:
                                self.number_next = 0
                                if len(ID) > 0:
                                    self.updata_textEdit_log_task.emit(
                                        "扫描" + str(box) + "第" + str(i + 1) + "片" + "玻片ID：" + str(
                                            ID[0]) + '\n')
                                    self.write_log_task.emit(0, "扫描" + str(box) + "第" + str(i + 1) + "玻片ID：" + str(
                                        ID[0]))
                                else:
                                    self.updata_textEdit_log_task.emit(
                                        "扫描" + str(box) + "第" + str(i + 1) + "片" + "玻片ID：" + str(
                                            '未识别到') + '\n')
                                    self.write_log_task.emit(1, "扫描" + str(box) + "第" + str(i + 1) + "玻片ID：" + str(
                                        '未识别到'))

                                # 将片子移动至显微镜处
                                self.judge_pdb("当前已经停止")
                                if self.Flage:
                                    pass
                                else:
                                    self.action_loader.release_camera()
                                    self.updata_textEdit_log_task.emit("提前退出")
                                    self.write_log_task.emit(0, "提前退出")
                                    break
                                self.action_loader.move_2_microscope_give()
                                self.write_log_task.emit(0, "装载器移动至显微镜处")
                                time.sleep(1)
                                # 显微镜移动至接片位置
                                self.judge_pdb("当前已经停止")
                                if self.Flage:
                                    pass
                                else:
                                    self.action_loader.release_camera()
                                    self.updata_textEdit_log_task.emit("提前退出")
                                    self.write_log_task.emit(0, "提前退出")
                                    break
                                self.action_mircoscope.move_2_loader_get()
                                self.write_log_task.emit(0, "显微镜移动至交接处")
                                time.sleep(1)
                                # 将片子送给显微镜载物台
                                self.judge_pdb("当前已经停止")
                                if self.Flage:
                                    pass
                                else:
                                    self.action_loader.release_camera()
                                    self.updata_textEdit_log_task.emit("提前退出")
                                    self.write_log_task.emit(0, "提前退出")
                                    break
                                loader_flage = self.action_loader.give_slide_to_microscope()
                                self.write_log_task.emit(0, "开始送片")
                                time.sleep(1)
                                if loader_flage == 1:
                                    self.write_log_task.emit(0, "送片成功")
                                else:
                                    self.updata_textEdit_log_task.emit(
                                        "给显微镜送片时卡住玻片：仓位号" + str(box) + "第" + str(i + 1) + "片" + '\n')
                                    self.write_log_task.emit(1, "给显微镜送片时卡住玻片：仓位号" + str(box) + "第" + str(
                                        i + 1) + "片")
                                    self.Flage = False
                                    self.judge_pdb("送片失败警告！！！")

                                    if self.Flage:
                                        pass
                                    else:
                                        self.action_loader.release_camera()
                                        self.updata_textEdit_log_task.emit("提前退出")
                                        self.write_log_task.emit(0, "提前退出")
                                        break
                                # 装载器后退
                                self.judge_pdb("当前已经停止")
                                if self.Flage:
                                    pass
                                else:
                                    self.action_loader.release_camera()
                                    self.updata_textEdit_log_task.emit("提前退出")
                                    self.write_log_task.emit(0, "提前退出")
                                    break
                                self.action_loader.loader_avoid()
                                self.write_log_task.emit(0, "装载器移动至避位处")
                                # 显微镜完成扫描后，移动至于装载器的交接位置
                                self.judge_pdb("当前已经停止")
                                if self.Flage:
                                    pass
                                else:
                                    self.action_loader.release_camera()
                                    break
                                self.write_log_task.emit(0, "显微镜开始扫描")
                                self.action_mircoscope.start(ID, IDall, crop_img)
                                self.write_log_task.emit(0, "显微镜扫描结束")
                                # 等待扫描完成
                                self.judge_pdb("当前已经停止")
                                if self.Flage:
                                    pass
                                else:
                                    self.action_loader.release_camera()
                                    break
                                self.action_mircoscope.move_2_loader_give()
                                self.write_log_task.emit(0, "显微镜移动至交接处")
                                # 装载器移动至显微镜交接处
                                self.judge_pdb("当前已经停止")
                                if self.Flage:
                                    pass
                                else:
                                    self.action_loader.release_camera()
                                    self.updata_textEdit_log_task.emit("提前退出")
                                    self.write_log_task.emit(0, "提前退出")
                                    break
                                self.action_loader.move_2_microscope_get()
                                self.write_log_task.emit(0, "装载器移动至显微镜处")
                                time.sleep(1)
                                # 从显微镜取回片子
                                self.judge_pdb("当前已经停止")
                                if self.Flage:
                                    pass
                                else:
                                    self.action_loader.release_camera()
                                    break
                                loader_flage = self.action_loader.get_slide_from_microscope()
                                time.sleep(1)
                                if loader_flage == 1:
                                    self.write_log_task.emit(0, "取片成功")
                                else:
                                    self.updata_textEdit_log_task.emit(
                                        "从显微镜取片时卡住玻片：仓位号" + str(box) + "第" + str(i + 1) + "片" + '\n')
                                    self.write_log_task.emit(1, "从显微镜取片时卡住玻片：仓位号" + str(box) + "第" + str(
                                        i + 1) + "片")
                                    self.Flage = False
                                    self.judge_pdb("取片失败警告！！！")
                                    if self.Flage:
                                        pass
                                    else:
                                        self.action_loader.release_camera()
                                        self.updata_textEdit_log_task.emit("提前退出")
                                        self.write_log_task.emit(0, "提前退出")
                                        break
                                # 显微镜复位
                                self.judge_pdb("当前已经停止")
                                if self.Flage:
                                    pass
                                else:
                                    self.action_loader.release_camera()
                                    self.updata_textEdit_log_task.emit("提前退出")
                                    self.write_log_task.emit(0, "提前退出")
                                    break
                                self.action_mircoscope.microscope_homezxy()
                                self.write_log_task.emit(0, "显微镜复位")
                                # 装载器回到片子放置的初始位置
                                self.judge_pdb("当前已经停止")
                                if self.Flage:
                                    pass
                                else:
                                    self.action_loader.release_camera()
                                    self.updata_textEdit_log_task.emit("提前退出")
                                    self.write_log_task.emit(0, "提前退出")
                                    break
                                self.action_loader.move_xz_to(slide_points_xz[i][0],
                                                              slide_points_xz[i][1] - self.action_loader.z_gap)
                                self.write_log_task.emit(0, "装载器移动至玻片仓回收位置")
                                # 将片子放回装载器
                                self.judge_pdb("当前已经停止")
                                if self.Flage:
                                    pass
                                else:
                                    self.action_loader.release_camera()
                                    self.updata_textEdit_log_task.emit("提前退出")
                                    self.write_log_task.emit(0, "提前退出")
                                    break
                                self.write_log_task.emit(0, "开始放片")
                                loader_flage = self.action_loader.give_slide_to_box()
                                if loader_flage == 1:
                                    self.write_log_task.emit(0, "放片成功")
                                else:
                                    self.updata_textEdit_log_task.emit(
                                        "放片时卡住玻片：仓位号" + str(box) + "第" + str(i + 1) + "片" + '\n')
                                    self.write_log_task.emit(1, "放片时卡住玻片：仓位号" + str(box) + "第" + str(
                                        i + 1) + "片")
                                    self.Flage = False
                                    self.judge_pdb("放片失败警告！！！")
                                    if self.Flage:
                                        pass
                                    else:
                                        self.action_loader.release_camera()
                                        self.updata_textEdit_log_task.emit("提前退出")
                                        self.write_log_task.emit(0, "提前退出")
                                        break
                                if self.Flage:
                                    self.updata_textEdit_log_task.emit(
                                        "已完成扫描玻片：仓位号：" + str(box) + "第" + str(i + 1) + "片" + '\n')
                                    self.write_log_task.emit(0, "已完成扫描玻片：仓位号：" + str(box) + "第" + str(
                                        i + 1) + "片")

                                else:
                                    self.updata_textEdit_log_task.emit(
                                        "中断扫描：仓位号：" + str(box) + "第" + str(i + 1) + "片" + '\n')
                                    self.write_log_task.emit(0, "中断扫描：仓位号：" + str(box) + "第" + str(
                                        i + 1) + "片")
                                    break
                            # 如果没有则放回去
                            else:
                                self.number_next = self.number_next + 1
                                self.judge_pdb("当前已经停止")
                                if self.Flage:
                                    pass
                                else:
                                    self.action_loader.release_camera()
                                    self.updata_textEdit_log_task.emit("提前退出")
                                    self.write_log_task.emit(0, "提前退出")
                                    break
                                self.action_loader.move_xz_to(slide_points_xz[i][0],
                                                              slide_points_xz[i][1] - self.action_loader.z_gap)
                                self.write_log_task.emit(0, "装载器移动至玻片仓回收位置")
                                self.updata_textEdit_log_task.emit(
                                    "扫描：仓位号：" + str(box) + "第" + str(i + 1) + "片" + "未识别到玻片ID" + '\n')
                                self.updata_textEdit_log_task.emit('正在放回')
                                self.write_log_task.emit(1, "扫描：仓位号：" + str(box) + "第" + str(
                                    i + 1) + "片" + "未识别到玻片ID正在放回")
                                self.judge_pdb("当前已经停止")
                                if self.Flage:
                                    pass
                                else:
                                    self.action_loader.release_camera()
                                    self.updata_textEdit_log_task.emit("提前退出")
                                    self.write_log_task.emit(0, "提前退出")
                                    break
                                loader_flage = self.action_loader.give_slide_to_box()
                                self.write_log_task.emit(0, "开始放片")
                                if loader_flage == 1:
                                    self.write_log_task.emit(0, "放片成功")
                                else:
                                    self.updata_textEdit_log_task.emit(
                                        "放片时卡住玻片：仓位号" + str(box) + "第" + str(i + 1) + "片" + '\n')
                                    self.write_log_task.emit(1, "放片时卡住玻片：仓位号" + str(box) + "第" + str(
                                        i + 1) + "片")
                                    self.Flage = False
                                    self.judge_pdb("放片失败警告！！！")
                                    if self.Flage:
                                        pass
                                    else:
                                        self.action_loader.release_camera()
                                        self.updata_textEdit_log_task.emit("提前退出")
                                        self.write_log_task.emit(0, "提前退出")
                                        break
                            # 扫描完最后的玻片

                            if i == len(slide_points_xz) - 1 and self.Flage == True:
                                self.judge_pdb("当前已经停止")
                                if self.Flage:
                                    pass
                                else:
                                    self.action_loader.release_camera()
                                    self.updata_textEdit_log_task.emit("提前退出")
                                    self.write_log_task.emit(0, "提前退出")
                                    break
                                self.action_loader.move_z_to(slide_points_xz[i][1] - self.action_loader.z_gap)
                                self.write_log_task.emit(0, "移动至最后一片处")
                                self.judge_pdb("当前已经停止")
                                if self.Flage:
                                    pass
                                else:
                                    self.action_loader.release_camera()
                                    break
                                loader_flage = self.action_loader.loader_last_push()
                                self.write_log_task.emit(0, "推动最后一片玻片")
                                if loader_flage == 1:
                                    self.write_log_task.emit(0, "推动最后一片玻片成功")

                                else:
                                    self.updata_textEdit_log_task.emit(
                                        "推动时卡住玻片：仓位号" + str(box) + "第" + str(i + 1) + "片" + '\n')
                                    self.write_log_task.emit(1, "推动时卡住玻片：仓位号" + str(box) + "第" + str(
                                        i + 1) + "片")
                                    self.judge_pdb("推片失败警告！！！")
                                    if self.Flage:
                                        pass
                                    else:
                                        self.action_loader.release_camera()
                                        self.updata_textEdit_log_task.emit("提前退出")
                                        self.write_log_task.emit(0, "提前退出")
                                        break
                                # 仓位清0，灯变绿
                                self.action_loader.set_led(int(box) - 1, self.action_loader.color.green)
                            if i == 14 or i == 29:
                                self.action_loader.move_z_to(0)
                                time.sleep(1)
                            if self.number_next >= 2:
                                self.action_loader.set_led(int(box) - 1, self.action_loader.color.green)
                                # 表示后面没有玻片了
                                self.updata_textEdit_log_task.emit(
                                    "后面没有玻片了：仓位号" + str(box) + '\n')
                                self.write_log_task.emit(0, "后面没有玻片了：仓位号" + str(box))

                                break
                    # 中断扫描
                    else:
                        self.updata_textEdit_log_task.emit(
                            "已停止当前扫描：仓位号" + str(box) + '\n')
                        self.write_log_task.emit(0, "已停止当前扫描：仓位号" + str(box))
                        self.action_loader.release_camera()
                        self.activate_pushbutton.emit()
                        break
                # 执行完所有片子的扫描流程
                self.action_loader.release_camera()
                self.activate_pushbutton.emit()
                config = configparser.ConfigParser()
                config.read('config.ini')
                config.set('Device', 'microscope', str(True))
                with open('config.ini', 'w') as configfile:
                    config.write(configfile)
            except Exception as e:
                self.activate_pushbutton.emit()
                self.write_log_task.emit(0, "当前扫描失败"+str(e))
                self.updata_textEdit_log_task.emit("当前扫描失败" + '\n')
        else:
            self.activate_pushbutton.emit()
            self.updata_textEdit_log_task.emit("上次扫描恶意中断，请退出软件检查设备，重启软件！！！" + '\n')

    def stop(self):
        self.RUN_SCAN.flage_run = False
        self.Flage = False
        self.updata_textEdit_log_task.emit("系统已收到停止信号，正在停止扫描..." + '\n')

    def pause(self):
        self.RUN_SCAN.flage_run = False
        self.updata_textEdit_log_task.emit("系统已收到停止信号，正在暂停扫描..." + '\n')
