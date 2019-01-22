from time import sleep
from machine import Pin, PWM
pwm = PWM(Pin(17, Pin.OUT), freq=50, duty=75)

pwm.duty(50)   # left
sleep(1)
pwm.duty(75)   # middle
sleep(1)
pwm.duty(100)  # right
sleep(1)
pwm.deinit()
