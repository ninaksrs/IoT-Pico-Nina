import random
import utime
from machine import Pin
import array, time

class ws2812b:
    def __init__(self, num_leds, state_machine, pin):
        self.num_leds = num_leds
        self.pin = Pin(pin, Pin.OUT)
        self.ar = array.array("I", [0 for _ in range(num_leds)])

    def show(self):
        for color in self.ar:
            for bit in range(24):
                if color & (1 << (23 - bit)):
                    self._send_one()
                else:
                    self._send_zero()
        time.sleep_us(50)

    def _send_one(self):
        self.pin(1)
        time.sleep_us(1)   # high
        self.pin(0)
        time.sleep_us(1)   # low

    def _send_zero(self):
        self.pin(1)
        time.sleep_us(0)   # short high
        self.pin(0)
        time.sleep_us(2)   # longer low

    def fill(self, r, g, b):
        for i in range(self.num_leds):
            self.set_pixel(i, r, g, b)

    def set_pixel(self, i, r, g, b):
        self.ar[i] = (g<<16) + (r<<8) + b


# ------------------------------
# ໃຊ້ງານ
# ------------------------------
ring_pin = 17   # GPIO ທີ່ເຊື່ອມ NeoPixel
numpix   = 8    # ຈຳນວນດວງ LED

strip = ws2812b(numpix, 0, ring_pin)  # ສ້າງ object
strip.fill(0, 0, 0)  # Clear RGB buffer
strip.show()         # Refresh display

while True:
    for i in range(numpix):
        strip.fill(0, 0, 0)
        r = random.randint(0, 50)
        g = random.randint(0, 50)
        b = random.randint(0, 50)
        strip.set_pixel(i, r, g, b)
        strip.show()
        print('LED:', i, r, g, b)
        utime.sleep(0.2)
