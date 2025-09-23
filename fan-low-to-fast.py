from machine import Pin, PWM
import time

# Initialize the motor fan
fan = PWM(Pin(13))
fan.freq(1000) # Set frequency

def set_speed(percent):
    if percent < 0:
        percent = 0
    if percent > 100:
        percent = 100
    duty = int(percent * 65535 / 100)
    fan.duty_u16(duty)
    
while True:
    for speed in range (0, 101, 20):
        set_speed(speed)
        print('Fan speed: ', speed, '%')
        time.sleep(2)
    for speed in range(100, -1, -20):
        set_speed(speed)
        print('Fan speed: ', speed, '%')
        time.sleep(2)