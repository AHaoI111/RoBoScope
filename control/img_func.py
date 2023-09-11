import cv2
import numpy as np


# 清晰度计算
def Sharpness(image):
    # # 将图像转换为灰度图像
    # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # # 计算x方向和y方向的梯度
    # sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0)
    # sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1)
    # # 计算梯度的幅值
    # magnitude = np.sqrt(np.square(sobelx) + np.square(sobely))
    # # 计算梯度幅值的平均值
    # mean_mag = np.mean(magnitude)
    # return mean_mag
    # 将图像转换为灰度图像
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # # 使用拉普拉斯算子计算图像的二阶导数
    # laplacian = cv2.Laplacian(gray, cv2.CV_32F)
    # # 计算拉普拉斯值的绝对值平均
    # mean_laplacian = np.mean(np.abs(laplacian))
    focus_measure = np.std(gray, axis=None)
    return focus_measure


def gray_world_algorithm(img):
    # 计算图像的B、G、R通道平均值
    avg_b = np.mean(img[:, :, 0])
    avg_g = np.mean(img[:, :, 1])
    avg_r = np.mean(img[:, :, 2])

    # 计算平均亮度
    avg_gray = (avg_b + avg_g + avg_r) / 3.0

    # 计算缩放因子
    scale_b = avg_gray / avg_b
    scale_g = avg_gray / avg_g
    scale_r = avg_gray / avg_r

    # 缩放各个通道的像素值
    adjusted_img = img.copy()
    adjusted_img[:, :, 0] = np.clip(img[:, :, 0] * scale_b, 0, 255)
    adjusted_img[:, :, 1] = np.clip(img[:, :, 1] * scale_g, 0, 255)
    adjusted_img[:, :, 2] = np.clip(img[:, :, 2] * scale_r, 0, 255)

    return adjusted_img

