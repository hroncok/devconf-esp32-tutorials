import network
ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid='upy_ap', password='pass1234',
          channel=7, authmode=network.AUTH_WPA2_PSK)
print(ap.ifconfig())
