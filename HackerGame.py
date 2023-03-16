import time

# Set up the initial variables
score = 0
health = 100

# Define the functions for each room
def room1():
    print("You are in the lobby of a corporate building.")
    time.sleep(1)
    print("You see a security guard patrolling the area.")
    time.sleep(1)
    print("What do you want to do?")
    choice = input("1. Hack the security system\n2. Sneak past the security guard\n> ")
    if choice == "1":
        print("You successfully hacked the security system!")
        global score
        score += 10
        time.sleep(1)
    else:
        print("The security guard spotted you and you lost 10 health points.")
        global health
        health -= 10
        time.sleep(1)
    room2()

def room2():
    print("You are in the server room.")
    time.sleep(1)
    print("You see a computer with a password prompt.")
    time.sleep(1)
    print("What do you want to do?")
    choice = input("1. Use a password cracker\n2. Try to guess the password\n> ")
    if choice == "1":
        if score >= 10:
            print("You successfully cracked the password and gained access to the system!")
            time.sleep(1)
            room3()
        else:
            print("You need to hack the security system first!")
            time.sleep(1)
            room2()
    else:
        print("You guessed the wrong password and triggered an alarm.")
        global health
        health -= 10
        time.sleep(1)
        room2()

def room3():
    print("You are in the electronics shop.")
    time.sleep(1)
    print("There are many things to interact with.")
    time.sleep(1)
    print("What do you want to do?")
    choice = input("1. Look at the laptops\n2. Examine the security cameras\n3. Check out the networking equipment\n> ")
    global score
    if choice == "1":
        print("You find a laptop with a hidden backdoor.")
        score += 20
        time.sleep(1)
    elif choice == "2":
        print("You discover that the security cameras are vulnerable to a brute force attack.")
        score += 20
        time.sleep(1)
    elif choice == "3":
        print("You find a router with a default password.")
        score += 20
        time.sleep(1)
    else:
        print("You didn't find anything useful.")
        time.sleep(1)
    room4()

def room4():
    print("You are in the CEO's office.")
    time.sleep(1)
    print("You see a safe behind the desk.")
    time.sleep(1)
    print("What do you want to do?")
    choice = input("1. Crack the safe\n2. Search the desk for a key\n> ")
    if choice == "1":
        print("You successfully cracked the safe and found the secret plans!")
        global score
        score += 50
        time.sleep(1)
        print("Congratulations, you win!")
        global health
        health = 0
    else:
        print("You didn't find a key.")
        time.sleep(1)
    room3()

# Start the game
print("Welcome to the cyber security and pentesting adventure game!")
time.sleep(1)
print("You are a hacker trying to gain unauthorized access to a corporate system.")
time.sleep(1)
print("You have 100 health points and a score of 0.")
time.sleep(1)
room1()
