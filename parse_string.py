#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup

def parse_string(url):
	response = requests.get(url)
	soup = BeautifulSoup(response.text, 'html.parser')
	h3var = soup.select('H3')
	h33var = str(h3var)
	print(f"ANSWER: {h33var[7:47:3]}")

def main():
	url = input("Enter a valid URL: ")
	response = requests.get(url)
	soup = BeautifulSoup(response.text, 'html.parser')
	h3var = soup.select('H3')
	h33var = str(h3var)
	print(f"{h33var[7:47:3]}")

if __name__ == "__main__":
	main()
