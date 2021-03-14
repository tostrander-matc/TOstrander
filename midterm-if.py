#!/usr/bin/env python3
print(f"\n")
print(f"Name: Tim Ostrander, first of his name\n")

count = 0
Total = 0
hFile = open("Midterm-if.txt", "r")
listfile = hFile.readlines()
for line in listfile:
	count += 1
	if "gmeach18@ed.gov" in line:
		print(line)
		Total +=(count - 1)
	elif "248.253.63.149" in line:
		print(line)
		Total +=(count - 1)
	elif "Whiteland" in line:
		print(line)
		Total +=(count - 1)
	elif "80.222.19.190" in line:
		print(line)
		Total +=(count - 1)
	elif "Kayley" in line:
		print(line)
		Total +=(count - 1)
	elif "dcassyqw@microsoft.com" in line:
		print(line)
		Total +=(count - 1)
	else:
		pass
hFile.close()
print(f"The total is: {Total}\n")
