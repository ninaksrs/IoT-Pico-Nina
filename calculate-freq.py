# The frequency in Hertz (Hz)
frequency = 40.0

# Calculate the time period in seconds (T = 1 / f)
time_period_s = 1 / frequency

# Calculate the half-period in microseconds, which is the on/off time for a square wave
# The factor 1,000,000 converts seconds to microseconds
half_period_us = (time_period_s / 2) * 1_000_000

print(f"Frequency: {frequency} Hz")
print(f"Full period: {time_period_s:.6f} seconds")
print(f"Half period for a square wave: {half_period_us:.2f} microseconds")

# Example of how you'd use this value in a MicroPython or CircuitPython script
# with a pin named 'buzzer'

import utime
import machine

buzzer = machine.Pin(12, machine.Pin.OUT)

while True:
    buzzer.value(1)
    utime.sleep_us(int(half_period_us))
    buzzer.value(0)
    utime.sleep_us(int(half_period_us))