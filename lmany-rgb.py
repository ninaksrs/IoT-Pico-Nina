import ws2812b
import utime
import random

ring_pin = 17
numpix = 8
strip = ws2812b.ws2812b(numpix, 0, ring_pin)
strip.fill(0, 0, 0)
strip.show()

# Define the color for the moving pixel
moving_pixel_color = (0, 0, 255) # This is blue

while True:
    # Loop backward from the last pixel (numpix - 1) down to 0
    for i in range(numpix - 1, -1, -1):
        strip.fill(0, 0, 0) # Clear the entire strip
        
        # Set the current pixel in the sequence to the desired color
        strip.set_pixel(i, moving_pixel_color[0], moving_pixel_color[1], moving_pixel_color[2])
        
        strip.show()
        utime.sleep_ms(100) # Control the animation speed (100ms delay)