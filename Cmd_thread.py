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
    QParallelAnimationGroup, Signal, QRect,QDateTime,Slot
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import torch
from ultralytics import YOLO
import os
import sys
import traceback
# 设置环境变量
os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'
### 本地库
from Global_info import _init, get_value,set_value

class CmdThread(QThread):

    # 添加新的信号用于接收参数更新
    receive_params = Signal(dict)

    def __init__(self,parent=None):
        # 初始化线程，传入摄像头设备编号
        QThread.__init__(self, parent)
        self.processIP = None
        self.processPort = None

        self.led_val=0
        self.servo_flag="stop"
        self.servo_re_flag="stop"
        self.conveyor_val=0

        self.led_for_choose=False
        self.servo_for_choose=False
        self.servo_re_for_choose=False
        self.conveyor_for_choose=False

        self.s=None ### 套接字相关
        self.conn=None
        self.addr=None

        self.select_mode = "stop"
        self.conn_flag= False
         # 连接信号到槽函数
        self.receive_params.connect(self.update_from_signal)

        # 初始化定时器
        self.timer = threading.Timer(0.7, self.update_params)
        self.timer.start()
    @Slot(dict)
    def update_from_signal(self, params_dict):
        """接收从主线程发送的参数更新"""
        # 更新参数
        if 'conveyor_ctrl' in params_dict:
            self.conveyor_val = params_dict['conveyor_ctrl']
        if 'led_ctrl' in params_dict:
            self.led_val = params_dict['led_ctrl']
        
    def run(self):
        try:
            self.processIP = get_value(f"IPcmd")
            self.processPort = get_value(f"Portcmd")
            print(f"命令单元正在连接... ")
            self.TCP_handle(self.processIP, self.processPort) #因为删减了UDP,所以这里直接用TCP,主要是留个UDP太鸡肋了,所以全用TCP吧
        except Exception as e:
            print(f"命令单元线程运行出错: {e}")
        finally:
            print(f"命令单元线程已终止")
            if self.s:
                self.s.close()
                self.conn_flag= False
            if hasattr(self, 'timer') and self.timer is not None:
                self.timer.cancel()
            self.quit()
            self.finished.emit()  # 发送结束信号
    def TCP_handle(self,processIP, processPort):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 创建一个TCP套接字
        self.s.bind((processIP, int(processPort)))  # 绑定套接字到IP地址和端口
        self.s.listen(1)  # 开始监听
        print(f"TCP  套接字配置已完成\nIP:{processIP}\nPort:{processPort}\n随时监听...")

        self.s.settimeout(5) # 设置超时时间为5秒
        try:
            self.conn, self.addr = self.s.accept()
            ##self.conn.settimeout(5) ## 为了应对物联网设备因断电等异常导致的套接字连接存在但无法使用的情况 但对于命令单元这种非一直收发工作的情况，不适用
            print("连接已建立:", self.addr)
        except socket.timeout:
            print("等待连接超时，继续检查配置")
            self.s.close()
            self.conn_flag= False
            return 404 #连接不理想(其它进程)则断开
        
        handshake = self.conn.recv(1024).decode('utf-8') # 握手过程
        if handshake == "ESP32cmd":
            print("握手成功，开始进行控制通信")
            self.conn.sendall("ok".encode('utf-8'))
            self.conn_flag = True
        else: # 握手失败的处理 [重连]
            num = round(random.uniform(0, 3), 1) #random a和b之间的随机浮点数,round 四舍五入到小数点后一位
            print(f"无效的握手信号，断开连接")
            self.conn.close()
            self.conn_flag = False
            return 404 #连接不理想(其它进程)则断开
        # 添加心跳计时器
        # last_heartbeat_time = time.time()
        
        while not self.isInterruptionRequested():
            try:
                # # 每30秒发送一次心跳包，保持连接活跃
                # current_time = time.time()
                # if current_time - last_heartbeat_time > 30:
                #     if self.conn:
                #         try:
                #             self.conn.sendall("heartbeat;".encode('utf-8'))
                #             print("发送心跳包保持连接")
                            
                #             # 设置短超时等待心跳响应
                #             self.conn.settimeout(2)
                #             try:
                #                 response = self.conn.recv(1024).decode('utf-8')
                #                 # 修复问题1：正确识别下位机的心跳响应
                #                 if response == "heartbeat_ack" or response.startswith("heartbeat_ack"):
                #                     print("收到心跳确认")
                #                 else:
                #                     print(f"收到未知响应: {response}")
                #             except socket.timeout:
                #                 print("心跳响应超时，但继续保持连接")
                #             except Exception as e:
                #                 print(f"接收心跳响应出错: {e}")
                            
                #             # 恢复正常超时设置
                #             self.conn.settimeout(None)
                            
                #         except Exception as e:
                #             print(f"发送心跳包失败: {e}")
                #             # 连接可能已断开，尝试重新建立连接
                #             if self.conn:
                #                 self.conn.close()
                #                 self.conn = None
                #             break
                #     last_heartbeat_time = current_time
                
                # # 短暂休眠，减少CPU使用
                time.sleep(10)
                pass
                
            except Exception as e:
                print(f"命令单元TCP监听出错:{e}")
                            
                # 获取堆栈跟踪信息
                tb = e.__traceback__
                traceback.print_tb(tb)
                
                if self.conn:
                    self.conn.close()
                    self.conn = None
                    self.conn_flag= False
                self.s.close()
                self.conn_flag= False
                break
        print("关闭TCP监听...")
        self.s.close()
        self.conn_flag= False
        self.quit()  # 请求退出事件循环

    def update_params(self):

        self.update_params_cmd = get_value("update_params_cmd") ## 常-更新外设参数
        if self.update_params_cmd=="yes" and self.conn_flag==True:
            self.ctrl_device("led")
            self.ctrl_device("conveyor") 
            set_value("update_params_cmd", "no")
            
        self.select_trigger = get_value("select_trigger") ## 非常-分拣触发
        if self.select_trigger=="yes" and self.conn_flag==True: 
            self.ctrl_device("select")
            set_value("select_trigger", "no")

        # 检查线程是否被请求中断，如果是则不再设置新的定时器
        if self.isInterruptionRequested():
            return
        # 重新设置定时器，以实现周期性调用
        if hasattr(self, 'timer'):
            self.timer.cancel()  # 取消之前的定时器
        self.timer = threading.Timer(0.9, self.update_params)
        self.timer.daemon = True  # 设置为守护线程，这样主线程结束时，定时器线程也会结束
        self.timer.start()

    def ctrl_device(self,select_request=None):
        
        try:
            if self.conn_flag==False:
                print(f"连接状态为断开，不执行设备控制命令[{select_request}]")
            else:
                if select_request =="led":
                    led_cmd = f"led_ctrl{self.led_val};"
                    self.conn.sendall((led_cmd).encode('utf-8')) # 发送led_ctrl命令，更改led亮度
                    print(f"设备控制命令已发送 {led_cmd}")

                if select_request =="conveyor":
                    conveyor_cmd = f"conveyor_ctrl{self.conveyor_val};" # 发送conveyor_ctrl命令，更改传送带转速
                    self.conn.sendall((conveyor_cmd).encode('utf-8'))
                    print(f"设备控制命令已发送 {conveyor_cmd}")

                if select_request =="select":
                    self.select_mode=get_value("select_mode")
                    if self.select_mode=="stop":
                        print("分拣模式为停止，不执行分拣命令")
                        return
                    select_cmd = "select;"
                    self.conn.sendall((select_cmd).encode('utf-8')) # 发送select命令，驱动电磁铁进行分拣
                    print(f"分拣命令已发送 {select_cmd}")

        except Exception as e:
            print(f"发送命令失败: {e}")
            # 标记连接已断开
            self.conn = None
            self.conn_flag= False
        

        

