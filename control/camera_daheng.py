# qt libraries

import control.camera as camera
import control.core as core


class Camera:

    def __init__(self, microcontroller):
        # load objects
        self.microcontroller = microcontroller
        try:
            # 加载对象
            self.camera = camera.Camera()
            self.camera.open()
            self.configurationManager = core.ConfigurationManager('./channel_configurations.xml')
            self.streamHandler = core.StreamHandler()
            self.liveController = core.LiveController(self.camera, self.microcontroller, self.configurationManager)
            self.configurationManagerled = self.configurationManager.configurations[0]
            self.camera.set_ROI(732,238,2560,2560)
            self.camera.set_exposure_time(self.configurationManagerled.exposure_time)
            self.camera.set_analog_gain(self.configurationManagerled.analog_gain)
            self.camera.set_wb_ratios(1.7070, 1, 1.1953)
            # self.camera.camera.BalanceWhiteAuto.set(1)
            LED_MATRIX_R_FACTOR = 1
            LED_MATRIX_G_FACTOR = 1
            LED_MATRIX_B_FACTOR = 1
            if self.configurationManagerled.illumination_source < 10:  # LED matrix
                self.microcontroller.set_illumination_led_matrix(self.configurationManagerled.illumination_source,
                                                                 r=(self.configurationManagerled.illumination_intensity / 100) * LED_MATRIX_R_FACTOR,
                                                                 g=(self.configurationManagerled.illumination_intensity / 100) * LED_MATRIX_G_FACTOR,
                                                                 b=(self.configurationManagerled.illumination_intensity / 100) * LED_MATRIX_B_FACTOR)
            else:
                self.microcontroller.set_illumination(self.configurationManagerled.illumination_source, self.configurationManagerled.illumination_intensity)
            self.imageDisplay = core.ImageDisplay()

            # 打开相机
            self.camera.set_software_triggered_acquisition()
            self.camera.set_callback(self.streamHandler.on_new_frame)
            self.camera.enable_callback()
            self.camera.start_streaming()
            self.streamHandler.image_to_display.connect(self.imageDisplay.enqueue)
        except:
            return
