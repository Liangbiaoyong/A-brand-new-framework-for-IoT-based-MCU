from machine import Pin
import time

LED = Pin(2,Pin.OUT)
YD = Pin(16,Pin.IN)  #是否接入上拉电阻

while True:
    if YD.value()==0:
#由于默认上拉电阻，所以有雨的时候才输出低电平
        LED.value(1)
        time.sleep(1)
    else:
        LED.value(0)
        time.sleep(1)
            