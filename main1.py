from machine import Pin,PWM,Timer
import time
import network,time,socket
from tftlcd import LCD32
LED = Pin(2,Pin.OUT)
KEY = Pin(0,Pin.IN,Pin.PULL_UP) 

RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
BLACK=(0,0,0)
WHITE=(255,255,255)
d = LCD32(portrait=3)
d.fill(WHITE)
d.printStr('Welcom you', 10, 200, RED, size=3)
d.printStr('that will be a good experience', 10, 230, GREEN, size=1)
import network,time,socket
from machine import Pin,Timer


def WIFI_Connect():
    WIFI_LED=Pin(2,Pin.OUT)
    wlan=network.WLAN(network.STA_IF)
    wlan.active(False)
    wlan.active(True)
    start_time= time.time()
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('Redmi',"01234567")
        
        while not wlan.isconnected():
            
            WIFI_LED.value(1)
            time.sleep_ms(300)
            WIFI_LED.value(0)
            time.sleep(0.3)
            if time.time()-start_time >3:
                print('WIFI Connected Timeout!')
                break
    if wlan.isconnected():
        WIFI_LED.value(1)
        print('network information:',wlan.ifconfig())
        return True
    else:
        return False


WIFI_Connect()
time.sleep(3)

d.fill(WHITE)
d.printStr('Are you ready?', 10, 200, RED, size=3)


while True:
   if KEY.value()==0: #按键被按下
       time.sleep_ms(10) #消除抖动
       if KEY.value()==0: #确认按键被按下
           break
        

d.fill(WHITE)
d.printStr("""I'm initializing'""", 10, 200, RED, size=1)


Beep = PWM(Pin(25),freq=0,duty=512)
Beep.freq(200)
time.sleep_ms(3000)
Beep.deinit()


#雨布复位
DIR_Rain=Pin(19,Pin.OUT)
DJ_Rain=PWM(Pin(18),freq=0,duty=512)


DIR_Rain.value(1)#高电平为雨布回收
DJ_Rain.freq(1000)
time.sleep(3)
DJ_Rain.deinit()


#竿子复位到初始状态
DIR=Pin(5,Pin.OUT)
DJ = PWM(Pin(23),freq=0,duty=512)

DIR.value(0)
DJ.freq(1000)
time.sleep(15)
DJ.deinit()


#开始初状态
DJ = PWM(Pin(23),freq=0,duty=512)
DIR.value(1)
DJ.freq(1000)
time.sleep(10)
DJ.deinit()

#反馈完成情况
d.fill(WHITE)
d.printStr('Step 1 complete', 10, 200, RED, size=3)
time.sleep(2)

d.fill(WHITE)
d.printStr('Have you hung up the clothes yet', 10, 200, RED, size=1)



#开始对晾衣模式进行选择   模式文件包含在模块中
while True:
   if KEY.value()==0: #按键被按下
       time.sleep(2)
       if KEY.value()==0: #确认按键被按下
           time.sleep(2)
           if KEY.value()==0:
               d.fill(WHITE)
               d.printStr('Expected to 12 h', 10, 200, RED, size=1)
               import mode2    #以两秒为一个模式选择梯度
               break
           else:
                d.fill(WHITE)
                d.printStr('Expected to 12 h', 10, 200, RED, size=1)
                import mode3
                break
       else:
            d.fill(WHITE)
            d.printStr('Expected to 6 h', 10, 200, RED, size=1)
            import normal_mode
            break
#蜂鸣器提示
Beep.freq(400)
time.sleep(3)

Beep.freq(200)
time.sleep(3)

Beep.freq(200)
time.sleep(3)

Beep.freq(400)
time.sleep(3)


Beep.deinit()
