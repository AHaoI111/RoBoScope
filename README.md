# RoBoScope
![20240719-145815](https://github.com/user-attachments/assets/89fec310-e673-4661-8866-6bc97346beed)

![20240719-150920](https://github.com/user-attachments/assets/9145ef40-7937-484d-93cc-8ccb687a7fbc)



# Modular automated microscope speeds up AI

It is designed to build a modular and automated microscope system that is easy to integrate and assemble. Improve efficiency in scientific research, medical diagnosis, production inspection and other fields, help researchers obtain large amounts of data faster, and accelerate experimental and research progress.

# Microbe
| Live tracking |
| --- |


https://github.com/user-attachments/assets/82111c3f-00d0-4994-a960-5d02d06a81c5


| sputum | sputum |
| --- | --- |
| ![2024_07_11_15_19_50_b99b92a7-f672-4d1b-83e2-3303e31f1fb7_017](https://github.com/user-attachments/assets/a3428081-760a-4b9b-966a-404961600a89) | ![2024_07_11_16_16_13_f265b1cf-8f75-4b06-aba2-54087af6f99d_050](https://github.com/user-attachments/assets/97e8c725-5bd1-4c2a-b78f-ae773537a747) |

| chromosomes | mouse bone marrow cell |
| --- | --- |
| ![ok](https://github.com/user-attachments/assets/b49c9b79-8a9b-47d2-90bd-f33d51b6c00b)  |  ![test](https://github.com/user-attachments/assets/22f955dc-8232-48f8-90c2-673a6dc3ddf2)|

| pathological sections |
| --- |
| ![20240730-124530](https://github.com/user-attachments/assets/830008ab-df47-41e9-85cc-f8d955273074)  |









In the software part, you can modify the modules appropriately according to your own needs to realize the application of automatic focusing, automatic scanning, and AI models.

## Update History

### Version 2.0 - 2025-2-26
- Release version V2.0 software
- Added AIhub function to configure scanning plans and AI models

### Version 1.0.1 - 2024-7-15
- Release version V1.0 software

### Version 1.0.0 - 2023-08-15
- Initial release


## Framework
![软件分层架构图](https://github.com/user-attachments/assets/1ba30ee2-fb81-40a6-ac0d-ae4441ef52e7)



## Project code structure
```
Bioscope
├── apply                       # 应用层
│   └── task_info.py            # 扫描任务方案参数
│   └── taskwork.py             # 扫描任务分发类
├── control                     # 控制层
│   └── core.py                 # 控制显微镜的核心代码
│   └── processing_handler.py   # 配置控制参数
│   └── utils.py               
│   └── utils_config.py
│   └── serial_peripherals.py
├── DataSaver                   # 数据存储
│   └── Saverdata.py            # 存储需要的业务数据
├── Drives                      # 驱动层
│   └── gxipy                   # 相机驱动
│   └── def.py                  # 初始化参数设置
│   └── camera.py               # 相机驱动功能类
│   └── loadercontroller.py     # 装载器驱动
│   └── microcontroller.py      # 显微镜驱动
├── UI                          # 界面
│   └── 、、、             
├── processing                  # 处理层
│   └── image_st.py             # 图像拼接
│   └── ocr.py                  # 玻片ocr识别
├── utils                       # 中间层
│   └── action_loader.py        # 装载器行为封装类
│   └── action_microscope.py    # 显微镜行为封装类
│   └── focus.py                # 对焦算法
│   └── read_config.py          # 读取参数文件
│   └── Route.py                # 扫描路径规划
│   └── Scan.py                 # 扫描
│   └── Search_device.py        # 设备开机自检
├── channel_configurations.xml  # 相机光源参数配置文件
├── config.yaml                 # 扫描参数配置文件
├── configuration_octopi.ini    # 相机光源参数配置文件
├── roboscope.py                     # 主程序入口
```
```
# Configuration File / 配置文件
# 注意！！！
**更换了硬件请注意检查软件以下参数设置**:
- **Camera  / 相机设置**:标定系数
- **Device  / 设备设置**:cameranumber/相机数量、firmware/控制器固件版本、
- **Sys /系统**：串口、当前系统
- **channel_configurations.xml**：该文件中的IlluminationSource/灯源口、CameraSN/相机编号

  


## Camera  / 相机设置

### High / 高倍率
- **RotateImageAnglehigh**: 90° / 图像旋转角度：90°
- **wbhigh**:
  - B: 1.3711 / 蓝色：1.3711
  - G: 1.0 / 绿色：1.0
  - R: 2.1797 / 红色：2.1797
- **高倍标定**: 6.3247e-05 / 高倍标定：6.3247e-05

### Low  / 低倍率
- **RotateImageAnglehigh**: 90° / 图像旋转角度：90°
- **wblow**:
  - B: 1.3594 / 蓝色：1.3594
  - G: 1.0 / 绿色：1.0
  - R: 2.1875 / 红色：2.1875
- **低倍标定**: 0.00126888841 / 低倍标定：0.00126888841

### Single / 单镜头
- **RotateImageAnglehigh**: 0° / 图像旋转角度：0°
- **wbone**:
  - B: 1.164 / 蓝色：1.164
  - G: 1.0 / 绿色：1.0
  - R: 1.5 / 红色：1.5
- **单镜头标定**: 0.0003125 / 单镜头标定：0.0003125






## Device  / 设备设置

- **cameranumber**: 2 / 相机数量：2
- **firmware**: V2 / 固件版本：V2
- **loaderflage**: false / 加载标志：false
- **microscope**: true / 显微镜：true




## ImageSaver / 图像保存设置

- **imagequailty**: 100 / 图像质量：100
- **imagestitchsize**: 320 / 图像拼接大小：320
- **maxworkers**: 4 / 最大工作线程：4
- **pixelformat**: PNG / 像素格式：PNG
- **queuenumber**: 625 / 队列数量：625
- **savepath**: Z:/ / 保存路径：Z:/




## Loader Settings / 装载器设置

- **Box 1 Start Point (X, Z)**: (159.4, 126.35) / 箱子1起始点（X, Z）：（159.4, 126.35）
- **Box 2 Start Point (X, Z)**: (210.05, 126.35) / 箱子2起始点（X, Z）：（210.05, 126.35）
- **Box 3 Start Point (X, Z)**: (259.95, 126.35) / 箱子3起始点（X, Z）：（259.95, 126.35）
- **Box 4 Start Point (X, Z)**: (310.25, 126.35) / 箱子4起始点（X, Z）：（310.25, 126.35）
- **Box X Spacing**: 50.0 / 箱子X间距：50.0
- **Box Z Spacing**: 3.5 / 箱子Z间距：3.5
- **Camera Exposure**: -4 / 相机曝光：-4
- **Camera Index**: 0 / 相机索引：0
- **Rectangle (X1, X2, Y1, Y2)**: (510, 1170, 500, 925) / 矩形（X1, X2, Y1, Y2）：（510, 1170, 500, 925）
- **slidepush**: 1000.0 / 滑动前进：1000.0
- **slidereturn**: 0.0 / 滑动返回：0.0
- **X Clearance**: 6.0 / X间隙：6.0
- **X End**: 34.3 / X结束：34.3
- **Z Camera**: 50.0 / Z相机：50.0
- **Z End**: 103.05 / Z结束：103.05
- **Z Lift**: 4.0 / Z升高：4.0
- **串口**: COM3 / 串口：COM3




## Microscope  / 显微镜设置

### High  / 高倍率
- **对焦经验值高倍**: 4.92028 / 对焦体验值：4.92028
- **高倍倍数**: 100 / 放大倍率：100
- **高倍对焦分辨率**: 0.001 / 对焦分辨率：0.001
- **高倍对焦方式**: 1 / 对焦方法：1
- **高倍对焦步数**: 40 / 对焦步数：40
- **高倍扫描中心xy (X, Y)**: (13.7178, 40.7023) / 扫描中心（X, Y）：（13.7178, 40.7023）
- **高倍扫描区域 (Height, Width)**: (2, 2) / 扫描区域（高度, 宽度）：（2, 2）
- **高倍隔点对焦步长**: 1 / 对焦步长：1

### Low  / 低倍率
- **低倍倍数**: 5 / 放大倍率：5
- **低倍对焦分辨率**: 0.006 / 对焦分辨率：0.006
- **低倍对焦方式**: 1 / 对焦方法：1
- **低倍对焦步数**: 30 / 对焦步数：30
- **低倍扫描中心xy (X, Y)**: (12.832, 34.057) / 扫描中心（X, Y）：（12.832, 34.057）
- **低倍扫描区域 (Height, Width)**: (8, 8) / 扫描区域（高度, 宽度）：（8, 8）
- **低倍隔点对焦步长**: 1 / 对焦步长：1
- **对焦经验值低倍**: 4.6 / 对焦体验值：4.6

### Single  / 单镜头
- **单镜头倍数**: 20 / 放大倍率：20
- **单镜头对焦分辨率**: 0.003 / 对焦分辨率：0.003
- **单镜头对焦方式**: 1 / 对焦方法：1
- **单镜头对焦步数**: 40 / 对焦步数：40
- **单镜头扫描中心xy (X, Y)**: (31.988, 39.055) / 扫描中心（X, Y）：（31.988, 39.055）
- **单镜头扫描区域 (Height, Width)**: (8, 8) / 扫描区域（高度, 宽度）：（8, 8）
- **单镜头隔点对焦步长**: 1 / 对焦步长：1
- **对焦经验值单镜头**: 3.80206 / 对焦体验值：3.80206

### Sys / 系统
- **lensgapx**: 35.811 / 镜头间隙X：35.811
- **lensgapy**: 0.053 / 镜头间隙Y：0.053
- **scanmode**: true / 扫描模式是否开启高低倍配合扫描：true
- **scanmultiple**: low / 双镜头不启用高低倍配合时，当前扫描放大倍率：低
- **X End**: 57.0 / X结束：57.0
- **Y End**: 32.1 / Y结束：32.1
- **串口**: COM10 / 串口：COM10
- **当前系统**: double / 当前系统：双




## Network / 网络设置

- **flag**: true / 标志：true
- **localip**: 192.168.0.199 / 本地IP：192.168.0.199
- **localport**: 8000 / 本地端口：8000
- **serverip**: 192.168.0.47 / 服务器IP：192.168.0.47
- **serverport**: 8000 / 服务器端口：8000




## Task / 任务设置

- **Box 1**: true / 箱子1：true
- **Box 2**: true / 箱子2：true
- **Box 3**: true / 箱子3：true
- **Box 4**: true / 箱子4：true
- **slidenumber**: 30 / 滑片数量：30
```

# Function introduction:

- 1Provides automatic autofocus function.
- 2Automatically plans the path based on the actual scanned area (in mm).
- 3Multiple autofocus modes: single autofocus for full-slide scanning, autofocus for each scan in region scanning, and intelligent autofocus.
- 4dual camera system


Firstly, you must have the supported hardware: a camera and a modular motorized microscope. 


Acknowledgement
control Code is largely based on octopi-research (https://github.com/hongquanli/octopi-research/tree/master/software)
