# -*- encoding: utf-8 -*-
"""
@Description:
扫描过程中的数据存储
@File    :   data.py
@Time    :   2024/07/16
@Author  :   Li QingHao
@Version :   2.0
@Time_END :  最后修改时间：
@Developers_END :  最后修改作者：
"""
import os
from datetime import datetime

from DataSaver.Graph import Graph_slide


# 解析数据
class data_processing:
    def __init__(self, code, numberw, numberh):
        self.PP_code = None
        self.numberw = numberw
        self.numberh = numberh

        #
        self.G = Graph_slide(code)

    def Save_data_1(self, code, label):
        # 录入数据库
        # 一级
        data = {'Code': code, 'label': label}
        root_id = self.G.add_node(data)
        data = {'root ID': root_id}
        self.G.set_attr_node(root_id, data)
        return root_id

    def Save_data_2(self, root_id, multiple, path, path_slide):
        # 录入数据库
        # 二级
        Code = multiple
        data = {}
        parent_code = self.G.get_node_info(root_id)['Data']['Code']
        data['Code'] = parent_code + '_' + Code
        data['label'] = Code
        data['视野数量'] = self.numberw * self.numberh
        data['视野长宽'] = [self.numberw, self.numberh]
        data['Image'] = path
        data['Image_slide'] = path_slide
        self.PP_code = self.G.add_node(data, root_id)
        return self.PP_code

    def Save_data_3(self, ID, Z, XY, point_xy_real, path,
                    formatted_a):
        try:
            # 录入数据库
            # 三级节点(多少张图就多少个)

            data = {}
            data['Code'] = 'Img' + ID + '_' + str(formatted_a)
            data['label'] = data['Code']
            data['Date'] = str(datetime.now())
            data['Pos_XY'] = [XY[0], XY[1]]
            data['Pos_XY_real'] = point_xy_real
            data['Pos_Z'] = [Z]
            data['Desc'] = '区域扫描'
            data['Image'] = path

            unique_id = self.G.add_node(data, self.PP_code)

        except Exception as e:
            with open("log.txt", "a") as log_file:
                log_file.write(str(e))

    def Save(self, path, uuid):
        folder_path = os.path.join(path)
        if not os.path.exists(folder_path):
            # 如果路径不存在，则创建文件夹
            os.makedirs(folder_path)
        self.G.save('./data/' + uuid + '/' + uuid + '.dat')
