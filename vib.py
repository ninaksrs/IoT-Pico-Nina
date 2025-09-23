from machine import Pin
from time import sleep

# Initialize the vibration motor module
vibration_motor = Pin(12, Pin.OUT)

def vibrate(vigration_time):
    vibration_motor.value(1)
    sleep(vigration_time)
    vibration_motor.value(0)

vibrate(2)

for i in range(3):
    vibrate(0.5)
    sleep(0.3)
    