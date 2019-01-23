import network
ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid='upy_ap', password='pass123', channel=7)
print(ap.ifconfig())
