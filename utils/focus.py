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
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        B, G, gray = cv2.split(image)
    else:
        gray = image
    blurred_image = cv2.blur(gray, (5, 5))
    # 计算Sobel算子在x和y方向上的梯度
    sobelx = cv2.Sobel(blurred_image, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(blurred_image, cv2.CV_64F, 0, 1, ksize=3)
    # 计算梯度幅值
    # laplacian = cv2.Laplacian(B_filtered, cv2.CV_64F, ksize=9)
    gradient_magnitude = np.sqrt(sobelx ** 2 + sobely ** 2)
    # 计算清晰度指标
    weighted_sharpness = np.sum(gradient_magnitude ** 2) / np.sum(gradient_magnitude)
    # sharpness2 = np.mean(gradient_magnitude)
    return weighted_sharpness


def Sharpness_sobel(image):
    # 将图像转换为灰度图像
    if len(image.shape) == 3:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        gray = image
    # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
    gradient_magnitude = np.sqrt(sobelx ** 2 + sobely ** 2)
    # 计算Sobel算子在x和y方向上的梯度
    sharpness = np.mean(gradient_magnitude)
    return sharpness


# def Sharpness(image):
#     # 将图像转换为灰度图像
#     if len(image.shape) == 3:
#         gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     else:
#         gray = image
#     # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#
#     # 计算Sobel算子在x和y方向上的梯度
#     sharpness = np.std(gray)
#
#     return sharpness


def Sharpness_chromosome(image):
    # 将图像转换为灰度图像
    if len(image.shape) == 3:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        gray = image

    # 获取图像的高度和宽度
    height, width = gray.shape

    # 计算中心点的矩形区域的坐标
    center_x, center_y = width // 2, height // 2
    half_width, half_height = width // 4, height // 4

    # 定义中心矩形区域
    start_x = center_x - half_width
    start_y = center_y - half_height
    end_x = center_x + half_width
    end_y = center_y + half_height

    # 确保坐标在有效范围内
    start_x = max(0, start_x)
    start_y = max(0, start_y)
    end_x = min(width, end_x)
    end_y = min(height, end_y)

    # 提取中心区域
    center_region = gray[start_y:end_y, start_x:end_x]

    # 计算中心区域的清晰度（标准差）
    sharpness = np.std(center_region)

    return sharpness
