### 导入封装库
import socket
import network
import time
import random
import machine
from machine import Pin, PWM, Timer

# 配置选项
MAX_RECONNECT_ATTEMPTS = 5  # 最大重连尝试次数
RECONNECT_DELAY = 3  # 重连延迟时间(秒)

# WiFi配置
# 主要WiFi配置
MAIN_SSID = 'HUAWEI_IOT_node'  # 主要WiFi名称
MAIN_PASSWORD = '111gogogo'  # 主要WiFi密码
MAIN_SERVER_IP = '192.168.8.8'  # 主要服务器IP地址
MAIN_SERVER_PORT = 53005  # 主要服务器端口号

# 备用WiFi配置列表
BACKUP_WIFI_LIST = [
    {
        'SSID': 'backup_iot_node',  # 备用WiFi名称1
        'PASSWORD': '111gogogo',  # 备用WiFi密码1
        'SERVER_IP': '192.168.140.225',  # 备用服务器IP地址1
        'SERVER_PORT': 53005  # 备用服务器端口号1
    },
    {
        'SSID': 'backup_iot_node2',  # 备用WiFi名称2
        'PASSWORD': '111gogogo',  # 备用WiFi密码2
        'SERVER_IP': '192.168.140.226',  # 备用服务器IP地址2
        'SERVER_PORT': 53005  # 备用服务器端口号2
    },
    {
        'SSID': 'backup_iot_node3',  # 备用WiFi名称3
        'PASSWORD': '111gogogo',  # 备用WiFi密码3
        'SERVER_IP': '192.168.140.227',  # 备用服务器IP地址3
        'SERVER_PORT': 53005  # 备用服务器端口号3
    }
]

# 当前使用的WiFi配置
SSID = MAIN_SSID
PASSWORD = MAIN_PASSWORD
SERVER_IP = MAIN_SERVER_IP
SERVER_PORT = MAIN_SERVER_PORT

# 是否使用备用WiFi配置
using_backup_wifi = False
# 当前使用的备用WiFi索引（-1表示使用主WiFi）
current_backup_index = -1

# 全局变量
connection_attempts = 0
last_connection_time = 0
led = None  # 照明led
conveyor = None  # 传送带
selector = None  # 分拣继电器
# s = None  # 套接字

###### 扫描并打印详细的附近Wi-Fi信息，检查是否需要使用备用WiFi
def scan_wlan():
    global SSID, PASSWORD, SERVER_IP, SERVER_PORT, using_backup_wifi, current_backup_index
    try:
        wlan = network.WLAN(network.STA_IF)
        wlan.active(False)
        wlan.active(True)
        mac_address = wlan.config('mac')
        print("MAC Address:", mac_address)
        mac_address_hex = ':'.join(['{:02x}'.format(b) for b in mac_address if b != 44])  # 过滤掉非十六进制字符，如逗号
        print("Human-readable MAC Address:", mac_address_hex)
        
        print("正在扫描附近Wi-Fi...")
        nets = wlan.scan()
        print("附近的Wi-Fi信息：")
        
        # 存储所有可用的SSID
        available_ssids = []
        
        for wifi in nets:
            # 检查元素是否为字节串并解码
            ssid = wifi[0].decode('utf-8') if isinstance(wifi[0], bytes) else wifi[0]
            bssid = ':'.join(['{:02x}'.format(b) for b in wifi[1]])
            channel = wifi[2]
            signal = wifi[3]
            
            # 添加到可用SSID列表
            available_ssids.append(ssid)
            
            # 打印所有信息
            print(f"SSID: {ssid}, BSSID: {bssid}, 信道: {channel}, 信号强度: {signal} dBm")
        
        # 首先检查主要SSID是否可用
        if MAIN_SSID in available_ssids:
            print(f"找到主要WiFi: {MAIN_SSID}，使用主要WiFi配置")
            SSID = MAIN_SSID
            PASSWORD = MAIN_PASSWORD
            SERVER_IP = MAIN_SERVER_IP
            SERVER_PORT = MAIN_SERVER_PORT
            using_backup_wifi = False
            current_backup_index = -1
        else:
            # 主要SSID不可用，逐个检查备用WiFi列表
            print(f"未找到主要WiFi: {MAIN_SSID}，开始检查备用WiFi列表")
            found_backup = False
            
            for i, backup_config in enumerate(BACKUP_WIFI_LIST):
                backup_ssid = backup_config['SSID']
                if backup_ssid in available_ssids:
                    print(f"找到备用WiFi[{i+1}]: {backup_ssid}，使用此备用WiFi配置")
                    SSID = backup_config['SSID']
                    PASSWORD = backup_config['PASSWORD']
                    SERVER_IP = backup_config['SERVER_IP']
                    SERVER_PORT = backup_config['SERVER_PORT']
                    using_backup_wifi = True
                    current_backup_index = i
                    found_backup = True
                    break
            
            if not found_backup:
                print("警告：未找到任何可用的WiFi网络，将继续使用主要WiFi配置尝试连接")
                SSID = MAIN_SSID
                PASSWORD = MAIN_PASSWORD
                SERVER_IP = MAIN_SERVER_IP
                SERVER_PORT = MAIN_SERVER_PORT
                using_backup_wifi = False
                current_backup_index = -1
        
        print(f"当前使用的WiFi配置: SSID={SSID}, SERVER_IP={SERVER_IP}, SERVER_PORT={SERVER_PORT}")
        return True
    except Exception as e:
        print(f"Wi-Fi扫描出错: {e}")
        return False

###### 连接到WiFi网络
def connect_wifi():
    global connection_attempts, last_connection_time, SSID, PASSWORD
    
    # 检查是否需要等待重连
    current_time = time.time()
    if current_time - last_connection_time < RECONNECT_DELAY and connection_attempts > 0:
        wait_time = RECONNECT_DELAY - (current_time - last_connection_time)
        if wait_time > 0:
            print(f"等待 {wait_time:.1f} 秒后重试连接...")
            time.sleep(wait_time)
    
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    
    if not wlan.isconnected():
        # 增加连接尝试次数
        connection_attempts += 1
        last_connection_time = time.time()
        
        print(f'正在连接WIFI... (尝试 {connection_attempts}/{MAX_RECONNECT_ATTEMPTS})')
        try:
            wlan.connect(SSID, PASSWORD)  # 连接到指定的WiFi网络
            
            # 设置连接超时
            timeout = 15  # 15秒超时
            start_time = time.time()
            i = 1
            
            while not wlan.isconnected():
                if time.time() - start_time > timeout:
                    print("连接超时！")
                    break
                    
                print(f"正在连接...{i}", end='\r')
                i += 1
                time.sleep(1)  # 每次循环等待1秒
            
            if wlan.isconnected():
                connection_attempts = 0  # 重置连接尝试次数
                print('\nWIFI连接成功!')
                print('WIFI网络配置信息:', wlan.ifconfig())
                return True
            else:
                print("\nWIFI连接失败!")
                if connection_attempts >= MAX_RECONNECT_ATTEMPTS:
                    print(f"已达到最大重连次数({MAX_RECONNECT_ATTEMPTS})，将重置设备...")
                    time.sleep(1)
                    machine.reset()  # 重置设备
                return False
                
        except Exception as e:
            print(f"WIFI连接出错: {e}")
            return False
    else:
        print('WIFI已连接')
        print('WIFI网络配置信息:', wlan.ifconfig())
        return True

###### 初始化相关io
def init_io():
    global led, conveyor, selector  # 声明全局变量
    try:
        led = PWM(Pin(3), freq=20000, duty=1023)  # 分拣照明LED  默认关闭，因为引脚做阴极，即占空比为1023
        conveyor = PWM(Pin(10), freq=20000, duty=0)  # 传送带  默认关闭，因为引脚做阴极，即占空比为1023
        selector = Pin(5, Pin.OUT, value=0)  # 分拣继电器，默认关闭

        print("IO设备初始化成功")
        return True
    except Exception as e:
        print(f'IO设备初始化出错: {e}')
        return False
        
######  led控制方法
def LED_output(i):  # 改变检测时的灯光亮度
    global led  # 声明led为全局变量
    try:
        if 0 <= i <= 1023:  # 检查占空比是否在规定范围内
            led.duty(i)  # 改变LED占空比
            print(f"LED占空比设置为: {i}")
            return True
        else:
            print("占空比超出范围(0-1023)，忽略命令")
            return False
    except Exception as e:
        print(f'LED控制出错: {e}')
        return False

######  传送带控制方法
def Conveyor_output(i): 
    global conveyor  
    try:
        if 0 <= i <= 1023:  # 检查占空比是否在规定范围内
            conveyor.duty(i)  # 改变占空比
            print(f"传送带占空比设置为: {i}")
            return True
        else:
            print("占空比超出范围(0-1023)，忽略命令")
            return False
    except Exception as e:
        print(f'传送带控制出错: {e}')
        return False

###### 分拣控制方法
def select_output():
    global selector  # 声明selector为全局变量
    try:
        # 通电0.2秒后自动断电的定时器回调函数
        def turn_off_selector(timer):
            selector.value(0)
            print("分拣继电器已关闭")
        
        # 激活继电器
        selector.value(1)
        print("分拣继电器已激活，将在0.2秒后关闭")
        
        # 设置定时器，0.2秒后关闭继电器
        timer = Timer(0)
        timer.init(period=200, mode=Timer.ONE_SHOT, callback=turn_off_selector)
        return True
    except Exception as e:
        print(f'分拣继电器控制出错: {e}')
        return False

###### 接收命令并进行其它控制
def rec_cmd():
    # global s  # 声明s为全局变量
    handshake_attempts = 0
    max_handshake_attempts = 10
    
    # 握手服务器
    while handshake_attempts < max_handshake_attempts:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(5)  # 增加超时时间到5秒
            print('正在连接服务器...')
            s.connect((SERVER_IP, SERVER_PORT))
            print('正在握手服务器...')
            
            handshake = "ESP32cmd"  # 发送握手信号
            s.sendall(handshake.encode('utf-8'))
            try:
                confirm = s.recv(1024).decode('utf-8')
                if confirm == "ok":  # 等待服务器发送确认信号
                    print("握手成功，开始接收命令")
                    break
                else:
                    print(f"未收到确认信号，断开连接 (收到: {confirm})")
                    s.close()
                    handshake_attempts += 1
                    time.sleep(1)
            except OSError as e:  # MicroPython使用OSError处理超时
                print(f"等待确认信号超时: {e}")
                s.close()
                handshake_attempts += 1
                time.sleep(1)
        except OSError as e:
            handshake_attempts += 1
            num = round(random.uniform(1, 3), 1)  # random a和b之间的随机浮点数,round 四舍五入到小数点后一位
            print(f"连接失败 ({handshake_attempts}/{max_handshake_attempts}): {e}")
            print(f"{num}s后重试握手...")
            time.sleep(num)
            if s:
                s.close()
        
        if handshake_attempts >= max_handshake_attempts:
            print("达到最大握手尝试次数，返回主循环重新连接WiFi")
            return False
    
    # 接收并处理命令
    try:
        # 设置更长的超时时间，适应上位机的命令发送间隔
        ## s.settimeout(60)  # 设置为60秒超时，足够应对上位机的命令发送间隔
        
        # 发送心跳包的最后时间
        ## last_heartbeat_time = time.time()
        
        # 记录上次接收数据的时间
        last_data_time = time.time()
        
        while True:
            try:
                # 使用非阻塞模式接收数据
                s.setblocking(False)
                try:
                    cmd = s.recv(1024).decode('utf-8')
                    if not cmd:  # 如果接收到空数据，可能是连接已关闭
                        print("接收到空数据，连接可能已关闭")
                        break
                    
                    # 更新上次接收数据的时间
                    last_data_time = time.time()
                    
                    print(f"收到命令: {cmd}")
                    # 处理可能包含多个命令的情况
                    commands = cmd.split(';')
                    for command in commands:
                        command = command.strip()
                        if not command:  # 跳过空命令
                            continue
                        
                        if command == "heartbeat":  # 处理心跳包
                            print("收到心跳包，保持连接")
                            # 回复心跳确认
                            s.sendall("heartbeat_ack".encode('utf-8'))
                            
                        elif command.startswith("led_ctrl"):  # 检查命令是否为照明LED的控制命令
                            try:
                                val_str = command.split("led_ctrl")[1].strip()
                                val = int(val_str)
                                LED_output(val)
                            except (ValueError, IndexError) as e:
                                print(f"LED命令解析错误: {e}, 命令: {command}")
                                
                        elif command.startswith("conveyor_ctrl"):
                            try:
                                val_str = command.split("conveyor_ctrl")[1].strip()
                                val = int(val_str)
                                Conveyor_output(val)
                            except (ValueError, IndexError) as e:
                                print(f"传送带命令解析错误: {e}, 命令: {command}")
                                
                        elif command == "select":  # 处理分拣命令
                            print("收到分拣命令，激活继电器")
                            select_output()
                            
                        else:
                            print(f"未知命令: {command}")
                except OSError as e:
                    # 在MicroPython中，非阻塞模式下没有数据可读会引发OSError
                    # 检查是否是EAGAIN或EWOULDBLOCK错误
                    if e.args[0] == 11 or e.args[0] == 35:  # EAGAIN或EWOULDBLOCK
                        # 没有数据可读，这是正常的
                        pass
                    else:
                        # 其他OSError错误
                        print(f"OSError: {e}")
                        raise
                except socket.error as e:
                    if e.args[0] == socket.EWOULDBLOCK:
                        # 没有数据可读，这是正常的
                        pass
                    else:
                        # 其他socket错误
                        print(f"Socket错误: {e}")
                        raise
                
                # 短暂休眠，减少CPU使用
                time.sleep(0.1)
                
                # 检查是否超过5秒未收到数据
                current_time = time.time()
                if current_time - last_data_time > 5:
                    print("超过5秒未收到数据，终止命令接收")
                    break
                
            except OSError as e:
                # 在MicroPython中，超时会引发OSError
                print(f"接收超时，继续等待... {e}")
                return
            
    except Exception as e:
        print(f'命令处理出错: {e}')
        return False
    finally:
        if s:
            s.close()
            print("关闭socket连接")
    return True

# 主程序
def main():
    print("\n===== ESP32 控制程序启动 =====\n")
    print(f"版本: 1.3.0 | 最大重连次数: {MAX_RECONNECT_ATTEMPTS}")
    print("==============================\n")
    
    # 初始扫描WiFi并选择配置
    scan_wlan()
    
    # 主循环
    while True:
        try:
            # 连接WiFi
            if not connect_wifi():
                print("WiFi连接失败，重试...")
                time.sleep(RECONNECT_DELAY)
                continue
                
            # 初始化IO设备
            if not init_io():
                print("IO设备初始化失败，重试...")
                time.sleep(2)
                continue
                
            # 接收命令
            if not rec_cmd():
                print("命令接收失败，重新连接...")
                time.sleep(1)
                continue
                
        except KeyboardInterrupt:
            print("\n程序被用户中断")
            break
        except Exception as e:
            print(f"主循环出错: {e}")
            time.sleep(5)

# 启动程序
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"程序崩溃: {e}")
    finally:
        # 清理资源
        print("程序结束，已清理资源")



