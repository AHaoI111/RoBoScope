import cv2
import numpy as np


# 清晰度计算
def Sharpness(image):
    # 将图像转换为灰度图像
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # 计算x方向和y方向的梯度
    sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0)
    sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1)
    # 计算梯度的幅值
    magnitude = np.sqrt(np.square(sobelx) + np.square(sobely))
    # 计算梯度幅值的平均值
    mean_mag = np.mean(magnitude)
    return mean_mag
