import socket
import time

address = ('', 48334)

receiving_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
receiving_socket.bind(address)
receiving_socket.settimeout(1)

while True:
    try:
        message = receiving_socket.recv(1024)
    except OSError:
        print('No message')
    else:
        print('Got', message)
