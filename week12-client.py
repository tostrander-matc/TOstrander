#!/usr/bin/env python3
import socket

RHOST = '127.0.0.1'
RPORT = 50007
SND_DATA = 'My Text to send'

C_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
C_SOCK.connect((RHOST, RPORT))
while True:
	SND_DATA = input("Enter a message: ")	
	C_SOCK.send(bytearray(SND_DATA, 'utf8'))
	RCV_DATA = C_SOCK.recv(1024)
	print(RCV_DATA)

C_SOCK.close()
