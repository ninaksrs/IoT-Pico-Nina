from machine import Pin
import utime

# Define the buzzer pin
buzzer = Pin(12, Pin.OUT)

def play_note(frequency, duration):
    """
    Plays a note of a specific frequency and duration on a buzzer.
    
    Args:
        frequency (int): The frequency of the note in Hz.
        duration (float): The duration of the note in seconds.
    """
    if frequency == 0:  # Handle rests (pauses)
        utime.sleep(duration)
        return
    
    # Calculate the period in microseconds from the frequency
    period_us = 1_000_000 / frequency
    
    # Calculate the number of cycles for the duration
    num_cycles = int(duration * frequency)
    
    for _ in range(num_cycles):
        buzzer.value(1)
        utime.sleep_us(int(period_us / 2))
        buzzer.value(0)
        utime.sleep_us(int(period_us / 2))

# Frequencies for the "Happy Birthday" melody (in the key of G)
note_g4 = 392
note_a4 = 440
note_b4 = 494
note_c5 = 523
note_d5 = 587
note_e5 = 659
note_f5_sharp = 740
note_g5 = 784
rest = 0

#"Happy Birthday" melody in notes
melody = [
    note_g4, note_g4, note_a4, note_g4, note_c5, note_b4,
    note_g4, note_g4, note_a4, note_g4, note_d5, note_c5,
    note_g4, note_g4, note_g5, note_e5, note_c5, note_b4, note_a4,
    note_f5_sharp, note_f5_sharp, note_e5, note_c5, note_d5, note_c5
]

# The durations for each note (in seconds)
durations = [
    0.25, 0.25, 0.5, 0.5, 0.5, 1.0,
    0.25, 0.25, 0.5, 0.5, 0.5, 1.0,
    0.25, 0.25, 0.5, 0.5, 0.5, 0.5, 1.0,
    0.25, 0.25, 0.5, 0.5, 0.5, 1.0
]

# Play the melody
def play_song():
    for note, duration in zip(melody, durations):
        play_note(note, duration)
        utime.sleep(0.05) # Small pause between notes for clarity
        
while True:
    play_song()