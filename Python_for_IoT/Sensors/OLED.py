from machine import Pin, I2C
i2c=I2C(0, scl=Pin(21), sda=Pin(20), freq=100000)
# i2c=I2C(1, scl=Pin(19),sda=Pin(18), freq=100000)

from ssd1306 import SSD1306_I2C
oled = SSD1306_I2C(128, 32, i2c)
c='-'
i=0
j=0
oled.fill(0) 
for i in range(20):
    oled.text(c, j, 0)
    oled.show()
    j+=8
j=0
a='|'
for i in range(5):
    oled.text(a, 0, j)
    oled.show()
    j+=5
j=0
for i in range(20):
    oled.text(c, j, 25)
    oled.show()
    j+=8
a='|'
j=0
for i in range(5):
    oled.text(a, 120, j)
    oled.show()
    j+=5
oled.text('Xaythavy', 30, 12)
oled.show()