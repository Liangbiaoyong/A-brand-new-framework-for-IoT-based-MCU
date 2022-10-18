from machine import Pin,PWM
import time


DIR=Pin(5,Pin.OUT)
DJ = PWM(Pin(23),freq=0,duty=400)

DIR.value(0)#低，向内
DJ.freq(1000)
time.sleep(1)

DJ.deinit()