from machine import Pin
import time

JDQ = Pin(20,Pin.OUT)
KEY=Pin(9,Pin.IN,Pin.PULL_UP)
state = 1


JDQ.value(state)

def fun(KEY):
    global state
    time.sleep_ms(10)
    if KEY.value()==0:
        state = not state
        JDQ.value(state)
        print(state)

KEY.irq(fun,Pin.IRQ_FALLING)


#外部终断中用下降沿来控制单片机的按键更加节能源，节约性能，控制稳定（下降沿的判断稳定）

  