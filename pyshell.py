print("PyShell v1.0.0")
print("Initializing variables...")
calcsuccess = False
print("Importing run functionality...")
from subprocess import call
print("Importing RNG...")
import random
print("Importing OS commands...")
import os
print("Setting booleans...")
UsingProgram = True
print("Importing time module...")
import time
print("Importing math module...")
import math
os.system('cls' if os.name == 'nt' else 'clear')
print("Welcome!")
print("Please type commands in lowercase; commands are case sensitive.")
print("Command arguments have NOT been developed yet; this is just a fun little prototype :3")
print("gTTS MUST be installed via pip.")
while UsingProgram == True:    
    cmd = input("pyshell >")
    if cmd == "help":
        print("Current command list:")
        print("'clear': Clear the commandline.")
        print("'calc': Basic calculator.")
        print("'explorer': Open Windows Explorer (Windows Only.)")
        print("'quit': End current pyshell session.")
        print("'rolld20': Generates random number from 1-20 (Like a 20 side die!)")
        print("'game': Semi-functional minigame")
    elif cmd == "clear":
        os.system('cls' if os.name == 'nt' else 'clear')
    elif cmd == "calc":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("------CALCULATOR------")
        print("What type of equation do you want to make?")
        print("1. Addition")
        print("2. Multiplication")
        print("3. Subtraction")
        print("4. Division")
        eqtype = input()
        os.system('cls' if os.name == 'nt' else 'clear')
        x = input("1st number (X): ")
        y = input("2nd number (Y): ")
        x = int(x)
        y = int(y)
        if eqtype == "1":
            calcres = x + y
            print(calcres)
            calcsuccess = True
        elif eqtype == "2":
            calcres = x * y
            print(calcres)
            calcsuccess = True
        elif eqtype == "3":
            calcres = x - y
            print(calcres)
            calcsuccess = True
        elif eqtype == "4":
            calcres = x / y
            print(calcres)
            calcsuccess = True
        else:
            print("Oops! Something went wrong.")
        if calcsuccess == True:
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
    elif cmd == "explorer":
        call(["explorer.exe"])
    elif cmd == "fortnite":
        print("PLACEHOLDER")
    elif cmd == "rolld20":
        roll = random.randint(1, 20)
        print("You rolled a ",roll,".")
    elif cmd == "game":
        print("Let me explain the rules:")
        print("You pick a number and i pick a number.")
        print("If our numbers match you win!")
        print("If the numbers do NOT match i win!")
        print("Got that? OK!")
        print("Now we select a difficulty from Easy to Impossible.")
        print("Easy: Number 1-2 (1)")
        print("Normal: 1-6 (2)")
        print("Hard 1-20 (3)")
        print("Very Hard: 1-100 (4)")
        print("Impossible: 1-1000 (5)")
        diff = 0
        diff = input("Choose a difficulty (1-5): ")
        diff = int(diff)
        print(diff)
        if diff == 1:
            urnumber = input("Pick a number 1-2: ")
            urnumber = int(urnumber)
            if urnumber == random.randint(1, 2):
                print("You win!")
            else:
                print("You lost...")
        elif diff == 2:
            urnumber = input("Pick a number 1-6: ")
            urnumber = int(urnumber)
            if urnumber == random.randint(1, 6):
                print("You win!")
            else:
                print("You lose...")
        elif diff == 3:
            urnumber = input("Pick a number 1-20: ")
            urnumber = int(urnumber)
            if urnumber == random.randint(1, 20):
                print("You win!")
            else:
                print("You lose...")
        elif diff == 4:
            urnumber = input("Pick a number 1-100: ")
            urnumber = int(urnumber)
            if urnumber == random.randint(1, 100):
                print("Cool! You win!")
            else:
                print("You lost :(")
        elif diff == 5:
            urnumber = input("Pick a number 1-1000: ")
            urnumber = int(urnumber)
            if urnumber == random.randint(1, 1000):
                print("The RNGods have blessed you today lol (also you win btw :3)")
            else:
                print("I told you it was impossible...")
                print("also you lost rip bozo :)")
        else:
            print("Oops! Something went wrong.")        
            time.sleep(5)
    elif cmd == "quit":
        UsingProgram = False
    else:
        print("Invalid Command. Commands MUST be lowercase. Use the 'help' command to view available commands.")
print("Thank you for using pyshell; See you next time!")
time.sleep(2)
os.system('cls' if os.name == 'nt' else 'clear')