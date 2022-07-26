import torch
import cpuinfo

# CPU
cpu = cpuinfo.get_cpu_info()['brand_raw']
print(f'CPU: {cpu}')


# GPU
if torch.cuda.is_available() == True:
    gpu = torch.cuda.get_device_name(0)
else:
    gpu='none'
print(f'GPU: {gpu}')