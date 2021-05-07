#!/usr/bin/env python3
import requests
import json
import argparse
import sys
import socket
import get_response
import parse_string
import parse_header
import parse_json
import socket_client

#Parser
parser = argparse.ArgumentParser(description="This is the final exam.")

#User Input (The Arguments)
parser.add_argument('-ip', '--ipAddress', dest='IpAdd', metavar='[a string]', type=str, required=True, help='Enter a valid IP Address.')
parser.add_argument('-f', '--function', dest='Func', metavar='[an integer]', type=int, required=True, help='Enter a valid function (1-5)')

args = parser.parse_args()

#Putting the arguments into scripts

if args.Func == 1:
	url = f"http://{args.IpAdd}/q{args.Func}"
	print(f"\nName: Tim Ostrander")
	print(f"http://172.31.28.252/q1")
	get_response.get_response(url)

elif args.Func == 2:
	url = f"http://{args.IpAdd}/q{args.Func}"
	print(f"\nName: Tim Ostrander")
	print(f"http://172.31.28.252/q2")
	parse_string.parse_string(url)

elif args.Func == 3:
	url = f"http://{args.IpAdd}/q{args.Func}"
	print(f"\nName: Tim Ostrander")
	print(f"http://172.31.28.252/q3")
	parse_header.parse_header(url)

elif args.Func == 4:
	url = f"http://{args.IpAdd}/q{args.Func}"
	print(f"\nName: Tim Ostrander")
	print(f"http://172.31.28.252/q4")
	parse_json.parse_json(url)

elif args.Func == 5:
	IpAdd = f"{args.IpAdd}"
	print(f"\nName: Tim Ostrander")
	print(f"http://172.31.28.252/q5")
	socket_client.socket_client(IpAdd)

else:
	pass
