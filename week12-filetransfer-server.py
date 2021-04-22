#!/usr/bin/env python3
import socket

HOST = ''
PORT = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

while(1):
	s.listen(1)
	conn, addr = s.accept()
	print('Connected by', addr)
	while 1:
		data = conn.recv(1024)
		file = open("funniestfile.txt", "wb")
		file.write(data)
		if not data: break
	conn.close()
