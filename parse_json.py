#!/usr/bin/env python3
import requests
import json

def parse_json(url):
	json_raw = requests.get(url)
	json_dict = json.loads(json_raw.text)
	for item in json_dict.values():
		for value in item:
			if 'George Orwell' in value.values():
				print(f"ANSWER: George Orwell")

def main():
	url = input("Enter a valid URL: ")
	json_raw = requests.get(url)
	json_dict = json.loads(json_raw.text)
	for item in json_dict.values():
		for value in item:
			if 'George Orwell' in value.values():
				print(f"ANSWER: George Orwell")

if __name__ == "__main__":
	main()
