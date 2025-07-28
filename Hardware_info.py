import torch

# if torch.cuda.is_available():
#     print("CUDA is available!")
#     num_gpus = torch.cuda.device_count()
#     print(f"Number of available GPUs: {num_gpus}")
#     device_name = torch.cuda.get_device_name(0)
#     print(f"Name of the first GPU: {device_name}")
# else:
#     print("CUDA is not available. Using CPU.")

# for i in range(torch.cuda.device_count()):
#         print(f"  - GPU {i}:")
#         print(f"    - 名称:", torch.cuda.get_device_name(i))

# import platform

# processor_name = platform.processor()
# print("处理器名称：", processor_name)


import wmi
from datetime import datetime, timedelta
# 连接WMI
wmi_obj = wmi.WMI()

# 获取处理器信息
# processors = wmi_obj.Win32_Processor()
# print(f"{processors}")
# for processor in processors:
#     print("处理器ID：", processor.ProcessorID)
#     print("处理器型号：", processor.Name)
#     print("处理器架构：", processor.Architecture)
#     print("处理器核心数：", processor.NumberOfCores)


# import psutil 
# cpu_info = psutil.cpu_info( )
# cpu_name = cpu_info [ 0 ] [ 'brand_raw' ]
# print ( cpu_name )
    
current_time = datetime.now().timestamp()
print(current_time)