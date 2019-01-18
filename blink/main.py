import time
from machine import Pin

led = Pin(2, Pin.OUT)
button = Pin(0, Pin.IN)
light = 0
old_btn = button.value()

while True:
    # led.value(1 - button.value())  # shine when holding

    led.value(light)
    if not old_btn and button.value():
        light = 0 if light else 1
    old_btn = button.value()
