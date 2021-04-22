#!/usr/bin/env python3
import socket

RHOST = '127.0.0.1'
RPORT = 50007

C_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
C_SOCK.connect((RHOST, RPORT))

hFile=open("funfile.txt", "rb")
SND_DATA = hFile.read()

C_SOCK.send(SND_DATA)

C_SOCK.close()
