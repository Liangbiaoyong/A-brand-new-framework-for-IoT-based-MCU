from machine import Pin, PWM
import time
 
S1 = PWM(Pin(5), freq=50, duty=0) # Servo1的引脚是18
 
def Servo(servo,angle):
    S1.duty(int(((angle+90)*2/180+0.5)/20*1023))
 
#-90度
Servo(S1,-90)
time.sleep(1)
 
#-90度
Servo(S1,-45)
time.sleep(1)
 
#-90度
Servo(S1,0)
time.sleep(1)
 
#-90度
Servo(S1,45)
time.sleep(1)
 
#-90度
Servo(S1,90)
time.sleep(1)