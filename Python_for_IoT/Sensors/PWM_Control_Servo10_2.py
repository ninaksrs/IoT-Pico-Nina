from machine import Pin, PWM
import utime

servo = PWM(Pin(7))
servo.freq(50)

# ຟັງຊັ່ນແປງຄ່າມຸມເປັນ pulse width
def my_map(x, in_min, in_max, out_min, out_max):
    return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

# ຟັງຊັ່ນຄວບຄຸມ servo
def servo_control(value):
    duty = my_map(value, 0, 180, 500000, 2500000)  # 0.5ms → 2.5ms
    servo.duty_ns(duty)

# ຟັງຊັ່ນປັບຄວາມໄວ
def sweep_with_speed(start, end, step=1, min_delay=0.02, max_delay=0.2):
    # ຈຳນວນມຸມທີ່ຈະເຄື່ອນ
    steps = abs(end - start) // step
    for i in range(steps + 1):
        angle = start + (step if end > start else -step) * i
        servo_control(angle)
        print("Angle:", angle)
        # ຄວາມໄວປ່ຽນແປງຈາກ max_delay → min_delay
        delay = max_delay - (i / steps) * (max_delay - min_delay)
        utime.sleep(delay)

# ໃຫ້ servo ຫມຸນໄປກັບດ້ວຍຄວາມໄວປັບໄດ້
while True:
    sweep_with_speed(0, 180, step=5)   # ຫມຸນໄປຂ້າງໜ້າ
    sweep_with_speed(180, 0, step=5)   # ຫມຸນກັບຄືນ
