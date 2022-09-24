import cv2
import torch
print(cv2.__version__)

print(torch.cuda.empty_cache() )
print(torch.cuda.is_available() )
print(torch.cuda.device_count() )
print(torch.cuda.get_device_name(0) )
print(torch.cuda.memory_reserved)
