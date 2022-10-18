import network,time,usocket
from machine import Pin,Timer

s = usocket.socket()

def Socket_fun(tim):
    text=s.recv(500)
    if text == "":
        pass
    else:
        print(text)
        s.send("copy down")
             


addr=('169.254.61.167',8080)
s.connect(addr)
s.send("Fack You")
print("OK")
    
tim = Timer(-1)
tim.init(period=1000,mode=Timer.PERIODIC,callback=Socket_fun)