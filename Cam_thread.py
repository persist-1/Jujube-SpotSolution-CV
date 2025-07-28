### 三方库
import socket
import threading
import cv2
import numpy as np
from PIL import Image
import io
import time
import random
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QDialog,QPushButton
from PySide6.QtGui import QIcon, QPixmap, QImage, QMouseEvent, QGuiApplication, QColor, QEnterEvent, Qt
from PySide6.QtCore import QPoint, QFile, QTimer, QEventLoop, QThread, QPropertyAnimation, QEasingCurve, \
    QParallelAnimationGroup, Signal, QRect,QDateTime, Slot
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import torch
from ultralytics import YOLO
from ultralytics import solutions
import os
import sys
import traceback
# 设置环境变量
os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'
# 禁用ultralytics自动更新和下载
os.environ['ULTRALYTICS_SKIP_PACKAGE_CHECK'] = '1'
os.environ['ULTRALYTICS_SKIP_DOWNLOAD'] = '1'
# 禁用模型自动下载
os.environ['ULTRALYTICS_SKIP_MODEL_DOWNLOAD'] = '1'
# 禁用object_counter自动下载
os.environ['ULTRALYTICS_SKIP_COUNTER_DOWNLOAD'] = '1'
### 本地库
from Global_info import _init, get_value,set_value

class CamThread(QThread):
    send_output_img = Signal(np.ndarray)
    
    # 添加新的信号用于接收参数更新
    receive_params = Signal(dict)
    
    def __init__(self, Cam,parent=None):
        # 初始化线程，传入摄像头设备编号
        QThread.__init__(self, parent)
        self.processIP = None
        self.processPort = None
        self.processCam = Cam #是 1 还是 2 摄像头,值就是整形1或2

        if os.path.exists(r"models\best.pt"):
            self.model=YOLO(r"models\best.pt")
            self.model_path=r"models\best.pt"
        else:
            print("模型不存在，请重新下载")
            
        self.model=self.model.cpu() # 默认加载模型到CPU

        self.iou_num=0.5 #默认yolo检测配置
        self.conf_num=0.5
        self.line_num=1
        self.sort_num=0.5

        self.yolo_text="" # 用于在图片上覆写参数

        self.img_init_flag = False # 图传开始标志位，用于标识是否开始传输图片

        self.s=None
        self.conn=None
        self.addr=None
        
        # 初始化计数器标志
        self.counter_init_flag = False
        self.counter = None
        self.counter_text = ""

        # 初始化图像相关参数
        self.origin_img=None
        self.img_shape =()

        # 初始化计数值
        self.in_count = 0
        self.out_count = 0
        self.classwise_counts = {}
        
        # 计数模式："IN"、"OUT"或"BOTH"(默认)
        self.count_mode = "IN"
        
        # 检测线颜色状态
        self.line_color = (225,105,65)  # BGR 默认 罗马蓝
        self.line_color_timer = None  # 用于恢复线颜色的计时器
        
        # 连接信号到槽函数
        self.receive_params.connect(self.update_from_signal)
        
        # 仍然保留定时器用于其他功能
        self.timer = threading.Timer(0.7, self.update_params)
        self.timer.start()
        
    @Slot(dict)
    def update_from_signal(self, params_dict):
        """接收从主线程发送的参数更新"""
        # 更新参数
        if 'iou_num' in params_dict:
            self.iou_num = params_dict['iou_num']
        if 'conf_num' in params_dict:
            self.conf_num = params_dict['conf_num']
        if 'line_num' in params_dict:
            self.line_num = params_dict['line_num']
        if 'sort_num' in params_dict:
            self.sort_num = params_dict['sort_num']
        if 'count_mode' in params_dict and params_dict['count_mode'] in ["IN", "OUT", "BOTH"]:
            self.count_mode = params_dict['count_mode']
            print(f"计数模式已更新为: {self.count_mode}")
                
        # 更新计数器的区域点
        if self.counter_init_flag:
            w, h = self.img_shape  # img_shape 是一个包含图像宽度和高度的元组 (width, height)
            # 使用sort_num值来计算计数线的水平位置，sort_num范围是0.1-0.9
            new_x = int(w * self.sort_num)
            self.line_points = [(new_x, 0), (new_x, h)]  # 使用图像的宽度和高度来设置计数线
            self.counter.region = self.line_points
        
    def run(self):
        try:
            self.processIP = get_value(f"IP{self.processCam}")
            self.processPort = get_value(f"Port{self.processCam}")
            print(f"{self.processCam}号摄像头正在连接... \n---IP{self.processCam}\n---Port{self.processCam}")
            self.TCP_handle(self.processIP, self.processPort) #因为删减了UDP,所以这里直接用TCP,主要是留个UDP太鸡肋了,所以全用TCP吧
        except Exception as e:
            print(f"线程运行出错: {e}")
        finally:
            print(f"camThread{self.processCam}线程已终止")
            if self.s:
                self.s.close()
                self.timer.cancel()
                self.quit()
            self.finished.emit()  # 发送结束信号
    def init_adjust_counter(self, img_shape):
        w, h = img_shape  # img_shape 是一个包含图像宽度和高度的元组 (width, height)
        # 使用sort_num值来计算计数线的水平位置，sort_num范围是0.1-0.9
        new_x = int(w * self.sort_num)
        self.line_points = [(new_x, 0), (new_x, h)]  # 使用图像的宽度和高度来设置计数线
        
        # 保存当前计数值（如果已有计数器）
        saved_in_count = 0
        saved_out_count = 0
        saved_classwise_counts = {}
        saved_counted_ids = []
        
        if self.counter:
            # 保存现有计数器的计数值
            saved_in_count = self.counter.in_count
            saved_out_count = self.counter.out_count
            saved_classwise_counts = self.counter.classwise_counts.copy() if hasattr(self.counter, 'classwise_counts') else {}
            saved_counted_ids = self.counter.counted_ids.copy() if hasattr(self.counter, 'counted_ids') else []
        
        # 根据计数模式设置计数方向
        count_in = self.count_mode in ["IN", "BOTH"]
        count_out = self.count_mode in ["OUT", "BOTH"]
        
        # 初始化对象计数器
        self.counter = solutions.ObjectCounter(
            show=False, 
            verbose=False,
            region=self.line_points, # 检测线位置
            line_width=1, # 检测线宽度
            model=self.model_path,
            iou=self.iou_num, 
            conf=self.conf_num,
            classes=[0,1],   #0好 1坏
            show_out=False,
            count_in=count_in,
            count_out=count_out
        )
        
        # 恢复计数值
        if saved_in_count > 0 or saved_out_count > 0 or saved_classwise_counts:
            self.counter.in_count = saved_in_count
            self.counter.out_count = saved_out_count
            
            # 恢复类别计数
            if saved_classwise_counts:
                self.counter.classwise_counts = saved_classwise_counts
            
            # 恢复已计数的ID列表
            if saved_counted_ids:
                self.counter.counted_ids = saved_counted_ids
                
            print(f"计数器已重新初始化，保留了现有计数：IN={saved_in_count}, OUT={saved_out_count}")
        
        # 更新计数文本
        self.update_counter_text()
 
    def TCP_handle(self,processIP, processPort):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 创建一个TCP套接字
        self.s.bind((processIP, int(processPort)))  # 绑定套接字到IP地址和端口
        self.s.listen(1)  # 开始监听
        print(f"TCP  套接字配置已完成\nIP:{processIP}\nPort:{processPort}\n随时监听...")

        self.s.settimeout(5) # 设置超时时间为5秒
        try:
            self.conn, self.addr = self.s.accept()
            self.conn.settimeout(5) ## 为了应对物联网设备因断电等异常导致的套接字连接存在但无法使用的情况
            print("连接已建立:", self.addr)
        except socket.timeout:
            print("等待连接超时，继续检查配置")
            self.s.close()
            return 404 #连接不理想(其它进程)则断开
        
        handshake = self.conn.recv(1024).decode('utf-8') # 握手过程
        if handshake == "ESP32cam":
            print("握手成功，开始接收图像数据")
            self.conn.sendall("ok".encode('utf-8'))
        else: # 握手失败的处理 [重连]
            num = round(random.uniform(0, 3), 1) #random a和b之间的随机浮点数,round 四舍五入到小数点后一位
            print(f"无效的握手信号，断开连接")
            self.conn.close()
            return 404 #连接不理想(其它进程)则断开
        while not self.isInterruptionRequested():
            try:
                fps = 0
                start_time = time.time()
                # 接收图像数据大小信息，并启动超时计时器
                data = self.conn.recv(4)
                if len(data) < 4:
                    print("图像大小信息接收失败")
                    break
                image_size = int.from_bytes(data, 'little') # print(f"图像大小:{image_size} ", end='', flush=True)
                # 接收图像数据
                data_received = b'' 
                while len(data_received) < image_size:
                    packet = self.conn.recv(image_size - len(data_received))
                    if not packet :  #or len(packet)<1000
                        print("图像数据包接收失败")
                        break
                    data_received += packet
                # 将接收到的数据转换为图像
                image = Image.open(io.BytesIO(data_received))
                img = np.asarray(image)
                img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
                self.img_shape = img.shape[1], img.shape[0]  # 获取图像的宽度和高度 (width, height)
                # 第一次运行时，初始化计数器
                if not self.counter_init_flag: 
                    self.init_adjust_counter(self.img_shape)
                    self.counter_init_flag = True #初始化标识
                # 始终保存原始图像副本，用于测试
                self.origin_img = img.copy()
                # 计算帧率
                end_time = time.time()
                elapsed_time = end_time - start_time
                start_time = end_time
                fps = 1 / elapsed_time
                fps_text=f"FPS:{fps:.1f}" 
                # 切换推理设备
                if get_value("shot_status")=="CPU": # CPU推理
                    self.model.cpu()
                    set_value("shot_status","default")
                if get_value("shot_status")=="GPU": # GPU单精度推理
                    try:self.model.cuda()
                    except:
                        print("GPU推理失败，切换至CPU")
                        # set_value("torch_device_info"," ")
                    set_value("shot_status","default")

                if get_value("yolo") == "yes": 
                    # 调用yolo推理
                    if get_value("yolo_counter")=="yes" and self.counter_init_flag:
                        _ = self.counter.count(self.origin_img)
                        # 更新计数文本
                        self.update_counter_text()
                    
                    # 进行普通预测
                    results = self.model.predict(img, show=False, verbose=False, iou=self.iou_num, conf=self.conf_num)
                     # 遍历检测结果
                    for result in results:
                        # 获取每个检测到的对象的边界框、标签和置信度
                        boxes = result.boxes
                        for box in boxes:
                            # 获取边界框坐标
                            x1, y1, x2, y2 = box.xyxy[0]
                            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                            # 获取标签和置信度
                            label = box.cls[0].item() 
                            confidence = box.conf[0]
                            
                            # 在图像上绘制边界框和标签，以及直径
                            cv2.rectangle(img, (x1, y1), (x2, y2), (0,255,127), thickness=int(self.line_num),lineType=cv2.LINE_AA)
                            cv2.putText(img, f'{self.model.names[label]} {confidence:.2f}', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (148,0,211), 2)
                            
                if get_value("yolo_re")=="yes": ### 参数信息绘制    puttext中org需要整数...
                    self.yolo_text=f"IOU:{self.iou_num}  Conf:{self.conf_num}  Line_width:{self.line_num}  Sort_loc:{self.sort_num}"
                    cv2.putText(img, fps_text, (int(img.shape[1]*0.01), int(img.shape[0]*0.08)), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2, cv2.LINE_AA) # FPS展示
                    cv2.putText(img, self.yolo_text, (int(img.shape[1]*0.01), int(img.shape[0]*0.04)), cv2.FONT_HERSHEY_SIMPLEX ,0.9, (237 ,149 ,100), 2, cv2.LINE_AA) # yolo参数展示
                    cv2.putText(img, f"device:{get_value('which_device')}", (int(img.shape[1]*0.01), int(img.shape[0]*0.98)), cv2.FONT_HERSHEY_SIMPLEX ,0.9, (0,69,255), 2, cv2.LINE_AA) # 推理设备展示
                    
                    
                    # 如果启用了计数功能，显示计数结果
                    if get_value("yolo_counter")=="yes" and self.counter_init_flag:
                        cv2.putText(img, self.counter_text, (int(img.shape[1]*0.01), int(img.shape[0]*0.12)), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 165, 255), 2, cv2.LINE_AA) # 计数结果展示
                        cv2.line(img, 
                                    (self.line_points[0][0], self.line_points[0][1]), 
                                    (self.line_points[1][0], self.line_points[1][1]), 
                                    color=self.line_color,  # 使用动态颜色
                                    thickness=2,
                                    lineType=cv2.LINE_AA)
                   
                self.send_output_img.emit(img) ### 发送信号
            except Exception as e:
                print(f"TCP监听出错:{e}")
                
                
                # 获取堆栈跟踪信息
                tb = e.__traceback__
                traceback.print_tb(tb)
                
                self.s.close()
                break
        print("关闭TCP监听...")
        self.s.close()
        self.quit()  # 请求退出事件循环

    def change_line_color(self, color=(48, 48, 255), duration=0.2):
        """临时改变检测线的颜色
        
        Args:
            color: 新的颜色，cv是默认BGR，默认为红色 (0, 0, 255)
            duration: 颜色持续时间（秒），默认为0.2秒
        """
        # 保存原来的颜色
        original_color = self.line_color
        # 设置新颜色
        self.line_color = color
        
        # 取消之前的计时器（如果存在）
        if self.line_color_timer is not None and self.line_color_timer.is_alive():
            self.line_color_timer.cancel()
        
        # 创建新的计时器来恢复颜色
        def restore_color():
            self.line_color = original_color
        
        self.line_color_timer = threading.Timer(duration, restore_color)
        self.line_color_timer.daemon = True # 设置为守护线程，这样主线程结束时，定时器线程也会结束
        self.line_color_timer.start()
    
    def update_counter_text(self):
        """更新计数器文本显示"""
        if not self.counter or not hasattr(self.counter, 'in_count') or not hasattr(self.counter, 'out_count'):
            return
            
        # 获取计数器的计数值
        in_count = self.counter.in_count
        out_count = self.counter.out_count
        
        # 检查计数是否有变化（表示有物体通过检测线）
        if hasattr(self, 'prev_in_count') and hasattr(self, 'prev_out_count'):
            if in_count > self.prev_in_count or out_count > self.prev_out_count:
                # 有物体通过检测线，改变线的颜色
                self.change_line_color()
        
        # 构建类别计数文本
        class_counts = []
        if hasattr(self.counter, 'classwise_counts'):
            # 保存之前的good类别计数，用于检测变化
            prev_good_in_count = 0
            if hasattr(self, 'prev_good_in_count'):
                prev_good_in_count = self.prev_good_in_count
            
            for cls_name, counts in self.counter.classwise_counts.items():
                class_count_text = f"{cls_name}: "
                if self.count_mode == "IN" or self.count_mode == "BOTH":
                    class_count_text += f"IN={counts['IN']} "
                if self.count_mode == "OUT" or self.count_mode == "BOTH":
                    class_count_text += f"OUT={counts['OUT']}"
                class_counts.append(class_count_text.strip())
        
        # 构建总计数文本
        total_text = "Total: "
        if self.count_mode == "IN" or self.count_mode == "BOTH":
            total_text += f"IN={in_count} "
        if self.count_mode == "OUT" or self.count_mode == "BOTH":
            total_text += f"OUT={out_count}"
        
        # 添加当前计数模式信息
        mode_text = f"[mode: {self.count_mode}]"
        
        # 合并所有计数文本
        if class_counts:
            self.counter_text = mode_text + " " + total_text + " | " + " | ".join(class_counts)
        else:
            self.counter_text = mode_text + " " + total_text

        # 直接从 counter 对象获取计数
        if self.counter and hasattr(self.counter, 'classwise_counts'):
            # good 类别计数
            good_counts = self.counter.classwise_counts.get('good', {'IN': 0, 'OUT': 0})
            good_in_count = good_counts.get('IN', 0)
            good_out_count = good_counts.get('OUT', 0)
            
            # bad 类别计数
            bad_counts = self.counter.classwise_counts.get('bad', {'IN': 0, 'OUT': 0})
            bad_in_count = bad_counts.get('IN', 0)
            bad_out_count = bad_counts.get('OUT', 0)
            
            # 检查good类别计数是否增加，如果增加则设置全局变量通知Cmd_thread发送select命令
            if hasattr(self, 'prev_good_in_count') and good_in_count > self.prev_good_in_count:
                print(f"检测到'good'类别计数增加: {self.prev_good_in_count} -> {good_in_count}")
                # 设置全局变量，通知Cmd_thread发送select命令
                set_value('select_trigger', 'yes')
                # 临时改变线的颜色为绿色，表示检测到好的产品
                # self.change_line_color(color=(0, 255, 0), duration=0.5)
            
            # 保存当前good类别计数，用于下次比较
            self.prev_good_in_count = good_in_count
            
            # 简易全局变量更新
            set_value('jujube_good_num', good_in_count)
            set_value('jujube_bad_num', bad_in_count)
        
        # 保存当前计数值，用于下次比较
        self.prev_in_count = in_count
        self.prev_out_count = out_count
    def update_params(self):
        # 其它更新参数
        pass
        
        # 检查线程是否被请求中断，如果是则不再设置新的定时器
        if self.isInterruptionRequested():
            return
        # 重新设置定时器，以实现周期性调用
        if hasattr(self, 'timer'):
            self.timer.cancel()  # 取消之前的定时器
        self.timer = threading.Timer(0.9, self.update_params)
        self.timer.daemon = True  # 设置为守护线程，这样主线程结束时，定时器线程也会结束
        self.timer.start()




