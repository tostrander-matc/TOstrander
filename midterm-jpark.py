#!/usr/bin/env python3
print(f"\nName: Timothy Ostrander\n")
#DICTIONARIES=======================
password_database = {"Username":"dnedry"}
password_database["Password"] = "please"

#DICT.N02
command_database = {"reboot":"Ok. I will reboot all park systems."}
command_database["shutdown"] = "Ok. I will shut down all park systems."
command_database["done"] = "I hate all this hacker stuff."

#TWO OBJECTS
white_rabbit_object = 0
counter = 0

while (white_rabbit_object == 0) and (counter < 3):
	input_user=input("Username: ")
	input_pass=input("Password: ")
	if input_user.lower() == password_database["Username"] and input_pass.lower() == password_database["Password"]:
		white_rabbit_object = 1
		print(f"\nHi, Dennis. You're still the best hacker in Jurassic Park.")
		print(command_database.keys())
		input_command=input("Enter one of the above commands: ")
		if input_command.lower() == "reboot":
			print(f"\n")
			print(command_database["reboot"])
		elif input_command.lower() == "shutdown":
			print(f"\n")
			print(command_database["shutdown"])
		elif input_command.lower() == "done":
			print(f"\n")
			print(command_database["done"])
		else:
			print(f"\nThe Lysine Contingency has been put into effect.")
	else:
		counter += 1
		print(f"You didn't say the magic word! {counter}")
		if counter == 3:
			print((f"You didn't say the magic word!\n") * 25)
