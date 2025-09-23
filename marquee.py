import ws2812b
import random
import utime

ring_pin = 17
numpix = 8
strip = ws2812b.ws2812b(numpix, 0, ring_pin)
strip.fill(0,0,0)
strip.show()

while True:
    for i in range(numpix  - 1, -1, -1):
        strip.fill(0,0,0)
        r = random.randint(0, 10)
        g = random.randint(0, 10)
        b = random.randint(0, 10)
        strip.set_pixel(i, r, g, b)
        strip.show()
        utime.sleep(.05)