from machine import Pin, ADC
import utime

rocker_x = ADC(27)
rocker_y = ADC(26)
button = Pin(28, Pin.IN, Pin.PULL_UP)


def read_x():
    value = int(rocker_x.read_u16() * 256 /665536)
    return value

def read_y():
    value = int(rocker_y.read_u16() * 256 /665536)
    return value

def button_state():
    press = False
    if button.value() == 0:
        press = True
    return press

while True:
    value_x = read_x()
    value_y = read_y()
    state = button_state()
    print("x: %d, y: %d, press: %s " %(value_x, value_y, state))
    utime.sleep(1)