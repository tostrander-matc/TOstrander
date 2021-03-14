#!/usr/bin/env python3

print(f"\nName: Timothy Ostrander")

hFile = open("slicing-file.txt", "r")
list = hFile.readlines()
#SLICE VARIABLES========================
a = list[-3]
a = a.replace('\n', '')
b = " ".join(list[2:5])
b = b.replace('\n', '')
c = " ".join(list[-10:-15:-2])
c = c.replace('\n', '')
d = " ".join(list[10:13])
d = d.replace('\n', '')
e = " ".join(list[-19:-22:-1])
e = e.replace('\n', '')
#ACTIONS===============================
print(f"\n{a} {b} {c} {d} {e}")



