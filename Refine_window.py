### 三方库
import sys
import random
import threading
import wmi
import time
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QDialog,QPushButton
from PySide6.QtGui import QIcon, QPixmap, QImage, QMouseEvent, QGuiApplication, QColor, QEnterEvent, Qt
from PySide6.QtCore import QPoint, QFile, QTimer, QEventLoop, QThread, QPropertyAnimation, QEasingCurve, \
    QParallelAnimationGroup, Signal, QRect
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import cv2
import numpy as np
import os
import ctypes
import torch
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("jujuju_blackpatch") #防任务栏图标异常，管用是真的，解释在最后，这个id可以是任意非重合其它appid的字符串(大概...)
### 本地库
from Ui_jujube import Ui_Mainbody ##### 主体UI导入
from custom_grips import CustomGrip ##### 拖动栏UI导入
from Global_info import _init, get_value,set_value ##### 全局变量导入
from Cam_thread import CamThread ##### 摄像头线程导入
from Cmd_thread import CmdThread ##### 命令单元线程导入


### 全局预设
WIDTH_LEFT_BOX_STANDARD = 85
WIDTH_LEFT_BOX_EXTENDED = 180

_init()
set_value('IPcam', '0.0.0.0')# 摄像头1默认配置
set_value('Portcam', 53002)

set_value('IPcmd', '0.0.0.0')# 命令单元默认配置
set_value('Portcmd', 53005)


set_value("yolo","no")
set_value("yolo_re","no")
set_value("yolo_counter","no")
set_value("which_device","default CPU")
class CustomUI(QWidget,Ui_Mainbody): #
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        ## 关闭系统标题栏
        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint | Qt.WindowSystemMenuHint | Qt.WindowMinimizeButtonHint| Qt.WindowMaximizeButtonHint) 
        #self.setAttribute(Qt.WA_TranslucentBackground) # 透明背景 ###| Qt.FramelessWindowHint | Qt.WindowSystemMenuHint | Qt.WindowMinimizeButtonHint| Qt.WindowMaximizeButtonHint
        
        ## 连接WMI
        self.wmi_obj = wmi.WMI()
        ## 中间栏的展开标识的初始配置
        self.CAMBOX=False
        self.YOLOBOX=False
        self.LOGBOX=False
        self.INFOBOX=False
        self.middleboxStep=0 
        
        ## 子线程初始化
        self.CamThread1 = CamThread("cam")# 初始化线程
        self.CmdThread= CmdThread()

        ## 为lineedit设置默认已经输入字符
        self.IPcam.setText("0.0.0.0") 
        self.Portcam.setText("53002")
        self.IPcmd.setText("0.0.0.0")
        self.Portcmd.setText("53005")
        
        ## yolo相关参数初始值
        self.iou_num=0.5
        self.conf_num=0.5
        self.line_num=2
        self.sort_num=0.5
        self.show_yolo_re.setEnabled(False) # 默认关闭yolo_re 后续当yolo应用时会启用
        self.params_dict_cam = {}
        ## 命令单元相关初始值
        self.conveyor_num=0
        self.LED_num=0 # 阳极驱动
        self.params_dict_cmd = {}

        ## 按钮[最小化, 最大化|还原, 关闭程序]
        self.minimizeButton.clicked.connect(self.showMinimized)  # 最小化
        self.maximizeButton.clicked.connect(self.max_restore)  # 最大化|还原
        self.closeButton.clicked.connect(self.sys_over)  # 关闭程序

        ## 按钮 [框架展开/关闭]
        self.menu_btn.clicked.connect(self.leftbox_transition)  # 左侧栏栏展开/关闭
        self.camera_btn.clicked.connect(lambda: self.middlebox_transition("cam_settings"))  # 中心栏展开/关闭
        self.yolo_btn.clicked.connect(lambda: self.middlebox_transition("yolo_settings"))  # 中心栏展开/关闭
        self.log_btn.clicked.connect(lambda: self.middlebox_transition("log_show"))  # 中心栏展开/关闭
        self.info_btn.clicked.connect(lambda: self.middlebox_transition("our_info"))  # 中心栏展开/关闭
        

        ## 按钮与滑条 [功能/参数]
        self.cam_set1.clicked.connect(lambda : self.camConfig("1")) #摄像头1配置
        self.cam_stop1.clicked.connect(lambda : self.camConfig("1stop")) #摄像头1停止

        self.cmd_set.clicked.connect(lambda : self.cmdConfig("start")) #命令单元配置
        self.cmd_stop.clicked.connect(lambda : self.cmdConfig("stop")) #命令单元停止

        self.show_yolo.clicked.connect(lambda x: self.cam_yolo_show_items()) # 展示yolo检测结果 #checkbox被点击只是会触发变量更新,没别的作用
        self.show_yolo_re.clicked.connect(lambda x: self.cam_yolo_show_items()) # 覆写yolo检测结果于图片

        self.yolo_counter.clicked.connect(lambda x: self.cmd_items()) # 计数开启
        self.jujube_select.clicked.connect(lambda x: self.cmd_items())  # 分拣开启

        self.CPU_shot.clicked.connect(lambda : self.device_choose()) # radiobutton被点击则触发推理设备选择与启用的判断
        self.GPU_shot.clicked.connect(lambda : self.device_choose())

        # 当前时间戳
        self.current_time = time.time()
        ## 信号驱动
        # 子线程->主线程
        self.CamThread1.send_output_img.connect(lambda x: self.showImg(x, self.showimg_left)) #其中初始化里的对象和信号槽都是不必要的，因为后期都会覆盖重构，放这里只是提示有这个东西，删了也不影响功能
        # 子线程->子线程
        # self.CamThread1.send_jujube_info.connect(lambda x:self.TimeMatch_thread.process_data(x)) 
        
        # ## 更新变量
        self.timer = threading.Timer(1.2, self.update_params)
        self.timer.start()
    def sys_over(self):
        # 停止定时器
        if hasattr(self, 'timer'):
            self.timer.cancel()

        # 停止摄像头线程
        if hasattr(self, 'CamThread1') and self.CamThread1.isRunning():
            print("正在关闭摄像头线程...")
            self.CamThread1.requestInterruption()
            # 处理挂起的事件，确保中断请求被处理
            QApplication.processEvents()
            # 等待线程终止，最多等待3秒
            if not self.CamThread1.wait(3000):
                print("摄像头线程未能在预期时间内终止")

        # 停止命令单元线程
        if hasattr(self, 'CmdThread') and self.CmdThread.isRunning():
            print("正在关闭命令单元线程...")
            self.CmdThread.requestInterruption()
            # 处理挂起的事件，确保中断请求被处理
            QApplication.processEvents()
            # 等待线程终止，最多等待3秒
            if not self.CmdThread.wait(3000):
                print("命令单元线程未能在预期时间内终止")

        # 使用QApplication.quit()来正确终止应用程序
        QApplication.quit()
    def max_restore(self): # 最大化|还原
        if self.isMaximized():
            self.showNormal()  # 取消最大化, 正常展示
        else:
            self.showMaximized()  # 窗口最大化
    def leftbox_transition(self): # 菜单栏展开/关闭 纯演示效果
        # standard = 90 = WIDTH_LEFT_BOX_STANDARD
        # maxExtend = 180 = WIDTH_LEFT_BOX_EXTENDED
        leftboxStart = self.leftbox.width()
        _IS_EXTENDED = leftboxStart == WIDTH_LEFT_BOX_EXTENDED

        if _IS_EXTENDED:
            leftboxEnd = WIDTH_LEFT_BOX_STANDARD
            self.status_info.setText(u"<--菜单栏关闭-->")
        else:
            leftboxEnd = WIDTH_LEFT_BOX_EXTENDED
            self.status_info.setText(u"<--菜单栏打开-->")
        self.animation_leftbox = QPropertyAnimation(self.leftbox, b"minimumWidth")# animation
        self.animation_leftbox.setDuration(500)  # ms
        self.animation_leftbox.setStartValue(leftboxStart)
        self.animation_leftbox.setEndValue(leftboxEnd)
        self.animation_leftbox.setEasingCurve(QEasingCurve.InOutQuint)
        self.animation_leftbox.start()
    def middlebox_transition(self,box): # 中心栏展开/关闭
        if box=="cam_settings":
            self.CAMBOX=not self.CAMBOX
            if self.CAMBOX:
                middleboxStart=0
                middleboxEnd=240
                self.middleboxStep+=260
            else:
                middleboxStart=240
                middleboxEnd=0
                if self.middleboxStep>0:
                    self.middleboxStep-=260
            self.middlebox.setMinimumWidth(self.middleboxStep)
            self.animation = QPropertyAnimation(self.cam_settings, b"minimumWidth") # 摄像头栏animation
            self.animation.setDuration(400)  # ms
            self.animation.setStartValue(middleboxStart) 
            self.animation.setEndValue(middleboxEnd)
            self.animation.setEasingCurve(QEasingCurve.InOutQuint)
            self.animation.start()
        if box=="yolo_settings":
            self.YOLOBOX=not self.YOLOBOX
            if self.YOLOBOX:
                middleboxStart=0
                middleboxEnd=240
                self.middleboxStep+=260
            else:
                middleboxStart=240
                middleboxEnd=0
                if self.middleboxStep>0:
                    self.middleboxStep-=260
            self.middlebox.setMinimumWidth(self.middleboxStep)
            self.animation = QPropertyAnimation(self.yolo_settings, b"minimumWidth") # yolo配置栏animation
            self.animation.setDuration(400)  # ms
            self.animation.setStartValue(middleboxStart) 
            self.animation.setEndValue(middleboxEnd)
            self.animation.setEasingCurve(QEasingCurve.InOutQuint)
            self.animation.start()
        if box=="log_show":
            self.LOGBOX=not self.LOGBOX
            if self.LOGBOX:
                middleboxStart=0
                middleboxEnd=240
                self.middleboxStep+=260
            else:
                middleboxStart=240
                middleboxEnd=0
                if self.middleboxStep>0:
                    self.middleboxStep-=260
            self.middlebox.setMinimumWidth(self.middleboxStep)
            self.animation = QPropertyAnimation(self.log_show, b"minimumWidth") # 日志信息栏animation
            self.animation.setDuration(400)  # ms
            self.animation.setStartValue(middleboxStart) 
            self.animation.setEndValue(middleboxEnd)
            self.animation.setEasingCurve(QEasingCurve.InOutQuint)
            self.animation.start()
        if box=="our_info":
            self.INFOBOX=not self.INFOBOX
            if self.INFOBOX:
                middleboxStart=0
                middleboxEnd=230
                self.middleboxStep+=260
            else:
                middleboxStart=230
                middleboxEnd=0
                if self.middleboxStep>0:
                    self.middleboxStep-=260
            self.middlebox.setMinimumWidth(self.middleboxStep)
            self.animation = QPropertyAnimation(self.our_info, b"minimumWidth") # 关于我们栏animation
            self.animation.setDuration(400)  # ms
            self.animation.setStartValue(middleboxStart) 
            self.animation.setEndValue(middleboxEnd)
            self.animation.setEasingCurve(QEasingCurve.InOutQuint)
            self.animation.start()
    def camConfig(self,whichCam): # 摄像头配置
        if whichCam=="1": #选择视角1 进行配置
            self.cam_set1.setEnabled(False) #  禁用按钮 最后再启用[5s]
            self.cam_set1.setStyleSheet("background-color: red")
            self.cam_set1.setText("正在规划线程...")

            set_value(f'IPcam', self.IPcam.text()) #将输入框文本获取
            set_value(f'Portcam', self.Portcam.text())

            self.IPcam.setPlaceholderText(f"当前IP:{get_value('IPcam')}")
            self.Portcam.setPlaceholderText(f"当前Port:{get_value('Portcam')}")
            if hasattr(self, 'CamThread1') and self.CamThread1.isRunning():
                print(f"camThread1线程终止中...")
                self.CamThread1.requestInterruption()
                self.CamThread1.wait()  # 等待线程真正结束
            self.CamThread1.send_output_img.disconnect() #解除旧信号与槽
            self.CamThread1 = CamThread("cam")
            self.CamThread1.send_output_img.connect(lambda x: self.showImg(x, self.showimg)) # 重新绑定信号槽
            self.CamThread1.start()
            QTimer.singleShot(5000, lambda:(self.cam_set1.setEnabled(True),self.cam_set1.setStyleSheet(" "),self.cam_set1.setText("启用TCP监听"))) #重新启用按钮
        elif whichCam=="1stop":
            self.cam_stop1.setEnabled(False) #  禁用按钮 最后再启用[2s]
            self.cam_stop1.setStyleSheet("background-color: red")
            self.cam_stop1.setText("正在关闭线程...")
            if hasattr(self, 'CamThread1') and self.CamThread1.isRunning():
                self.CamThread1.requestInterruption()
                self.CamThread1.wait()  # 等待线程真正结束
            self.show_yolo.setChecked(False)
            set_value("yolo","no")
            self.show_yolo_re.setChecked(False)
            set_value("yolo_re","no")
            self.yolo_counter.setChecked(False)
            self.CPU_shot.setChecked(False)
            self.GPU_shot.setChecked(False)
            QTimer.singleShot(2000, lambda:(self.cam_stop1.setEnabled(True),self.cam_stop1.setStyleSheet(" "),self.cam_stop1.setText("结束线程"))) #2S结束,重新启用按钮
    def cmdConfig(self,flag): # 命令单元配置
        if flag == "start":
            self.cmd_set.setEnabled(False) #  禁用按钮 最后再启用[5s]
            self.cmd_set.setStyleSheet("background-color: red")
            self.cmd_set.setText("正在规划线程...")

            set_value(f'IPcmd', self.IPcmd.text()) #将输入框文本获取
            set_value(f'Portcmd', self.Portcmd.text())

            self.IPcmd.setPlaceholderText(f"当前IP:{get_value('IPcmd')}")
            self.Portcmd.setPlaceholderText(f"当前Port:{get_value('Portcmd')}")
            if hasattr(self, 'CmdThread') and self.CmdThread.isRunning():
                print(f"CmdThread线程终止中...")
                self.CmdThread.requestInterruption()
                self.CmdThread.wait()  # 等待线程真正结束
            self.CmdThread = CmdThread()
            self.CmdThread.start()
            QTimer.singleShot(5000, lambda:(self.cmd_set.setEnabled(True),self.cmd_set.setStyleSheet(" "),self.cmd_set.setText("启用TCP监听"))) #重新启用按钮
        elif flag == "stop":
            self.cmd_stop.setEnabled(False) #  禁用按钮 最后再启用[2s]
            self.cmd_stop.setStyleSheet("background-color: red")
            self.cmd_stop.setText("正在关闭线程...")
            if hasattr(self, 'CmdThread') and self.CmdThread.isRunning():
                self.CmdThread.requestInterruption()
                self.CmdThread.wait()  # 等待线程真正结束
            QTimer.singleShot(2000, lambda:(self.cmd_stop.setEnabled(True),self.cmd_stop.setStyleSheet(" "),self.cmd_stop.setText("结束线程"))) #2S结束,重新启用按钮
    def showImg(self,img, label): ### label图片展示
        try:
            img_src = img
            ih, iw, _ = img_src.shape
            w = label.geometry().width()
            h = label.geometry().height()
            # keep original aspect ratio
            if iw / w > ih / h:
                scal = w / iw
                nw = w
                nh = int(scal * ih)
                img_src_ = cv2.resize(img_src, (nw, nh))
            else:
                scal = h / ih
                nw = int(scal * iw)
                nh = h
                img_src_ = cv2.resize(img_src, (nw, nh))

            frame = cv2.cvtColor(img_src_, cv2.COLOR_BGR2RGB)
            img = QImage(frame.data, frame.shape[1], frame.shape[0], frame.shape[2] * frame.shape[1],
                            QImage.Format_RGB888)
            label.setPixmap(QPixmap.fromImage(img))
            #print("S ", end='', flush=True)
        except Exception as e:
            print(repr(e))
        

    def changeValue_new(self):
        ### 滑条部分
        self.params_dict_cam = {}
        self.params_dict_cmd = {}
        ########################################################################################################### cam相关 滑条数值获取
        self.iou_num = self.iou_slider.value()
        self.iou_num = self.iou_num / 100 # 原值1-99 处理后为0.01-0.99
        self.params_dict_cam['iou_num'] = self.iou_num
        
        self.conf_num = self.conf_slider.value()
        self.conf_num = self.conf_num / 100 # 原值1-99 处理后为0.01-0.99
        self.params_dict_cam['conf_num'] = self.conf_num

        self.line_num = self.line_slider.value() # 原值1-99 处理后为1-99
        self.line_num = self.line_num / 10 # 原值10-50 处理后为1-5 thickness需要int类型,留到counter部分转化
        self.params_dict_cam['line_num'] = self.line_num
        
        self.sort_num = self.sort_slider.value() # 原值10-90 处理后为0.1-0.9
        self.sort_num = self.sort_num / 100 # 原值10-90 处理后为0.1-0.9 thickness需要int类型,留到counter部分转化
        self.params_dict_cam['sort_num'] = self.sort_num
        ########################################################################################################### cmd相关 滑条数值获取
        self.conveyor_num = self.conveyor_value.value() # 原值10-90 处理后为0.1-0.9
        self.conveyor_num = self.conveyor_num * 10 # 原值0-99 处理后为9-990
        self.params_dict_cmd['conveyor_ctrl'] = self.conveyor_num
        
        self.LED_num = self.LED_value.value() # 原值10-90 处理后为0.1-0.9
        self.LED_num = self.LED_num * 10 ### 990 - (x * 10) # 原值0-99 处理后为990-0
        self.params_dict_cmd['led_ctrl'] = self.LED_num
        ###########################################################################################################

    def cam_yolo_show_items(self):
        ### YOLO部分 参数应用检测
        if self.show_yolo.isChecked(): 
            set_value("yolo", "yes")
            self.show_yolo_re.setEnabled(True)
            # 启动yolo检测前若没设置推理设备，则默认设置为cpu
            self.GPU_shot.setCheckable(False)
            self.CPU_shot.setChecked(True)
            # self.device_choose()
        else:
            set_value("yolo", "no")
            self.show_yolo_re.setEnabled(False)
            self.show_yolo_re.setChecked(False) #当父checkbox关闭时,子checkbox也关闭，并且消选
        ## 参数展示检测
        if self.show_yolo_re.isChecked(): 
            set_value("yolo_re", "yes") 
        else:
            set_value("yolo_re", "no")
    def cmd_items(self):
        ## 计数启用检测
        if self.yolo_counter.isChecked(): 
            set_value("yolo_counter", "yes")
        else:
            set_value("yolo_counter", "no")
        ### 分拣启用检测
        if self.jujube_select.isChecked():
            set_value("select_mode", "start")
        else:
            set_value("select_mode", "stop")
        

    def device_choose(self): ### 推理设备选择部分
        if self.CPU_shot.isChecked():
            set_value("shot_status","CPU")
            self.processors = self.wmi_obj.Win32_Processor()
            self.Show_device.setText(f"推理设备: \n{self.processors[0].Name}") # 没办法,torch就算用device方法切换cpu,仍然打印出gpu信息,就选个别的库打印cpu信息吧,反正功能上正常就行
            set_value("which_device",self.processors[0].Name)
        elif self.GPU_shot.isChecked(): # 其实直接用else也可以,只是为了可读性
            set_value("shot_status","GPU")
            try: 
                self.Show_device.setText(f"推理设备: \n{torch.cuda.get_device_name(0)}") # 显示设备
                set_value("which_device",torch.cuda.get_device_name(0))
            except: 
                self.GPU_shot.setCheckable(False)
                self.CPU_shot.setChecked(True)
                pass
    
    def update_params(self):
        self.changeValue_new() # 更新参数
        ###########################################################################################################
        # 如果有参数更新，通过信号发送给相应线程
        if self.params_dict_cam and hasattr(self, 'CamThread1'):
            self.CamThread1.receive_params.emit(self.params_dict_cam)
        if self.params_dict_cmd and hasattr(self, 'CmdThread'):
            self.CmdThread.receive_params.emit(self.params_dict_cmd)
        #########################################################################################################
        ## 滑条label展示数值
        self.iou_label.setText(f"IOU阈值: {self.iou_num}") 
        self.conf_label.setText(f"置信度阈值: {self.conf_num}")
        self.line_label.setText(f"边框宽度: {self.line_num}")
        self.sort_label.setText(f"分拣阈值线: {self.sort_num}")
        self.LED_label.setText(f"LED亮度: {self.LED_num/10}%")###setText(f"LED亮度: {(990-self.LED_num)/10}%")
        self.conveyor_label.setText(f"传送带速率: {self.conveyor_num/10}%")
        ######################################################################################################### 
        # 在这里更新其它参数
        self.jujube_status.setText(f"红枣计数:    健康: {str(get_value('jujube_good_num'))}    不健康: {str(get_value('jujube_bad_num'))}")
        set_value("update_params_cmd", "yes")
        # 重新设置定时器，以实现周期性调用
        if hasattr(self, 'timer'):
            self.timer.cancel()  # 取消之前的定时器
        self.timer = threading.Timer(1.2, self.update_params)
        # self.timer.daemon = True  # 设置为守护线程，这样主线程结束时，定时器线程也会结束
        self.timer.start()

            
            




class MyWindow(CustomUI): ### 这个类是继承原窗口ui后，额外增加了窗口行为方法，例如边缘拖动，窗口大小改变，窗口拖动等
    # 定义关闭信号
    closed = Signal()
    def __init__(self):
        super(MyWindow, self).__init__()
        self.center()
        # --- 拖动窗口 改变窗口大小 --- #
        self.left_grip = CustomGrip(self, Qt.LeftEdge)
        self.right_grip = CustomGrip(self, Qt.RightEdge)
        self.top_grip = CustomGrip(self, Qt.TopEdge)
        self.bottom_grip = CustomGrip(self, Qt.BottomEdge)
        # --- 拖动窗口 改变窗口大小 --- #
        self.animation_window = None
    def mousePressEvent(self, event: QMouseEvent) -> None:
        if event.button() == Qt.LeftButton:
            self.mouse_start_pt = event.globalPosition().toPoint()
            self.window_pos = self.frameGeometry().topLeft()
            self.drag = True
    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        if self.drag:
            distance = event.globalPosition().toPoint() - self.mouse_start_pt
            self.move(self.window_pos + distance)
    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        if event.button() == Qt.LeftButton:
            self.drag = False
    def center(self):
        # Pyside6获取屏幕参数
        screen = QGuiApplication.primaryScreen().size()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2,
                  (screen.height() - size.height()) / 2 - 10)
    def resizeEvent(self, event): # 拖动窗口 改变窗口大小
        # Update Size Grips
        self.resizeGrip()

    def resizeGrip(self):
        """ x:  控件左上角在父控件中的x坐标。
            y:  控件左上角在父控件中的y坐标。
            width: 控件的宽度。
            eight: 控件的高度。"""
        self.left_grip.setGeometry(0, 10, 10, self.height())
        self.right_grip.setGeometry(self.width() - 10, 10, 10, self.height())
        self.top_grip.setGeometry(0, 0, self.width(), 10)
        self.bottom_grip.setGeometry(0, self.height() - 10, self.width(), 10)

    def closeEvent(self, event):
        # 停止定时器
        if hasattr(self, 'timer'):
            self.timer.cancel()

        # 停止摄像头线程
        if hasattr(self, 'CamThread1') and self.CamThread1.isRunning():
            print("正在关闭摄像头线程...")
            self.CamThread1.requestInterruption()
            # 处理挂起的事件，确保中断请求被处理
            QApplication.processEvents()
            # 等待线程终止，最多等待3秒
            if not self.CamThread1.wait(3000):
                print("摄像头线程未能在预期时间内终止")

        # 停止命令单元线程
        if hasattr(self, 'CmdThread') and self.CmdThread.isRunning():
            print("正在关闭命令单元线程...")
            self.CmdThread.requestInterruption()
            # 处理挂起的事件，确保中断请求被处理
            QApplication.processEvents()
            # 等待线程终止，最多等待3秒
            if not self.CmdThread.wait(3000):
                print("命令单元线程未能在预期时间内终止")

        event.accept()
    def showEvent(self, event):
        super().showEvent(event)
        if not event.spontaneous():
            # 这里定义显示动画
            self.animation = QPropertyAnimation(self, b"windowOpacity")
            self.animation.setDuration(500)  # 动画时间500毫秒
            self.animation.setStartValue(0)  # 从完全透明开始
            self.animation.setEndValue(1)  # 到完全不透明结束
            self.animation.start()











if __name__ == "__main__":

    # 获取当前文件的绝对路径
    current_file_path = os.path.abspath(__file__)
    # 获取当前文件所在的目录
    current_dir = os.path.dirname(current_file_path)
    print("当前文件的绝对路径:", current_file_path)
    print("当前文件所在的目录:", current_dir)

    app = QApplication(sys.argv)     # app = QApplication([])
    app.setWindowIcon(QIcon(r'images\my_icon\apple_val.jpg'))  # 设置应用程序图标
    apple = MyWindow()
    apple.show()
    # app.exec()
    app.quit()
    sys.exit(app.exec())

"""
    在信号与槽部分一定要分清方法调用和函数对象，捏妈妈的，吃大亏了

    还有一件事, 线程对象重新初始化之前一定要断开旧的信号与槽, 不然99%出问题, 信号铁铁不知道跑哪去了

    还有一件事, 用线程的requestInterruption()方法, 在线程中执行isInterruptionRequested()方法获取中断请求, 别傻乎乎quit()了
    虽然我也不知道为什么...反正好用

    关于任务栏异常和解决，ai的说法：
        ctypes模块来调用Windows API，具体是SetCurrentProcessExplicitAppUserModelID函数。
        这个函数的作用是为当前进程设置一个明确的AppUserModelID。AppUserModelID是Windows 7及以后版本中引入的一个概念，它用于帮助操作系统区分不同的应用程序，
        特别是在任务栏的跳跃列表和通知区域中。
        当你为一个窗口设置了图标（如使用QApplication.setWindowIcon），Windows会尝试为该窗口在任务栏创建一个图标。
        如果Windows无法正确地识别应用程序的身份，它可能会在任务栏中使用默认的图标，而不是你指定的图标，导致出现所谓的“任务栏图标异常”。

    

"""