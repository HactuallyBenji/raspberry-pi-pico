import machine

green_led = machine.Pin(15, machine.Pin.OUT)
green_led.on()

yellow_led = machine.Pin(14, machine.Pin.OUT)
yellow_led.on()

red_led = machine.Pin(13, machine.Pin.OUT)
red_led.on()

red_led.toggle()