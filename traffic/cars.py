from machine import Pin
from neopixel import NeoPixel
from time import sleep

NUM_LEDS = 8

# this goes to data pin
datapin = Pin(18, Pin.OUT)  # XXX check num

np = NeoPixel(datapin, NUM_LEDS)

RED = (10, 0, 0)
YELLOW = (10, 4, 0)
GREEN = (0, 10, 0)
OFF = (0, 0, 0)

TIME_REGULAR = 7
TIME_YELLOW = 2

np[2] = OFF
np[1] = OFF
np[0] = OFF

while True:
    np[2] = RED
    np[1] = OFF
    np.write()
    sleep(TIME_REGULAR)

    np[1] = YELLOW
    np.write()
    sleep(TIME_YELLOW)

    np[2] = OFF
    np[1] = OFF
    np[0] = GREEN
    np.write()
    sleep(TIME_REGULAR)

    np[1] = YELLOW
    np[0] = OFF
    np.write()
    sleep(TIME_YELLOW)
