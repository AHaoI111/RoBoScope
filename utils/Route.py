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


# 玻片竖直放置x、y倒
def get_route(image, center_x, center_y, region_w, region_h, calibration):
    points_4 = []
    points_xy_real = []
    points_xy = []
    if len(image.shape) == 2:
        h, w = image.shape
    else:
        h, w, _ = image.shape

    view_w_mm = w * calibration
    view_h_mm = h * calibration

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
    for i in range(int(number_y)):
        if i % 2 == 0:
            for j in range(int(number_x)):
                if x_mm - (i + 0.5) * w * calibration > center_x and y_mm - (j + 0.5) * h * calibration > center_y:
                    points_xy_real.append([x_mm-(i+0.5)*view_w_mm, y_mm-(j+0.5)*view_w_mm, 1])
                    points_xy.append([i, j, 1])
                elif x_mm - (i + 0.5) * w * calibration > center_x and y_mm - (j + 0.5) * h * calibration < center_y:
                    points_xy_real.append([x_mm-(i+0.5)*view_w_mm, y_mm-(j+0.5)*view_w_mm, 2])
                    points_xy.append([i, j, 2])
                elif x_mm - (i + 0.5) * w * calibration < center_x and y_mm - (j + 0.5) * h * calibration < center_y:
                    points_xy_real.append([x_mm-(i+0.5)*view_w_mm, y_mm-(j+0.5)*view_w_mm, 3])
                    points_xy.append([i, j, 3])
                elif x_mm - (i + 0.5) * w * calibration < center_x and y_mm - (j + 0.5) * h * calibration > center_y:
                    points_xy_real.append([x_mm-(i+0.5)*view_w_mm, y_mm-(j+0.5)*view_w_mm, 4])
                    points_xy.append([i, j, 4])
        else:
            for j in range(int(number_x) - 1, -1, -1):
                if x_mm - (i + 0.5) * w * calibration > center_x and y_mm - (j + 0.5) * h * calibration > center_y:
                    points_xy_real.append([x_mm-(i+0.5)*view_w_mm, y_mm-(j+0.5)*view_w_mm, 1])
                    points_xy.append([i, j, 1])
                elif x_mm - (i + 0.5) * w * calibration > center_x and y_mm - (j + 0.5) * h * calibration < center_y:
                    points_xy_real.append([x_mm-(i+0.5)*view_w_mm, y_mm-(j+0.5)*view_w_mm, 2])
                    points_xy.append([i, j, 2])
                elif x_mm - (i + 0.5) * w * calibration < center_x and y_mm - (j + 0.5) * h * calibration < center_y:
                    points_xy_real.append([x_mm-(i+0.5)*view_w_mm, y_mm-(j+0.5)*view_w_mm, 3])
                    points_xy.append([i, j, 3])
                elif x_mm - (i + 0.5) * w * calibration < center_x and y_mm - (j + 0.5) * h * calibration > center_y:
                    points_xy_real.append([x_mm-(i+0.5)*view_w_mm, y_mm-(j+0.5)*view_w_mm, 4])
                    points_xy.append([i, j, 4])

    return points_4, points_xy, points_xy_real, number_x, number_y
