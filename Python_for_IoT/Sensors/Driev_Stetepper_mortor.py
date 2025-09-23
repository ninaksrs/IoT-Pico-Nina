from machine import Pin
from time import sleep

# ກຳນົດ GPIO ສຳລັບ stepper
pins = [Pin(0, Pin.OUT), Pin(1, Pin.OUT), Pin(2, Pin.OUT), Pin(3, Pin.OUT)]

# ລຳດັບການສັ່ງ step (half-step mode)
seq = [
    [1,0,0,0],
    [1,1,0,0],
    [0,1,0,0],
    [0,1,1,0],
    [0,0,1,0],
    [0,0,1,1],
    [0,0,0,1],
    [1,0,0,1]
]

def step_motor(steps, delay):
    for _ in range(steps):
        for pattern in seq:
            for i in range(4):
                pins[i].value(pattern[i])
            sleep(delay)

# ທົດລອງໃຫ້ motor ຫັນ 1 ຮອບ (4096 steps ສໍາລັບ 28BYJ-48)
step_motor(4096, 0.002)