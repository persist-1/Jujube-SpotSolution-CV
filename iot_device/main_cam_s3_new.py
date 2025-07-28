import socket
import network
import camera
import time
import random
import gc
import machine

###-----该模块为CAM2,监测right视角-----###
###  端口53002

# 配置选项
MAX_RECONNECT_ATTEMPTS = 5  # 最大重连尝试次数
RECONNECT_DELAY = 3  # 重连延迟时间(秒)
IMAGE_QUALITY = 12  # 图像质量(0-63，值越小质量越高)
#FRAME_SIZE = camera.FRAME_VGA  # 图像尺寸
FRAME_RATE = 20  # 每秒帧数
LOW_POWER_MODE = False  # 低功耗模式

# 主要WiFi配置
MAIN_SSID = 'HUAWEI_IOT_node'  # 主要WiFi名称
MAIN_PASSWORD = '111gogogo'  # 主要WiFi密码
MAIN_SERVER_IP = '192.168.8.8'  # 主要服务器IP地址
MAIN_SERVER_PORT = 53002  # 主要服务器端口号

# 备用WiFi配置列表
BACKUP_WIFI_LIST = [
    {
        'SSID': 'backup_iot_node',  # 备用WiFi名称1
        'PASSWORD': '111gogogo',  # 备用WiFi密码1
        'SERVER_IP': '192.168.140.225',  # 备用服务器IP地址1
        'SERVER_PORT': 53002  # 备用服务器端口号1
    },
    {
        'SSID': 'backup_iot_node2',  # 备用WiFi名称2
        'PASSWORD': '111gogogo',  # 备用WiFi密码2
        'SERVER_IP': '192.168.140.226',  # 备用服务器IP地址2
        'SERVER_PORT': 53002  # 备用服务器端口号2
    },
    {
        'SSID': 'backup_iot_node3',  # 备用WiFi名称3
        'PASSWORD': '111gogogo',  # 备用WiFi密码3
        'SERVER_IP': '192.168.140.227',  # 备用服务器IP地址3
        'SERVER_PORT': 53002  # 备用服务器端口号3
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

# 扫描并打印详细的附近Wi-Fi信息，检查是否需要使用备用WiFi
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

# 连接到WiFi网络
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

# 初始化摄像头
def init_camera():
    try:
        print("初始化摄像头...")
        camera.deinit()
        camera.init()
        
        # 设置摄像头参数
        #camera.framesize(camera.FRAME_XGA)  # 设置帧大小
        camera.flip(1)  # 根据需要调整摄像头方向 
        camera.mirror(0)  # right不翻转
        camera.quality(IMAGE_QUALITY)  # 设置图像质量
        camera.contrast(2)  # 增加对比度
        camera.brightness(1)  # 调整亮度
        camera.saturation(0)  # 饱和度
        camera.speffect(0)  # 特效：正常
        camera.whitebalance(1)  # 白平衡：自动
        
        # 设置帧率
        #camera.framesize(FRAME_SIZE)
        
        print("摄像头初始化完成")
        return True
    except Exception as e:
        print(f"摄像头初始化出错: {e}")
        return False

# 发送图像数据到服务器
def send_image():
    handshake_attempts = 0
    max_handshake_attempts = 10
    
    # 握手服务器
    while handshake_attempts < max_handshake_attempts:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(5)  # 设置超时时间
            print('正在连接服务器...')
            s.connect((SERVER_IP, SERVER_PORT))
            print('正在握手服务器...')
            
            handshake = "ESP32cam"  # 发送握手信号
            s.sendall(handshake.encode('utf-8')) 
            confirm = s.recv(1024).decode('utf-8')
            if confirm == "ok":  # 等待服务器发送确认信号
                print("收到确认信号，开始发送图像")
                break
            else:
                print(f"未收到确认信号，断开连接 (收到: {confirm})")
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

    # 发送图像
    frames_sent = 0
    start_time = time.time()
    try:
        while True:
            # 捕获图像
            buf = camera.capture()
            if not buf:
                print("图像捕获失败，重试...")
                time.sleep(0.1)
                continue
                
            # 发送图像大小
            s.sendall(len(buf).to_bytes(4, 'little'))
            # 发送图像数据
            s.sendall(buf)
            
            # 计算帧率
            frames_sent += 1
            elapsed = time.time() - start_time
            if elapsed >= 5:  # 每5秒显示一次帧率
                fps = frames_sent / elapsed
                print(f"发送帧率: {fps:.1f} FPS")
                frames_sent = 0
                start_time = time.time()
                # 执行垃圾回收
                gc.collect()
            else:
                print(".", end='')
                
            # 根据需要调整发送间隔
            time.sleep(0.05)
            
            # 低功耗模式
            if LOW_POWER_MODE and frames_sent % 10 == 0:
                # 每10帧休眠一次以节省电力
                time.sleep(0.2)
                
    except Exception as e:
        print(f'\n图像传输出错: {e}')
        return False
    finally:
        if 's' in locals() and s:
            s.close()
            print("关闭socket连接")
    return True

# 主程序
def main():
    print("\n===== ESP32-CAM 图像传输程序启动 =====\n")
    print(f"版本: 1.3.0 | 模式: {'低功耗' if LOW_POWER_MODE else '正常'}")
    print(f"图像质量: {IMAGE_QUALITY} | 目标帧率: {FRAME_RATE} FPS")
    print(f"主WiFi: {MAIN_SSID} | 备用WiFi数量: {len(BACKUP_WIFI_LIST)}")
    print("======================================\n")
    
    # 初始扫描WiFi
    scan_wlan()
    
    # 主循环
    while True:
        try:
            # 连接WiFi
            if not connect_wifi():
                print("WiFi连接失败，重试...")
                time.sleep(RECONNECT_DELAY)
                continue
                
            # 初始化摄像头
            if not init_camera():
                print("摄像头初始化失败，重试...")
                time.sleep(2)
                continue
                
            # 发送图像
            if not send_image():
                print("图像传输失败，重新连接...")
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
        camera.deinit()
        print("程序结束，已清理资源")


