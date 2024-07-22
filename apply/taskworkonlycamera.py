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
        self.action_mircoscope.flag = True
        self.action_mircoscope.flage_run = True
        self.Flage = True

    def run(self, box):
        """
        执行自动送片加扫描的任务流程。
        此方法首先使设备复位，然后按照预设的点位信息进行片子的自动取出、送至显微镜、扫描、再放回装载器的过程。
        该过程中涉及显微镜与装载器的多次协作动作。
        """
        if self.config['Device']['microscope']:
            self.box = box
            try:
                # 设备复位，包括显微镜和装载器的复位动作
                # 加载配置
                # 记录是否恶意退出
                self.action_mircoscope.microscope_homezxy()
                ID = ['20240704']
                IDall = ['20240704']
                self.action_mircoscope.start(ID, IDall)
                self.activate_pushbutton.emit()
            except Exception as e:
                self.activate_pushbutton.emit()
                self.write_log_task.emit(0, "当前扫描失败" + str(e))
                self.updata_textEdit_log_task.emit("当前扫描失败" + '\n')
        else:
            self.activate_pushbutton.emit()
            self.updata_textEdit_log_task.emit("上次扫描恶意中断，请退出软件检查设备，重启软件！！！" + '\n')

    def pause(self):
        self.action_mircoscope.pause()
        self.updata_textEdit_log_task.emit("正在暂停扫描..." + '\n')
