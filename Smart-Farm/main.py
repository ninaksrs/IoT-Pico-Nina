from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import utime
from color import color
import RGB_lights as RGB


i2c_1 = I2C(0, scl=Pin(21), sda=Pin(20), freq=100000)
oled = SSD1306_I2C(128, 32, i2c_1)

i2c_2 = I2C(1, scl=Pin(19), sda=Pin(18), freq=100000)
Color = color(i2c_2)

utime.sleep(1)

while True:
    oled.fill(0)
    RGB.rgb_green(1)
    r, g, b = Color.GetRGBValue()
    
    # Simple color detection logic based on a range of values
    if r > g * 2.0 and r > b * 2.0 and r > 100:
        detected_color = "Red"
    elif g > r * 2.0 and g > b * 2.0 and g > 100:
        detected_color = "Green"
    elif b > r * 2.0 and b > g * 2.0 and b > 100:
        detected_color = "Blue"
    elif r > 200 and g > 200 and b > 200:
        detected_color = "White"
    elif r < 50 and g < 50 and b < 50:
        detected_color = "Black"
    else:
        detected_color = "R:%3d G:%3d B:%3d" % (r, g, b)
        r_det = "R:%3d" %(r)
        g_det = "G:%3d" %(g)
        b_det = "B:%3d" %(b)

    # Print to the terminal
    print("Detected Color: %s" % detected_color)
    print("RGB Values: R:%3d G:%3d B:%3d" % (r, g, b))
    
    
    # Display on the OLED
    print("Color Detecting...")
    oled.text("Color: %s" % detected_color, 0, 0)
    oled.show()
    utime.sleep(1)