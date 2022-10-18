from machine import Pin,Timer
import time,dht

print('ok1')

d = dht.DHT11(Pin(27))
time.sleep(1)

print('ok2')

def dht_get(tim):
    d.measure()
     #采集温度
    print(str(d.temperature())+"C")
    print(str(d.humidity())+"%")
    print(1)

tim=Timer(-1)
print("Timer is ok")
tim.init(period=2000,mode=Timer.PERIODIC,callback=dht_get)
