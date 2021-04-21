#!/usr/bin/env
import socket

HOST = ''
PORT = 56789
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

while(1):
	s.listen(1)
	conn, addr = s.acccept()
	print('Connected by', addr)
	while 1
		data = conn.recv(1024)
		if not data: break
		conn.sendall(data)
	conn.close()
