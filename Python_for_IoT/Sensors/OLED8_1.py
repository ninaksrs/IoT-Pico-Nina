from machine import Pin, I2C
import ssd1306
import utime

# ກຳນົດ I2C (SDA=GP0, SCL=GP1)
i2c = I2C(0, scl=Pin(21), sda=Pin(20), freq=400000)

# ກວດຫາ address ຂອງ OLED
print("I2C address:", i2c.scan())

# ສ້າງ object ຈໍ OLED (128x64)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# ລອງສະແດງຂໍ້ຄວາມ
oled.fill(0)  # ລ້າງຈໍ
oled.text("Hello, Pico!", 0, 0)
oled.text("OLED Test", 2, 0)
oled.text("Nice!", 4, 0)   
oled.show()

# ສະແດງຕົວເລກນັບ
'''for i in range(10):
    oled.fill(0)
    oled.text("Counting:", 0, 0)
    oled.text(str(i), 0, 20)
    oled.show()
    utime.sleep(1)'''
