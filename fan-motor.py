from machine import Pin, PWM
import time

# Initialize the motor fan
fan = PWM(Pin(13))
fan.freq(1000) # Set frequency

btn = Pin(0, Pin.IN, Pin.PULL_UP)

btn_state = False
last_press_time = 0

# Numerical remapping
def my_map(x, in_min, in_max, out_min, out_max):
    return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

# Set the fan speed, speed=[0, 100]
def pwm_motor(speed):
    if speed > 100 or speed < 0:
        print('Please enter a limited speed value of 0-100 ')
        return
    pulse = my_map(speed, 0, 100, 0, 65535)
    fan.duty_u16(pulse)

def switch_btn():
    # Use a small delay for debouncing
    time.sleep_ms(20) 
    return btn.value() == 0

def ramp_up_and_down(step_size, delay_ms):
    print("Ramping up...")
    # Ramp up from 0 to 100 in specified steps
    for speed in range(0, 101, step_size):
        pwm_motor(speed)
        time.sleep_ms(delay_ms)
        print(f"Speed: {speed}%")

    print("\nRamping down...")
    # Ramp down from 100 to 0 in specified steps
    for speed in range(100, -1, -step_size):
        pwm_motor(speed)
        time.sleep_ms(delay_ms)
        print(f"Speed: {speed}%")

    print("\nMotor cycle complete.")


while True:
    current_time = time.ticks_ms()
    if switch_btn() and (current_time - last_press_time > 300): # Add debouncing
        last_press_time = current_time
        btn_state = not btn_state
        print(f"Button pressed. Motor state: {'ON' if btn_state else 'OFF'}")
        ramp_up_and_down(20, 500)
        
    if btn_state:
        pwm_motor(100)
    else:
        pwm_motor(0)