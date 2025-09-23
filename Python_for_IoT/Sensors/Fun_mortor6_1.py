from machine import Pin, PWM
import time

# ຕິດິັ້ງ PWM ຂາ GP13
fan = PWM(Pin(13))
fan.freq(1000)  # ຄວາມຖີ່ 1kHz

# ຟັງເຊີ້ນປັບຄວາມໄວຂອງພັດລົມ (0 - 100%)
def set_speed(percent):
    if percent < 0:
        percent = 0
    if percent > 100:
        percent = 100
    duty = int(percent * 65535 / 100)  # ແປງເປັນ duty cycle 16-bit
    fan.duty_u16(duty)

# ທົດສອບການທຳງານ
while True:
    for speed in range(0, 101, 20):  # ຈາກ 0% → 100%
        set_speed(speed)
        print("Fan speed:", speed, "%")
        time.sleep(2)
    for speed in range(100, -1, -20):  # ຈາກ 100% → 0%
        set_speed(speed)
        print("Fan speed:", speed, "%")
        time.sleep(2)
