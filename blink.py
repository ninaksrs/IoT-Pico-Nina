from machine import Pin
import time
led_onboard = Pin("LED", Pin.OUT)

while True:
    led_onboard.value(1)
    print('on')
    time.sleep(1)
    led_onboard.value(0)
    print('off')
    time.sleep(1)