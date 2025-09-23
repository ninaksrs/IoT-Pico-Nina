from machine import Pin
import utime

led = Pin('LED', Pin.OUT)
key = Pin(0, Pin.IN, Pin.PULL_UP)

print('default value of btn: ', key.value())

def on():
    led.value(1)
def off():
    led.value(0)

def press():
    if key.value() == 0:
        return True
    return False

while True:
    if press() == True:
        print("press: ", key.value())
        on()
        utime.sleep(.1)
    else:
        off()

