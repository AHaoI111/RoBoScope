# RoBoScope
![20240719-145815](https://github.com/user-attachments/assets/89fec310-e673-4661-8866-6bc97346beed)

![20240719-150920](https://github.com/user-attachments/assets/9145ef40-7937-484d-93cc-8ccb687a7fbc)



# Modular automated microscope speeds up AI

It is designed to build a modular and automated microscope system that is easy to integrate and assemble. Improve efficiency in scientific research, medical diagnosis, production inspection and other fields, help researchers obtain large amounts of data faster, and accelerate experimental and research progress.

# Microbe
| Live tracking |
| --- |
| 
https://github.com/user-attachments/assets/82111c3f-00d0-4994-a960-5d02d06a81c5
|
| sputum | sputum |
| --- | --- |
| ![2024_07_11_15_19_50_b99b92a7-f672-4d1b-83e2-3303e31f1fb7_017](https://github.com/user-attachments/assets/a3428081-760a-4b9b-966a-404961600a89) | ![2024_07_11_16_16_13_f265b1cf-8f75-4b06-aba2-54087af6f99d_050](https://github.com/user-attachments/assets/97e8c725-5bd1-4c2a-b78f-ae773537a747) |
| chromosomes | mouse bone marrow cell |
| --- | --- |
| ![ok](https://github.com/user-attachments/assets/b49c9b79-8a9b-47d2-90bd-f33d51b6c00b)  | ![test](https://github.com/user-attachments/assets/22f955dc-8232-48f8-90c2-673a6dc3ddf2) |









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

### Version 1.0.1 - 2024-7-15
- Release version V1.0 software

### Version 1.0.0 - 2023-08-15
- Initial release


# Function introduction:

- 1Provides automatic autofocus function.
- 2Automatically plans the path based on the actual scanned area (in mm).
- 3Multiple autofocus modes: single autofocus for full-slide scanning, autofocus for each scan in region scanning, and intelligent autofocus.
- 4dual camera system


Firstly, you must have the supported hardware: a camera and a modular motorized microscope. 


Acknowledgement
control Code is largely based on octopi-research (https://github.com/hongquanli/octopi-research/tree/master/software)
