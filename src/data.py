from datetime import datetime


def Save_data_1(Graph_class, ID):
    # 录入数据库
    # 一级
    data = {'Code': ID, 'label': ID}
    root_id = Graph_class.add_node(data)
    return root_id


def Save_data_2(Graph_class,root_id, ID, multiple, Focusing_method, w,h):
    # 录入数据库
    # 二级
    Code = multiple
    data = {}
    parent_code = Graph_class.get_node_info(root_id)['Data']['Code']
    data['Code'] = parent_code + '_' + Code
    data['label'] = Code
    data['对焦方式'] = Focusing_method
    data['视野数量'] = w*h
    # 获取第一个位置的最大值

    data['视野长宽'] = [w, h]
    data['拼接图'] = 'pic\\' + ID + '\\' + ID + '.png'
    PP_code = Graph_class.add_node(data, root_id)
    return PP_code


def Save_data_3(Graph_class, PP_code, ID, Z, a, XY, timesave, results,point_xy_real):
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
    data['Image'] = 'pic\\' + ID + '\\' + timesave + '_' + ID + '_' + str(a) + '.png'
    data['bbox'] = results[0].boxes.xywhn.tolist()
    data['Annotation'] = [int(x) for x in results[0].boxes.cls.tolist()]
    data['Confidence'] = results[0].boxes.conf.tolist()
    unique_id = Graph_class.add_node(data, PP_code)
