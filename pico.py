from machine import Pin, PWM
from time import sleep

pwm = PWM(Pin(18))
pwm.freq(50)

button = Pin(14, Pin.IN, Pin.PULL_DOWN)

shouldLock = True

def setServoCycle(position):
    pwm.duty_u16(position)
    sleep(0.01)
    
while True:
    while button.value():
        if shouldLock:
            for pos in range(1500,8300,100):
                setServoCycle(pos)
                print(pwm.duty_u16())
            shouldLock = False
        else:
            for pos in range(8300,1500,-100):
                setServoCycle(pos)
                print(pwm.duty_u16())
            shouldLock = True