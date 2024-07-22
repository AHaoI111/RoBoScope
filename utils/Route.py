# -*- encoding: utf-8 -*-
"""
@Description:
显微镜路径计算
@File    :   action_loader.py
@Time    :   2024/07/16
@Author  :   Li QingHao
@Version :   2.0
@Time_END :  最后修改时间：
@Developers_END :  最后修改作者：
"""


def get_route(image, center_x, center_y, region_w, region_h, calibration):
    points_4 = []
    points_xy = []
    if len(image.shape) == 2:
        h, w = image.shape
    else:
        h, w, _ = image.shape

    # 起始点
    x_mm = center_x + region_w / 2
    y_mm = center_y + region_h / 2
    # 4点
    points_4.append([center_x + region_w / 4, center_y + region_h / 4])
    points_4.append([center_x + region_w / 4, center_y - region_h / 4])

    points_4.append([center_x - region_w / 4, center_y - region_h / 4])
    points_4.append([center_x - region_w / 4, center_y + region_h / 4])

    # 视野个数
    if int(region_w / (w * calibration)) % 2 == 0:
        number_x = int(region_w / (w * calibration))
    else:
        number_x = int(region_w / (w * calibration)) + 1
    if int(region_h / (h * calibration)) % 2 == 0:
        number_y = int(region_h / (h * calibration))
    else:
        number_y = int(region_h / (h * calibration)) + 1
    # 规划路径
    for i in range(int(number_x)):
        if i % 2 == 0:
            for j in range(int(number_y)):
                if (i + 0.5) * w * calibration + x_mm > center_x and (j + 0.5) * h * calibration + y_mm > center_y:
                    points_xy.append([i, j, 1])
                elif (i + 0.5) * w * calibration + x_mm > center_x and (j + 0.5) * h * calibration + y_mm < center_y:
                    points_xy.append([i, j, 2])
                elif (i + 0.5) * w * calibration + x_mm < center_x and (j + 0.5) * h * calibration + y_mm < center_y:
                    points_xy.append([i, j, 3])
                elif (i + 0.5) * w * calibration + x_mm < center_x and (j + 0.5) * h * calibration + y_mm > center_y:
                    points_xy.append([i, j, 4])
        else:
            for j in range(int(number_y) - 1, -1, -1):
                if (i + 0.5) * w * calibration + x_mm > center_x and (j + 0.5) * h * calibration + y_mm > center_y:
                    points_xy.append([i, j, 1])
                elif (i + 0.5) * w * calibration + x_mm > center_x and (j + 0.5) * h * calibration + y_mm < center_y:
                    points_xy.append([i, j, 2])
                elif (i + 0.5) * w * calibration + x_mm < center_x and (j + 0.5) * h * calibration + y_mm < center_y:
                    points_xy.append([i, j, 3])
                elif (i + 0.5) * w * calibration + x_mm < center_x and (j + 0.5) * h * calibration + y_mm > center_y:
                    points_xy.append([i, j, 4])

    return points_4, points_xy, x_mm, y_mm, number_x, number_y, h, w
