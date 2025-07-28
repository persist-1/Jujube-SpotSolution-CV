   
        # self.iou_slider.valueChanged.connect(lambda x: self.changeValue(x, 'iou_slider'))  # iou 参数条
        # self.conf_slider.valueChanged.connect(lambda x: self.changeValue(x, 'conf_slider'))  # conf 参数条
        # self.line_slider.valueChanged.connect(lambda x: self.changeValue(x, 'line_slider'))  # line 宽度条
        # self.sort_slider.valueChanged.connect(lambda x: self.changeValue(x, 'sort_slider'))  # 分拣阈值条     滑条数值变化时顺便检查checkbox状态,就不额外写槽函数了
        # self.conveyor_value.valueChanged.connect(lambda x: self.changeValue(x, 'conveyor_value'))  # 传送带速度
        # self.LED_value.valueChanged.connect(lambda x: self.changeValue(x, 'LED_value'))  # LED灯亮度

    # def changeValue(self, x, flag):
    #     ### 滑条部分
    #     self.params_dict_cam = {}
    #     self.params_dict_cmd = {}
    #     ########################################################################################################### cam相关 滑条数值获取
    #     if flag == 'iou_slider':
    #         self.iou_num = x / 100 # 原值1-99 处理后为0.01-0.99
    #         self.params_dict_cam['iou_num'] = self.iou_num
            
    #     elif flag == 'conf_slider':
    #         self.conf_num = x / 100 # 原值1-99 处理后为0.01-0.99
    #         self.params_dict_cam['conf_num'] = self.conf_num

    #     elif flag == 'line_slider':
    #         self.line_num = x / 10 # 原值10-50 处理后为1-5 thickness需要int类型,留到counter部分转化
    #         self.params_dict_cam['line_num'] = self.line_num
            
    #     elif flag == 'sort_slider':
    #         self.sort_num = x / 100 # 原值10-90 处理后为0.1-0.9 thickness需要int类型,留到counter部分转化
    #         self.params_dict_cam['sort_num'] = self.sort_num
    #     ########################################################################################################### cmd相关 滑条数值获取
    #     elif flag == 'conveyor_value':
    #         self.conveyor_num = x * 10 # 原值0-99 处理后为9-990
    #         self.params_dict_cmd['conveyor_ctrl'] = self.conveyor_num
            
    #     elif flag== "LED_value":
    #         self.LED_num = x * 10 ### 990 - (x * 10) # 原值0-99 处理后为990-0
    #         self.params_dict_cmd['led_ctrl'] = self.LED_num
        
    #     else:
    #         pass
    #     ###########################################################################################################