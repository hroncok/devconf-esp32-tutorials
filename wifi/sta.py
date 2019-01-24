import network
from time import sleep

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('Red Hat Guest', 'navigate17')

while not wlan.isconnected():
    print('Connecting....')
    sleep(1)

print(wlan.ifconfig())
