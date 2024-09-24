# -*- encoding: utf-8 -*-
import cv2
import numpy as np


def correction(image):
    pts1 = np.float32([[257, 374], [1757, 416], [1738, 906], [242, 929]])

    # 定义四个点在目标图像中的坐标
    pts2 = np.float32([[294, 453], [1393, 453], [1393, 819], [294, 819]])

    # 计算透视变换矩阵
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    return cv2.warpPerspective(image, matrix, (image.shape[1], image.shape[0]))
