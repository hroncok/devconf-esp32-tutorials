import time
import socket

address = ('192.168.4.1', 48334)

sending_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    message = b'Hello'
    print('Sending', message)
    sending_socket.sendto(message, address)
    time.sleep(1/2)
