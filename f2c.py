#!/usr/bin/env python3

def f2c(number):
	degrees_fahrenheit = int(number)
	degrees_celsius = (degrees_fahrenheit - 32) * 5/9
	return degrees_celsius

def main():
	number = input("Enter a temperature in degrees Fahrenheit: ")
	conversion = f2c(number)
	print(conversion)

if __name__ == "__main__":
	main()


