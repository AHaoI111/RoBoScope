import control.camera as camera
import control.microcontroller as microcontroller
import control.core as core


class Camera:
    def __init__(self, sn1, sn2, exposure_time1, analog_gain1, exposure_time2, analog_gain2):
        try:
            # 加载对象
            self.camera1 = camera.Camera(sn=sn1)
            self.camera2 = camera.Camera(sn=sn2)
            # 打开相机
            self.camera1.open()
            self.camera2.open()
            # 设置相机参数
            ####相机1
            # self.camera1.camera.BalanceWhiteAuto.set(2)
            offset_x = (732 // 8) * 8
            offset_y = (238 // 8) * 8
            self.camera1.set_ROI(offset_x, offset_y, 2560, 2560)
            self.camera1.set_exposure_time(exposure_time1)
            self.camera1.set_analog_gain(analog_gain1)
            self.camera1.set_software_triggered_acquisition()
            self.camera1.start_streaming()
            ####相机2
            self.camera2.camera.BalanceWhiteAuto.set(2)
            self.camera2.set_ROI(offset_x, offset_y, 2560, 2560)
            self.camera2.set_exposure_time(exposure_time2)
            self.camera2.set_analog_gain(analog_gain2)

            self.camera2.set_software_triggered_acquisition()
            self.camera2.start_streaming()


        except:
            return


class Microscope:
    def __init__(self):
        try:
            #
            self.microcontroller = microcontroller.Microcontroller()
            self.navigationController = core.NavigationController(self.microcontroller)
            # 显微镜初始化
            self.microcontroller.initialize_drivers()
            self.microcontroller.configure_actuators()
            # 设置z限位
            self.navigationController.set_z_limit_pos_mm(5.4)
        except:
            return


class device:
    def __init__(self):
        self.configurationManager = core.ConfigurationManager('./channel_configurations.xml')
        self.configuration_Lightpathleft = self.configurationManager.configurations[0]
        self.configuration_Lightpathright = self.configurationManager.configurations[1]
        self.Microscope = Microscope()
        self.CameraAll = Camera(self.configuration_Lightpathleft.camera_sn, self.configuration_Lightpathright.camera_sn,
                                self.configuration_Lightpathleft.exposure_time,
                                self.configuration_Lightpathleft.analog_gain,
                                self.configuration_Lightpathright.exposure_time,
                                self.configuration_Lightpathright.analog_gain)
