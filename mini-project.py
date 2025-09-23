from machine import Pin
import utime
import time

# init components
#OUTPUT
led_pin = [1,2,3]
rgb = []

for led in led_pin:
    led = Pin(led, Pin.OUT)
    rgb.append(led)

