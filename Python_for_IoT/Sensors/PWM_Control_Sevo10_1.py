from machine import Pin, PWM
import utime

servo = PWM(Pin(7))
servo.freq(50)

# ຟັງຊັ່ນແປງຄ່າມຸມເປັນ pulse width
def my_map(x, in_min, in_max, out_min, out_max):
    return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

# ຟັງຊັ່ນຄວບຄຸມ servo
def servo_control(value):
    if value > 180 or value < 0:
        print('ກະລຸນາໃສ່ຄ່າ 0-180 ')
        return
    duty = my_map(value, 0, 180, 500000, 2500000)  # 0°=0.5ms, 180°=2.5ms
    servo.duty_ns(duty)

# ປັບມຸມທີລະ 10°
while True:
    for angle in range(0, 181, 10):  # 0 → 180
        servo_control(angle)
        print("Angle:", angle)
        utime.sleep(0.5)

    for angle in range(180, -1, -10):  # 180 → 0
        servo_control(angle)
        print("Angle:", angle)
        utime.sleep(0.5)
