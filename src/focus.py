# import numpy as np
import cv2

# def Sharpness(image):
#     # 将图像转换为灰度图像
#     if len(image.shape) == 3:
#         gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     else:
#         gray = image
#     # focus_measure = np.std(gray, axis=None)
#     # 将图像转换为灰度图
#     # gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#
#     # 使用Laplacian算子进行边缘检测
#     laplacian = cv2.Laplacian(gray, cv2.CV_64F)
#
#     # 计算Laplacian结果的方差，作为图像对焦清晰度的评估指标
#     focus_measure = np.var(laplacian)
#     return focus_measure

# import cv2
import torch


def Sharpness(image):
    # 将图像转换为灰度图像
    if len(image.shape) == 3:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        gray = image

    # 将灰度图像转换为PyTorch张量，并将其移动到CUDA设备上
    gray_tensor = torch.from_numpy(gray).float().unsqueeze(0).unsqueeze(0).cuda()

    # 创建Laplacian算子作为卷积核
    laplacian_kernel = torch.tensor([[0, -1, 0],
                                     [-1, 4, -1],
                                     [0, -1, 0]], device='cuda').float().unsqueeze(0).unsqueeze(0)

    # 使用conv2d函数进行卷积操作
    laplacian = torch.abs(torch.nn.functional.conv2d(
        gray_tensor,
        laplacian_kernel,
        padding=1
    ))

    # 计算Laplacian结果的方差，作为图像对焦清晰度的评估指标
    focus_measure = torch.var(laplacian)

    # 将结果从GPU移动回CPU，并将其转换为标量值
    focus_measure = focus_measure.item()

    return focus_measure
