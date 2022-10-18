import network,socket,time
from machine import Pin,Timer
#连接的WIFI只能是2.4G频段

ssid={'1':'TP-LINK_605', '1p':'15811755873',
      '2':'Redmi', '2p':'01234567','3':'XHSD','3p':'88888888','4':'ldsyzx1','4p':''}



def WIFI_Connect():
    WIFI_LEDy=Pin(18,Pin.OUT)
    WIFI_LED=Pin(2,Pin.OUT)
    wlan=network.WLAN(network.STA_IF)
    wlan.active(False)
    wlan.active(True)
    wlan.ifconfig(('192.168.0.4','255.255.255.0','192.168.0.1','8.8.8.8'))
    start_time=time.time()#从现在开始记录开始时间，
                           #为后来的超时判断提供依据
    
    if not wlan.isconnected():
        print('Connecting network....')
        wlan.connect(ssid['4'],ssid['4p'])
        
        while not wlan.isconnected():
            WIFI_LEDy.value(1)
            time.sleep(0.5)
            WIFI_LEDy.value(0)
            WIFI_LED.value(1)
            time.sleep(0.5)
            WIFI_LED.value(0)
            
            print(wlan.scan())
            if time.time()-start_time >3:
                print('WIFI connecting timeout!')
                break
    else:
        pass
    
    if wlan.isconnected():
        print('network is connected')
        print('nectwork information: ',wlan.ifconfig())
        WIFI_LEDy.value(1)
        return True
        
    else:
        WIFI_LED.value(1)
        return False
    
    
WIFI_Connect()