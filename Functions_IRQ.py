from machine import Pin
import time

JDQ = Pin(22,Pin.OUT)
KEY=Pin(0,Pin.IN,Pin.PULL_UP)
state = 0

def fun(KEY):
    global state
    time.sleep_ms(10)
    if KEY.value()==0:
        state = not state
        JDQ.value(state)


KEY.irq(fun,Pin.IRQ_FALLING)
print(ok)


#外部终断中用下降沿来控制单片机的按键更加节能源，节约性能，控制稳定（下降沿的判断稳定）
