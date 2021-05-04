#!/usr/bin/env python3
import requests
import sys
import argparse
import json

parser = argparse.ArgumentParser(description="This is the last assignment before the final.")

parser.add_argument('-ip', '--ipAddress', dest='varIP', metavar='[a string]', default='hello', type=str, required=False, help='Enter -ip and an IP address.')

args = parser.parse_args()

url = f"http://ipinfo.io/{args.varIP}/json"

jsonResp = requests.get(url)

myDict = json.loads(jsonResp.text)

for key in myDict:
	print(f"{key} : {myDict[key]}")
