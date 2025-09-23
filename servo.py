#still find the error

from machine import Pin, PWM
import utime
servo = PWM(Pin(7))
servo.freq(50)

def my_map(x, in_min, in_max, out_min, out_max):
    return int((x - in_min)*(out_max - out_min) / (in_max - in_max) + out_min)

def servo_control(value):
    if value > 180 or value < 0:
        print('Please enter a limited speed value of 0-180 ')
        return
    duty = my_map(value, 0, 180, 500000, 2_500_000)
    servo.duty_ns(duty)
    
while True:
    servo_control(0)
    utime.sleep(1)
    servo_control(180)
    utime.sleep(1)