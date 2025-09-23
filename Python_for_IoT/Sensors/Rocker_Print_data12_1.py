from machine import ADC, Pin, PWM
import utime

# Setup Joystick
xAxis = ADC(Pin(27))   # VRx
button = Pin(28, Pin.IN, Pin.PULL_UP)  # SW button

# Setup Servo
servo = PWM(Pin(15))
servo.freq(50)

# Mapping function (0–65535 -> 0–180 degrees)
def my_map(x, in_min, in_max, out_min, out_max):
    return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

# Servo control
def servo_control(angle):
    duty = my_map(angle, 0, 180, 500000, 2500000)
    servo.duty_ns(duty)

while True:
    xValue = int(xAxis.read_u16()*256/65536)
    angle = my_map(xAxis.read_u16(), 0, 65535, 0, 180)  # map joystick to 0–180
    servo_control(angle)

    print("X:", xValue, "Angle:", angle, "Button:", button.value())
    utime.sleep(0.5)
