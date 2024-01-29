import machine

green_led = machine.Pin(15, machine.Pin.OUT)
green_led.off()
green_led.on()

yellow_led = machine.Pin(14, machine.Pin.OUT)
yellow_led.on()


weather_url = 