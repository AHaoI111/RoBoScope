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
import numpy as np

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
    for i in range(int(number_x)):
        if i % 2 == 0:
            for j in range(int(number_y)):
                if x_mm - (i + 0.5) * w * calibration >= center_x and y_mm - (j + 0.5) * h * calibration >= center_y:
                    points_xy_real.append([x_mm - (i + 0.5) * view_w_mm, y_mm - (j + 0.5) * view_w_mm, 1])
                    points_xy.append([i, j, 1])
                elif x_mm - (i + 0.5) * w * calibration >= center_x and y_mm - (j + 0.5) * h * calibration <= center_y:
                    points_xy_real.append([x_mm - (i + 0.5) * view_w_mm, y_mm - (j + 0.5) * view_w_mm, 2])
                    points_xy.append([i, j, 2])
                elif x_mm - (i + 0.5) * w * calibration <= center_x and y_mm - (j + 0.5) * h * calibration <= center_y:
                    points_xy_real.append([x_mm - (i + 0.5) * view_w_mm, y_mm - (j + 0.5) * view_w_mm, 3])
                    points_xy.append([i, j, 3])
                elif x_mm - (i + 0.5) * w * calibration <= center_x and y_mm - (j + 0.5) * h * calibration >= center_y:
                    points_xy_real.append([x_mm - (i + 0.5) * view_w_mm, y_mm - (j + 0.5) * view_w_mm, 4])
                    points_xy.append([i, j, 4])
        else:
            for j in range(int(number_y) - 1, -1, -1):
                if x_mm - (i + 0.5) * w * calibration >= center_x and y_mm - (j + 0.5) * h * calibration >= center_y:
                    points_xy_real.append([x_mm - (i + 0.5) * view_w_mm, y_mm - (j + 0.5) * view_w_mm, 1])
                    points_xy.append([i, j, 1])
                elif x_mm - (i + 0.5) * w * calibration >= center_x and y_mm - (j + 0.5) * h * calibration <= center_y:
                    points_xy_real.append([x_mm - (i + 0.5) * view_w_mm, y_mm - (j + 0.5) * view_w_mm, 2])
                    points_xy.append([i, j, 2])
                elif x_mm - (i + 0.5) * w * calibration <= center_x and y_mm - (j + 0.5) * h * calibration <= center_y:
                    points_xy_real.append([x_mm - (i + 0.5) * view_w_mm, y_mm - (j + 0.5) * view_w_mm, 3])
                    points_xy.append([i, j, 3])
                elif x_mm - (i + 0.5) * w * calibration <= center_x and y_mm - (j + 0.5) * h * calibration >= center_y:
                    points_xy_real.append([x_mm - (i + 0.5) * view_w_mm, y_mm - (j + 0.5) * view_w_mm, 4])
                    points_xy.append([i, j, 4])

    return points_4, points_xy, points_xy_real, number_x, number_y


def swap_farthest_with_first(points):
    distances = [np.sqrt(x ** 2 + y ** 2) for x, y in points]
    farthest_index = np.argmax(distances)
    points[0], points[farthest_index] = points[farthest_index], points[0]
    return points


def sort_by_closeness(points):
    if not points:
        return points

    # 计算点到原点的距离
    def distance_to_origin(point):
        return np.sqrt(point[0] ** 2 + point[1] ** 2)

    # 找到距离原点最远的点作为起点
    start_index = np.argmax([distance_to_origin(p) for p in points])
    sorted_points = [points[start_index]]  # 初始化排序后的点列表
    remaining_points = points[:start_index] + points[start_index + 1:]  # 剩余未排序的点

    # 依次找到距离前一个点最近的点
    while remaining_points:
        last_point = sorted_points[-1]  # 当前最后一个点

        # 找到距离 last_point 最近的点
        closest_index = np.argmin([np.sqrt((p[0] - last_point[0]) ** 2 + (p[1] - last_point[1]) ** 2)
                                   for p in remaining_points])

        closest_point = remaining_points[closest_index]
        sorted_points.append(closest_point)  # 添加到排序后的列表
        remaining_points.pop(closest_index)  # 从剩余点中移除

    return sorted_points