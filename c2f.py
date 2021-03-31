#!/usr/bin/env python3

def c2f(number):
	degrees_celsius = int(number)
	degrees_celsius = (degrees_celsius * 9/5) + 32
	return degrees_celsius

def main():
	number = input("Enter a temperature in degrees Celsius: ")
	conversion = c2f(number)
	print(conversion)

if __name__ == "__main__":
	main()
