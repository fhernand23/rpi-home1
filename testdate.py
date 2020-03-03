from datetime import datetime
import time,os

MON = 0
TUE = 1
WED = 2
THU = 3
FRI = 4
SAT = 5
SUN = 6

dt = datetime.now()
lt = time.localtime()

# t = time.strftime("%d-%m-%Y %H:%M:%S", time.localtime())
print(dt)
print(dt.weekday())
print(dt.hour)
print(dt.minute)
print(dt.hour*100+dt.minute)

