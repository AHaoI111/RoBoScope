# 电机对象
class motion:
    def __init__(self):
        self.microcontroller = None
        self.navigationController = None

        try:
            import control.microcontroller as microcontroller
            import control.core as core

            # 
            self.microcontroller = microcontroller.Microcontroller()
            self.navigationController = core.NavigationController(self.microcontroller)
            # reinitialize motor drivers and DAC (in particular for V2.1 driver board where PG is not functional)
            self.microcontroller.initialize_drivers()

            # configure the actuators
            self.microcontroller.configure_actuators()
            self.navigationController.set_z_limit_pos_mm(2.32)
        except:
            print('! 电机未检测到 !')
