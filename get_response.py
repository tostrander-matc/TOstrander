#!/usr/bin/env python3
import requests

def get_response(url):
	response = requests.get(url)
	print(f"ANSWER: {response.text}")

def main():
	url = input("Enter a valid URL: ")
	response2 = requests.get(url)
	print(f"{response2.text}")

if __name__ == "__main__":
	main()
