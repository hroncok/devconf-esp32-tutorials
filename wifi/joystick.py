import network
ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid='joystick', password='joystick', channel=2)
print(ap.ifconfig())


import time
import socket
from machine import Pin

pins = [
    Pin(n, Pin.IN, Pin.PULL_UP)
    for n in (21, 19, 18, 5)
]

led = Pin(2, Pin.OUT)

def get_message():
    return bytes(b'01'[p.value()] for p in pins)

address = ('255.255.255.255', 48334)

sending_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

last_send_time = time.ticks_ms()
last_message = None
while True:
    message = get_message()
    time_now = time.ticks_ms()
    if time.ticks_diff(time_now, last_send_time) > 1000 or last_message != message:
        print('Sending', message)
        sending_socket.sendto(message, address)
        last_send_time = time_now
        last_message = message

    led.value(1 - led.value())
    time.sleep(0.01)
