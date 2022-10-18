from machine import Pin,PWM
import time

Beep = PWM(Pin(10),freq=0,duty=200)
#pin=25

Beep.freq(50)
time.sleep_ms(1000)
    
Beep.freq(50)
time.sleep(1)

Beep.freq(600)
time.sleep(1)

Beep.freq(800)
time.sleep(1)

Beep.deinit()