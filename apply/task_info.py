

def apply_task_info(config_info):
    task_info = {}
    if config_info['Microscope']['sys']['当前系统'] == 'single':
        task_info = {
            'sys': config_info['Microscope']['sys']['当前系统'],
            'Multiple': config_info['Microscope']['single']['单镜头倍数'],
            'FocusMode': config_info['Microscope']['single']['单镜头对焦方式'],
            'center_x': float(config_info['Microscope']['single']['单镜头扫描中心xy']['x']),
            'center_y': float(config_info['Microscope']['single']['单镜头扫描中心xy']['y']),
            'region_w': int(config_info['Microscope']['single']['单镜头扫描区域']['w']),
            'region_h': int(config_info['Microscope']['single']['单镜头扫描区域']['h']),
            'calibration': float(config_info['Camera']['single']['单镜头标定']),
            'zpos_start': float(config_info['Microscope']['single']['对焦经验值单镜头']),
            'focu_number': int(config_info['Microscope']['single']['单镜头对焦步数']),
            'focu_size': float(config_info['Microscope']['single']['单镜头对焦分辨率']),
            'ImageStitchSize': int(config_info['ImageSaver']['imagestitchsize']),
            'fcous_Gap': int(config_info['Microscope']['single']['单镜头隔点对焦步长']),
            'Xend': float(config_info['Microscope']['sys']['xend']),
            'Yend': float(config_info['Microscope']['sys']['yend']),
            'Yend': float(config_info['Microscope']['sys']['scanmode']),
            'savepath': config_info['ImageSaver']['savepath']
        }
    elif config_info['Microscope']['sys']['当前系统'] == 'double':
        boxes = []
        if config_info['Task']['box_1']:
            boxes.append(1)
        if config_info['Task']['box_2']:
            boxes.append(2)
        if config_info['Task']['box_3']:
            boxes.append(3)
        if config_info['Task']['box_4']:
            boxes.append(4)
        task_info = {
            'sys': config_info['Microscope']['sys']['当前系统'],
            'scanmode': config_info['Microscope']['sys']['scanmode'],
            'scanmultiple': config_info['Microscope']['sys']['scanmultiple'],
            'Multiple_low': config_info['Microscope']['low']['低倍倍数'],
            'Multiple_high': config_info['Microscope']['high']['高倍倍数'],
            'FocusMode_low': config_info['Microscope']['low']['低倍对焦方式'],
            'FocusMode_high': config_info['Microscope']['high']['高倍对焦方式'],
            'center_x_low': float(config_info['Microscope']['low']['低倍扫描中心xy']['x']),
            'center_y_low': float(config_info['Microscope']['low']['低倍扫描中心xy']['y']),
            'center_x_high': float(config_info['Microscope']['high']['高倍扫描中心xy']['x']),
            'center_y_high': float(config_info['Microscope']['high']['高倍扫描中心xy']['y']),
            'region_w_low': int(config_info['Microscope']['low']['低倍扫描区域']['w']),
            'region_h_low': int(config_info['Microscope']['low']['低倍扫描区域']['h']),
            'region_w_high': int(config_info['Microscope']['high']['高倍扫描区域']['w']),
            'region_h_high': int(config_info['Microscope']['high']['高倍扫描区域']['h']),
            'calibration_low': float(config_info['Camera']['low']['低倍标定']),
            'calibration_high': float(config_info['Camera']['high']['高倍标定']),
            'zpos_start_low': float(config_info['Microscope']['low']['对焦经验值低倍']),
            'zpos_start_high': float(config_info['Microscope']['high']['对焦经验值高倍']),
            'focu_number_low': int(config_info['Microscope']['low']['低倍对焦步数']),
            'focu_number_high': int(config_info['Microscope']['high']['高倍对焦步数']),
            'focu_size_low': float(config_info['Microscope']['low']['低倍对焦分辨率']),
            'focu_size_high': float(config_info['Microscope']['high']['高倍对焦分辨率']),
            'ImageStitchSize': int(config_info['ImageSaver']['imagestitchsize']),
            'fcous_Gap_low': int(config_info['Microscope']['low']['低倍隔点对焦步长']),
            'fcous_Gap_high': int(config_info['Microscope']['high']['高倍隔点对焦步长']),
            'Xend': float(config_info['Microscope']['sys']['xend']),
            'Yend': float(config_info['Microscope']['sys']['yend']),
            'lens_gap_x': float(config_info['Microscope']['sys']['lensgapx']),
            'lens_gap_y': float(config_info['Microscope']['sys']['lensgapy']),
            'savepath': config_info['ImageSaver']['savepath'],
            'boxes': boxes,
            'slidenumber': config_info['Task']['slidenumber']

        }
    return task_info
