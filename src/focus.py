import numpy as np
import cv2


def Sharpness(image):
    # 将图像转换为灰度图像
    if len(image.shape) == 3:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        gray = image
    focus_measure = np.std(gray, axis=None)
    return focus_measure
