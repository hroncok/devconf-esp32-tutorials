from machine import Pin, PWM
from neopixel import NeoPixel
from time import sleep

NUM_LEDS = 8

ledpin = Pin(18, Pin.OUT)  # XXX check num
servopin = Pin(15, Pin.OUT)  # XXX check num

RED = (10, 0, 0)
WHITE = (7, 7, 7)
OFF = (0, 0, 0)

OPEN = 40
CLOSED = 90

np = NeoPixel(ledpin, NUM_LEDS)
pwm = PWM(servopin, freq=50, duty=OPEN)


TIME_REGULAR = 12
TIME_TRAIN = 12  # at least 4

np[1] = OFF
np[6] = OFF
np[7] = OFF

while True:
    for i in range(TIME_REGULAR):
        if i % 2 == 0:
            np[1] = OFF
        else:
            np[1] = WHITE
        np.write()
        sleep(1)
    np[1] = OFF

    for i in range(TIME_TRAIN):
        if i % 2 == 0:
            np[6] = OFF
            np[7] = RED
        else:
            np[6] = RED
            np[7] = OFF
        if i == 2:
            pwm.duty(CLOSED)
        if i == TIME_TRAIN - 2:
            pwm.duty(OPEN)
        np.write()
        sleep(1)
    np[6] = OFF
    np[7] = OFF

