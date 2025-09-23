import time
from machine import Pin, I2C

# Pin configuration for the I2C bus
i2c = I2C(1, scl=Pin(19), sda=Pin(18), freq=100000)

print("Scanning I2C bus...")
devices = i2c.scan()

if devices:
    print("Found I2C devices at addresses:", [hex(d) for d in devices])
else:
    print("No I2C devices found.")