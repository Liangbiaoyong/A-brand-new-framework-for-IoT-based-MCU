d.fill(WHITE)
d.printStr('Expected to 12 h', 10, 200, RED, size=1)


Rest_Time=1
from machine import Pin,Timer
import time,dht
print('ok1')


d = dht.DHT11(Pin(27))
time.sleep(1)
def dht_get(tim):
    d.measure()
     #采集温度
    d.fill(WHITE)
    d.printStr(str(d.temperature()+"C"), 10, 200, RED, size=1)
    global WD
    global SD
    d.printStr(str(d.humidity()+"%"), 10, 200, RED, size=1)
    WD=int(d.temperature())
    SD=int(d.humidity())
    
Rain=Pin(16,Pin.IN,Pin.PULL_UP)



#定义外部中断函数
def adv_rain(Rain):
    Beep = PWM(Pin(25),freq=0,duty=512)
    Beep.freq(200)
    time.sleep_ms(3000)
    Beep.deinit()

#竿子复位到避雨状态
    DIR=Pin(5,Pin.OUT)
    DJ = PWM(Pin(23),freq=0,duty=512)

    DIR.value(0)
    DJ.freq(1000)
    time.sleep(8)
    DJ.deinit()


#展开雨布
    DIR_Rain=Pin(19,Pin.OUT)
    DJ_Rain=PWM(Pin(18),freq=0,duty=512)


    DIR_Rain.value(0)#高电平为雨布回收
    DJ_Rain.freq(1000)
    time.sleep(5)
    DJ_Rain.deinit()



def spead(Rain):
    Rest_Time=Rest_Time=0.5

    DJ.freq(200)
    time.sleep(3)
    Beep.deinit()


    FX.value(1)
    DJ.freq(400)
    time.sleep(20)
    DJ.deinit()


    FX.value(1)
    DJ2.freq(200)
    time.sleep(20)
    DJ2.deinit()


#设置跟下雨有关的回调函数
Rain.irq(adv_rain,Pin.IRQ_FALLING)
Rain.irq(spread,Pin.IRQ_RISING)


def TIME():
    
    start_time=time.time()
    TIME=time.time()-start_time()
    return(TIME%1800)


#如果到达每半个小时的最后一秒
while TIME()=1799:
     
    if Rest_Time>0:
        dht_get(tim)

        time.sleep_h(0.5)
        dht_get(tim)
        
        if Rain.value()==0:
            Rest_Time=Rest_Time+0.3
        if WD>30:
            JS=0.75
        if 25<=WD<=30:
            JS=0.5
        if WD<25:
            JS=0.4
        if SD>60:
            JS = 0.8*JS
        if 40<=SD<=60:
            pass
        else:
            JS=1.2*JS

        Rest_Time=Rest_Time-JS

        sen=str('Expected to ',str(Rest_Time),'h')
        d.fill(WHITE)
        d.printStr(sen, 10, 200, RED, size=1)
    else:
        d.printStr("OK!!!", 10, 200, RED, size=3)
        print('over')


#开始烘干
Drying=Pin(32,Pin.OUT)
Drying.value(0)
time.sleep_min(10)
Drying.value(1)

#除臭杀菌
Incense=Pin(22,Pin.OUT)
Incense.value(0)
time.sleep(60)
Incense.value(1)
