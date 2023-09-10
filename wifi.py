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
        
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    
    return ip

def open_socket(ip):
    address = (ip, 80)
    connection = socket.socket()
    connection.bind(address)
    connection.listen(1)
    print(connection)

try:
    ip = connect()
    open_socket(ip)
except KeyboardInterrupt:
    machine.reset()