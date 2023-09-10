from machine import Pin, PWM
from time import sleep

pwm = PWM(Pin(18))
pwm.freq(50)

button = Pin(14, Pin.IN, Pin.PULL_DOWN)
sensor = Pin(15, Pin.IN)

sensor_data = []

shouldLock = True
saw_0 = False

def setServoCycle(position):
    pwm.duty_u16(position)
    sleep(0.01)
    
while True:
    if sensor.value() == 0:
        saw_0 = True
        sensor_data.append(0)
    if saw_0:
        while 
    
print(sensor_data)
    
