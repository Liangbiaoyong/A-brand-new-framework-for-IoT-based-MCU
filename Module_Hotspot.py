import network,machine


def hotspot():
    hotspot=network.WLAN(network.AP_IF)
    hotspot.active(True)
    hotspot.config(essid='ESP-AP')
    hotspot.config(max_clients=3)
    print('hotspot is open,',hotspot.active())
    
hotspot()
