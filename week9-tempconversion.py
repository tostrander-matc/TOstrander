#!/usr/bin/env python3

import c2f
import f2c

temp = (input("Enter a temperature to convert (in degrees): "))
measure = input("Convert to Fahrenheit or Celsius? (Type C or F): ")
if measure == "F":
	conversion = c2f.c2f(temp)
	print(f"\n{temp} degrees Celsius converts to {conversion} degrees Fahrenheit.")
elif measure == "C":
	conversion = f2c.f2c(temp)
	print(f"\n{temp} degrees Fahrenheit converts to {conversion} degrees Celsius.")
else:
	print("You didn't pick a valid measure!")

