from machine import Pin,I2C,Timer
import onewire,ds18x20

ow = onewire.OneWire(Pin(6))
ds= ds18x20.DS18X20(ow)
rom = ds.scan()

def temp_get(tim):
    ds.convert_temp()
    temp = ds.read_temp(rom[0])
    print(str('%.2f'%temp)+' C')
    
tim=Timer(0)
tim.init(period=3000,mode=Timer.PERIODIC,callback=temp_get)