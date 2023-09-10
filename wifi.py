import network
import socket
import ujson
from time import sleep
import machine

def connect():
    
    with open('secrets.json') as fp:
        secrets = ujson.loads(fp.read())
        
    ssid = secrets['network']['ssid']
    password = secrets['network']['pass']
    
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
    print(wlan.ifconfig())
    print("Pico: " + wlan.ifconfig()[0])

try:
    connect()
except KeyboardInterrupt:
    machine.reset()