import time
from machine import Pin, PWM

led = Pin(2, Pin.OUT)


for _ in range(5):
    led.value(1)
    time.sleep(1/2)
    led.value(0)
    time.sleep(1/2)

for _ in range(5000):
    led.value(1)
    time.sleep(2/1000)
    led.value(0)
    time.sleep(1/1000)

led.value(0)
time.sleep(1)

for _ in range(5000):
    led.value(1)
    time.sleep(1/1000)
    led.value(0)
    time.sleep(2/1000)

led.value(0)
time.sleep(1)

pwm = PWM(led, freq=50, duty=512)
time.sleep(10)
pwm.deinit()

pwm = PWM(led, freq=50, duty=256)
time.sleep(10)
pwm.freq(1)
pwm.duty(256)
time.sleep(10)
pwm.freq(100)
