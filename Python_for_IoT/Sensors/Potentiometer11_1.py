from machine import ADC, PWM, Pin
import utime

# Initialize the potentiometer to pin 28 (ADC function)
rp = ADC(28)

# Read the current analog value of the potentiometer and return [0, 100]
def get_value():
    return int(rp.read_u16() * 101 / 65536)

# Print the current value of the potentiometer cyclically, value=[0, 100]
servo = PWM(Pin(7))
servo.freq(50)
def my_map(x, in_min, in_max, out_min, out_max):
    return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

# Control servo, value=[0, 180]
def servo_control(value):
    if value > 180 or value < 0:
        print('Please enter a limited speed value of 0-180 ')
        return
    duty = my_map(value, 0, 180, 500000, 2500000)
    servo.duty_ns(duty)
while True:
    value = get_value()
    servo_control(value*1.8)
    utime.sleep(.2)