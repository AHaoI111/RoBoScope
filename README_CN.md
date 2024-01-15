# AutoFocus-BIOscope
![titel](https://github.com/AHaoI111/AutoFocus-BIOscope/assets/108380260/00084c35-edab-44c1-a5bc-fb7400202397)

### Version 1.0.1 - 2024-01-15
- 新增功能：双镜头系统

### Version 1.0.0 - 2023-08-15
- 首次发布


这是一个模块化动化显微镜的项目。
用于搭建模块化自动化的显微镜系统，该系统易于集成与组装，软件部分拥有自动对焦、搭载识别模型自动识别微生物的功能。

# 功能介绍：
- 1提供自动对焦功能
- 2根据实际扫描的区域(mm)，自动规划路径
- 3多种对焦方式：全片扫描只对焦一次、区域扫描每次都对焦、智能对焦
- 4双镜头系统


首先，你必须要有支持的硬件：相机和模块化电动显微镜。

其次，需要将模型放在UI/model/目录下(模型下载地址：链接：https://pan.baidu.com/s/1V6RZauGDAlvvb9XeouCPqw?pwd=1234 提取码：1234)
当然你也可以根据需求自己训练模型

软件界面如下
<img width="1919" alt="屏幕截图 2024-01-15 150718" src="https://github.com/AHaoI111/AutoFocus-BIOscope/assets/108380260/f919ea60-5867-4c25-981c-65b05d5b67c7">




确认
控制部分代码有部分基于 octopi-research (https://github.com/hongquanli/octopi-research/tree/master/software)


