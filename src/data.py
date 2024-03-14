from datetime import datetime


def Save_data_1(Graph_class, ID):
    # 录入数据库
    # 一级
    data = {'Code': ID, 'label': ID}
    root_id = Graph_class.add_node(data)
    return root_id


def Save_data_2(Graph_class, root_id, ID, multiple, Focusing_method, w, h):
    # 录入数据库
    # 二级
    Code = multiple
    data = {}
    parent_code = Graph_class.get_node_info(root_id)['Data']['Code']
    data['Code'] = parent_code + '_' + Code
    data['label'] = Code
    data['对焦方式'] = Focusing_method
    data['视野数量'] = w * h
    # 获取第一个位置的最大值

    data['视野长宽'] = [w, h]
    data['Image'] = 'pic\\' + ID + '\\' + multiple + '\\' + ID + '.jpg'
    PP_code = Graph_class.add_node(data, root_id)
    return PP_code


def Save_data_3(Graph_class, PP_code, ID, Z, a, XY, timesave, results, point_xy_real, result_boxes_bacteria,
                result_cls_bacteria, multiple, PixelFormat):
    # 录入数据库
    # 三级节点(多少张图就多少个)
    data = {}
    data['Code'] = 'Img' + ID + '_' + str(a)
    data['label'] = data['Code']
    data['Date'] = str(datetime.now())
    data['Pos_XY'] = [XY[0], XY[1]]
    data['Pos_XY_real'] = point_xy_real
    data['Pos_Z'] = [Z]
    data['Desc'] = '区域扫描'
    data['Image'] = 'pic\\' + ID + '\\' + multiple + '\\' + timesave + '_' + ID + '_' + str(a) + '.' + PixelFormat
    data['bbox_cell'] = results[0].boxes.xyxy.tolist()
    data['bbox_bacteria'] = result_boxes_bacteria
    data['Annotation_cell'] = [int(x) for x in results[0].boxes.cls.tolist()]
    data['Annotation_bacteria'] = result_cls_bacteria
    data['Confidence'] = results[0].boxes.conf.tolist()
    unique_id = Graph_class.add_node(data, PP_code)
