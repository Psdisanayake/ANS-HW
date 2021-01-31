#!/usr/bin/env python3

import socket

IP = "127.0.0.1"  # loopback address ()
PORT = 8090        # Port to listen on (non-privileged ports are > 1023)
AMT_DATA = 64


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as mySocket:
    mySocket.connect((HOST, PORT))
    mySocket.sendall(b'Hello, Test')
    data = mySocket.recv(AMT_DATA)

print('Received', repr(data))