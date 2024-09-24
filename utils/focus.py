# -*- encoding: utf-8 -*-
"""
@Description:
对焦算法
@File    :   action_loader.py
@Time    :   2024/07/16
@Author  :   Li QingHao
@Version :   2.0
@Time_END :  最后修改时间：
@Developers_END :  最后修改作者：
"""
import cv2
import numpy as np


# def Sharpness(image):
#     # 将图像转换为灰度图像
#     if len(image.shape) == 3:
#         gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     else:
#         gray = image
#     # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#
#     # 计算Sobel算子在x和y方向上的梯度
#     sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=5)
#     sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=5)
#
#     # 计算梯度幅值
#     gradient_magnitude = np.sqrt(sobelx ** 2 + sobely ** 2)
#
#     # 计算清晰度指标
#     sharpness = np.mean(gradient_magnitude)
#
#     return sharpness

def Sharpness(image):
    # 将图像转换为灰度图像
    if len(image.shape) == 3:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        gray = image
    # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 计算Sobel算子在x和y方向上的梯度
    sharpness = np.std(gray)

    return sharpness
