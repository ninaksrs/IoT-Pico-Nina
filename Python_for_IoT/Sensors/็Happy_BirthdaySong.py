from machine import Pin, PWM
from time import sleep

# ກຳນົດ passive buzzer ຢູ່ pin 15
buzzer = PWM(Pin(15))

# ຄ່າໂຕນ (frequency Hz) ສຳລັບເພງ Happy Birthday
tones = {
    "C4": 262,
    "D4": 294,
    "E4": 330,
    "F4": 349,
    "G4": 392,
    "A4": 440,
    "B4": 494,
    "C5": 523
}

# ບັນທຶກເນື້ອເພງ Happy Birthday
song = [
    ("C4", 0.4), ("C4", 0.2), ("D4", 0.6), ("C4", 0.6), ("F4", 0.6), ("E4", 1.2),
    ("C4", 0.4), ("C4", 0.2), ("D4", 0.6), ("C4", 0.6), ("G4", 0.6), ("F4", 1.2),
    ("C4", 0.4), ("C4", 0.2), ("C5", 0.6), ("A4", 0.6), ("F4", 0.6), ("E4", 0.6), ("D4", 1.2),
    ("B4", 0.4), ("B4", 0.2), ("A4", 0.6), ("F4", 0.6), ("G4", 0.6), ("F4", 1.2)
]

# ຟັງຊັນສະແດງເພງ
def play(note, duration):
    if note == "P":  # ພັກ (pause)
        buzzer.duty_u16(0)
    else:
        buzzer.freq(tones[note])
        buzzer.duty_u16(30000)  # ຄ່າຄວາມດັງ
    sleep(duration)
    buzzer.duty_u16(0)  # ປິດສຽງຫຼັງຈາກແຕ່ລະໂນ໊ດ
    sleep(0.05)

# ສະແດງເພງ Happy Birthday
for note, duration in song:
    play(note, duration)

buzzer.deinit()
