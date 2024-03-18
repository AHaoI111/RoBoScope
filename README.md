# BIOscope
![titel](https://github.com/AHaoI111/AutoFocus-BIOscope/assets/108380260/92a20afe-fb91-4a0d-a9fc-f5793b6586da)

# Modular automated microscope speeds up AI

It is designed to build a modular and automated microscope system that is easy to integrate and assemble. Improve efficiency in scientific research, medical diagnosis, production inspection and other fields, help researchers obtain large amounts of data faster, and accelerate experimental and research progress.

https://github.com/AHaoI111/AutoFocus-BIOscope/assets/108380260/e978af60-ad5f-4a3b-a9f7-c766cb06645b


In the software part, you can modify the modules appropriately according to your own needs to realize the application of automatic focusing, automatic scanning, and AI models.


## 项目代码结构

```
Bioscope
├── control                     # 硬件驱动控制基于octopi-research
│   └── _def.py                 # 初始参数设置-控制单片机
│   └── camera.py               # 相机驱动的的抽象类
│   └── microcontroller.py      # 位移台驱动的抽象类
│   └── core.py                 # 控制运动的抽象类
│   └── ...                     # 其他的抽象类
├── DataProcessing 
│   └── data.py                 # 根据需求处理原始数据 
├── src 
│   └── UI
│        └── ICON               # 图标
│        └── GifSplashScreen.py # 软件初始化加载动画                   
│        └── ui.py              # 原始设计的ui界面
│        └── GUI_bioscope.py    # 基于ui界面抽象设置功能类
│   └── ImageAcquisition
│        └── Device             # 基于control封装的硬件启动抽象类
│        └── Route.py           # 规划自动扫描路径类                   
│        └── Run.py             # 应用运动控制联合相机拍照抽象类
│        └── focus.py           # 自动对焦算法
│   └── DataSaver
│        └── Graph.py           # 保存原始数据类                   
│        └── model.py           # 查看原始数据类
│        └── Saverdata.py       # 保存原始图片、扫描数据、AI推理等队列抽象类
│   └── model
│        └── model.py           # 用于加载模型、设置推理等AI模型抽象类                   
│        └── model.pt           # 模型文件
├── main.py                     # 程序入口
├── config.ini                  # 扫描参数配置文件
├── configuration_octopi.txt    # 位移台参数配置文件
├── channel_configurations.xml  # 相机光源参数配置文件
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
