import time

Time = time.localtime()
 
currentTime = time.strftime("%H:%M:%S", Time)
print(currentTime)
