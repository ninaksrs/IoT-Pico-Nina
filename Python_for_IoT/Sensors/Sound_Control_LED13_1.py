from machine import Pin, ADC
import utime

# ການຕັ້ງຄ່າ sensor ແລະ LED
sound = ADC(Pin(26))   # AO pin
led = Pin(15, Pin.OUT)

# ກໍານົດ threshold ສໍາລັບສຽງ
threshold = 20000

while True:
    sound_value = sound.read_u16()  # ຄ່າ 0–65535
    print("Sound Level:", sound_value)

    if sound_value > threshold:
        led.value(1)   # ເປີດ LED ເມື່ອສຽງດັງ
    else:
        led.value(0)   # ປິດ LED ເມື່ອສຽງເບົາ

    utime.sleep(1)
