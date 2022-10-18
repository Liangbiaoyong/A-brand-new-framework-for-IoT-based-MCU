from tftlcd import LCD32
import time

RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
BLACK=(0,0,0)
WHITE=(255,255,255)
d = LCD32(portrait=2)
d.fill(WHITE)
d.printStr('ASPSE', 72, 100, RED, size=4)
d.printStr('the new frame', 83, 140, GREEN, size=2)



from machine import Pin,PWM
import time

Beep = PWM(Pin(25),freq=0,duty=512)


Beep.freq(30)
time.sleep(0.384)
    
Beep.freq(900)
time.sleep(0.613)


Beep.deinit()






