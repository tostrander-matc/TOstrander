#!/usr/bin/env python3

import subprocess

completedProcess = subprocess.run(['ps','-axco','command'],stdout=subprocess.PIPE)
myProc = completedProcess.stdout.decode().split('\n')

print(f"There are {len(myProc) - 1} items in the object.\n")
for line in myProc:
	print(line)


