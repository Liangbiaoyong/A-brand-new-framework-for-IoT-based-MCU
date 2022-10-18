from machine import Pin,Timer

led=Pin(18,Pin.OUT)
Conter=0
Fun_Num=0

def fun(tim):
    global Conter
    Conter = Conter+1
    print(Conter)
    led.value(Conter%2)
    
tim = Timer(-1)
tim.init(period=1000,mode=Timer.PERIODIC,callback=fun)

