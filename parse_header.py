#!/usr/bin/env python3
import requests

def parse_header(url):
	response = requests.get(url)
	answer = response.headers["MATC-HEADER"]
	print(f"ANSWER: {answer}")
def main():
	url = input("Enter a valid URL: ")
	response = requests.get(url)
	print(response.headers["MATC-HEADER"])

if __name__ == "__main__":
	main()
