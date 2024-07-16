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
├── apply                       # 应用层
│   └── GUI_bioscope.py         # UI功能类
│   └── ui_mainwindow.py        # UI原始界面类
│   └── taskwork.py             # 扫描任务分发类
├── control                     # 控制层
│   └── core.py                 # 控制显微镜的核心代码
│   └── processing_handler.py   # 配置控制参数
│   └── utils.py               
│   └── utils_config.py         
├── DataSaver                   # 服务层
│   └── data.py                 # 存储需要的业务数据
│   └── Graph.py                # 存储方法
│   └── Saverdata.py            # 扫描过程中存储图片和数据
├── Drives                      # 驱动层
│   └── gxipy                   # 相机驱动
│   └── def.py                  # 初始化参数设置
│   └── camera.py               # 相机驱动功能类
│   └── loadercontroller.py     # 装载器驱动
│   └── microcontroller.py      # 显微镜驱动
├── processing                  # 处理层
│   └── image_st.py             # 图像拼接
│   └── ocr.py                  # 玻片ocr识别
├── utils                       # 中间层
│   └── action_loader.py        # 装载器行为封装类
│   └── action_microscope.py    # 显微镜行为封装类
│   └── focus.py                # 对焦算法
│   └── read_config.py          # 读取参数文件
│   └── Route.py                # 扫描路径规划
│   └── Search_device.py        # 设备开机自检
├── channel_configurations.xml  # 相机光源参数配置文件
├── config.yaml                 # 扫描参数配置文件
├── configuration_octopi.ini    # 相机光源参数配置文件
├── main.py                     # 主程序入口
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
