#!/usr/bin/env python3 

print("""You enter a dark room with three doors. 
Do you go through door #1, door #2, or door #3?""")


door = input("-> ")

# == Door Number 1 logic =======================
if door == "1":

    print("The Balrog, Durin's Bane, stands before you.")
    print("What do you do?\n")

    print("1. Stand your ground. 'You shall not pass!'")
    print("2. Yell at Legolas to shoot it down.")

    # == Balrog logic ============================
    balrog = input("-> ")

    if balrog == "1":
        print("1) You save the Fellowship, but plunge to to the depths of Khazad-Dum.")
    elif balrog == "2":
        print("2) The arrow clangs off the Balrog, completely ineffective. Uh oh!")
    else:
        print(f"N) There's no avoiding the fight.")
        print("Middle-Earth is doomed!")

# == Door Number 2 Logic =====================
elif door == "2":
    print("You stare into the firey chasm below at the forge of Orodruin.\n")
    
    print("1. Destroy the ring.")
    print("2. Contemplate destroying the ring.")
    print("3. Take the ring for yourself.")
    
    # == ring Logic ======================
    ring = input("-> ")

    if ring == "1" or ring == "2":
        print("1) Gollum attacks you, taking the ring and falling into the fires below!")
        print("1) The eagles come to your rescue!")
    else:
        print("N) The armies of Mordor take you by surprise.")
        print("N) Sauron regains possession of the ring reigns supreme!")

# == Door Number 2 Logic =====================
elif door == "3":
    print("You're suddenly on a boat, with Samwise Gamgee staring at you from the shore.\n")
    
    print("1. 'I'm going to Mordor alone, Sam.'")
    print("2. 'Hurry, Sam, get on the boat!'")
    
    # == ring Logic ======================
    frodo = input("-> ")

    if frodo == "1":
        print("1) 'Of course you are,' replies Sam, 'and I'm coming with you!'")
    elif frodo == "2":
        print("2) 'Don't go out so far, I can't swim, Mister Frodo!'")
    else:
        print(f"N) You have no choice, Sam is coming with you.")

else:
    print("Are you afraid of doors or something?")
