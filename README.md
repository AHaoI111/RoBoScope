# BIOscope
![titel](https://github.com/AHaoI111/AutoFocus-BIOscope/assets/108380260/92a20afe-fb91-4a0d-a9fc-f5793b6586da)

# Modular automated microscope speeds up AI

It is designed to build a modular and automated microscope system that is easy to integrate and assemble. Improve efficiency in scientific research, medical diagnosis, production inspection and other fields, help researchers obtain large amounts of data faster, and accelerate experimental and research progress.

https://github.com/AHaoI111/AutoFocus-BIOscope/assets/108380260/e978af60-ad5f-4a3b-a9f7-c766cb06645b


In the software part, you can modify the modules appropriately according to your own needs to realize the application of automatic focusing, automatic scanning, and AI models.

## Framework
![软件分层架构图](https://github.com/user-attachments/assets/1ba30ee2-fb81-40a6-ac0d-ae4441ef52e7)



## Project code structure

```
Bioscope
├── control                     # Hardware driver control is based on octopi-research
│   └── _def.py                 # Initial parameter setting-control microcontroller
│   └── camera.py               # Camera driver abstract class
│   └── microcontroller.py      # Abstract class for stage driver
│   └── core.py                 # Abstract class that controls movement
│   └── ...                     # Other abstract classes
├── DataProcessing 
│   └── data.py                 # Process raw data as needed
├── src 
│   └── UI
│        └── ICON               # icon
│        └── GifSplashScreen.py # Software initialization loading animation           
│        └── ui.py              # Original designed UI interface
│        └── GUI_bioscope.py    # Set functional classes based on UI interface abstraction
│   └── ImageAcquisition
│        └── Device             # Hardware startup abstract class based on control encapsulation
│        └── Route.py           # Planning automatic scan path class                  
│        └── Run.py             # Apply motion control combined with camera to take pictures abstract class
│        └── focus.py           # Autofocus algorithm
│   └── DataSaver
│        └── Graph.py           # Save original data class                
│        └── model.py           # View original data class
│        └── Saverdata.py       # Queue abstract classes that save original pictures, scanned data, AI inference, etc.
│   └── model
│        └── model.py           # AI model abstract class used to load models, set up inference, etc.                   
│        └── model.pt           # model file
├── main.py                     # Program entrance
├── config.ini                  # Scan parameter configuration file
├── configuration_octopi.txt    # Displacement stage parameter configuration file
├── channel_configurations.xml  # Camera light source parameter configuration file
```


## Update History

### Version 1.0.1 - 2024-3-13
- 🚀🚀🚀The new software installation package can be installed and used directly, and automatic scanning is enabled
- Download link 链接：https://pan.baidu.com/s/11eVjChxItaPmSHyAD-PdJw?pwd=1234 
提取码：1234

### Version 1.0.1 - 2024-1-15
- Added feature dual camera system

### Version 1.0.0 - 2023-08-15
- Initial release


# Function introduction:

- 1Provides automatic autofocus function.
- 2Automatically plans the path based on the actual scanned area (in mm).
- 3Multiple autofocus modes: single autofocus for full-slide scanning, autofocus for each scan in region scanning, and intelligent autofocus.
- 4dual camera system


Firstly, you must have the supported hardware: a camera and a modular motorized microscope. 

Secondly, you need to place the model in the model/ directory (model download link: link：https://pan.baidu.com/s/1V6RZauGDAlvvb9XeouCPqw?pwd=1234 
The extraction code：1234). 
Of course, you can also train your own model according to your needs.


Acknowledgement
control Code is largely based on octopi-research (https://github.com/hongquanli/octopi-research/tree/master/software)
