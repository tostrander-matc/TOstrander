#!/usr/bin/env python3
#hFile = open("/etc/passwd", "r")
#strfiletxt = hFile.read()
#print(strfiletxt)
#print(len(strfiletxt))
#print(f"The len function counts the number of characters in the /etc/passwd file.")
#hFile.close()

#hFile = open("/etc/passwd", "r")
#listfiletxt = hFile.readlines()
#print(listfiletxt)
#print(f"\n")
#print(len(listfiletxt))
#print(f"\nThe len function counts the number of items in the list, in this case.")
#print(f"\nA list might be most useful depending on the file, such as names or passwords.")
#hFile.close()
hFile = open("/etc/passwd", "r")
var = 0
for line in hFile:
	print(line)
	print(len(line))
	var +=len(line)  
hFile.close()
print(var)
print(f"This is good way to display information if you wanted to make changes as admin.")
