#!/usr/bin/env python3
import requests
import socket

def socket_client(IpAdd):
	RHOST = IpAdd
	myPortRange = range(5000,6000)
	myTimeout = 2
	SND_DATA = 'secret'
	SND_BYTE = str.encode(SND_DATA)
	for RPORT in myPortRange:
		C_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		C_SOCK.settimeout(myTimeout)
		try:
			C_SOCK.connect((RHOST, RPORT))
			C_SOCK.send(SND_BYTE)
			RCV_DATA = C_SOCK.recv(1024)
			RCV_DCODE = RCV_DATA.decode()
			print(RCV_DCODE)
			C_SOCK.close()
		except socket.error as e:
			pass
			C_SOCK.close()

def main():
	RHOST = input("Enter a valid IP Address: ")
	myPortRange = range(5000,6000)
	myTimeout = 2
	SND_DATA = 'secret'
	SND_BYTE = str.encode(SND_DATA)
	for RPORT in myPortRange:
		C_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		C_SOCK.settimeout(myTimeout)
		try:
			C_SOCK.connect((RHOST, RPORT))
			C_SOCK.send(SND_BYTE)
			RCV_DATA = C_SOCK.recv(1024)
			RCV_DCODE = RCV_DATA.decode()
			print(f"ANSWER: {RCV_DCODE}")
			C_SOCK.close()
		except socket.error as e:
			pass
			C_SOCK.close()

if __name__ == "__main__":
	main()
