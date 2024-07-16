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
import torch
import numpy as np
import concurrent.futures


def Sharpness(image):
    # 将图像转换为灰度图像
    if len(image.shape) == 3:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        gray = image

    # 将灰度图像转换为PyTorch张量，并将其移动到CUDA设备上
    gray_tensor = torch.from_numpy(gray).float().unsqueeze(0).unsqueeze(0).cuda()

    # 创建5x5的Sobel算子作为卷积核
    sobel_kernel_x = torch.tensor([[-2, -1, 0, 1, 2],
                                   [-3, -2, 0, 2, 3],
                                   [-4, -3, 0, 3, 4],
                                   [-3, -2, 0, 2, 3],
                                   [-2, -1, 0, 1, 2]], device='cuda').float().unsqueeze(0).unsqueeze(0)

    sobel_kernel_y = torch.tensor([[-2, -3, -4, -3, -2],
                                   [-1, -2, -3, -2, -1],
                                   [0, 0, 0, 0, 0],
                                   [1, 2, 3, 2, 1],
                                   [2, 3, 4, 3, 2]], device='cuda').float().unsqueeze(0).unsqueeze(0)

    # 使用conv2d函数进行卷积操作
    sobelx = torch.nn.functional.conv2d(
        gray_tensor,
        sobel_kernel_x,
        padding=2
    )

    sobely = torch.nn.functional.conv2d(
        gray_tensor,
        sobel_kernel_y,
        padding=2
    )

    # 计算梯度幅值
    gradient_magnitude = torch.sqrt(sobelx ** 2 + sobely ** 2)

    # 计算清晰度指标
    sharpness = torch.mean(gradient_magnitude).item()

    return sharpness


def merge_images(images):
    # images为img列表
    def select_values_from_channels(channels):
        height, width, c = channels.shape
        magnitudes = np.zeros((height, width, c), dtype=np.float32)

        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = [executor.submit(process_channel, channels[:, :, i]) for i in range(c)]
            for i, future in enumerate(concurrent.futures.as_completed(futures)):
                result = future.result()
                magnitudes[:, :, i] = result

        max_channel_index = np.argmax(magnitudes, axis=2)
        selected_pixels = channels[np.arange(height)[:, None], np.arange(width), max_channel_index]
        return selected_pixels

    def process_channel(channel):
        sobel_x = cv2.Sobel(channel, cv2.CV_64F, 1, 0, ksize=3)
        sobel_y = cv2.Sobel(channel, cv2.CV_64F, 0, 1, ksize=3)
        magnitude = cv2.magnitude(sobel_x, sobel_y)
        ksize = (21, 21)
        smoothed_image = cv2.blur(magnitude, ksize)
        return smoothed_image

    def focus_images(imgs):
        img_array = np.array(imgs)
        return img_array[:, :, :, 0], img_array[:, :, :, 1], img_array[:, :, :, 2]

    img_b, img_g, img_r = focus_images(images)

    channels_b = np.dstack(img_b) if img_b is not None else None
    channels_g = np.dstack(img_g) if img_g is not None else None
    channels_r = np.dstack(img_r) if img_r is not None else None

    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(executor.map(select_values_from_channels, [channels_b, channels_g, channels_r]))

    selected_pixel_b, selected_pixel_g, selected_pixel_r = results

    merged_image = cv2.merge([selected_pixel_b, selected_pixel_g, selected_pixel_r])

    return merged_image
