import math 
import time
num = int(input('Enter a number:'))
ms = int(input('Enter the number of milliseconds to wait:'))
time.sleep(ms / 1000)
sqrt_num = math.sqrt(num)
print(f"Square root of {num} after {ms} milliseconds is {sqrt_num}")
